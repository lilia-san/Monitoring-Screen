import streamlit as st
import matplotlib.pyplot as plt
from streampages.Dataset import chart_data,data,vehicle_types
import pandas as pd
import numpy as np
import plotly.express as px
#import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

def traffic_chart():
    st.header("📊 Traffic Volume Analysis")

    # --- Step 1: Select Date ---
    date = st.date_input("Choose a specific date to display appropriate data")

    # Filter the data by date
    chart_data["Date"] = chart_data["Timestamp"].dt.date

    # --- Step 2: Choose Chart Type ---
    chart_type = st.radio("Select chart type:", ["Line Chart", "Bar Chart", "Pie Chart"], horizontal=True)

    # --- Step 3: Show Selected Chart ---
    st.write(f"**Traffic Volume displayed for:** {date}")

    if chart_type in ["Line Chart", "Bar Chart"]:
        if chart_type == "Line Chart":
            st.line_chart(chart_data, x="Hours", y=["Vehicles_In", "Vehicles_Out"], color=["#eb58d9", "#0000FF"])
        else:
            st.bar_chart(chart_data, x="Hours", y=["Vehicles_In", "Vehicles_Out"], color=["#eb58d9", "#0000FF"])

    elif chart_type == "Pie Chart":
        # Aggregate for pie chart
        s1 = chart_data["Vehicles_In"].sum()
        s2 = chart_data["Vehicles_Out"].sum()

        labels = ['Vehicles In', 'Vehicles Out']
        sizes = [s1, s2]
        explode = (0, 0.1)  # explode Out

        fig1, ax1 = plt.subplots()
        ax1.pie(
            sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90, colors=["#eb58d9", "#0000FF"]
        )
        ax1.axis('equal')  # Keep the pie a circle
        st.pyplot(fig1)

  
    # 2. Global Traffic Chart
    # -------------------------------
    st.subheader("📊 Total Traffic Over Time")

    total_traffic = data.groupby('Timestamp')['Count'].sum().reset_index()
    fig_total = px.line(total_traffic, x='Timestamp', y='Count',
                        title="Total Vehicle Count Over Time",
                        labels={"Count": "Vehicles"})
    st.plotly_chart(fig_total, use_container_width=True)

    # 3. Per-Vehicle-Type Charts
    # -------------------------------
    st.subheader("🚗 Traffic by Vehicle Type")

    vehicle_cols = st.columns(len(vehicle_types))

    for i, v_type in enumerate(vehicle_types):
        df_v = data[data['Vehicle Type'] == v_type].groupby('Timestamp')['Count'].sum().reset_index()
        fig = px.line(df_v, x='Timestamp', y='Count', title=f"{v_type} Count Over Time")
        vehicle_cols[i].plotly_chart(fig, use_container_width=True)
    
    # 5. Optional: Summary Stats
    # -------------------------------
    st.sidebar.title("🔎 Quick Stats")
    total_count = int(chart_data['Vehicles_In'].sum()) + int(chart_data['Vehicles_Out'].sum())
    st.sidebar.metric("📦 Total Vehicles Counted", f"{total_count:,}")

    # Add a new column with total traffic for each hour
    chart_data["Total"] = chart_data["Vehicles_In"] + chart_data["Vehicles_Out"]
    
    # Find the hour with the highest total traffic
    top_hour = chart_data.loc[chart_data["Total"].idxmax(), "Hours"]
    
    # Display in sidebar
    st.sidebar.metric("⏰ Busiest Hour", f"{top_hour}:00")

    top_type = data.groupby('Vehicle Type')['Count'].sum().idxmax()
    st.sidebar.metric("🚘 Most Frequent Vehicle", top_type)

