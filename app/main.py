# app.py
import streamlit as st
from prediction_helper import predict, compute_derived_features

st.set_page_config(page_title="🥤 CodeX Beverage Price Predictor", layout="wide")

st.markdown("<h1 style='text-align: center;'>🥤 CodeX Beverage Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Your inputs instantly generate hidden scores (ZAS, CF_AB, BSI) — used by our model to predict your beverage price range.</p>", unsafe_allow_html=True)
st.markdown("---")

# --- Input Controls (outside form so they update dynamically)
st.header("👤 Demographics")
col1, col2 = st.columns(2)
with col1:
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    occupation = st.selectbox("Occupation", ['Working Professional', 'Student', 'Entrepreneur', 'Retired'])
    gender = st.radio("Gender", ['M', 'F'], horizontal=True)
with col2:
    zone = st.selectbox("Zone", ['Semi-Urban', 'Urban', 'Metro', 'Rural'])
    income_level = st.selectbox("Income Level", ['<10L', '10L - 15L', '16L - 25L', '26L - 35L', '> 35L', 'Not Reported'])

st.header("🥤 Consumption Behavior")
col3, col4 = st.columns(2)
with col3:
    consume_frequency = st.selectbox("Consume Frequency (Weekly)", ['0-2 times', '3-4 times', '5-7 times'])
    current_brand = st.selectbox("Current Brand", ['Newcomer', 'Established'])
    size = st.selectbox("Preferable Consumption Size", ['Small (250 ml)', 'Medium (500 ml)', 'Large (1 L)'])
with col4:
    awareness = st.selectbox("Awareness of Other Brands", ['0 to 1', '2 to 4', 'above 4'])
    reasons = st.selectbox("Reasons for Choosing Brands", ['Availability', 'Quality', 'Price', 'Brand Reputation'])

st.header("🎨 Preferences")
col5, col6 = st.columns(2)
with col5:
    flavor = st.selectbox("Flavor Preference", ['Traditional', 'Exotic'])
    purchase_channel = st.selectbox("Purchase Channel", ['Online', 'Retail Store'])
with col6:
    packaging = st.selectbox("Packaging Preference", ['Simple', 'Premium', 'Eco-Friendly'])
    health_concerns = st.selectbox("Health Concerns", [
        'Low (Not very concerned)',
        'Medium (Moderately health-conscious)',
        'High (Very health-conscious)'
    ])
    consumption_situation = st.selectbox("Typical Consumption Situations", [
        'Social (eg. Parties)', 'Active (eg. Sports, gym)', 'Casual (eg. At home)'
    ])

# --- Prepare Input Dict
input_dict = {
    "age": age,
    "gender": gender,
    "zone": zone,
    "occupation": occupation,
    "income_levels": income_level,
    "consume_frequency(weekly)": consume_frequency,
    "current_brand": current_brand,
    "preferable_consumption_size": size,
    "awareness_of_other_brands": awareness,
    "reasons_for_choosing_brands": reasons,
    "flavor_preference": flavor,
    "purchase_channel": purchase_channel,
    "packaging_preference": packaging,
    "health_concerns": health_concerns,
    "typical_consumption_situations": consumption_situation
}

# --- Live Derived Feature Calculation
derived = compute_derived_features(input_dict)

st.markdown("### 📊 Derived Numerical Scores (auto-updating)")
colA, colB, colC = st.columns(3)
with colA:
    st.metric("ZAS Score", f"{derived['zas_score']:.2f}")
with colB:
    st.metric("CF_AB Score", f"{derived['cf_ab_score']:.2f}")
with colC:
    st.metric("BSI", f"{derived['bsi']:.2f}")

# --- Predict Button (after seeing derived values)
if st.button("🎯 Predict Price Range"):
    prediction = predict(input_dict)
    st.markdown(
        f"<h2 style='text-align: center; color: green;'>💡 Predicted Price Range: <b>{prediction}</b></h2>",
        unsafe_allow_html=True
    )
