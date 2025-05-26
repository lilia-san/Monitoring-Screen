import pandas as pd
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from sklearn.svm import SVC
from sklearn.metrics import *
from datetime import datetime
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier 
from sklearn.ensemble import GradientBoostingClassifier

def processing():
    scaler = StandardScaler()
    encoder = LabelEncoder()

    df = pd.read_csv("TrafficTwoMonth.csv")
   
    x = df.iloc[:,[2,7]]
    y = df.iloc[:,-1]

    x = pd.get_dummies(x, columns=['Day of the week']).astype(int)

    x[["Total"]] = scaler.fit_transform(x[["Total"]])
    y = encoder.fit_transform(y)
    return (x, y)


def training_model(x,y,model_name):
    x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2,random_state=0)
    results = model_name(random_state = 0)
    results.fit(x_train, y_train)
    y_pred = results.predict(x_test)
    cm = confusion_matrix(y_test,y_pred)
    return (y_test, y_pred)


def evaluate_model(y_true, y_pred, model_name):
    acc = accuracy_score(y_true, y_pred)
    rec = recall_score(y_true, y_pred,average="macro")
    f1 = f1_score(y_true, y_pred,average="macro")
    return {"Model": model_name, "ACC": acc, "REC": rec, "F1": f1}


def show_case(results):
    df_results = pd.DataFrame(results)

    # Display Data Table
    st.subheader("Model Performance Metrics")
    st.dataframe(df_results)

    # Plot Grouped Bar Chart
    st.subheader("Model Comparison: Accuracy (ACC), Recall (REC), F1-score (F1)")

    metrics = ["ACC", "REC", "F1"]
    models = df_results["Model"]
    x = np.arange(len(models))  # the label locations
    width = 0.2  # the width of the bars

    fig, ax = plt.subplots(figsize=(10, 6))
    
    for i, metric in enumerate(metrics):
        ax.bar(x + i * width, df_results[metric], width, label=metric)

    ax.set_xlabel("Model")
    ax.set_ylabel("Score")
    ax.set_title("Model Comparison by Metric")
    ax.set_xticks(x + width)
    ax.set_xticklabels(models, rotation=45)
    ax.legend()
    ax.grid(axis='y', linestyle='--', alpha=0.7)

    st.pyplot(fig)

def prediction():
    x,y = processing()
    y_test, y_rfc_pred = training_model(x,y,RandomForestClassifier)
    rf_results = evaluate_model(y_test, y_rfc_pred, "RandomForest Classifier")

    y_test, y_svc_res_pred = training_model(x,y,SVC)
    svc_res_results = evaluate_model(y_test, y_svc_res_pred, "SVM")

    y_test, y_gbm_pred = training_model(x,y,GradientBoostingClassifier)
    gbm_results = evaluate_model(y_test, y_gbm_pred, "Gradient Boosting")   

    results = [rf_results,  svc_res_results, gbm_results]
    show_case(results)

#prediction()