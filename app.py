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

# Custom CSS for general app styling, top navigation bar, and zoom for mobile
st.markdown("""
    <style>
    /* Top Navigation Bar Styling */
    .topnav {
        background-color: #ffffff;
        overflow: hidden;
        display: flex;
        justify-content: center;
        padding: 4px 50px;
    }

    .topnav a {
        color: #333333;
        text-align: center;
        padding: 0 26px;
        text-decoration: none;
        font-size: 26px;
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
        margin-top: 20px;
    }

    /* Apply default zoom level for mobile devices */
    @media only screen and (max-width: 768px) {
        html {
            zoom: 0.4;
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
            gap: 30px;
            margin-top: 50px;
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
                <h2 style="font-size:36px;">"Engineering Solutions, Managing Projects, Delivering Impact."</h2>
                <p style="background-color: #ffffff10; padding: 20px; border-radius: 10px; font-size: 18px;">
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
st.markdown('<div class="content">', unsafe_allow_html=True)

if selected_page == "about":
    add_profile_image("Yashwanth sai Tatineni.jpeg", width=250)
    st.markdown("""
        <div style="text-align: center; margin-top: 20px;">
            <a href="https://www.linkedin.com/in/yashwanth-sai-tatineni-80b4ab1b7/" target="_blank">
                <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
            </a>
            <a href="https://github.com/yt6363" target="_blank">
                <img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white" alt="GitHub">
            </a>
            <a href="https://www.upwork.com/freelancers/~Yashwanth" target="_blank">
                <img src="https://img.shields.io/badge/Upwork-6fda44?style=for-the-badge&logo=upwork&logoColor=white" alt="Upwork">
            </a>
        </div>
    """, unsafe_allow_html=True)

elif selected_page == "resume":
    resume()

elif selected_page == "experience":
    experience()

elif selected_page == "projects":
    projects()

elif selected_page == "contact":
    contact()

st.markdown('</div>', unsafe_allow_html=True)
