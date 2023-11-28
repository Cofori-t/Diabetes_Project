import streamlit as st

st.title("Test-Diabetes Prediction")

st.write("""
### Project description

Test

""")

import pickle
import pandas as pd

age = st.slider('Age[years]: Range 1-100', 1, 100)
hypertension = st.number_input('Hypertension: No=0  Yes=1',0, 1)
heart_disease = st.number_input('Heart_disease: No=0 Yes=1',0, 1)
bmi = st.slider('BMI[kg/m**2]: Range 16.0-80.0',16.0, 80.0)
HbA1c_level = st.slider('HbA1c_Level[%]: Range 4.0-10.0',4.0,10.0)
blood_glucose_level = st.slider('Blood_Glucose_Level[mg/dL]: Range 60-250', 60.0,250.0)
gender_num  = st.number_input('Gender_num: male=0 female=1 other=2',0,2)
smoking_history_num  = st.number_input('Smoking_History_num: No Info = -1, never = 0, former=1, current = 2,not current = 3, ever = 4',-1,4)
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

pickle_in=open('pipe_pkl1','rb')
pipe=pickle.load(pickle_in)

prediction = pipe.predict(new_input)
if (prediction[0]==1):
    st.write("The Person is Diabetic")
else:
    st.write("The Person is Not Diabetic")
    
