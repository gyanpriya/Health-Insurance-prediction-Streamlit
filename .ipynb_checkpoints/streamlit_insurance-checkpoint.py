#Streamlit 
import streamlit as st
import pickle

# Inject custom CSS
st.markdown(
    """
    <style>
    body {
        background-color: black;
        color: white;
    }
    .stButton>button {
        background-color: #1f77b4;
        color: white;
    }
    .stTextInput>div>input {
        color: black;
    }
    .stSelectbox>div>select {
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Load the models
with open('gb_model.pkl', 'rb') as f:
    gradient_model = pickle.load(f)

with open('rf_model.pkl', 'rb') as f:
    random_forest_model = pickle.load(f)

# Define the function to make predictions
def predict_insurance_price(model, input_data):
    prediction = model.predict([input_data])
    return prediction[0]

# Streamlit app
st.title('Insurance Cost Prediction')

# Define columns for layout
col1, col2 = st.columns(2)

# Input fields
with col1:
    age = st.number_input('Age', min_value=0, max_value=120, value=25)
    diabetes = st.selectbox('Diabetes', ['No', 'Yes'])
    blood_pressure = st.selectbox('Blood Pressure Problems', ['No', 'Yes'])
    transplants = st.selectbox('Any Transplants', ['No', 'Yes'])
    chronic_diseases = st.selectbox('Any Chronic Diseases', ['No', 'Yes'])

with col2:
    height = st.number_input('Height (cm)', min_value=50, max_value=250, value=170)
    weight = st.number_input('Weight (kg)', min_value=30, max_value=200, value=70)
    allergies = st.selectbox('Known Allergies', ['No', 'Yes'])
    cancer_history = st.selectbox('History Of Cancer In Family', ['No', 'Yes'])
    major_surgeries = st.number_input('Number Of Major Surgeries', min_value=0, max_value=10, value=0)

# Convert categorical inputs to numerical values
diabetes = 1 if diabetes == 'Yes' else 0
blood_pressure = 1 if blood_pressure == 'Yes' else 0
transplants = 1 if transplants == 'Yes' else 0
chronic_diseases = 1 if chronic_diseases == 'Yes' else 0
allergies = 1 if allergies == 'Yes' else 0
cancer_history = 1 if cancer_history == 'Yes' else 0

# Input data
input_data = [age, diabetes, blood_pressure, transplants, chronic_diseases, height, weight, allergies, cancer_history, major_surgeries]

# Predict buttons
if st.button('Predict Insurance Price using Gradient Boosting Model'):
    prediction = predict_insurance_price(gradient_model, input_data)
    st.write(f'Predicted Insurance Price (Gradient Boosting): ${prediction:.2f}')

if st.button('Predict Insurance Price using Random Forest Model'):
    prediction = predict_insurance_price(random_forest_model, input_data)
    st.write(f'Predicted Insurance Price (Random Forest): ${prediction:.2f}')