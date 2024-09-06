# Import necessary libraries
import pandas as pd
import numpy as np
import os
import plotly.express as px
import plotly.io as pio
from autots import AutoTS

# Print the current working directory
print(os.getcwd())

# Load the dataset
data = pd.read_csv("COVID19 data for overall INDIA.csv")

# Display the first few rows of the dataset
print(data.head())

# Check for missing values in the dataset
print(data.isnull().sum())

# Drop the 'Date' column as it is not needed
data = data.drop("Date", axis=1)

# Display the cleaned dataset
print(data.head())

# Set Plotly renderer for displaying plots
# For Jupyter Notebooks, use 'iframe' renderer
# For running scripts outside of Jupyter, use 'browser' or 'notebook'
pio.renderers.default = 'browser'  # Change to 'iframe' if running in Jupyter Notebook

# Plot daily confirmed cases
fig = px.bar(data, x='Date_YMD', y='Daily Confirmed')
fig.show()

# Plot daily confirmed cases vs daily deaths
cases = data["Daily Confirmed"].sum()
deceased = data["Daily Deceased"].sum()
labels = ["Confirmed", "Deceased"]
values = [cases, deceased]
fig = px.pie(data, values=values, names=labels, title='Daily Confirmed Cases vs Daily Deaths', hole=0.5)
fig.show()

# Plot daily deaths
fig = px.bar(data, x='Date_YMD', y='Daily Deceased')
fig.show()

# Forecasting with AutoTS
model = AutoTS(forecast_length=30, frequency='infer', ensemble='simple')
model = model.fit(data, date_col="Date_YMD", value_col='Daily Deceased', id_col=None)
prediction = model.predict()
forecast = prediction.forecast

# Print the forecast for the next 30 days
print(forecast)

