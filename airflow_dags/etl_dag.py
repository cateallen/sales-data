
# Set the task dependencies
extract_task >> transform_task >> load_task


##ETL_dag.py flow
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
import pandas as pd
from sqlalchemy import create_engine

# Here is where I define ETL functions

def extract():
    # Example of extracting data from a CSV file
    data = pd.read_csv('/path/to/sales_data.csv')
    print("Data extracted")
    return data

def transform(**kwargs):
    ti = kwargs['ti'] 
    data = ti.xcom_pull(task_ids='extract_data')
    data['date'] = pd.to_datetime(data['date'])
    data = data.dropna()
    print("Data transformed")
    return data


    def load(**kwargs):
    ti = kwargs['ti']
    data = ti.xcom_pull(task_ids='transform_data')  # Pull data from transform task
    # Load the data into a SQLite database
    engine = create_engine('sqlite:///sales_data.db')
    data.to_sql('sales', con=engine, if_exists='replace')
    print("Data loaded into the database")

# Define the default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 10, 11),
    'retries': 1,
}

# Define the DAG
with DAG(
    'sales_data_etl_pipeline',
    default_args=default_args,
    description='A simple ETL pipeline for sales data',
    schedule_interval='@daily',  # Set to run daily
    catchup=False,  # Only run future jobs
) as dag:

    # Define tasks
    extract_task = PythonOperator(
        task_id='extract_data',
        python_callable=extract,
    )

    transform_task = PythonOperator(
        task_id='transform_data',
        python_callable=transform,
        provide_context=True  # Enable passing context for XComs
    )

    load_task = PythonOperator(
        task_id='load_data',
        python_callable=load,
        provide_context=True
    )

 # Set task dependencies: Extract -> Transform -> Load
    extract_task >> transform_task >> load_task
