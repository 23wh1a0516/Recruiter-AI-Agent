import streamlit as st
import os
import sys

# Get project root directory
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "..", ".."))

sys.path.insert(0, project_root)

from backend.resume_parser import extract_text, extract_email, extract_skills, extract_experience
st.set_page_config(page_title="Recruiter AI Agent", layout="wide")

st.title("Recruiter AI Agent - Resume Parser")

st.write("Upload a resume (PDF or DOCX) to extract skills and details.")

# Upload Resume
uploaded_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])

if uploaded_file is not None:

    # Save uploaded file temporarily
    temp_path = os.path.join("temp_resume", uploaded_file.name)
    os.makedirs("temp_resume", exist_ok=True)

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("Resume uploaded successfully!")

    # Extract text
    text = extract_text(temp_path)

    # Extract details
    email = extract_email(text)
    skills = extract_skills(text)
    experience = extract_experience(text)

    st.subheader("Extracted Information")

    st.write("Email:", email)
    st.write("Experience:", experience, "years")

    st.subheader("Extracted Skills")

    if skills:
        for skill in skills:
            st.write("•", skill)
    else:
        st.write("No skills detected from predefined list.")

    # Show raw extracted text (optional)
    with st.expander("View Extracted Resume Text"):
        st.write(text)