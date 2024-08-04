import pickle
import streamlit as st

st.header("Insurance Premium Prediction")

col1, col2 = st.columns(2)

Age = st.number_input('Please enter your Age', 18, 100)
Height = col1.number_input('Please enter your height', 130, 200)
Weight = col2.number_input('Please enter your weight', 50, 300)

Diabetes = col1.selectbox(" Are you having Diabetes ",
['No','Yes'])
BPProblems = col1.selectbox(" Are you having BP",
['No','Yes'])
AnyTransplants = col1.selectbox(" Did you had any Transplants ",
['No','Yes'])
AnyChronicDiseases = col2.selectbox(" Are you Diagnosed with any Chronic diseases ",
['No','Yes'])
KnownAllergies = col2.selectbox(" Are you having any Allergies ",
['No','Yes'])
HistoryOfCancer = col2.selectbox(" Are you having any History of Cancer in your Family ",
['No','Yes'])

NumberofMajorSurgeries = st.number_input('Any number of major surgeries you undergone ', 0, 3)

encode_values = {
"Diabetes": {"Yes":1,"No":0},
"BPProblems": {"Yes":1,"No":0},
"AnyTransplants": {"Yes":1,"No":0},
"AnyChronicDiseases": {"Yes":1,"No":0},
"KnownAllergies": {"Yes":1,"No":0},
"HistoryOfCancer": {"Yes":1,"No":0}
}

def model_pred(Diabetes_e, BPProblems_e, AnyTransplants_e, AnyChronicDiseases_e,
                    KnownAllergies_e, HistoryOfCancer_e, Age, Height, Weight, NumberofMajorSurgeries):
 with open('IA.pkl','rb') as file:
  model = pickle.load(file)
  new_X = [[Age,Diabetes_e,BPProblems_e,AnyTransplants_e,AnyChronicDiseases_e,Height,
            Weight,KnownAllergies_e,HistoryOfCancer_e,NumberofMajorSurgeries]]
  return model.predict(new_X)


if(st.button("Predict Premium Price")):
 Diabetes_e=encode_values["Diabetes"][Diabetes]
 BPProblems_e = encode_values["BPProblems"][BPProblems]
 AnyTransplants_e = encode_values["AnyTransplants"][AnyTransplants]
 AnyChronicDiseases_e = encode_values["AnyChronicDiseases"][AnyChronicDiseases]
 KnownAllergies_e = encode_values["KnownAllergies"][KnownAllergies]
 HistoryOfCancer_e = encode_values["HistoryOfCancer"][HistoryOfCancer]

 price = model_pred(Diabetes_e, BPProblems_e, AnyTransplants_e, AnyChronicDiseases_e,
                    KnownAllergies_e, HistoryOfCancer_e, Age, Height, Weight, NumberofMajorSurgeries)
 st.text("Predicted Premium Price is: "+str(price))







