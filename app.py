import streamlit as st
from main import get_explanation

st.set_page_config(page_title="AI Knowledge Explainer")

st.title("🧠 AI Knowledge Explainer")

topic = st.text_input("Enter a Topic", placeholder="e.g. NLP, Blockchain")

level = st.slider(
    "Select Explanation Level",
    1, 5, 3
)

if st.button("🚀 Generate Explanation"):
    explanation = get_explanation(topic, level)

    st.success("Explanation generated")

    st.subheader(f"📘 Explanation of {topic} (Level {level})")
    st.markdown(explanation)   # 🔥 THIS IS WHERE IT APPEARS