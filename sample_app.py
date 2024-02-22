import streamlit as st
import joblib

# Load the trained model
random_forest_model = joblib.load('random_forest_model.pkl')

# Define the function to make predictions
def predict_not_fully_paid(features):
    prediction = random_forest_model.predict(features)
    return prediction

# Create the Streamlit web app
st.title('Loan Repayment Prediction')

# Add input fields for user input
feature_names = X_train.columns.tolist()
user_input = {}
for feature in feature_names:
    user_input[feature] = st.number_input(f'Enter {feature}', value=0.0)

# Convert user input into a DataFrame
input_df = pd.DataFrame([user_input])

# Add a button to make predictions
if st.button('Predict'):
    prediction = predict_not_fully_paid(input_df)
    st.write('Prediction:', prediction)
