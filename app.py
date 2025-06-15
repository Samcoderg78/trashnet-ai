import streamlit as st
import requests
from PIL import Image
import numpy as np
import google.auth
from google.auth.transport.requests import Request

# Vertex AI Endpoint Configuration
PROJECT_ID = "trashnet"  # Replace if different
ENDPOINT_ID = "1655826028523683840"
REGION = "us-central1"
PREDICTION_URL = f"https://{REGION}-aiplatform.googleapis.com/v1/projects/{PROJECT_ID}/locations/{REGION}/endpoints/{ENDPOINT_ID}:predict"

# Authentication
credentials, project = google.auth.default()
auth_req = Request()
credentials.refresh(auth_req)

st.title("♻️ AI Waste Classifier")

uploaded_file = st.file_uploader("Upload a waste image:", type=["jpg", "jpeg", "png"])
if uploaded_file:
    try:
        # Preprocess image
        img = Image.open(uploaded_file).resize((224, 224))
        img_array = np.array(img) / 255.0  # Normalize
        
        # Get fresh auth token
        credentials.refresh(auth_req)
        token = credentials.token
        
        # Send prediction request
        response = requests.post(
            PREDICTION_URL,
            headers={
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            },
            json={"instances": [img_array.tolist()]}
        )
        
        # Display results
        st.image(img, caption="Uploaded Image", use_column_width=True)
        
        if response.status_code == 200:
            prediction = response.json()["predictions"][0]
            st.success(f"Prediction: {prediction}")
        else:
            st.error(f"Error: {response.text}")
            
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
