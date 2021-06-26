import streamlit as st 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import altair as alt

from pycaret.classification import load_model, predict_model

#---------------------------------------------------------------

#load model
model = load_model("machine_failure_classifier")

#----------------------------------------------------------------

@st.cache
def load_dataframe(data):
    df = pd.read_csv(data) #read the csv file
    return df #return the dataframe

def predict(model, input_df):
    predictions_df = predict_model(estimator=model, data=input_df)
    predictions = predictions_df['Label'][0]
    return predictions

#----------------------------------------------------------------

def run():

    st.title('Make predictions on sensors data')

    type_variable = st.radio("Type", ['M', 'L', 'H'])

    air_temperature = st.number_input("Air Temperature (in Kelvin)",
    min_value=295.0, max_value=305.0, value=298.0)

    process_temperature = st.number_input("Process Temperature (in Kelvin)", 
    min_value = 305.0, max_value = 315.0, value = 310.0)

    rotational_speed = st.number_input("Rotational Speed (in rpm)", 
    min_value = 1165.0, max_value = 2890.0, value = 1535.0)

    torque = st.number_input("Torque (in Newton-Metre)", min_value = 3.8, max_value = 76.6,
    value = 40.5)

    tool_wear = st.number_input("Tool Wear (in Minutes)", min_value = 0.1, max_value = 253.0,
    value = 107.0)

    input_dict = {
        'type': type_variable,
        'air temperature': air_temperature,
        'process temperature': process_temperature,
        'rotational speed': rotational_speed,
        'torque': torque,
        'tool wear': tool_wear
    }

    input_data = pd.DataFrame([input_dict])
    st.table(input_data)

    if st.button("Predict"):
        output_result = predict(model, input_data)
        if output_result == 0:
            st.success("There are less chances of an engine failure!!")
        elif output_result == 1:
            st.error("High possibility of an engine failure!!")        

if __name__ == '__main__':
     run()
