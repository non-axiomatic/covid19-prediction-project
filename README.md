# covid19-prediction-project
This project leverages historical data of COVID-19 cases and deaths in India from January 30, 2020, to January 18, 2022. The goal is to predict the number of COVID-19 deaths for the next 30 days using the AutoTS (Automated Time Series) method. 

## Environment Setup & Installation
Clone the Repository:

```bash
git clone https://github.com/non-axiomatic/covid19-prediction-project.git
cd covid19-prediction-project
```

## Create a Virtual Environment and Install the Required Packages

1. Create a virtual environment with `pyenv`:

    ```bash
    pyenv virtualenv <python_version> <env_name>
    ```

    Replace `<python_version>` with the desired Python version (e.g., `3.11.4` I used in this project) and `<env_name>` with your chosen environment name (e.g., `covid19_env`).

2. Activate the virtual environment:

    ```bash
    pyenv activate <env_name>
    ```

    Replace `<env_name>` with the name of the environment you created (e.g., `covid19_env`).

3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```


3. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```


## Usage

Run the script

```bash
python covid19_prediction.py
```

The script will generate predictions based on the historical data and save the results in the specified output directory.

## Data

The dataset used in this project is COVID19 data for overall INDIA.csv. It contains historical COVID-19 case and death data for India.

## Features

- Visualizes daily confirmed cases and deaths.
- Calculates death rate.
- Forecasts deaths for the next 30 days using the AutoTS library.

