import streamlit as st
import pandas as pd
import pickle
import numpy as np
from fpdf import FPDF

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="Diabetes Prediction App",
    page_icon="🩺",
    layout="centered"
)

st.markdown("""
<style>

/* ================= BACKGROUND WITH MEDICAL ICONS ================= */
.stApp {
    background-color: #000000;
    background-image: url("data:image/svg+xml;utf8,
    <svg xmlns='http://www.w3.org/2000/svg' width='200' height='200' viewBox='0 0 200 200'>
        <g fill='none' stroke='rgba(255,255,255,0.08)' stroke-width='2'>
            <path d='M40 20 v30 h-10 v20 h10 v30 h20 v-30 h10 v-20 h-10 v-30z'/>
            <circle cx='150' cy='50' r='15'/>
            <path d='M130 120 h40 v10 h-40z'/>
            <path d='M60 150 l20 -20 l20 20'/>
            <circle cx='150' cy='150' r='10'/>
        </g>
    </svg>");
    background-repeat: repeat;
    background-size: 180px;
    font-family: 'Segoe UI', sans-serif;
}

/* ================= GLASS EFFECT MAIN CONTAINER ================= */
.block-container {
    background: rgba(15, 15, 15, 0.7);
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    border-radius: 20px;
    padding: 2rem;
}

/* ================= HEADINGS ================= */
h1 {
    color: #ffffff !important;
    font-weight: 700;
}

h2, h3, h4, h5 {
    color: #e5e5e5 !important;
    font-weight: 600;
}

/* ================= TEXT ================= */
p, label, span {
    color: #dcdcdc !important;
}

/* ================= INPUT FIELDS ================= */
input, textarea, select {
    background-color: rgba(30,30,30,0.95) !important;
    color: #ffffff !important;
    border-radius: 10px !important;
    border: 1px solid #333333 !important;
}

/* ================= BUTTON ================= */
.stButton > button {
    background: linear-gradient(135deg, #4facfe, #00f2fe);
    color: #000000;
    font-weight: 700;
    border-radius: 14px;
    padding: 0.6em 1.8em;
    border: none;
}

.stButton > button:hover {
    transform: scale(1.03);
}

/* ================= SIDEBAR ================= */
section[data-testid="stSidebar"] {
    background-color: rgba(5,5,5,0.95);
}

section[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

/* ================= REMOVE WHITE HEADER ================= */
div[data-testid="stHeader"] {
    background: transparent !important;
}

</style>
""", unsafe_allow_html=True)
# ------------------ LOAD MODEL ------------------
with open("rf_model.pkl", "rb") as model_file:
    rfc = pickle.load(model_file)

def predict_diabetes(features):
    return rfc.predict([features])[0]

def get_recipe_table():
    recipes = pd.DataFrame({
        "Recipe Name": [
            "Oats Porridge",
            "Vegetable Omelette",
            "Sprouts Salad",
            "Idli Sambar",
            "Vegetable Upma",
            "Dal Tadka",
            "Paneer Curry",
            "Vegetable Khichdi",
            "Vegetable Soup",
            "Grilled Chicken",
            "Vegetable Stir Fry"
        ],

        "YouTube Recipe Link": [
            "https://youtu.be/niLP5pLD4UQ?si=XZBO--ELKwuWwUMi",
            "https://youtu.be/dQw5jddxsvI?si=NNtEsd4jCT6ss4sW",
            "https://youtu.be/F98AxI4dNmM?si=eKERSVbSQtVPmQa3",
            "https://youtu.be/C_HqlzkWHo0?si=8JsBv6aCUq6IajLr",
            "https://youtu.be/KNsC1GIhT0Q?si=1mntGrn7y5XuTQ-a",
            "https://youtu.be/1QT2bDBsrYw?si=C7WkEdF6GC_KetHZ",
            "https://youtu.be/U1LVDFwi8qI?si=wuwZiWMknfEXZs83",
            "https://youtu.be/65OiSh2jSPw?si=YWQfgLjbkgu91QEO",
            "https://youtu.be/pQP0wYejBes?si=LeXpoaOursOmLaqI",
            "https://youtu.be/Wmnaqwa4-1E?si=d8KgGV3qsxzBKsaE",
            "https://youtu.be/gBlBuj_rBuw?si=LaqFeRyMztvlS20i"
        ]
    })

    return recipes
