import streamlit as st
from PIL import Image
import requests
from io import BytesIO

# Set page configuration
st.set_page_config(layout="wide")

# Page header with styling
st.markdown(
    """
    <h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Experience</h1>
    """,
    unsafe_allow_html=True
)

# Placeholder images (use URLs for logos if they aren't available locally)
datadoit_logo_url = "https://via.placeholder.com/80"
avidea_logo_url = "https://via.placeholder.com/80"

# Load images from URLs
response_datadoit = requests.get(datadoit_logo_url)
datadoit_logo = Image.open(BytesIO(response_datadoit.content))

response_avidea = requests.get(avidea_logo_url)
avidea_logo = Image.open(BytesIO(response_avidea.content))

# Define the experience entries
experience_entries = [
    {
        "company": "Avidea",
        "title": "AI Engineer (End-of-studies Internship)",
        "duration": "Feb 2024 - May 2024",
        "description": [
            "Trained a car damage segmentation model to identify 6 damage types in insurance subscription images.",
            "Created and containerized an API, enabling deployment and integration by the web team on Avidea’s demo page.",
            "Reduced the necessary time to process images by a factor of 3 and cut workforce requirements by 20%."
        ],
        "skills": ["MMDetection", "Ultralytics", "YOLOv8", "Label Studio", "Docker", "Flask"],
        "logo": avidea_logo,
        "link": "https://www.avidea.tn/"
    },
    {
        "company": "DataDoIt",
        "title": "AI Engineer (Summer Internship)",
        "duration": "Jul 2023 - Aug 2023",
        "description": [
            "Developed an API for scanning and displaying local network RTSP camera streams.",
            "Explored the NVIDIA TAO toolkit 4.0 and trained and benchmarked various object detection models from its vast model zoo, achieving 0.90 mAP for the best model, YOLOv4.",
            "Explored methods for enhancing model precision with limited real data, settling on training on mixed data (real + synthetic) and validating on real data only.",
            "Achieved a 0.96 mAP50 on the validation set using the YOLOv8 model with mixed data and generated a TensorRT engine to optimize the model for inference."
        ],
        "skills": ["Python", "Linux", "Flask", "NVIDIA TAO", "Ultralytics", "YOLOv8"],
        "logo": datadoit_logo,
        "link": "https://data-doit.com/"
    }
]

# CSS styling for a modern, sleek look
css_styles = """
<style>
    .experience-container {
        padding: 20px;
        border-radius: 10px;
        background-color: #f9f9f9;
        margin-bottom: 25px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .experience-header {
        font-size: 22px;
        font-weight: bold;
        color: #1f77b4;
    }
    .experience-duration {
        font-size: 15px;
        color: #6c757d;
    }
    .experience-description {
        font-size: 15px;
        color: #333;
    }
    .skills-tag {
        display: inline-block;
        background-color: #007bff;
        color: white;
        padding: 5px 10px;
        border-radius: 10px;
        margin-right: 5px;
        margin-top: 10px;
        font-size: 12px;
    }
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# Render each experience in a clean card-like format
for exp in experience_entries:
    with st.container():
        st.markdown("<div class='experience-container'>", unsafe_allow_html=True)

        # Two columns for logo and details
        logo_col, details_col = st.columns((1, 4))

        with logo_col:
            st.image(exp["logo"], width=80)

        with details_col:
            # Header with company link
            st.markdown(
                f"<h3 class='experience-header'>{exp['title']} @ <a href='{exp['link']}' target='_blank'>{exp['company']}</a></h3>",
                unsafe_allow_html=True
            )
            st.markdown(f"<p class='experience-duration'>{exp['duration']}</p>", unsafe_allow_html=True)

            # Description bullet points
            st.markdown("<ul style='padding-left: 20px;'>", unsafe_allow_html=True)
            for desc in exp["description"]:
                st.markdown(f"<li class='experience-description'>{desc}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)

            # Skills tags
            for skill in exp["skills"]:
                st.markdown(f"<span class='skills-tag'>{skill}</span>", unsafe_allow_html=True)

        st.markdown("</div>", unsafe_allow_html=True)
