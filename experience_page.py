import streamlit as st
from PIL import Image

def experience():
    # Header for the experience section
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Experience</h1>",
        unsafe_allow_html=True
    )
    
    # List of experience entries
    experience_entries = [
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Present", "details": ""}
            ],
            "description": """
                <ul>
                    <li>Spearheaded a streamlined grading process to enhance consistency and reduce turnaround time, demonstrating process management skills and contributing to overall course quality.</li>
                    <li>Provided one-on-one support to students by clearing doubts in Basic Electric Course and assisting in PHY 211 and 212 Labs, enhancing their understanding and performance.</li>
                </ul>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Overview Intern", "duration": "Apr 2022 - May 2022", "details": "On-site"}],
            "location": "📍 Bengaluru, Karnataka, India",
            "description": """
                <ul>
                    <li>Worked in a government-owned organization specializing in avionics and electronic warfare.</li>
                    <li>Took responsibility for product management, focusing on the product life cycle of RWR (Radio warning receiver).</li>
                    <li>Performed quality testing and operated THV (temperature, humidity, and vibration) chamber.</li>
                </ul>
            """,
            "skills": ["Power Electronics Design", "Product Management"],
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - May 2025", "details": "Part-time | On-site"}
            ],
            "description": """
                <ul>
                    <li>Led the scheduling, grading, and progress tracking for laboratory sessions, ensuring smooth operation and effective communication among stakeholders.</li>
                    <li>Collaborated on Laboratory Curriculum Optimization, which involved developing new modules and assessment methods, improving efficiency and engagement for over 140 undergraduate students.</li>
                </ul>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "Hybrid"}],
            "location": "📍 Kanpur, Uttar Pradesh, India",
            "description": """
                <ul>
                    <li>Assisted in quality assurance for transformer manufacturing, ensuring ISO 9001 compliance.</li>
                    <li>Supported project management activities: timeline management, resource allocation, and risk assessment.</li>
                    <li>Conducted root cause analysis and implemented corrective actions to enhance product quality.</li>
                    <li>Utilized Microsoft Project and Primavera P6 for project tracking & reporting.</li>
                    <li>Collaborated with cross-functional teams to streamline workflows and improve efficiency.</li>
                </ul>
            """,
            "skills": ["Project Plans", "Multiple Projects"],
            "logo": "https://img.freepik.com/premium-vector/high-voltage-electrical-transformer-icon_609277-5895.jpg?w=1800"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "Hybrid"}],
            "location": "📍 Hyderabad, Telangana, India",
            "description": """
                <ul>
                    <li>Develop standards and processes for marketing operations, including 15 templates and workflows.</li>
                    <li>Assist project managers with risk logs, project status, and resource scheduling for 10 projects and a team of 25.</li>
                    <li>Manage and update the CRM with 500+ client records with their property listings.</li>
                </ul>
            """,
            "skills": ["Quality Management", "Microsoft Excel"],
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        }
    ]

    # Render each experience entry in a two-column layout
    cols = st.columns(2)
    for idx, exp in enumerate(experience_entries):
        col = cols[idx % 2]  # Alternates between columns
        with col:
            details = exp['role'][0].get('details', '')
            st.markdown(
                f"""
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <img src="{exp['logo']}" style="width: 60px; height: 60px; object-fit: contain;"/>
                        <div>
                            <h3 style="margin: 0; color: #2b6cb0;">{exp['company']}</h3>
                            <p style="font-size: 13px; color: #6c757d; margin: 0;">{exp['location']}</p>
                        </div>
                    </div>
                    <h5 style="color: #333; margin: 10px 0;">{exp['role'][0]['title']}</h5>
                    <p style="font-size: 13px; color: #6c757d;">{exp['role'][0]['duration']}{" | " + details if details else ""}</p>
                    <div style="font-size: 13px; color: #4a5568; margin-top: 10px;">{exp['description']}</div>
                    <div style="margin-top: 10px;">
                        {" ".join([f"<span style='background-color: #e0e0e0; color: #333; padding: 3px 8px; border-radius: 5px; font-size: 12px; margin-right: 5px; margin-bottom: 5px; display: inline-block;'>{skill}</span>" for skill in exp['skills']])}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
