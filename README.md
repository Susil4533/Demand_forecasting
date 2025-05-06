# Logistics Demand Forecasting 
## Project Overview
This project focuses on forecasting product demand in logistics using various machine learning models. The goal is to predict future sales based on historical data to optimize inventory and supply chain management.
## Features
* Data preprocessing and cleaning<br>
* Multiple forecasting models implemented <br>
  ARIMA <br>
  LightGBM <br>
  LSTM <br>
* Model evaluation <br>
* Visualization of result <br>

## Dataset 
The project uses sales and pricing data, calendar information, and processed aggregated sales data. <br>
Large raw data files are excluded from the repository due to size constraints.

## Installation 
* Clone the repository
  git clone https://github.com/Susil4533/Demand_forecasting.git <br>
  cd Demand_forecasting
* Create and activate a Python virtual environment <br>
  python -m venv venv <br>
  venv\Scripts\activate
* Insstall dependencies <br>
  pip install -r requirements.txt
## Usage 
* Run data preprocessing scripts in the data/ folder. <br>
* Train models located in respective folders (ArimaModel/, LGBM/, LSTM/). <br>
* Use notebooks or scripts to evaluate and visualize forecasting results. <br>

## Data 
Due to file size limits, raw data files (*.csv) are not included in this repository. <br>
* You can download the original datasets from [(https://www.kaggle.com/c/m5-forecasting-accuracy/data)].
* Place your data files in the data/raw/ and data/processed/ folders as expected by the scripts.
  
