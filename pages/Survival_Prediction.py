import streamlit as st
import pandas as pd
import pickle
import random

# Load model
with open("models/model_pipeline.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Prediction", page_icon="🧮", layout="wide")
st.title("🧮 Predict Titanic Survival")

# Layout: 2 main columns (Details | Summary + Prediction)
col1, col2 = st.columns([1, 1])

# Passenger Input
with col1:
    st.header("👤 Passenger Details")
    sex = st.selectbox("Sex", ["male", "female"])
    age = st.slider("Age", 0, 80, 30)
    fare = st.slider("Fare", 0.0, 500.0, 50.0)
    pclass = st.selectbox("Passenger Class", [1, 2, 3])
    sibsp = st.number_input("Siblings/Spouses aboard", min_value=0, max_value=10, value=0)
    parch = st.number_input("Parents/Children aboard", min_value=0, max_value=10, value=0)
    embarked = st.selectbox("Port of Embarkation", ["C", "Q", "S"])
    title = st.selectbox("Title", ["Mr", "Mrs", "Miss", "Master", "Other"])

    input_df = pd.DataFrame({
        'sex': [sex],
        'age': [age],
        'fare': [fare],
        'pclass': [pclass],
        'sibsp': [sibsp],
        'parch': [parch],
        'embarked': [embarked],
        'title': [title]
    })

    predict = st.button("🔍 Predict Survival")

# Passenger Summary + Prediction Output
with col2:
    st.header("🏄‍♂️ Passenger Summary")
    st.markdown(f"""
    - **Sex:** {sex}  
    - **Age:** {age}  
    - **Fare:** ${fare}  
    - **Class:** {pclass}  
    - **Siblings/Spouses Aboard:** {sibsp}  
    - **Parents/Children Aboard:** {parch}  
    - **Embarked at:** {embarked}  
    - **Title:** {title}  
    """)

    # Display prediction result if Predict button is clicked
    if predict:
        st.markdown("---")
        st.subheader("📈 Prediction Result")
        prediction = model.predict(input_df)[0]
        probability = model.predict_proba(input_df)[0][1]

        if prediction == 1:
            st.success(f"✅ Passenger is likely to survive (Probability: {probability:.2%})")
        else:
            st.error(f"❌ Passenger is likely to not survive (Probability: {probability:.2%})")

    st.markdown("---")
    st.caption("🌊 *Titanic Fact:*")
    facts = [
        "Titanic sank in less than 3 hours after hitting the iceberg.",
        "The ship's band played music as it sank.",
        "Only one lifeboat returned to look for survivors.",
        "There were not enough lifeboats for everyone onboard.",
        "Titanic had a gym, a pool, and its own newspaper.",
    ]
    st.info(random.choice(facts))
