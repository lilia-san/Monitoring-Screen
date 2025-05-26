import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime

vehicles_in = np.random.randint(100, size=(24))
vehicles_out = np.random.randint(100, size=(24))
chart_data = pd.DataFrame(
    {
        "Hours": list(range(24)),
        "Vehicles_In": vehicles_in,
        "Vehicles_Out": vehicles_out
    }
 )



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
