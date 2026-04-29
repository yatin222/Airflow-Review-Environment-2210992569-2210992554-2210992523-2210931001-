# nielsen-airflow-dags-repo/dags/hello_world_review_dag.py
from airflow.models.dag import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id='hello_world_review_app_dag',
    start_date=datetime(2023, 1, 1),
    schedule_interval=None, # This DAG runs manually
    catchup=False,
    tags=['review_app', 'sample'],
    doc_md="""
    #### Hello World Review App DAG
    This is a simple DAG to test the Airflow review environment.
    It just prints a message and the current date.
    """
) as dag:
    print_hello = BashOperator(
        task_id='print_hello',
        bash_command='echo "Hello from review app DAG! This is version 1."',
    )

    print_date = BashOperator(
        task_id='print_date',
        bash_command='date',
    )

    print_hello >> print_date