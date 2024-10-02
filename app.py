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
)

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
                    👋 Hi, I'm Yashwanth an engineering management student with hands-on experience in project management, 
                    quality assurance, and data analysis. My expertise spans across industries, where I have optimized workflows, managed timelines, 
                    and conducted in-depth data analysis using SQL and Tableau. With a passion for innovative problem-solving, 
                    I am currently pursuing certifications in Six Sigma Green Belt and CAPM, which enhance my ability to deliver excellence in project execution. 
                    I am driven by a desire to apply my skills to meaningful, impact-driven projects.
                </p>
            </div>
        </div>
    """, unsafe_allow_html=True)

# Top Navigation Bar
st.markdown(
    """
    <style>
    .top-navbar {
        background-color: #ffffff;
        padding: 10px 0;
        text-align: center;
        border-bottom: 1px solid #ddd;
        margin-bottom: 20px;
    }
    .top-navbar a {
        margin: 0 15px;
        font-size: 20px;
        text-decoration: none;
        color: #333;
        font-weight: bold;
    }
    .top-navbar a:hover {
        color: #FF4B4B;
    }
    .top-navbar a.active {
        color: #FF4B4B;
    }
    </style>
    <div class="top-navbar">
        <a href="/?page=about-me" class="{ 'active' if st.session_state.get('current_page') == 'about-me' else '' }">About Me</a>
        <a href="/?page=resume" class="{ 'active' if st.session_state.get('current_page') == 'resume' else '' }">Resume</a>
        <a href="/?page=experience" class="{ 'active' if st.session_state.get('current_page') == 'experience' else '' }">Experience</a>
        <a href="/?page=projects" class="{ 'active' if st.session_state.get('current_page') == 'projects' else '' }">Projects</a>
        <a href="/?page=contact" class="{ 'active' if st.session_state.get('current_page') == 'contact' else '' }">Contact</a>
    </div>
    """,
    unsafe_allow_html=True
)

# Determine which page to display
current_page = st.experimental_get_query_params().get("page", ["about-me"])[0]

# Main Content
if current_page == "about-me":
    # Removed the header "About Me" and enlarged the profile image and text
    add_profile_image("Yashwanth sai Tatineni.jpeg", width=250)

    # Social media links arranged compactly below the text
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

elif current_page == "resume":
    resume()

elif current_page == "experience":
    experience()

elif current_page == "projects":
    projects()

elif current_page == "contact":
    contact()
