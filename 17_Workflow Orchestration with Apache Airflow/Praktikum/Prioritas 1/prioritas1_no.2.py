from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from random import sample

default_args = {
    'owner': 'putridia',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 20),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=2),
}

def generate_random_numbers():
    numbers = sample(range(1, 51), 25)
    return numbers

def calculate_sum(ti):
    numbers = ti.xcom_pull(task_ids='generate_random_numbers', key='return_value')
    total = sum(numbers)
    ti.xcom_push(key='sum_of_numbers', value=total)

def check_even_sum(ti):
    total = ti.xcom_pull(task_ids='calculate_sum', key='sum_of_numbers')
    if total % 2 == 0:
        result = 'Even Sum'
    else:
        result = 'Odd Sum'
    print(result)

with DAG(
    dag_id="calculator_dag",
    default_args=default_args,
    description="prioritas1.no2 DAG",
    start_date=datetime(2024, 4, 20),
    schedule_interval='@daily',
) as dag:

    task1 = PythonOperator(
        task_id='generate_random_numbers',
        python_callable=generate_random_numbers)

    task2 = PythonOperator(
        task_id='calculate_sum',
        python_callable=calculate_sum,
        provide_context=True)

    task3 = PythonOperator(
        task_id='check_even_sum',
        python_callable=check_even_sum)

task1 >> task2 >> task3