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
            "logo": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAq1BMVEX///8AAAD09PQgICDJ..."
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
