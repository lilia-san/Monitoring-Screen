import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objs as go
from datetime import datetime, timedelta

# ----------------------
# Simulate Historical Data
# ----------------------

def prediction():
    np.random.seed(42)

   # hours = pd.date_range(end=datetime.now() "2023-12-06", "2023-12-09 23:00:00", freq="h", periods=72, freq='h')
    hours = pd.date_range(start="2023-12-06 08:00", periods=72, freq='h')
    vehicle_count = np.random.poisson(lam=80, size=72) + np.sin(np.linspace(0, 3*np.pi, 72)) * 20

    data = pd.DataFrame({'Timestamp': hours, 'Vehicle Count': vehicle_count})
    data.set_index('Timestamp', inplace=True)

    # ----------------------
    # Simulate Predictions
    # ----------------------
    forecast_hours = 12
    last_time = data.index[-1]
    future_times = [last_time + timedelta(hours=i) for i in range(1, forecast_hours + 1)]
    predicted_count = (np.random.poisson(lam=90, size=forecast_hours) + (np.sin(np.linspace(0, 2*np.pi, forecast_hours)) * 15)).astype(int)
    predicted_count = np.maximum(predicted_count, 0)

    forecast = pd.DataFrame({
        'Timestamp': future_times,
        'Predicted Count': predicted_count
    })
    forecast.set_index('Timestamp', inplace=True)

    # ----------------------
    # Streamlit UI
    # ----------------------
    st.title("📊 Traffic Prediction Dashboard")
    st.markdown("Visualize traffic volume and forecast for the next few hours using historical trends.")

    # Line chart with past and future
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=data.index, y=data['Vehicle Count'],
                            mode='lines+markers', name='Historical', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=forecast.index, y=forecast['Predicted Count'],
                            mode='lines+markers', name='Forecast', line=dict(color='orange', dash='dash')))

    fig.update_layout(title="Traffic Volume Forecast",
                    xaxis_title="Time",
                    yaxis_title="Number of Vehicles",
                    template="plotly_white")

    st.plotly_chart(fig, use_container_width=True)

    # ----------------------
    # User Controls
    # ----------------------
    st.sidebar.header("Forecast Controls")
    range_hours = st.sidebar.slider("How many hours ahead to view?", 1, 12, 6)
    subset_forecast = forecast.head(range_hours)

    st.subheader(f"🔮 Forecast for the Next {range_hours} Hours")
    #st.dataframe(subset_forecast)
    # Make a copy to avoid modifying the original DataFrame
    subset_display = subset_forecast.copy()

# Format index to remove seconds (keep only date and hour)
    subset_display.index = subset_display.index.strftime('%Y-%m-%d %H:00')

# Show it
    st.dataframe(subset_display)

    # Optional peak indicator
    peak_hour = subset_forecast['Predicted Count'].idxmax()
    peak_value = subset_forecast['Predicted Count'].max()
    st.markdown(f"**⏰ :red[Expected Peak Hour:]** {peak_hour.strftime('%Y-%m-%d %H:%M')} with {int(peak_value)} vehicles.")


