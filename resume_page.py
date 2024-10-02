import streamlit as st
import base64

def resume():
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")

    # Display PDF file in an iframe
    resume_path = "Yashwanth sai Tatineni Resume.pdf"  # Update this with the correct path to your PDF
    with open(resume_path, "rb") as pdf_file:
        base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")
        pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf"></iframe>'
        st.markdown(pdf_display, unsafe_allow_html=True)

    # Add a download button for the PDF
    with open(resume_path, "rb") as pdf_file:
        st.download_button(label="Download Resume", data=pdf_file, file_name="Yashwanth_sai_Tatineni_Resume.pdf", mime="application/pdf")
