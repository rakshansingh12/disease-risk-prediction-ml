import streamlit as st
import numpy as np
import joblib

# Title
st.title("🧬 Alzheimer’s Disease Risk Prediction")

st.write(
    "Upload a CSV file containing gene expression values "
    "to estimate Alzheimer’s disease probability."
)

# Load model and preprocessing objects
model = joblib.load("model_logistic.pkl")
scaler = joblib.load("scaler.pkl")
selected_indices = np.load("selected_gene_indices.npy")

# File uploader
uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    try:
        # Load data
        data = np.loadtxt(uploaded_file, delimiter=",")

        # Ensure correct shape
        if data.ndim == 1:
            data = data.reshape(1, -1)

        # Step 1: Log2 transform
        data_log = np.log2(data + 1)

        # Step 2: Scale
        data_scaled = scaler.transform(data_log)

        # Step 3: Select top genes
        data_selected = data_scaled[:, selected_indices]

        # Step 4: Predict
        prediction = model.predict(data_selected)
        probability = model.predict_proba(data_selected)[:, 1]

        st.subheader("Prediction Result")

        if prediction[0] == 1:
            st.error("Predicted Class: Alzheimer’s Disease")
        else:
            st.success("Predicted Class: Control")

        st.write(f"Alzheimer’s Risk Probability: {probability[0]:.4f}")

    except Exception as e:
        st.error(f"Error processing file: {e}")
