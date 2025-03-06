import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

# A simple mock model that predicts demand based on user inputs
def mock_predict_demand(weather_condition, charging_slots_available):
    """
    A mock function to simulate a demand prediction. 
    In reality, this would be replaced with an actual model prediction.
    """
    weather_mapping = {'Sunny': 1, 'Cloudy': 0.8, 'Rainy': 0.5, 'Snowy': 0.2}
    weather_factor = weather_mapping.get(weather_condition, 0.5)  # Default to 'Rainy' if not found
    
    # Simulate prediction logic based on weather and available charging slots
    predicted_demand = charging_slots_available * weather_factor
    return predicted_demand

# Streamlit UI
st.title("EV Charging Station Demand Prediction")
st.write("Enter the details of the station to predict the demand.")

# Collect user inputs
station_id = st.number_input("Station ID", min_value=0, max_value=100, value=1)
weather_condition = st.selectbox(
    "Weather Condition", ["Sunny", "Cloudy", "Rainy", "Snowy"], index=0
)
charging_slots_available = st.number_input(
    "Charging Slots Available", min_value=0, max_value=50, value=10
)

# Predict button
if st.button("Predict Demand"):
    # Simulate demand prediction using mock model
    prediction = mock_predict_demand(weather_condition, charging_slots_available)
    
    # Show the predicted demand
    st.write(f"Predicted Demand: {prediction:.5f}")
    
    # You could add more info, such as an explanation or advice
    st.write("Higher predicted demand suggests more need for charging slots.")