from datetime import datetime, timedelta
from airflow import DAG
import os
import numpy as np
import pandas as pd
from ingestion import DataLakeBuilder
from transformation import DataWarehouseLoader
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'putridia',
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 12),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'data_pipeline',
    default_args=default_args,
    schedule_interval=timedelta(days=1),
    catchup=False,
    start_date=datetime(2023, 3, 12)
)

# Define the data ingestion task
def ingest_data():
    data_lake_builder = DataLakeBuilder()

    csv_files = ['events.csv', 'customers.csv', 'tickets.csv', 'transactions.csv', 'customer_feedback.csv']
    data_source = 'data_source'
    parquet_dir = 'data_parquet'

    if not os.path.exists(parquet_dir):
        os.makedirs(parquet_dir)

    for file in csv_files:
        file_path = os.path.join(data_source, file)
        df = data_lake_builder.read_csv(file_path)
        df = data_lake_builder.handle_missing_values(df)
        df = data_lake_builder.handle_outliers(df, 'total_amount')
        numeric_columns = df.select_dtypes(include=[np.number]).columns
        for col in numeric_columns:
            df = data_lake_builder.handle_outliers(df, col)
        parquet_file = os.path.join(parquet_dir, file.split('.')[0] + '.parquet')
        data_lake_builder.save_to_parquet(df, parquet_file)
        
ingest_data_task = PythonOperator(
    task_id='ingest_data',
    python_callable=ingest_data,
    dag=dag,
)

# Define the data transformation task
def transform_data():
    loader = DataWarehouseLoader()
    
    transactions = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/transactions.parquet')
    tickets = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/tickets.parquet')
    events = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/events.parquet')   
    customer_feedback = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/customer_feedback.parquet')
    customer = loader.load_data('C:/Users/ASUS/OneDrive/Documents/GitHub/de_putri-dia-lestari/18_Code Competence 2 DE/Praktikum/data_parquet/customers.parquet')

    tickets_sold, revenue, feedback = loader.transform_data(transactions, tickets, events, customer_feedback, customer)

    loader.save_to_warehouse(tickets_sold, 'tickets_sold_per_event')
    loader.save_to_warehouse(revenue, 'revenue_per_event')
    loader.save_to_warehouse(feedback, 'feedback_analysis')

transform_data_task = PythonOperator(
    task_id='transform_data',
    python_callable=transform_data,
    dag=dag,
)

ingest_data_task >> transform_data_task