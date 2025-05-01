# Import the Streamlit library for creating web applications easily.
import streamlit as st

# Import the joblib library for loading our saved machine learning model.
import joblib

# Load the trained spam detection model from the specified file path.
# We're using joblib.load() to load the pickled Pipeline object.
model = joblib.load('../models/spam_model.pkl')

# Set the title of the Streamlit web application. This will appear at the top of the page.
st.title("Spam Message Classifier")

# Create a text area input widget where the user can enter a message.
# The label "Enter a message:" will be displayed above the text area.
message = st.text_area("Enter a message:")

# Create a button labeled "Predict".
# The code inside the 'if' block will be executed when this button is clicked.
if st.button("Predict"):
    # Make a prediction using the loaded model.
    # model.predict() expects a list of text messages to predict on.
    # We're passing a list containing the single message entered by the user.
    prediction = model.predict([message])
    
    # Display the prediction result.
    # If the prediction is 1, we display "SPAM"; otherwise (if it's 0), we display "HAM".
    # prediction[0] accesses the first (and only) element of the prediction array.
    st.write("Result:", "SPAM" if prediction[0] == 1 else "HAM")