import streamlit as st
import pickle
import pandas as pd

# --------------------------------------------------
# Load Model
# --------------------------------------------------

with open("laptop_price_model.pkl", "rb") as file:
    model = pickle.load(file)


# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Laptop Price Predictor",
    page_icon="💻",
    layout="centered"
)

st.title("💻 Laptop Price Predictor")
st.write("Enter the laptop specifications to estimate its price.")

st.divider()


# --------------------------------------------------
# Input Features
# --------------------------------------------------

brand = st.number_input(
    "Brand Code",
    min_value=0.0,
    value=0.0,
    help="Enter the numerical brand code used during model training."
)

spec_rating = st.number_input(
    "Specification Rating",
    min_value=0.0,
    value=50.0
)

ram = st.number_input(
    "RAM",
    min_value=1.0,
    value=8.0
)

ram_type = st.number_input(
    "RAM Type Code",
    min_value=0.0,
    value=0.0,
    help="Enter the numerical RAM type code used during training."
)

rom = st.number_input(
    "ROM / Storage",
    min_value=1.0,
    value=512.0
)

rom_type = st.number_input(
    "ROM Type Code",
    min_value=0.0,
    value=0.0,
    help="Enter the numerical ROM type code used during training."
)

display_size = st.number_input(
    "Display Size (inches)",
    min_value=1.0,
    value=15.6
)

resolution_width = st.number_input(
    "Resolution Width",
    min_value=1.0,
    value=1920.0
)

resolution_height = st.number_input(
    "Resolution Height",
    min_value=1.0,
    value=1080.0
)

os = st.number_input(
    "OS Code",
    min_value=0.0,
    value=0.0,
    help="Enter the numerical OS code used during training."
)

warranty = st.number_input(
    "Warranty",
    min_value=0.0,
    value=1.0
)


# --------------------------------------------------
# Prediction
# --------------------------------------------------

if st.button("🔮 Predict Laptop Price"):

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