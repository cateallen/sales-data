
# Sales Data ETL Pipeline

This project demonstrates an ETL pipeline using Apache Airflow. The pipeline extracts sales data from a CSV file, transforms it, and loads it into a SQLite database.

## Key points of this project
- Extracts sales data from multiple sources (CSV, API).
- Cleans and aggregates the data by product category and month.
- Loads the processed data into an SQLite database.
- Provides visual reports using Matplotlib.

## How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/cateallen/sales-data.git
   cd sales-data


## Running the ETL Pipeline with Apache Airflow

1. **Install Dependencies**:
   Ensure you have installed all necessary packages by running:
   ```bash
   pip install -r requirements.txt

2. **Initialize Airflow**:
    ```bash
    airflow db init

3. **Start Airflow Scheduler**
    ```bash
    airflowscheduler


4. **Start Airflow Webserver**
In a seperate terminal
    ```bash
    airflow webserver --port 8080

5. **Access Airflow UI**
http://localhost:8080 to monitor the DAG and toggle the DAG to "on". You can trigger it manually or let it run when its scheduled.

6. **Run the DAG**
a. In the Airflow web UI (http://localhost:8080/), you will see your DAG listed.
b. Toggle it on to start the scheduling.
c. You can trigger manually the DAG by clicking the Trigger DAG button at the Airflow web UI (http://localhost:8080/)


7. **View Logs and Monitor Progress**
a. You can monitor each task in the DAG and view logs to debug issues that arise
b. Airflow provides a detailed view of the DAG's status and history of all tasks
