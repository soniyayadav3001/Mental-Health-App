import streamlit as st

st.set_page_config(page_title="Student Mental Health Risk Scorer", layout="centered")
st.title("🧠 Student Mental Health Risk Scorer")
st.markdown("This app gives a simple mental health risk score based on your inputs.")

st.markdown("### 🎓 Student Information")

gender = st.selectbox("Choose your gender", ["Female", "Male", "Other"])

age = st.slider("Age", 16, 30, 20)

course = st.selectbox("What is your course?", ["B.Tech", "B.Sc", "BA", "B.Com", "Other"])

year = st.selectbox("Your current year of Study", ["First Year", "Second Year", "Third Year", "Final Year"])

cgpa = st.slider("Your CGPA", 0.0, 10.0, 8.29, step=0.01)

marital_status = st.selectbox("Marital status", ["Single", "Married", "Divorced"])

st.markdown("### 🧠 Mental Health Conditions")

depression = st.radio("Do you have Depression?", ["Yes", "No"])
anxiety = st.radio("Do you have Anxiety?", ["Yes", "No"])
panic_attack = st.radio("Do you have Panic attack?", ["Yes", "No"])

def calculate_score():
    score = 0

    if depression == "Yes":
        score += 30
    if anxiety == "Yes":
        score += 30
    if panic_attack == "Yes":
        score += 30

    if cgpa >= 9.0:
        score -= 10
    elif cgpa < 6.0:
        score += 10

    if age >= 22:
        score += 5

    return max(0, min(100, score))


if st.button("🎯 Calculate My Mental Health Risk"):
    score = calculate_score()
    st.metric("Your Mental Health Risk Score", f"{score} / 100")

    if score <= 30:
        st.success("🟢 You seem to be at **low** mental health risk.")
    elif 31 <= score <= 60:
        st.warning("🟡 You may be experiencing **moderate** stress. Consider talking to someone.")
    else:
        st.error("🔴 You are at **high** mental health risk. Please consider consulting a counselor.")

    
    st.markdown("---")
    st.write("Note: This tool is for awareness purposes only and is not a medical diagnosis. For any concerns, please consult a professional.")
    st.caption("👩‍💻 Made by **Soniya Yadav💙**")

