import streamlit as st
from streamlit_option_menu import option_menu
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
            margin-top: 50px;
            margin-right: 50px;
            border: 5px solid #FF4B4B;
        }}
        .profile-container {{
            display: flex;
            align-items: center;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .text-container {{
            max-width: 400px;
            margin-left: 20px;
        }}
        </style>
        <div class="profile-container">
            <img class="profile-img" src="data:image/png;base64,{base64_img}">
            <div class="text-container">
                <h2 style="font-size:30px;">Aspiring AI Engineer</h2>
                <p style="background-color: #ffffff10; padding: 15px; border-radius: 10px; font-size: 16px;">
                    👋 Hi, I'm Yashwanth! I am currently pursuing my Master of Engineering Management at Pennsylvania State University Harrisburg.
                    I bring both motivation and commitment to make meaningful contributions in engineering and AI fields.
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
    st.header("")
    add_profile_image("Yashwanth sai Tatineni.jpeg", width=150)

    # Social media links
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://linkedin.com/in/Yashwanth)")
    with col2:
        st.markdown("[![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Yashwanth)")
    with col3:
        st.markdown("[![Upwork](https://img.shields.io/badge/Upwork-6fda44?style=for-the-badge&logo=upwork&logoColor=white)](https://www.upwork.com/freelancers/~Yashwanth)")

elif selected_page == "Resume":
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")
    # Add resume details here...

elif selected_page == "Experience":
    st.header("Experience")
    st.write("Here are some of my roles and responsibilities:")
    # Add experience details here...

elif selected_page == "Projects":
    st.header("Projects")
    st.write("Here are some of the projects I've worked on:")
    # Add project details here...

elif selected_page == "Contact":
    st.header("Contact Me")
    st.write("Feel free to reach out via the form below:")
    # Add contact form here...
