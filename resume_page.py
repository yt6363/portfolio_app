import streamlit as st

def resume():
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")

    # Public link to the resume (replace with your actual hosted link)
    resume_url = "https://drive.google.com/file/d/14uBFlzeC86-Sx65Kci1Qcg7pGqmUdfw_/view?usp=drive_link"  # Replace with your actual link

    # Embed the PDF using an iframe
    st.markdown(f"""
        <div style="text-align: center;">
            <iframe src="{resume_url}" width="700" height="1000"></iframe>
        </div>
    """, unsafe_allow_html=True)

    # Provide a download link for the resume
    st.markdown(f'[Download Resume](https://example.com/Yashwanth_sai_Tatineni_Resume.pdf)', unsafe_allow_html=True)
