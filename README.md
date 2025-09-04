# 🧠 Student Mental Health Risk Scorer
A simple Streamlit-based web app to assess the mental health risk score of students based on their inputs.  

---

## 🔹 Overview
This project provides an easy-to-use interface for students to evaluate their mental health risk.  
The app considers factors such as **depression, anxiety, panic attacks, age, and CGPA** to calculate a risk score.  

---

## ✅ Key Features
- Interactive student input form 🎓  
- Mental health conditions assessment: Depression, Anxiety, Panic Attacks 🧠  
- Calculates a **risk score (0-100)** based on responses 🎯  
- Provides guidance based on risk level: Low, Moderate, High 🔴🟡🟢  
- User-friendly interface using **Streamlit** 💻  

---

## 🔹 Tech Stack
🟢 Python  
🟢 Streamlit (Web App Interface)  
🟢 Numpy / Pandas (optional for further extensions)  

---

## 🔹 Implementation Steps
1️⃣ Collect student information: Gender, Age, Course, Year, CGPA  
2️⃣ Gather mental health conditions: Depression, Anxiety, Panic Attacks  
3️⃣ Calculate risk score using a scoring function based on inputs  
4️⃣ Display the risk score with appropriate guidance  
5️⃣ Deploy the app using Streamlit  

---

## 🔹 How the Risk Score is Calculated
- Each mental health condition (Depression, Anxiety, Panic Attacks) adds **30 points** if present  
- CGPA ≥ 9 → subtract 10 points, CGPA < 6 → add 10 points  
- Age ≥ 22 → add 5 points  
- Final score is capped between 0 and 100  

**Risk Levels:**
- **0–30:** Low risk 🟢  
- **31–60:** Moderate risk 🟡  
- **61–100:** High risk 🔴  

---

## 🔹 Future Improvements
- ✅ Include more mental health factors like stress, sleep, and lifestyle habits 🧘‍♂️  
- ✅ Add data visualization of mental health trends among users 📊  
- ✅ Deploy as a hosted web app for wider accessibility 🌐  
- ✅ Integrate resources and guidance links for students in need ❤️  
- ✅ Implement a machine learning model to predict mental health risk more accurately 🤖  

---

## ⚠️ Note
This tool is for **awareness purposes only** and is **not a medical diagnosis**.  
Consult a professional for any concerns.

---

## 🔹 How to Use
1. Clone the repository  
2. Install dependencies:
```bash
pip install streamlit
