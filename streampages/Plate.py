import streamlit as st
import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta
import string

    
# Generate random plate numbers with 2 letters + 4 digits
def generate_plate_number():
    letters = ''.join(random.choices(string.ascii_uppercase, k=2))
    digits = ''.join(random.choices(string.digits, k=4))
    return str(letters + digits)

# Generate a random date in 2025
def random_date_2025():
    start_date = datetime(2025, 1, 1)
    end_date = datetime(2025, 3, 31)
    random_days = random.randint(0, (end_date - start_date).days)
    return start_date + timedelta(days=random_days)

# Cache the generated DataFrame
@st.cache_data
def generate_data():
    areas = ['Saint Michel', 'Sikekodji', 'Quartier Jaq', 'Haie Vive', 'Marina', 'Zongo', 'Arconville', 'Ganhi', 'PK6', 'Cadjèhoun', 'Fidjrossè', 'Kouhounou']
    camera_numbers = list(range(1, 10))

    data = {
        "Plate Number": [generate_plate_number() for _ in range(100)],
        "Date": [random_date_2025().strftime('%Y-%m-%d') for _ in range(100)],
        "Area": [random.choice(areas) for _ in range(100)],
        "Camera Number": [random.choice(camera_numbers) for _ in range(100)]
    }
    return pd.DataFrame(data)

def tracking():
    st.title("Plate Number Tracking")
    df = generate_data()
    st.dataframe(df)

    plate = st.text_input("Enter Plate Number:")

    if st.button("Search"):
        if plate in df['Plate Number'].values:
            st.success("Plate found!")
            st.write(df[df['Plate Number'] == plate])
        else:
            st.error("Plate not found.")
