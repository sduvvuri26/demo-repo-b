from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="dag_b1",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False,
):
    EmptyOperator(task_id="start")
