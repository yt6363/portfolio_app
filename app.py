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

# Custom CSS for general app styling and top navigation bar styling
st.markdown("""
    <style>
    /* General Styling for Responsive Layout */
    body {
        font-family: 'Arial', sans-serif;
    }

    /* Top Navigation Bar Styling */
    .topnav {
        background-color: #ffffff;
        overflow: hidden;
        display: flex;
        justify-content: center;
        padding: 10px 20px;
        flex-wrap: wrap; /* Ensures the menu wraps for smaller screens */
    }

    .topnav a {
        color: #333333;
        text-align: center;
        padding: 8px 16px;
        text-decoration: none;
        font-size: 20px;
        font-weight: 500;
    }

    .topnav a:hover {
        color: #2b6cb0;
    }

    .topnav a.active {
        color: #ff4b4b;
        font-weight: bold;
    }

    /* Hide top navigation bar for mobile screens and show hamburger icon */
    @media screen and (max-width: 768px) {
        .topnav {
            display: none;
        }

        .hamburger-menu {
            display: block;
            position: fixed;
            top: 10px;
            right: 10px;
            z-index: 1000;
            cursor: pointer;
        }

        .menu-items {
            display: none;
            position: fixed;
            top: 50px;
            right: 10px;
            background-color: #ffffff;
            box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
            z-index: 1000;
            padding: 10px;
            border-radius: 8px;
        }

        .menu-items a {
            display: block;
            color: #333333;
            text-decoration: none;
            padding: 8px 16px;
            font-size: 18px;
        }

        .menu-items a:hover {
            color: #2b6cb0;
        }

        .menu-items a.active {
            color: #ff4b4b;
        }
    }

    /* Hamburger icon styling */
    .hamburger-menu {
        display: none;
        width: 30px;
        height: 30px;
        cursor: pointer;
    }

    .bar {
        display: block;
        width: 100%;
        height: 5px;
        background-color: #333;
        margin: 4px 0;
        transition: 0.4s;
    }
    </style>
""", unsafe_allow_html=True)

# Hamburger menu for mobile
st.markdown("""
    <div class="hamburger-menu" onclick="toggleMenu()">
        <div class="bar"></div>
        <div class="bar"></div>
        <div class="bar"></div>
    </div>
    <div class="menu-items" id="mobileMenu">
        <a href="?page=about" target="_self" class="{active_about}">About Me</a>
        <a href="?page=resume" target="_self" class="{active_resume}">Resume</a>
        <a href="?page=experience" target="_self" class="{active_experience}">Experience</a>
        <a href="?page=projects" target="_self" class="{active_projects}">Projects</a>
        <a href="?page=contact" target="_self" class="{active_contact}">Contact</a>
    </div>
""".format(
    active_about='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'about' else '',
    active_resume='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'resume' else '',
    active_experience='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'experience' else '',
    active_projects='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'projects' else '',
    active_contact='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'contact' else ''
), unsafe_allow_html=True)

# JavaScript to handle hamburger menu toggle
st.markdown("""
    <script>
    function toggleMenu() {
        var menu = document.getElementById("mobileMenu");
        if (menu.style.display === "block") {
            menu.style.display = "none";
        } else {
            menu.style.display = "block";
        }
    }
    </script>
""", unsafe_allow_html=True)

# Top Navigation Bar for Larger Screens
if st.experimental_get_query_params().get('page', ['about'])[0] not in ["mobile"]:
    st.markdown("""
        <div class="topnav">
            <a href="?page=about" target="_self" class="{active_about}">About Me</a>
            <a href="?page=resume" target="_self" class="{active_resume}">Resume</a>
            <a href="?page=experience" target="_self" class="{active_experience}">Experience</a>
            <a href="?page=projects" target="_self" class="{active_projects}">Projects</a>
            <a href="?page=contact" target="_self" class="{active_contact}">Contact</a>
        </div>
    """.format(
        active_about='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'about' else '',
        active_resume='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'resume' else '',
        active_experience='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'experience' else '',
        active_projects='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'projects' else '',
        active_contact='active' if st.experimental_get_query_params().get('page', ['about'])[0] == 'contact' else ''
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
            gap: 30px;
            margin-top: 50px;
            flex-wrap: wrap; /* To support smaller screens */
            text-align: center; /* Align text properly on smaller devices */
        }}
        .text-container {{
            max-width: 600px;
            margin-top: 20px;
            font-size: 18px;
        }}
        </style>
        <div class="profile-container">
            <img class="profile-img" src="data:image/jpeg;base64,{base64_img}">
            <div class="text-container">
                <h2 style="font-size:28px;">"Engineering Solutions, Managing Projects, Delivering Impact."</h2>
                <p style="background-color: #ffffff10; padding: 20px; border-radius: 10px; font-size: 16px;">
                    👋 Hi, I'm Yashwanth, an engineering management student with hands-on experience in project management, 
                    quality assurance, and data analysis...
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Main Content - Section Rendering Based on Selected Page
selected_page = st.experimental_get_query_params().get('page', ['about'])[0]
if selected_page == "about":
    add_profile_image("Yashwanth sai Tatineni.jpeg", width=200)

elif selected_page == "resume":
    resume()

elif selected_page == "experience":
    experience()

elif selected_page == "projects":
    projects()

elif selected_page == "contact":
    contact()
