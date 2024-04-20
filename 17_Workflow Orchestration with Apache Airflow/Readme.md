# Summary Workflow Orchestration with Apache Airflow

## Apache Airflow 

Sebuah tools untuk melakukan Workflow Orchestration atau pengelolaan berbagai workflow yang ada. Workflow adalah sekumpulan tugas yang terhubung satu sama lain untuk mencapai tertentu. Masing-masing task akan dijalankan oleh sebuah operator.

## DAG (Directed Acyclic Graph)
Sebuah graf yang digunakan untuk menggambarkan sebuah workflow. Pada 1 DAG akan terdiri dari beberapa task yang dimana task tersebut akan menggunakan operator. Task sendiri adalah sebuah unit tugas yang digunakan untuk menjalankan aktivitas tertentu dan task tentunya membutuhkan operator untuk prosesnya. Sifat-sifat DAG yaitu:
- Hanya bersifat satu arah (acyclic)
- Bisa terdiri dari berbagai task dengan operator yang berbeda
- Satu task bisa melakukan percabangan ke task lain.
- Berbagai task bisa menuju satu task yang sama

Pada Apache Airflow sendiri, 1 task memiliki lifecycle nya sendiri. 

## Tahapan Lifecycle Task pada Apache Airflow diantaranya sebagai berikut : 

- Scheduled: Task dijadwalkan untuk dijalankan pada waktu yang ditentukan.
- Queued: Task ditambahkan ke antrian untuk dieksekusi oleh worker.
- Running: Task sedang dieksekusi oleh worker.
- Success: Task telah berhasil dieksekusi dan menghasilkan output yang diharapkan.
- Failed: Task gagal dieksekusi karena suatu kesalahan.
- Skipping: Task dilewati karena tidak perlu dieksekusi.
- Upstream Failed: Task tidak dapat dieksekusi karena task upstreamnya gagal.
- Deferred: Task ditunda untuk dieksekusi di masa depan.
- Rescheduled: Task dijadwalkan kembali untuk dieksekusi di masa depan.
- Killed: Task dihentikan secara paksa.

## Perubahan Status Task
Status task dapat berubah-ubah selama siklus hidupnya. Berikut adalah beberapa contoh perubahan status task:

- Scheduled -> Queued: Ketika task dijadwalkan untuk dijalankan, statusnya berubah menjadi "Queued".
- Queued -> Running: Ketika worker mengambil task dari antrian, statusnya berubah menjadi "Running".
- Running -> Success: Ketika task berhasil dieksekusi, statusnya berubah menjadi "Success".
- Running -> Failed: Ketika task gagal dieksekusi, statusnya berubah menjadi "Failed".
- Queued -> Skipping: Ketika task dilewati, statusnya berubah menjadi "Skipping".
- Queued -> Upstream Failed: Ketika task upstreamnya gagal, statusnya berubah menjadi "Upstream Failed".
- Queued -> Deferred: Ketika task ditunda, statusnya berubah menjadi "Deferred".
- Deferred -> Queued: Ketika task ditunda dan waktu pengundurannya telah tiba, statusnya berubah kembali menjadi "Queued".
- Rescheduled -> Queued: Ketika task dijadwalkan ulang, statusnya berubah menjadi "Queued".
- Running -> Killed: Ketika task dihentikan secara paksa, statusnya berubah menjadi "Killed".

## Create DAG with Bash Operator

```bash
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator

default_args = {
    'owner': 'putridia',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='soy_factory_v1',
    default_args=default_args,
    description='Soy factory simulation',
    start_date=datetime(2024, 4, 1),
    schedule_interval='@daily'
) as dag:

    t1 = BashOperator(
        task_id='task1',
        bash_command='echo collect soybeans',
    )

    t2 = BashOperator(
        task_id='task2',
        bash_command='echo create tempe',
    )

    t3 = BashOperator(
        task_id='task3',
        bash_command='echo create soy bean milk',
    )

    t4 = BashOperator(
        task_id='task4',
        bash_command='echo distribute items',
    )

    # task1 --> task2
    #   |   --> task3
    t1 >> [t2, t3]

    #t2 --> t4
    #t3 --> t4
    t2 >> t4
    t3 >> t4
```

## Create DAG dengan PythonOperator
  
```bash
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def add(number1, number2):
    result = number1 + number2
    return f"{number1} + {number2} = {result}"

default_args = {
    'owner': 'putridia',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='simple_python_dag_v1',
    default_args=default_args,
    description='simple DAG with python',
    start_date=datetime(2024, 4, 1),
    schedule_interval='@daily'
) as dag:

    t1 = PythonOperator(
        task_id='add_task',
        python_callable=add,
        op_kwargs={'number1': 1, 'number2': 5},
    )
```

## XCOM in DAG

XCOM adalah sebutan dari Cross Communication yang memungkinkan antar task dapat bertukar atau mengirim data. Catatan untuk XCOM:

Cocok digunakan untuk data dengan ukuran kecil
Tidak cocok untuk data dengan ukuran yang besar seperti sebuah DataFrame, file dan data lain Contoh : alt text

## Taskflow DAG
Dapat digunakan untuk membuat data pipeline di Airflow.

- ## Create taskflow DAG

```bash
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator

def add(number1, number2):
    result = number1 + number2
    return f"{number1} + {number2} = {result}"

default_args = {
    'owner': 'putridia',
    'retries': 5,
    'retry_delay': timedelta(minutes=2),
}

with DAG(
    dag_id='simple_python_dag_v1',
    default_args=default_args,
    description='simple DAG with python',
    start_date=datetime(2024, 4, 1),
    schedule_interval='@daily'
) as dag:

    t1 = PythonOperator(
        task_id='add_task',
        python_callable=add,
        op_kwargs={'number1': 1, 'number2': 5},
    )
```

