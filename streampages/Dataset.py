import streamlit as st
import pandas as pd
import numpy as np
import random


vehicles_in = np.random.randint(1000, size=(24))
vehicles_out = np.random.randint(1000, size=(24))
chart_data = pd.DataFrame(
    {
        "Timestamp": pd.date_range(start="2025-01-01", periods=24, freq='h'),
        "Hours": list(range(24)),
        "Vehicles_In": vehicles_in,
        "Vehicles_Out": vehicles_out
    }
 )

# Sample dataset
vehicle_types = ['Car', 'Truck', 'Bus', 'Motorcycle']
date_range = pd.date_range("2023-12-06", "2023-12-09 23:00:00", freq="h")
n = len(date_range)

data = pd.DataFrame({
    "Timestamp": np.tile(date_range, len(vehicle_types)),
    "Vehicle Type": np.repeat(vehicle_types, n),
    "Count": np.random.poisson(lam=60, size=n * len(vehicle_types))
})

# Add day & hour for later use
data["Date"] = data["Timestamp"].dt.date
data["Hour"] = data["Timestamp"].dt.hour


daysofweek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
days = np.tile(daysofweek,1000)
Count_in = np.random.randint(500, size=(7000))
Count_out = np.random.randint(500, size=(7000)) 
dataset = pd.DataFrame(
    {
        "Days": days,
        "Hour": np.random.randint(0, 24, 7000),
        "Amount of Vehicles In": Count_in,
        "Amount of Vehicles Out": Count_out,
        "Weather": [random.choice(["Rainy", "Sunny"]) for x in range(7000)],
        "Traffic predictions": [random.choice([ "light Traffic", "Normal Traffic", "Heavy Traffic"]) for x in range(7000)]
    }
)
