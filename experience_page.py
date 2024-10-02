import streamlit as st
from PIL import Image
from pathlib import Path

# Set page configuration
st.set_page_config(layout="wide")

# Page header with a divider
st.header("Experience")

# Paths to assets and CSS
datadoit_logo = Image.open("assets/datadoit.png")
avidea_logo = Image.open("assets/avidea.png")

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

# CSS styling
css_styles = """
<style>
    .experience-container {
        padding: 15px 0;
    }
    .experience-header {
        font-size: 24px;
        font-weight: bold;
        color: #2b6cb0;
    }
    .experience-duration {
        font-size: 16px;
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
        border-radius: 5px;
        margin-right: 5px;
        margin-top: 10px;
        font-size: 13px;
    }
</style>
"""
st.markdown(css_styles, unsafe_allow_html=True)

# Display each experience entry
for exp in experience_entries:
    with st.container():
        # Create two columns, one for image and one for text
        image_column, text_column = st.columns((1, 5))

        # Display company logo
        with image_column:
            st.image(exp["logo"], width=80)

        # Display experience details
        with text_column:
            # Header with company link
            st.markdown(
                f"<h2 class='experience-header'>{exp['title']} @ <a href='{exp['link']}' target='_blank'>{exp['company']}</a></h2>",
                unsafe_allow_html=True
            )
            st.markdown(f"<p class='experience-duration'>{exp['duration']}</p>", unsafe_allow_html=True)

            # Description bullet points
            st.markdown("<ul>", unsafe_allow_html=True)
            for desc in exp["description"]:
                st.markdown(f"<li class='experience-description'>{desc}</li>", unsafe_allow_html=True)
            st.markdown("</ul>", unsafe_allow_html=True)

            # Skills tags
            for skill in exp["skills"]:
                st.markdown(f"<span class='skills-tag'>{skill}</span>", unsafe_allow_html=True)

