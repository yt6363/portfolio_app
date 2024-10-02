import streamlit as st
import os

def resume():
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")

    # Path to the local resume file
    resume_path = "Yashwanth sai Tatineni Resume.pdf"

    # Check if file exists
    if os.path.exists(resume_path):
        # Add a download button for the PDF
        with open(resume_path, "rb") as pdf_file:
            st.download_button(label="Download Resume", data=pdf_file, file_name="Yashwanth_sai_Tatineni_Resume.pdf", mime="application/pdf")
    else:
        st.error("Resume file not found. Please ensure the file is in the correct location.")
