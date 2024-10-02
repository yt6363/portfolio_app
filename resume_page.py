import streamlit as st

def resume():
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")

    # Direct download link for the resume (created from the Google Drive link)
    resume_url = "https://drive.google.com/uc?export=download&id=14uBFlzeC86-Sx65Kci1Qcg7pGqmUdfw_"

    # Embed the PDF using an iframe
    st.markdown(f"""
        <div style="text-align: center;">
            <iframe src="{resume_url}" width="700" height="1000"></iframe>
        </div>
    """, unsafe_allow_html=True)

    # Provide a download link for the resume
    st.markdown(f'[Download Resume]({resume_url})', unsafe_allow_html=True)
