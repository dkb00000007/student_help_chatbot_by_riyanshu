# educational_assistant.py

import streamlit as st
import google.generativeai as genai

# Setup Gemini
genai.configure(api_key="AIzaSyC0HWOGXnjbm1zKd0B6I8lVy_oCxYw2xXI")
model = genai.GenerativeModel("gemini-2.0-flash")

st.set_page_config(page_title="Educational Assistant Bot", layout="centered")

st.title("📘 Educational Assistant Bot")

option = st.selectbox("Choose a service", ["Ask a Subject Question", "Get Study Resources", "Academic Planning"])

if option == "Ask a Subject Question":
    question = st.text_input("Enter your academic question:")
    if st.button("Get Answer"):
        if question:
            with st.spinner("Thinking..."):
                response = model.generate_content(question)
                st.success("Answer:")
                st.markdown(response.text)
        else:
            st.warning("Please enter a question.")

elif option == "Get Study Resources":
    topic = st.text_input("Enter topic or subject (e.g. Algebra, Python basics):")
    if st.button("Suggest Resources"):
        if topic:
            prompt = f"Suggest study resources (YouTube, books, articles, PDFs) for the topic: {topic}"
            response = model.generate_content(prompt)
            st.success("Resources:")
            st.markdown(response.text)
        else:
            st.warning("Please enter a topic.")

elif option == "Academic Planning":
    goal = st.text_input("Enter your academic goal (e.g. Prepare Python in 10 days):")
    if st.button("Generate Study Plan"):
        if goal:
            prompt = f"Create a personalized, realistic study plan for this academic goal: {goal}"
            response = model.generate_content(prompt)
            st.success("Study Plan:")
            st.markdown(response.text)
        else:
            st.warning("Please enter a goal.")
