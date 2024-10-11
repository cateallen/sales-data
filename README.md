
# Sales Data ETL Pipeline

This project demonstrates an ETL (Extract, Transform, Load) pipeline that processes sales data from CSV files or an API, transforms it, and loads it into a SQL database. The pipeline also includes visualizations for reporting monthly sales.

## Project Features
- Extracts sales data from multiple sources (CSV, API).
- Cleans and aggregates the data by product category and month.
- Loads the processed data into an SQLite database.
- Provides visual reports using Matplotlib.

## How to Run the Project

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/ETL_Project.git
   cd ETL_Project


2. Install Dependencies
conda create -n etl_project python=3.8
conda activate etl_project
pip install -r requirements.txt

3. Run ETL pipeline
python etl.py

4. Create the data visualization
python visualize.py

## Setup airflow to schedule and manage the pipeline

# Install Apache Airflow: pip install apache-airflow
# Initialize the dtb: airflow db init
# Setup the airflow home directory: export AIRFLOW_HOME=~/airflow
# Make sure the 'sales_etl_dag.py' file is in: ~/airflow/dags/
## Below is an example DAG for an ETL pipeline. this will run daily and catchup equals false so that prior missed runs before the current day do not run

from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

# Define your ETL functions
def extract():
    # Code to extract data
    print("Extracting data...")

def transform():
    # Code to transform data
    print("Transforming data...")

def load():
    # Code to load data
    print("Loading data into the database...")

# Define the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 1, 1),
    'retries': 1,
}

with DAG('sales_data_etl_pipeline',
         default_args=default_args,
         schedule_interval='@daily',  # Runs daily, can be adjusted
         catchup=False) as dag:

    # Define tasks
    extract_task = PythonOperator(task_id='extract_data', python_callable=extract)
    transform_task = PythonOperator(task_id='transform_data', python_callable=transform)
    load_task = PythonOperator(task_id='load_data', python_callable=load)

    # Define task dependencies
    extract_task >> transform_task >> load_task

## Start Airflow Sscheduler & Airflow Web Server
airflow scheduler
airflow webserver --port 8080

## Trigger and Monitor the DAG
1. In the Airflow web UI (http://localhost:8080/), you will see your DAG listed.
2. Toggle it on to start the scheduling.
3. You can trigger manually the DAG by clicking the Trigger DAG button at the Airflow web UI (http://localhost:8080/)

## View Logs and Monitor Progress
1. You can monitor each task in the DAG and view logs to debug issues that arise
2. Airflow provides a detailed view of the DAG's status and history of all tasks






