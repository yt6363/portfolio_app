import streamlit as st
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

# Custom HTML Meta Tag for Forcing Desktop-like View on Mobile
st.markdown("""
    <meta name="viewport" content="width=1200, initial-scale=0.4, maximum-scale=0.4, user-scalable=no">
    <style>
    /* Top Navigation Bar Styling */
    .topnav {
        background-color: #ffffff;
        overflow: hidden;
        display: flex;
        justify-content: center;
        padding: 4px 20px;
    }

    .topnav a {
        color: #333333;
        text-align: center;
        padding: 0 15px;
        text-decoration: none;
        font-size: 24px;
        font-weight: 500;
    }

    .topnav a:hover {
        color: #2b6cb0;
    }

    .topnav a.active {
        color: #ff4b4b;
        font-weight: bold;
    }

    /* Custom CSS for content section */
    .content {
        margin-top: 20px; /* Ensure content is not overlapped by navigation */
        min-width: 1200px; /* Force content to render as a desktop width */
    }

    /* Responsive styling to maintain desktop-like view */
    @media only screen and (max-width: 768px) {
        .stApp {
            min-width: 1200px; /* Force desktop width */
        }

        .profile-img {
            width: 150px !important;
            height: 150px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Top Navigation Bar
selected_page = st.experimental_get_query_params().get('page', ['about'])[0]

st.markdown("""
    <div class="topnav">
        <a href="?page=about" target="_self" class="{active_about}">About Me</a>
        <a href="?page=resume" target="_self" class="{active_resume}">Resume</a>
        <a href="?page=experience" target="_self" class="{active_experience}">Experience</a>
        <a href="?page=projects" target="_self" class="{active_projects}">Projects</a>
        <a href="?page=contact" target="_self" class="{active_contact}">Contact</a>
    </div>
""".format(
    active_about='active' if selected_page == 'about' else '',
    active_resume='active' if selected_page == 'resume' else '',
    active_experience='active' if selected_page == 'experience' else '',
    active_projects='active' if selected_page == 'projects' else '',
    active_contact='active' if selected_page == 'contact' else ''
), unsafe_allow_html=True)

# Function to create circular images with custom CSS styling
def add_profile_image(image_path, width):
    # Encode image to base64
    with open(image_path, "rb") as img_file:
        img_bytes = img_file.read()
    base64_img = base64.b64encode(img_bytes).decode()

    # Render circular image using CSS
    st.markdown(f"""
        <style>
        .profile-img {{
            width: {width}px;
            height: {width}px;
            border-radius: 50%;
            object-fit: cover;
            border: 6px solid #FF4B4B;
        }}
        .profile-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 20px;
            margin-top: 30px;
        }}
        .text-container {{
            max-width: 600px;
            margin-left: 10px;
            font-size: 18px;
        }}
        </style>
        <div class="profile-container">
            <img class="profile-img" src="data:image/jpeg;base64,{base64_img}">
            <div class="text-container">
                <h2 style="font-size:32px;">"Engineering Solutions, Managing Projects, Delivering Impact."</h2>
                <p style="background-color: #ffffff10; padding: 15px; border-radius: 10px; font-size: 18px;">
                    👋 Hi, I'm Yashwanth, an engineering management student with hands-on experience in project management, 
                    quality assurance, and data analysis. My expertise spans across industries, where I have optimized workflows, managed timelines, 
                    and conducted in-depth data analysis using SQL and Tableau. With a passion for innovative problem-solving, 
                    I am currently pursuing certifications in Six Sigma Green Belt and CAPM, which enhance my ability to deliver excellence in project execution. 
                    I am driven by a desire to apply my skills to meaningful, impact-driven projects.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main Content - Section Rendering Based on Selected Page
st.