def show_recipe_table():
    st.subheader("🍽️ Healthy Recipe Videos (Click to Watch)")
    recipe_df = get_recipe_table()
    st.table(recipe_df)

def diabetic_recommendations():
    st.warning("🍽️ Recommended Diet for Diabetic Patient")
    st.markdown("""
    - 🥦 Green vegetables (spinach, broccoli)
    - 🍎 Low sugar fruits (apple, berries, guava)
    - 🌾 Whole grains (brown rice, oats)
    - 🥜 Nuts & seeds (almonds, walnuts)
    - 🐟 Lean protein (fish, eggs, pulses)

    ❌ Avoid:
    - Sugary foods & drinks
    - White bread, white rice
    - Fried & junk foods
    """)

    st.info("🩺 Healthcare & Lifestyle Tips")
    st.markdown("""
    - Monitor blood sugar regularly
    - Walk or exercise 30 mins daily 🚶‍♂️
    - Take medicines/insulin as prescribed
    - Maintain healthy weight
    - Visit doctor regularly
    """)


def non_diabetic_recommendations():
    st.success("🥗 Healthy Diet to Stay Diabetes-Free")
    st.markdown("""
    - Balanced diet with vegetables & fruits
    - Whole grains instead of refined foods
    - Adequate water intake 💧
    - Limit sugar & processed foods
    """)

    st.info("🛡️ Preventive Healthcare Tips")
    st.markdown("""
    - Exercise at least 30 mins daily 🏃‍♀️
    - Maintain healthy BMI
    - Get sugar levels checked yearly
    - Reduce stress & sleep well 😴
    - Avoid smoking & alcohol
    """)
    weekly_diet_plan()
    monthly_diet_plan()
    show_recipe_table()

def diabetic_schedule():
    st.error("🔴 Diabetes Management Schedule")



    exercise = pd.DataFrame({
        "Activity": ["Walking", "Yoga", "Cycling"],
        "Duration": ["30 mins", "20 mins", "20 mins"]
    })

    medicine = pd.DataFrame({
        "Type": ["Oral Medication", "Insulin (if prescribed)"],
        "Example": ["Metformin*(if doctor prescribed)", "As per doctor advice"]
    })


    st.subheader("🏃 Physical Activity")
    st.table(exercise)

    st.subheader("💊 Medication (Doctor Prescribed)")
    st.table(medicine)

    st.caption("⚠️ Medicines are indicative. Always consult a doctor.")
    weekly_diet_plan()
    monthly_diet_plan()
    show_recipe_table()


def risk_schedule():
    st.warning("🟡 Patient is at Risk of Diabetes")

    diet = pd.DataFrame({
        "Meal": ["Breakfast", "Lunch", "Dinner"],
        "Recommendation": [
            "High fiber foods, fruits",
            "Balanced diet, low carbs",
            "Light meal, vegetables"
        ]
    })

    activity = pd.DataFrame({
        "Exercise": ["Walking", "Jogging", "Yoga"],
        "Duration": ["30 mins", "15 mins", "20 mins"]
    })



    st.subheader("🍽️ Diet Plan")
    st.table(diet)

    st.subheader("🏃 Exercise Plan")
    st.table(activity)


    weekly_diet_plan()
    monthly_diet_plan()

def predict_stage(prediction, glucose):
    if prediction == 1:
        return "Diabetic"
    elif glucose >= 110:
        return "At Risk"
    else:
        return "Normal"

