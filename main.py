import streamlit as st
import pickle

model = pickle.load(open("smp.pkl", "rb"))

st.set_page_config(page_title="SmartGrades Predictor", page_icon="🎓", layout="centered")
st.title("🎓 SmartGrades Predictor")
st.write("This app predicts student marks based on study hours using a trained Machine Learning model.")
st.subheader("📘 Enter Study Hours")
sh = st.number_input("Study Hours", min_value=0.0, max_value=12.0, step=0.5)

if st.button("🔮 Predict Marks"):
    res = model.predict([[sh]])[0][0].round(2)
    st.success(f"📊 Predicted Marks: **{res}** / 100")

    if res >= 90:
        st.balloons()
        st.info("Excellent! Hard work pays off. 🎉")
    elif res >= 60:
        st.info("Good! Keep studying consistently. 📚")
    else:
        st.warning("Needs improvement. Stay focused and practice more. 💪")


st.markdown("---")
st.caption("⚡ Developed with Streamlit & Machine Learning")
