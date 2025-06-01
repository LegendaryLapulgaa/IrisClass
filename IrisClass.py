import streamlit as st
import numpy as np
import joblib

# Load the trained model
model = joblib.load('iris_classifier.pkl')

# Define feature input
st.title("Iris Flower Classifier 🌸")
st.write("Enter measurements to predict the species of an Iris flower.")

# Input fields
sepal_length = st.slider('Sepal length (cm)', 4.0, 8.0, 5.8)
sepal_width = st.slider('Sepal width (cm)', 2.0, 4.5, 3.0)
petal_length = st.slider('Petal length (cm)', 1.0, 7.0, 4.35)
petal_width = st.slider('Petal width (cm)', 0.1, 2.5, 1.3)

# Prediction
if st.button("Predict"):
    input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])
    prediction = model.predict(input_data)[0]
    
    # Optional: If your model returns numeric labels, map them to class names
    class_names = ["setosa", "versicolor", "virginica"]
    predicted_class = class_names[prediction]
    
    st.success(f"The predicted Iris species is: **{predicted_class}**")
