import streamlit as st
from streamlit_option_menu import option_menu
from resume_page import resume
from experience_page import experience
from projects_page import projects
from contact_page import contact

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
    I am currently pursuing a Master of Engineering Management at Pennsylvania State University Harrisburg, and have a Bachelor of Electrical and Electronics from Ramaiah Institute of Technology. 
    I have experience in engineering, quality, and project management, with a passion for improving processes and finding innovative solutions.
    """)
    st.image("path/to/your/image.jpg", width=300, caption="T Yashwanth Sai")

elif selected_page == "Resume":
    resume()

elif selected_page == "Experience":
    experience()

elif selected_page == "Projects":
    projects()

elif selected_page == "Contact":
    contact()
