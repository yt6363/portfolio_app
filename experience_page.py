import streamlit as st
from PIL import Image

def experience():
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
                <ol>
                    <li>Assist faculty in special projects</li>
                    <li>Laboratory instruction</li>
                    <li>Grading assignments for 140 undergraduate students</li>
                </ol>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        # Add more experiences as required
    ]

    # Render each experience entry in a "sleek card" format
    for exp in experience_entries:
        # Card container with reduced padding and no visible border
        st.markdown(
            """
            <div style="
                padding: 15px; 
                margin-bottom: 15px; 
                background-color: #ffffff;
                box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
                border-radius: 10px;
            ">
            """, unsafe_allow_html=True
        )

        # Company logo and name
        cols = st.columns([0.5, 9.5])  # Adjusted column ratios to reduce space around the logo
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=60, use_column_width=False)
        with cols[1]:
            st.markdown(f"<h3 style='margin-bottom: 2px; color: #2b6cb0;'>{exp['company']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d; margin-top: -5px;'>{exp['location']}</p>", unsafe_allow_html=True)

        # Role entries
        for role in exp["role"]:
            st.markdown(f"<h5 style='color: #333; margin-bottom: 2px;'>{role['title']}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 13px; color: #6c757d; margin-top: -10px;'>{role['duration']} | {role['details']}</p>", unsafe_allow_html=True)

        # Additional Description (Optional)
        if "description" in exp:
            with st.expander("View Details"):
                st.markdown(f"{exp['description']}", unsafe_allow_html=True)

        # Key skills as horizontally aligned tags
        if "skills" in exp:
            tags_html = """
                <div style='margin-top: 5px; display: flex; flex-wrap: wrap;'>
            """
            for skill in exp["skills"]:
                tags_html += f"""
                <span style="
                    background-color: #007bff; 
                    color: white; 
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

        # Close card container
        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
