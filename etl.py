
# Extract Phase

# Importing packages
import pandas as pd
import requests

# Loading the data from API
response = requests.get('https://api.example.com/sales')
sales_data = response.json()

# Transform Phase

# Cleaning data
data.dropna(inplace=True)  # Drop rows with missing values
data['date'] = pd.to_datetime(data['date'])  # Convert to datetime

# Aggregation: Grouping sales by month and product category
monthly_sales = data.groupby([data['date'].dt.month, 'product_category']).agg({'sales': 'sum'})

# Load Phase
from sqlalchemy import create_engine

# Create a database engine
engine = create_engine('sqlite:///sales_data.db')

# Load data into the database
monthly_sales.to_sql('monthly_sales', engine, if_exists='replace')


