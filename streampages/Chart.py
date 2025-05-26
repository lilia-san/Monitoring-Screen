import streamlit as st
import matplotlib.pyplot as plt
from streampages.Dataset import chart_data
from datetime import datetime

def traffic_chart():
    date = st.date_input("Choose a specific date to display appropriate data")
    st.write("Data displayed for: ", date)
    #option = st.selectbox( "Please select your chart type", ("Line Charts", "Bar Charts", "Pie Charts"),)

    #if option == "Line Charts":
    st.line_chart(chart_data, x="Hours", y=["Vehicles_In", "Vehicles_Out"], color=["#eb58d9" , "#0000FF"], y_label="Number of Vehicles")
    #elif option == "Bar Charts":
    st.bar_chart(chart_data, x="Hours", y=["Vehicles_In", "Vehicles_Out"], color=["#eb58d9" , "#0000FF"], y_label="Number of Vehicles")
    #elif option == "Pie Charts":
    s1 = chart_data["Vehicles_In"].sum()
    s2 = chart_data["Vehicles_Out"].sum()
    labels = 'Vehicles_In', 'Vehicles_Out'
    sizes = [s1, s2]
    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90,colors=["#eb58d9" , "#0000FF"])
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot(fig1)

#traffic_chart()