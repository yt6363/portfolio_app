import streamlit as st
from PIL import Image

def experience():
    # Header for the experience section
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Experience</h1>",
        unsafe_allow_html=True
    )

    # List of experience entries (easy to modify and add/remove content)
    experience_entries = [
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - Present", "details": "Part-time | On-site"}
            ],
            "description": """
                <ul>
                    <li>Assist faculty in special projects</li>
                    <li>Laboratory instruction</li>
                    <li>Grading assignments for 140 undergraduate students</li>
                </ul>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        # Add more experiences as needed
    ]

    # Render each experience entry with a simple and clean design
    for exp in experience_entries:
        # Company logo and name (no container or box for a cleaner look)
        cols = st.columns([0.5, 9.5])  # Adjust column ratios for proper spacing
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=50, use_column_width=False)
        with cols[1]:
            st.markdown(f"<h3 style='margin-bottom: 5px; color: #2b6cb0;'>{exp['company']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d; margin-top: -5px;'>{exp['location']}</p>", unsafe_allow_html=True)

        # Role entries
        for role in exp["role"]:
            st.markdown(f"<h5 style='color: #333; margin-bottom: 2px;'>{role['title']}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 13px; color: #6c757d; margin-top: -10px;'>{role['duration']} | {role['details']}</p>", unsafe_allow_html=True)

        # Expandable description
        if "description" in exp:
            with st.expander("Responsibilities and Contributions"):
                st.markdown(f"{exp['description']}", unsafe_allow_html=True)

        # Key skills presented as simple tags without extra styling
        if "skills" in exp:
            tags_html = "<div style='margin-top: 10px;'>"
            for skill in exp["skills"]:
                tags_html += f"""
                <span style="
                    background-color: #e0e0e0; 
                    color: #333; 
                    padding: 3px 8px; 
                    border-radius: 5px; 
                    font-size: 12px;
                    margin-right: 5px;
                    margin-bottom: 5px;
                    display: inline-block;
                ">
                    {skill}
                </span>
                """
            tags_html += "</div>"
            st.markdown(tags_html, unsafe_allow_html=True)

        # Add some space after each experience entry for better separation
        st.markdown("<hr style='border: none; border-top: 1px solid #e0e0e0;'>", unsafe_allow_html=True)

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
