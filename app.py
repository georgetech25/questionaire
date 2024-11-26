import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
import joblib

# Load pre-trained model (replace 'model.pkl' with your model file)
# Ensure the model is trained beforehand
# 
model = joblib.load('virological_model')

st.set_page_config(
    page_title='Eces Ace5',
    page_icon='ecew.jpeg'
)
    



# App Title
st.title("Virological Status Prediction")

# Sections Based on Questionnaire
st.header("Demographic Information")
Age = st.text_input("Age")
Gender = st.selectbox("Gender: (0 for MALE, 1 for FEMALE, 2 for OTHER)",[0,1,2])
Education_Level = st.selectbox("Education Level:  (0 for NO EDUCATION, 1 for PRIMARY, 2 for SECONDARY, 3 for HIGHER EDUCATION)",[0 ,1, 2 , 3] )
Marital_Status = st.selectbox("Marital Status:  (0 for SINGLE, 1 for MARRIED, 2 DIVORCE, 3 for WIDOWED)",[0,1,2,3])

st.header("Treatment History")
ART_Duration = st.text_input("Duration on ART")
Changed_Regimen = st.selectbox("Changed ART Regimen? (0 for NO, 1 for YES)", [0,1])
Side_Effects = st.selectbox("Experienced Side Effects? (0 for NO, 1 for YES)", [0,1])

st.header("Adherence to Treatment")
Adherence = st.selectbox("Adherence to Medication? (0 for RARELY, 1 for SOMETIMES, 2 for ALWAYS)", [0,1,2])
Missed_Doses = st.text_input("Missed Doses in a Month")

st.header("Clinical Information")
Viral_Load = st.selectbox("Last Viral Load Test : (0 for UNKNWON, 1 for UNDETECTED, 2, for DETECTED)", [0,1,2])
CD4_Count = st.text_input("Last CD4 Count Result")

st.header("Behavioral and Lifestyle Data")
Smoking = st.selectbox("Do you smoke? (0 for NO, 1 for YES)", [0,1])
Alcohol = st.selectbox("Do you consume alcohol?  (0 for NO, 1 for YES) ",[0,1])
Recreational_Drugs = st.selectbox("Do you use recreational drugs?  (0 for NO, 1 for YES)",[0,1])

# Collect Input Data
# input_data = {
#     "age": Age,
#     "gender": Gender,
#     "education": Education_Level,
#     "marital_status": Marital_Status,
#     "art_duration": ART_Duration,
#     "changed_regimen": Changed_Regimen,
#     "side_effects": Side_Effects,
#     "adherence": Adherence,
#     "missed_doses": Missed_Doses,
#     "viral_load": Viral_Load,
#     "cd4_count": CD4_Count,
#     "smoking": Smoking,
#     "alcohol": Alcohol,
#     "recreational_drugs": Recreational_Drugs,
# }

# DataFrame for model input
# input_df = pd.DataFrame([input_data])

# Prediction
if st.button("PREDICT"):
    prediction = model.predict([[Age,Gender,Education_Level,Marital_Status,ART_Duration	,Changed_Regimen,Side_Effects,Adherence,	Missed_Doses,Viral_Load,	CD4_Count,Smoking,Alcohol,Recreational_Drugs]])
    output = round(prediction[0],2)
    st.success('Your Virological prediction is  :  {}   '. format(output))
    
    
    if prediction ==0:
        st.write('You are Virologically Suppressed and your Treatment status is GOOD')
    else:
        st.write('You are Virologically Unsuppressed and your Treatment status is BAD, Go for Adherence Councelling')