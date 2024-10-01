import streamlit as st
from streamlit_option_menu import option_menu

# Page setup
st.set_page_config(
    page_title="T Yashwanth Sai's Portfolio",
    page_icon="👤",
    layout="wide",
)

# Sidebar Navigation
with st.sidebar:
    selected_page = option_menu(
        menu_title="Navigation",
        options=["About Me", "Resume", "Experience", "Projects", "Contact"],
        icons=["person-fill", "file-text", "briefcase", "folder", "envelope"],
        menu_icon="cast",
        default_index=0,
    )

# Main Content
if selected_page == "About Me":
    st.title("Hello! I'm T Yashwanth Sai 👋")
    st.markdown("""
    I am currently pursuing a Master of Engineering Management at Pennsylvania State University Harrisburg, and I have a Bachelor of Electrical and Electronics from Ramaiah Institute of Technology. 
    I have experience in engineering, quality, and project management, with a passion for improving processes and finding innovative solutions.
    """)
    st.image("path/to/your/image.jpg", width=300, caption="T Yashwanth Sai")

elif selected_page == "Resume":
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

elif selected_page == "Experience":
    st.header("Experience")
    st.write("Below are some of my roles and responsibilities:")
    
    st.subheader("Graduate Wage Associate at Pennsylvania State University")
    st.write("""
    - Assisted faculty in special projects and provided laboratory instruction to over 140 students.
    - Helped with grading assignments and facilitating student engagement.
    """)

    st.subheader("Marketing Operations Intern at Incredible India Projects Pvt Ltd")
    st.write("""
    - Assisted in developing standards and templates for marketing operations.
    - Managed CRM with 500+ client records, and helped in project scheduling.
    """)

elif selected_page == "Projects":
    st.header("Academic Projects")
    st.write("Here are some of the projects I've worked on:")

    st.subheader("Health Insurance Company Database")
    st.write("""
    - Developed a SQL database to manage health insurance records for over 300 patients, including demographics and physician data.
    """)

    st.subheader("EV Charging Management System")
    st.write("""
    - Developed algorithms for priority-based scheduling of electric vehicle charging.
    - Created mathematical models for prioritization and return-on-investment (ROI).
    """)

elif selected_page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out via the form below:")

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            st.success("Thank you! Your message has been sent.")


