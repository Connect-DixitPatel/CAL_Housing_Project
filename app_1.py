import pickle
import streamlit as st
import numpy as np
import pandas as pd

# title of the app
st.title("California House Price Prediction for XYZ Brokerage Company") 

# load the model
model = pickle.load(open('Pickle_Model\model_Lin_reg.pkl', 'rb'))

# predict the price of the house for input cols
features = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']

# prompt the user to enter the input values
st.write("Enter the input values and predict the price of the house:")

user_input={}

for col in features:
    user_input[col]=st.number_input(f"Enter values for {col}", value=0.0)
    
# convert the user input into a dataframe
user_input_df= pd.DataFrame(user_input, index=[0])

# prediction button
if st.button("Predict_Price"):
    try:
        prediction = model.predict(user_input_df)
        st.write(f"Predicted Price for this particular house is: ${prediction[0]*100000} (USD)")
    except:
        st.write("Please enter valid values for all input features.")