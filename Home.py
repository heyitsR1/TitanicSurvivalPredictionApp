
import streamlit as st

st.set_page_config(page_title="Titanic Survival App", page_icon="🚢")
st.title("🚢 Titanic Survival Prediction App")


st.markdown("""
:titanic: Welcome to the **Titanic Survival Prediction App**!  
This app uses a machine learning model to predict whether a passenger would have survived the Titanic disaster.

---

### :clipboard: How to Use

1. Select **🧮 Predict Titanic Survival** from the sidebar.
2. Fill in passenger details (like age, sex, fare, class, etc.).
3. Click the **Predict Survival** button.
4. You'll see whether the passenger is :green[likely to survive] or :red[not survive], along with the probability.

---

### 🏫 Project Background

- This app was developed as part of a class workshop for **DATA200: Applied Statistical Analysis**,  
  led by **Professor Ayush Regmi**.
- The goal was to apply classification techniques and build an interpretable model using real-world data.

---

### 🤖 About the Model

We use a `scikit-learn` pipeline that includes preprocessing and a classification model. The classifier is a **Random Forest**, which performs well on non-linear data.

Example structure:

```python
Pipeline(steps=[
    ("preprocessing", preprocessor),
    ("classifier", RandomForestClassifier(random_state=42))
])
```
""")
