import streamlit as st
import pandas as pd
import numpy as np
import random


vehicles_in = np.random.randint(1000, size=(24))
vehicles_out = np.random.randint(1000, size=(24))
chart_data = pd.DataFrame(
    {
        "Timestamp": pd.date_range(start="2025-05-25", periods=24, freq='h'),
        "Hours": list(range(24)),
        "Vehicles_In": vehicles_in,
        "Vehicles_Out": vehicles_out
    }
 )

hours = pd.date_range(end=pd.Timestamp.now(), periods=7 * 24, freq='h')  # last 7 days
vehicle_types = ['Car', 'Truck', 'Bus', 'Motorcycle']
data = pd.DataFrame({
        'Timestamp': np.tile(hours, len(vehicle_types)),
        'Vehicle Type': np.repeat(vehicle_types, len(hours)),
        'Count': np.random.poisson(lam=60, size=len(hours) * len(vehicle_types)),
})
data['Day'] = data['Timestamp'].dt.day_name()
data['Hour'] = data['Timestamp'].dt.hour


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
