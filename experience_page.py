import streamlit as st
from PIL import Image

def experience():
    # Removed Experience Header

    # List of experience entries
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
            "skills": ["Project Plans", "Professional Skills", "Leadership" ],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        # Add more entries as needed...
    ]

    # Render each experience entry in a two-column layout
    cols = st.columns(2)
    for idx, exp in enumerate(experience_entries):
        col = cols[idx % 2]  # Alternates between columns

        with col:
            # Company logo and name
            st.markdown(
                f"""
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <img src="{exp['logo']}" style="width: 60px; height: 60px;"/>
                        <div>
                            <h3 style="margin: 0; color: #2b6cb0;">{exp['company']}</h3>
                            <p style="font-size: 13px; color: #6c757d; margin: 0;">{exp['location']}</p>
                        </div>
                    </div>
                    <h5 style="color: #333; margin: 10px 0;">{exp['role'][0]['title']}</h5>
                    <p style="font-size: 13px; color: #6c757d;">{exp['role'][0]['duration']} | {exp['role'][0]['details']}</p>
                    <div style="font-size: 13px; color: #4a5568; margin-top: 5px;">{exp['description']}</div>
                    <div style="margin-top: 5px; display: flex; flex-wrap: wrap;">
                """,
                unsafe_allow_html=True
            )

            # Render skills as tags with no box shadow and light grey background
            for skill in exp["skills"]:
                st.markdown(
                    f"""
                    <span style="
                        background-color: #e0e0e0; 
                        color: #333; 
                        padding: 3px 8px; 
                        border-radius: 5px; 
                        font-size: 12px;
                        margin-right: 5px;
                        margin-bottom: 5px;
                    ">
                        {skill}
                    </span>
                    """,
                    unsafe_allow_html=True
                )

            st.markdown("</div></div>", unsafe_allow_html=True)

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
