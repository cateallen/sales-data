
#Setup
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# Define ETL functions
def extract():
    data = pd.read_csv('data/sales_data.csv'')
    return data

def transform(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='extract_data')
    data['date'] = pd.to_datetime(data['date'])
    return data

def load(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='transform_data')
    engine = create_engine('sqlite:///sales_data.db')
    data.to_sql('sales', con=engine, if_exists='replace')

# Define DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 11),
    'retries': 1,
}

with DAG('sales_data_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    extract_task = PythonOperator(task_id='extract_data', python_callable=extract)
    transform_task = PythonOperator(task_id='transform_data', python_callable=transform, provide_context=True)
    load_task = PythonOperator(task_id='load_data', python_callable=load, provide_context=True)

    extract_task >> transform_task >> load_task

