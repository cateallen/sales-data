#Create the Pipeline with Apache Airflow

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define DAG
dag = DAG('sales_etl_pipeline', start_date=datetime(2024, 1, 1))

# Define tasks
extract_task = PythonOperator(task_id='extract', python_callable=extract_function, dag=dag)
transform_task = PythonOperator(task_id='transform', python_callable=transform_function, dag=dag)
load_task = PythonOperator(task_id='load', python_callable=load_function, dag=dag)

# Set task dependencies
extract_task >> transform_task >> load_task