def weekly_diet_plan():
    st.subheader("📅 Weekly Diet Plan")

    diet = pd.DataFrame({
        "Day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
        "Breakfast": [
            "Oats Porridge",
            "Vegetable Omelette",
            "Sprouts Salad",
            "Idli Sambar",
            "Oats Porridge",
            "Vegetable Omelette",
            "Vegetable Upma"
        ],
        "Lunch": [
            "Dal Tadka",
            "Paneer Curry",
            "Vegetable Khichdi",
            "Dal Tadka",
            "Paneer Curry",
            "Vegetable Khichdi",
            "Dal Tadka"
        ],
        "Dinner": [
            "Vegetable Soup",
            "Grilled Chicken",
            "Vegetable Stir Fry",
            "Vegetable Soup",
            "Grilled Chicken",
            "Vegetable Stir Fry",
            "Vegetable Soup"
        ]
    })

    st.table(diet)

def monthly_diet_plan():
    st.subheader("🗓️ Monthly Diet Plan")

    diet = pd.DataFrame({
        "Week": ["Week 1", "Week 2", "Week 3", "Week 4"],
        "Focus": [
            "Blood Sugar Control",
            "High Fiber Intake",
            "Protein Strength",
            "Balanced Maintenance"
        ],
        "Recommended Recipes": [
            "Oats Porridge, Vegetable Soup",
            "Sprouts Salad, Dal Tadka",
            "Paneer Curry, Grilled Chicken",
            "Vegetable Khichdi, Stir Fry"
        ]
    })

    st.table(diet)


def diabetes_risk_score(glucose, bmi, age):
    score = 0

    # Glucose contribution
    if glucose >= 140:
        score += 40
    elif glucose >= 110:
        score += 25

    # BMI contribution
    if bmi >= 30:
        score += 25
    elif bmi >= 25:
        score += 15

    # Age contribution
    if age >= 45:
        score += 15
    elif age >= 35:
        score += 10

    return min(score, 100)

def show_risk_progression(glucose, bmi, age):
    current_risk = diabetes_risk_score(glucose, bmi, age)
    future_risk = min(current_risk + 15, 100)
    improved_risk = max(current_risk - 20, 5)

    st.subheader("📈 Diabetes Risk Progression Score")

    st.metric("📌 Current Risk", f"{current_risk}%")
    st.metric("⏳ Future Risk (1–3 Years)", f"{future_risk}%")
    st.metric("💪 Risk After Lifestyle Improvement", f"{improved_risk}%")

    st.info("""
    ✔ Regular exercise  
    ✔ Weight reduction  
    ✔ Low sugar & low carb diet  
    ✔ Stress management  
    """)

def personalized_summary(stage, glucose, bmi):
    st.subheader("🧠 Personalized Health Summary")

    if stage == "Diabetic":
        st.write(f"""
        - High glucose level ({glucose}) detected
        - BMI ({bmi}) indicates elevated risk
        - Immediate lifestyle and diet control required
        """)
    elif stage == "At Risk":
        st.write("""
        - Borderline glucose levels
        - Early prevention can reverse risk
        """)
    else:
        st.write("""
        - Healthy glucose and BMI levels
        - Continue current lifestyle
        """)

def predict_with_confidence(features):
    proba = rfc.predict_proba([features])[0]
    confidence = max(proba) * 100
    return rfc.predict([features])[0], confidence

def generate_pdf(stage, glucose, bmi, age):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, "Diabetes Prediction Report", ln=True)

    pdf.set_font("Arial", size=12)
    pdf.ln(5)
    pdf.cell(0, 10, f"Diabetes Stage: {stage}", ln=True)
    pdf.cell(0, 10, f"Glucose Level: {glucose}", ln=True)
    pdf.cell(0, 10, f"BMI: {bmi}", ln=True)
    pdf.cell(0, 10, f"Age: {age}", ln=True)
    pdf.ln(5)
    pdf.multi_cell(0, 8, "Note: This report is generated using a Machine Learning model. "
                         "Please consult a doctor for medical advice.")

    return pdf

# ------------------ UI ------------------
st.title("🩺 Diabetes Prediction App")
st.write("Enter patient details to predict the likelihood of diabetes.")

