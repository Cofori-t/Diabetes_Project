import streamlit as st
import sklearn
import pickle
import pandas as pd

#st.set_page_config(layout="wide",
                  #page_title="Prediction: Diabetes using Logistic Model",
    #page_icon="📽️")  # this needs to be the first Streamlit command

st.sidebar.title("Control Panel")
st.write("---")
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
#st.markdown("*Check out the [article](https://www.crosstab.io/articles/staged-rollout-analysis) for a detailed walk-through!*")
with st.container():
    # add a divider
    st.sidebar.write("---")
    #add header for the input part
    st.sidebar.subheader("1. Complete: questionnaire. 2. Click on: Submit Answers")
    st.sidebar.write("##")
    
#st.sidebar.subheader("Distribution of diabetic")

#import pickle
#import pandas as pd

#st.markdown("# Main page 🎈")
#st.sidebar.markdown("# Main page 🎈")

age = st.sidebar.number_input('What is your age[Years]?: Range 1 - 100',min_value=1, max_value=100, step=1)
hypertension = st.sidebar.number_input('Do you have a high blood pressure (Hypertension))? - Choose your answer: No=0  Yes=1', min_value=0, max_value=1, step=1)
heart_disease = st.sidebar.number_input('Do you have Heart_disease? - Choose your answer: No=0  Yes=1)',min_value=0, max_value=1, step=1)
bmi = st.sidebar.number_input('What is your BMI[kg/m**2] - Enter your value: Range 10.0 - 96.0)',min_value=10.0, max_value=96.0, step=.1)
HbA1c_level = st.sidebar.number_input('What is your haemoglobin value (HbA1c_Level[%]) - Enter your value: Range 3.0 - 10.0)',min_value=3.0, max_value=10.0, step=.1)
blood_glucose_level = st.sidebar.number_input('Your Glucose Level (Blood_Glucose_Level[mg/dL]) - Enter your value: range 60 - 250)', min_value=60, max_value=300, step=1)
gender_num  = st.sidebar.number_input('What is your Gender (Gender_num) -  Choose your answer: male=0  female=1  other=2)',min_value=0, max_value=2, step=1)
smoking_history_num  = st.sidebar.number_input('Your Smoking Habits (Smoking_History_num) - Choose your answer: No Info = -1  never = 0  former=1  current = 2  not_current = 3  ever = 4)',
                                               min_value=-1, max_value=4, step=1)
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

#pipe=pickle.load(open('WBS/ML/pipe.pkl1','rb'))
#load model and create new dataframe
with st.container():
    #pipe=pickle.load(open('WBS/ML/pipe_pkl1','rb'))
    pipe=pickle.load(open('pipe_pkl1','rb'))

# create a botton for prediction

#if st.sidebar.button('Submit Answers'):
    
    prediction = pipe.predict(new_input)
    

#st.markdown("# Results ")
st.markdown("# Results ")
if st.sidebar.button('Submit Answers'):
  if (prediction[0]==1):
    st.write("# Yes!!!! likely of been Diabetic")
  else:
    st.write("# No!! I am not Diabetic 🎉")
    

# 7 add like for help
with st.container():
    #add a divider
    st.write("---")
    st.title("Conclusion")
    st.write("""
            This model only detect, if there is a likelihood of being diabetic OR Not and not the Type.
            
            For further diagnosis, PLEASE consult your physician, who will confirm on which type, and remedies to take.
            
            There are different of Diabetes: TYPES: 1, 2, Pre-diabates, Gestational Diabetes. 
            
            Symptoms: thirsty, freq. Urination, Weight Loss, fatigue and weakness
            """)
    st.subheader("""[More Information about Diabetes]([https://www.worldpopulationreview.com/country-rankings/diabetes-rates-by-country])""")
    st.subheader("""[Data source](https://www.kaggle.com/code/jayrdixit/diabetes-prediction/input?select=diabetes_prediction_dataset.csv)""")
    
    st.write("##")
    st.write("---")
    
    
#from PIL import Image

#Load an image from a local file (e.g., 'sunrise.jpg')
#image = Image.open('sunrise.jpg')

#Display the image with an optional caption
#st.image(image, caption='Sunrise by the mountains')
