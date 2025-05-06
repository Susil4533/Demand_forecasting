from statsmodels.tsa.arima.model import ARIMAResults

model = ARIMAResults.load('model/arima_model.pkl')

import streamlit as st
from statsmodels.tsa.arima.model import ARIMAResults
import pandas as pd
import matplotlib.pyplot as plt

st.title("Pre-Trained ARIMA Forecast Viewer")

# Load model from the model folder
@st.cache_resource
def load_model():
    return ARIMAResults.load('model/arima_model.pkl')

model = load_model()

steps = st.slider("Select forecast horizon (periods ahead)", min_value=1, max_value=52, value=10)

uploaded_file = st.file_uploader("Upload historical time series CSV ", type=["csv"])

if st.button("Show Forecast"):
    forecast_result = model.get_forecast(steps=steps)
    forecast = forecast_result.predicted_mean
    conf_int = forecast_result.conf_int()

    st.subheader("Forecasted Values")
    st.write(forecast)

    fig, ax = plt.subplots(figsize=(10, 5))

    # Plot historical data if uploaded
    if uploaded_file is not None:
        data = pd.read_csv(uploaded_file, parse_dates=[0])
        data.set_index(data.columns[0], inplace=True)
        ts = data.iloc[:, 0]
        ts.plot(ax=ax, label='Historical Data')

    forecast.plot(ax=ax, label='Forecast', color='red')
    ax.fill_between(conf_int.index, conf_int.iloc[:, 0], conf_int.iloc[:, 1], color='pink', alpha=0.3)

    ax.set_title("ARIMA Forecast")
    ax.legend()
    st.pyplot(fig)
