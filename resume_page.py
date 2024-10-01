import streamlit as st

def resume():
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")
    st.markdown("""
    **Education:**
    - **Master of Engineering Management** - Pennsylvania State University Harrisburg (Jan 2023 - Dec 2024)
      - CGPA: 3.7
    - **Bachelor of Electrical and Electronics Engineering** - Ramaiah Institute of Technology (Aug 2018 - Sept 2022)

    **Work Experience:**
    - **Graduate Wage Associate** - Pennsylvania State University (Sept 2023 - May 2024)
      - Assisted faculty in special projects and instructed undergraduate students.
    - **Teaching Assistant** - Pennsylvania State University (Jan 2023 - Dec 2023)
      - Assisted students in courses such as Digital Design and Electrical Communication.
    - **Marketing Operations Intern** - Incredible India Projects Pvt Ltd (May 2022 - Dec 2022)
      - Developed standards and assisted project managers with project risk logs and schedules.
    
    **Skills:**
    - Tools: Microsoft Project, Figma, Confluence, JIRA, Primavera P6, MATLAB, Python, SQL, Tableau, SEO.
    - Certifications: PMI CAPM (On-going), Google Project Management Certificate.
    """)
    st.download_button(label="Download Resume", data=open("path/to/your_resume.pdf", "rb"), file_name="Yashwanth_Sai_Resume.pdf")
