from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.python import PythonOperator
import requests
import pandas as pd

default_args = {
    "owner": "putridia",
    "retries": 1,
    "retry_delay": timedelta(minutes=2),
}

def fetch_data_from_api(**kwargs):
    api_url = "https://fakestoreapi.com/products"
    response = requests.get(api_url)
    data = response.json()
    kwargs['ti'].xcom_push(key='data_from_api', value=data)

def write_to_csv_file(**kwargs):
    data = kwargs['ti'].xcom_pull(key='data_from_api')
    df = pd.DataFrame(data)
    df.to_csv("products.csv", index=False)

def write_to_txt_file(**kwargs):
    data = kwargs['ti'].xcom_pull(key='data_from_api')
    with open("products.txt", "w") as f:
        for item in data:
            f.write(str(item) + "\n")

def print_task_completed(**kwargs):
    print("Task completed!")

with DAG(
    dag_id="fetch_data_and_write_files",
    default_args=default_args,
    start_date=datetime(2024, 5, 1),
    schedule_interval='@daily',
) as dag:

    fetch_data_task = PythonOperator(
        task_id="fetch_data_from_api",
        python_callable=fetch_data_from_api,
        provide_context=True,
    )

    write_to_csv_task = PythonOperator(
        task_id="write_to_csv_file",
        python_callable=write_to_csv_file,
        provide_context=True,
    )

    write_to_txt_task = PythonOperator(
        task_id="write_to_txt_file",
        python_callable=write_to_txt_file,
        provide_context=True,
    )

    print_completion_task = PythonOperator(
        task_id="print_task_completed",
        python_callable = print_task_completed,
        provide_context = True,
    )

    # Define task dependencies
    fetch_data_task >> [write_to_csv_task, write_to_txt_task] >> print_completion_task