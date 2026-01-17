import streamlit as st
from reviewer import review_code

st.set_page_config(page_title="AI Code Reviewer", layout="wide")

st.title("🧠 AI Code Reviewer (Local & Free)")

language = st.selectbox("Select Language", ["Python", "JavaScript", "C", "Java"])

code_input = st.text_area(
    "Paste your code here",
    height=300,
    placeholder="Paste your code..."
)

if st.button("Review Code"):
    if code_input.strip() == "":
        st.warning("Please paste some code.")
    else:
        with st.spinner("Reviewing your code..."):
            review = review_code(code_input, language.lower())
            st.subheader("📋 Review")
            st.markdown(review)
            