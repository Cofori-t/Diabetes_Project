
import streamlit as st
import sklearn
import pickle
import pandas as pd
import numpy as np


st.sidebar.title(":blue[Control Panel]")

st.sidebar.subheader(" ",divider='rainbow' )

st.title("Am I a potential Diabetic Patient?")

st.write("""
## Project description
# Introduction

Diabetes is a disease that occurs when the blood glucose, also called blood sugar, is too high.

According to the International Diabetes Federation (IDF) data, 537 million people live with Diabetes, which may increase to 643 million by 2030 and to 783 million by 2045.

As my project work, I have created a model that could be used to predict the likelihood of Diabetes in patients based on their Medical history and Demographic details.:

Dependent Var: 
Gender, Age, Hypertension(Blood-Pressure), Heart Disease, Body Mass Index (BMI), Smoking history, HbA1c level, and Blood Glucose Level

Target Var: 
Diabetes. (Categorical outcome)

Machine Learning Algorithm using Logistic Regression Model.

""")

with st.container():
   
    st.sidebar.subheader(" :blue[1. Complete: questionnaire. 2. Click on: Submit Answers]")
    st.sidebar.write("##")
    
age = st.sidebar.slider('What is your age:blue[[Years]]?',1, 80, 3, 1)
hypertension = st.sidebar.number_input('Do you have a high blood pressure (Hypertension)?: :blue[No=0  Yes=1]',min_value=0, max_value=1)
heart_disease = st.sidebar.number_input('Do you have Heart_disease?: :blue[No=0  Yes=1]',min_value=0, max_value=1)
bmi = st.sidebar.slider('What is your BMI :blue[[kg/m**2]]',10.00, 96.00, 24.5,0.5)
HbA1c_level = st.sidebar.slider('What is your haemoglobin value :blue[(HbA1c_Level[%])]', 3.5, 9.0, 5.0, 0.1 )
blood_glucose_level = st.sidebar.slider('Your Glucose Level :blue[(Blood_Glucose_Level[mg/dL])]', 80, 300, 80, 5)
gender_num  = st.sidebar.number_input('What is your Gender (Gender_num): :blue[male=0  female=1  other=2]',min_value=0, max_value=2, step=1)
smoking_history_num  = st.sidebar.number_input('Your Smoking Habits (Smoking_History_num): :blue[No Info = -1  never = 0  former=1  current = 2  not_current = 3  ever = 4]',min_value=-1, max_value=4, step=1)

with st.container():
    new_input = pd.DataFrame({
                         "age":[age],
                         "hypertension":[hypertension], 
                         "heart_disease":[heart_disease],
                         "bmi":[bmi],
                         "HbA1c_level":[HbA1c_level],
                         "blood_glucose_level":[blood_glucose_level],
                         "gender_num":[gender_num],
                         "smoking_history_num":[smoking_history_num]
      
})


with st.container():
    pipe=pickle.load(open('pipe_pkl1','rb'))
    
    prediction = pipe.predict(new_input)
    
st.snow()

st.markdown("## Results ")

st.subheader(" " ,divider='rainbow' )

st.sidebar.subheader(" " ,divider='rainbow' )

if st.sidebar.button('Submit Answers',type="primary"):
  if (prediction[0]==1):
    st.write("# :red[Yes!!!! likely of been Diabetic]")
  else:
    st.write("# :green[No!! I am not Diabetic] 🎉")
    
st.subheader(" " ,divider='rainbow' ) 

# 7 add like for help
with st.container():
    
    st.title("Conclusion")
    st.write("""
             This model only detect, if there is a likelihood of being diabetic OR Not. 
             
             There are different of Types of Diabetes namely:
             
             TYPES: 1, 2, Pre-diabates, Gestational Diabetes.
             
             For further diagnosis, PLEASE consult your physician, who will:
             
             1. confirm on the Type, 
             
             2. give the needed Care Advice.   
             
             """)
    
    st.subheader("References" ,divider='rainbow') 
        
    st.subheader("""[More Information about Diabetes](https://worldpopulationreview.com/country-rankings/diabetes-rates-by-country) 
                   
                """)
    
    st.subheader("""[More Information about - BMI, HbA1c, Glucose_level ](https://www.forbes.com/health/body/normal-blood-sugar-levels/)""")
    

    st.subheader("""[Data source](https://www.kaggle.com/code/jayrdixit/diabetes-prediction/input?select=diabetes_prediction_dataset.csv)""")
    
    st.write("##")
    st.subheader(" " ,divider='rainbow' )

    
