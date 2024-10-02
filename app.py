import streamlit as st
from streamlit_option_menu import option_menu
from resume_page import resume
from experience_page import experience
from projects_page import projects
from contact_page import contact
import base64

# Page setup
st.set_page_config(
    page_title="T Yashwanth Sai's Portfolio",
    page_icon="👤",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for general app styling
st.markdown("""
    <style>
    /* General adjustments for light theme */
    body {
        background-color: #f8f9fa;
    }

    /* Sidebar styling */
    .css-1lcbmhc.e1fqkh3o3 {
        background-color: #ffffff !important;
        border-right: 1px solid #d3d3d3;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
    }

    /* Profile Image CSS */
    .profile-img {
        width: 200px;
        height: 200px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #FF4B4B;
    }

    .profile-container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 20px;
        margin-top: 30px;
        flex-wrap: wrap; /* Allow wrapping on small screens */
    }

    .text-container {
        max-width: 90%;
        text-align: center;
        font-size: 16px;
    }

    h2.quote {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 15px;
        color: #2b6cb0;
    }

    /* General page adjustments for mobile */
    @media only screen and (max-width: 768px) {
        .profile-img {
            width: 150px;
            height: 150px;
        }

        h2.quote {
            font-size: 20px;
        }

        .text-container {
            font-size: 14px;
            margin-top: 15px;
        }
    }

    /* Sidebar Navigation adjustments for modern look */
    ul[data-testid="stSidebarNav"] {
        padding-top: 10px;
    }

    li.css-1v0mbdj.e1fqkh3o3 {
        padding: 8px 20px !important;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }

    li.css-1v0mbdj.e1fqkh3o3:hover {
        background-color: #ff4b4b1a;
    }

    li.css-1v0mbdj.e1fqkh3o3 > div {
        font-weight: 500 !important;
        color: #2b6cb0 !important;
    }

    </style>
""", unsafe_allow_html=True)

# Function to create circular images with custom CSS styling
def add_profile_image(image_path, width):
    # Encode image to base64
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
    base64_img = base64.b64encode(img_bytes).decode()

    # Render circular image using CSS
    st.markdown(f"""
        <div class="profile-container">
            <img class="profile-img" src="data:image/jpeg;base64,{base64_img}">
            <div class="text-container">
                <h2 class="quote">"Engineering Solutions, Managing Projects, Delivering Impact."</h2>
                <p style="background-color: #ffffff10; padding: 15px; border-radius: 10px; font-size: 16px;">
                    👋 Hi, I'm Yashwanth, an engineering management student with hands-on experience in project management, 
                    quality assurance, and data analysis. My expertise spans across industries, where I have optimized workflows, managed timelines, 
                    and conducted in-depth data analysis using SQL and Tableau. With a passion for innovative problem-solving, 
                    I am currently pursuing certifications in Six Sigma Green Belt and CAPM, which enhance my ability to deliver excellence in project execution. 
                    I am driven by a desire to apply my skills to meaningful, impact-driven projects.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

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
    add_profile_image("Yashwanth sai Tatineni.jpeg", width=200)

    # Social media links arranged compactly below the text
    st.markdown("""
    <div style="text-align: center; margin-top: 20px;">
        <a href="https://www.linkedin.com/in/yashwanth-sai-tatineni-80b4ab1b7/" target="_blank">
            <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
        </a>
        <a href="https://github.com/yt6363">
            <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
        </a>
        <a href="https://www.upwork.com/freelancers/~Yashwanth" target="_blank">
            <img src="https://img.shields.io/badge/Upwork-6fda44?style=for-the-badge&logo=upwork&logoColor=white" alt="Upwork">
        </a>
    </div>
    """, unsafe_allow_html=True)

elif selected_page == "Resume":
    resume()

elif selected_page == "Experience":
    experience()

elif selected_page == "Projects":
    projects()

elif selected_page == "Contact":
    contact()
