import streamlit as st
import numpy as np
import pickle

# Load model
model = pickle.load(open("model.pkl","rb"))

# Page config
st.set_page_config(
    page_title="Smart Crop Recommendation",
    page_icon="🌾",
    layout="wide"
)

# CSS Styling
st.markdown("""
<style>

.main-title{
text-align:center;
font-size:45px;
font-weight:bold;
color:white;
}

.header{
background: linear-gradient(90deg,#2E7D32,#66BB6A);
padding:25px;
border-radius:10px;
margin-bottom:25px;
}

.stButton>button{
width:100%;
background-color:#2E7D32;
color:white;
font-size:18px;
border-radius:10px;
height:3em;
}

.result{
background-color:#E8F5E9;
padding:25px;
border-radius:10px;
font-size:24px;
font-weight:bold;
text-align:center;
color:#1B5E20;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="header"><p class="main-title">🌾 Smart Crop Recommendation System</p></div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    ["Crop Recommendation", "About Project"]
)

# -------------------------
# MAIN PAGE
# -------------------------

if page == "Crop Recommendation":

    st.subheader("Enter Soil and Weather Conditions")

    col1, col2 = st.columns(2)

    with col1:

        N = st.number_input(
            "Nitrogen (kg/ha)",
            min_value=0,
            max_value=140,
            value=50
        )

        P = st.number_input(
            "Phosphorus (kg/ha)",
            min_value=5,
            max_value=145,
            value=50
        )

        K = st.number_input(
            "Potassium (kg/ha)",
            min_value=5,
            max_value=205,
            value=50
        )

        temperature = st.number_input(
            "Temperature (°C)",
            min_value=8.0,
            max_value=43.0,
            value=25.0
        )

    with col2:

        humidity = st.number_input(
            "Humidity (%)",
            min_value=14.0,
            max_value=100.0,
            value=60.0
        )

        ph = st.number_input(
            "Soil pH",
            min_value=3.5,
            max_value=10.0,
            value=6.5
        )

        rainfall = st.number_input(
            "Rainfall (mm)",
            min_value=20.0,
            max_value=300.0,
            value=100.0
        )

    # Predict button
    if st.button("🌱 Recommend Crop"):

        data = np.array([[N,P,K,temperature,humidity,ph,rainfall]])

        prediction = model.predict(data)[0]

        st.markdown(
            f'<div class="result">Recommended Crop: {prediction}</div>',
            unsafe_allow_html=True
        )

        # Crop images
        crop_images = {
            "rice":"https://upload.wikimedia.org/wikipedia/commons/6/6f/Rice_Plant.jpg",
            "maize":"https://upload.wikimedia.org/wikipedia/commons/0/0c/Maize.jpg",
            "cotton":"https://upload.wikimedia.org/wikipedia/commons/f/fd/CottonPlant.JPG",
            "banana":"https://upload.wikimedia.org/wikipedia/commons/8/8a/Banana_tree.jpg",
            "mango":"https://upload.wikimedia.org/wikipedia/commons/9/90/Hapus_Mango.jpg"
        }

        crop_tips = {
            "rice":"Rice grows best in high humidity and heavy rainfall.",
            "maize":"Maize grows well in warm climate with moderate rainfall.",
            "cotton":"Cotton requires warm temperature and well-drained soil.",
            "banana":"Banana needs tropical climate and regular irrigation.",
            "mango":"Mango grows well in warm climate and deep soil."
        }

        if prediction in crop_images:
            st.image(crop_images[prediction], width=400)

        if prediction in crop_tips:
            st.info("🌱 Growing Tip: " + crop_tips[prediction])


# -------------------------
# ABOUT PAGE
# -------------------------

elif page == "About Project":

    st.title("About This Project")

    st.write("""
This project predicts the **best crop to grow** based on soil nutrients and weather conditions.

### Features Used
- Nitrogen (kg/ha)
- Phosphorus (kg/ha)
- Potassium (kg/ha)
- Temperature (°C)
- Humidity (%)
- Soil pH
- Rainfall (mm)

### Machine Learning Model
We used **Random Forest Classifier** to train the model.

### Technology Stack
- Python
- Streamlit
- Scikit-learn
- Pandas
- NumPy
""")