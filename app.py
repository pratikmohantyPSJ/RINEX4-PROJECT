import streamlit as st 
import joblib 

#load the joblib model 
model_nb = joblib.load('')

#user input 
st.title("BMI PREDICTOR")
ip = st.text_input("Enter your weight:")
ip = st.text_input("Enter your height:")

#predict the bmi
op = model_nb.predict([ip])
if st.button('PREDICT'):
  st.title(op[0])  #prints the output - bmi  
