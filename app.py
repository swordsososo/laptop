import streamlit as st
import joblib
import pandas as pd

# Load model
model = joblib.load("laptop_price_model")

# Page configuration
st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Predictor")
st.write("Enter the laptop specifications below to predict its price.")

st.divider()

# -----------------------------
# User Inputs
# -----------------------------

brand = st.selectbox(
    "Brand",
    [
        "Acer",
        "Apple",
        "Asus",
        "Dell",
        "HP",
        "Lenovo",
        "MSI",
        "Microsoft",
        "Samsung",
        "Other"
    ]
)

spec_rating = st.number_input(
    "Specification Rating",
    min_value=0.0,
    max_value=100.0,
    value=50.0
)

ram = st.number_input(
    "RAM",
    min_value=1,
    max_value=128,
    value=8
)

ram_type = st.selectbox(
    "RAM Type",
    [
        "DDR3",
        "DDR4",
        "DDR5",
        "LPDDR3",
        "LPDDR4",
        "LPDDR4X",
        "LPDDR5",
        "Other"
    ]
)

brand_map = {
    "Acer": 0,
    "Apple": 1,
    "Asus": 2
}

rom = st.number_input(
    "ROM / Storage",
    min_value=1,
    max_value=8192,
    value=512
)

rom_type = st.selectbox(
    "ROM Type",
    [
        "SSD",
        "HDD",
        "eMMC",
        "Hybrid",
        "Other"
    ]
)

display_size = st.number_input(
    "Display Size (inches)",
    min_value=10.0,
    max_value=20.0,
    value=15.6
)

resolution_width = st.number_input(
    "Resolution Width",
    min_value=640,
    max_value=8000,
    value=1920
)

resolution_height = st.number_input(
    "Resolution Height",
    min_value=480,
    max_value=5000,
    value=1080
)

os = st.selectbox(
    "Operating System",
    [
        "Windows",
        "macOS",
        "Linux",
        "Chrome OS",
        "DOS",
        "Other"
    ]
)

warranty = st.number_input(
    "Warranty (years)",
    min_value=0,
    max_value=10,
    value=1
)

# -----------------------------
# Prediction
# -----------------------------

if st.button("🔮 Predict Laptop Price"):

    # IMPORTANT:
    # These columns must be in exactly the same
    # order as the model's training features.

    input_data = pd.DataFrame({
        "brand": [brand],
        "spec_rating": [spec_rating],
        "Ram": [ram],
        "Ram_type": [ram_type],
        "ROM": [rom],
        "ROM_type": [rom_type],
        "display_size": [display_size],
        "resolution_width": [resolution_width],
        "resolution_height": [resolution_height],
        "OS": [os],
        "warranty": [warranty]
    })

    try:
        prediction = model.predict(input_data)

        st.success(
            f"💰 Predicted Laptop Price: Rs. {prediction[0]:,.2f}"
        )

    except Exception as e:
        st.error("Prediction failed.")
        st.exception(e)