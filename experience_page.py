import streamlit as st
from PIL import Image  # For logo resizing if needed
import base64

def experience():
    st.header("Experience")

    # List of experience entries (easy to modify and add/remove content)
    experience_entries = [
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - Present", "details": "Part-time | On-site"},
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Oct 2023", "details": "10 months"}
            ],
            "location": "Pennsylvania, United States",
            "skills": "Project Plans, Professional Skills, Leadership, and +27 skills",
            "logo": "https://upload.wikimedia.org/wikipedia/en/7/7e/Pennsylvania_State_University_seal.png"  # Replace with the actual logo URL if applicable
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "8 mos | Hybrid"}],
            "location": "Hyderabad, Telangana, India",
            "description": "Develop standards and processes for marketing operations, including 15 templates and workflows.",
            "skills": "Quality Management, Microsoft Excel, and +11 skills",
            "logo": "https://via.placeholder.com/100x100.png"  # Replace with the actual logo URL if applicable
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Student Intern", "duration": "Apr 2022 - May 2022", "details": "2 mos | On-site"}],
            "location": "Bengaluru, Karnataka, India",
            "description": "Worked as an intern under electronic warfare and avionics SBU.",
            "skills": "Power Electronics Design, Product Management, and +19 skills",
            "logo": "https://via.placeholder.com/100x100.png"  # Replace with the actual logo URL if applicable
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "4 mos | Hybrid"}],
            "location": "Kanpur, Uttar Pradesh, India",
            "description": "Supported quality assurance for transformer manufacturing and ISO 9001 compliance.",
            "skills": "Project Plans, Multiple Projects, and +2 skills",
            "logo": "https://via.placeholder.com/100x100.png"  # Replace with the actual logo URL if applicable
        }
    ]

    # Render each experience entry in a "card" format
    for exp in experience_entries:
        # Card container
        st.markdown(
            """
            <div style="
                border: 1px solid #e6e6e6; 
                border-radius: 10px; 
                padding: 20px; 
                margin-bottom: 20px; 
                background-color: #f9f9f9;
                box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
            ">
            """, unsafe_allow_html=True
        )

        # Company logo and name
        cols = st.columns([1, 4])
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=80)
        with cols[1]:
            st.markdown(f"<h2 style='margin-bottom: 10px; color: #2b6cb0;'>{exp['company']}</h2>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d;'>{exp['location']}</p>", unsafe_allow_html=True)

        # Role entries
        for role in exp["role"]:
            st.markdown(f"<h4 style='color: #333; margin-bottom: 5px;'>{role['title']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d;'>{role['duration']}  |  {role['details']}</p>", unsafe_allow_html=True)

        # Additional Description (Optional)
        if "description" in exp:
            st.markdown(f"<p style='font-size: 15px; color: #4a5568;'>{exp['description']}</p>", unsafe_allow_html=True)

        # Key skills and others
        st.markdown(f"<p style='font-weight: bold; color: #2b6cb0;'>Skills:</p> <p style='color: #4a5568;'>{exp['skills']}</p>", unsafe_allow_html=True)

        # Close card container
        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