st.sidebar.header("⚙️ Input Options")
option = st.sidebar.radio("Choose input method", ["Manual Input", "Upload CSV"])

# ------------------ MANUAL INPUT ------------------
if option == "Manual Input":

    pregnancies = st.number_input("Pregnancies", 0, 20, 1)
    glucose = st.number_input("Glucose", 0, 300, 1)
    blood_pressure = st.number_input("Blood Pressure", 0, 200, 1)
    skin_thickness = st.number_input("Skin Thickness", 0, 100, 1)
    insulin = st.number_input("Insulin", 0, 1000, 1)
    bmi = st.number_input("BMI", 0.0, 100.0, 1.0)
    dpf = st.number_input("Diabetes Pedigree Function", 0.0, 3.0, 1.0)
    age = st.number_input("Age", 0, 120, 1)

    if st.button("🔍 Predict"):

        features = [
            pregnancies, glucose, blood_pressure,
            skin_thickness, insulin, bmi, dpf, age
        ]

        prediction = predict_diabetes(features)
        stage = predict_stage(prediction, glucose)

        show_risk_progression(glucose, bmi, age)
        st.write(f"**Diabetes Stage:** {stage}")
        if stage == "Diabetic":
            st.error("🏥 Visit Diabetologist Immediately")
        elif stage == "At Risk":
            st.warning("🧑‍⚕️ Doctor Visit Recommended in 3 Months")
        else:
            st.success("✅ Annual Checkup is Sufficient")

        prediction, confidence = predict_with_confidence(features)
        st.metric("Model Confidence", f"{confidence:.2f}%")
        st.progress(int(confidence))

        # ------------------ DIABETIC CASE ------------------
        if prediction == 1:
            st.error("⚠️ Patient is Diabetic")

            personalized_summary(stage, glucose, bmi)
            diabetic_recommendations()

            pdf = generate_pdf(stage, glucose, bmi, age)
            st.download_button(
                label="📄 Download Medical Report (PDF)",
                data=pdf.output(dest="S").encode("latin-1"),
                file_name="Diabetes_Report.pdf",
                mime="application/pdf",
                key="download_pdf_diabetic"
            )

            # Stage-based schedule
            if stage == "Diabetic":
                diabetic_schedule()
                pdf2 = generate_pdf(stage, glucose, bmi, age)
                st.download_button(
                    label="📄 Download Diabetic Schedule",
                    data=pdf2.output(dest="S").encode("latin-1"),
                    file_name="Diabetic_Schedule_Report.pdf",
                    mime="application/pdf",
                    key="download_pdf_diabetic_schedule"
                )

            elif stage == "At Risk":
                risk_schedule()
                pdf3 = generate_pdf(stage, glucose, bmi, age)
                st.download_button(
                    label="📄 Download Risk Schedule",
                    data=pdf3.output(dest="S").encode("latin-1"),
                    file_name="Risk_Schedule_Report.pdf",
                    mime="application/pdf",
                    key="download_pdf_risk_schedule"
                )

        # ------------------ NON-DIABETIC CASE ------------------
        else:
            st.success("✅ Patient is Not Diabetic")

            non_diabetic_recommendations()

            pdf4 = generate_pdf(stage, glucose, bmi, age)
            st.download_button(
                label="📄 Download Medical Report (PDF)",
                data=pdf4.output(dest="S").encode("latin-1"),
                file_name="Normal_Report.pdf",
                mime="application/pdf",
                key="download_pdf_normal"
            )

# ------------------ CSV UPLOAD ------------------
elif option == "Upload CSV":

    uploaded_file = st.file_uploader("📂 Upload CSV file", type=["csv"])

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)

        predictions = rfc.predict(df)
        df["Prediction"] = predictions

        st.write(df)

        st.download_button(
            label="⬇️ Download Predictions",
            data=df.to_csv(index=False),
            file_name="predictions.csv",
            mime="text/csv"
        )