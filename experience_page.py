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
            "skills": ["Project Plans", "Professional Skills", "Leadership", "+27 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Oct 2023", "details": "10 months"}
            ],
            "description": """
                <ol>
                    <li>Assisted students in Digital Design, Electrical Communication course and developed course modules.</li>
                    <li>Led hands-on sessions and expedited grading for junior engineers in Control Systems and Electromagnetism, enhancing learning and practical skills.</li>
                </ol>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership", "+27 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "8 mos | Hybrid"}],
            "location": "📍 Hyderabad, Telangana, India",
            "description": """
                <ol>
                    <li>Develop standards and processes for marketing operations, including 15 templates and workflows.</li>
                    <li>Assist project managers with risk logs, project status, and resource scheduling for 10 projects and a team of 25.</li>
                    <li>Manage and update the CRM with 500+ client records with their property listings.</li>
                </ol>
            """,
            "skills": ["Quality Management", "Microsoft Excel", "+11 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Student Intern", "duration": "Apr 2022 - May 2022", "details": "2 mos | On-site"}],
            "location": "📍 Bengaluru, Karnataka, India",
            "description": """
                <ol>
                    <li>Worked in a government-owned organization specializing in avionics and electronic warfare.</li>
                    <li>Took responsibility for product management, focusing on the product life cycle of RWR (Radio warning receiver).</li>
                    <li>Performed quality testing and operated THV (temperature, humidity, and vibration) chamber.</li>
                </ol>
            """,
            "skills": ["Power Electronics Design", "Product Management", "+19 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "4 mos | Hybrid"}],
            "location": "📍 Kanpur, Uttar Pradesh, India",
            "description": """
                <ol>
                    <li>Assisted in quality assurance for transformer manufacturing, ensuring ISO 9001 compliance.</li>
                    <li>Supported project management activities: timeline management, resource allocation, and risk assessment.</li>
                    <li>Conducted root cause analysis and implemented corrective actions to enhance product quality.</li>
                    <li>Utilized Microsoft Project and Primavera P6 for project tracking & reporting.</li>
                    <li>Collaborated with cross-functional teams to streamline workflows and improve efficiency.</li>
                </ol>
            """,
            "skills": ["Project Plans", "Multiple Projects", "+2 skills"],
            "logo": "data:image/png;base64,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"
        }
    ]

    # Render each experience entry in a "sleek card" format
    for exp in experience_entries:
        # Card container with reduced padding and no border
        st.markdown(
            """
            <div style="
                padding: 15px; 
                margin-bottom: 15px; 
                background-color: #ffffff;
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
            st.markdown(f"<p style='font-size: 13px; color: #6c757d; margin-top: -5px;'>{exp['location']}</p>", unsafe_allow_html=True)

        # Role entries
        for role in exp["role"]:
            st.markdown(f"<h5 style='color: #333; margin-bottom: 2px;'>{role['title']}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 13px; color: #6c757d; margin-top: -10px;'>{role['duration']} | {role['details']}</p>", unsafe_allow_html=True)

        # Additional Description (Optional)
        if "description" in exp:
            st.markdown(f"<p style='font-size: 13px; color: #4a5568; margin-top: 5px;'>{exp['description']}</p>", unsafe_allow_html=True)

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
