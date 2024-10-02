import streamlit as st
from PIL import Image

def experience():
    # List of experience entries
    experience_entries = [
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - Present", "details": "Part-time | On-site"}
            ],
            "description": [
                "Assist faculty in special projects.",
                "Laboratory instruction.",
                "Grading assignments for 140 undergraduate students."
            ],
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Oct 2023", "details": ""}
            ],
            "description": [
                "Assisted students in Digital Design and Electrical Communication courses.",
                "Led hands-on sessions and expedited grading for junior engineers in Control Systems and Electromagnetism.",
                "Developed course modules to enhance learning and practical skills."
            ],
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [
                {"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "Hybrid"}
            ],
            "description": [
                "Developed standards and processes for marketing operations, including 15 templates and workflows.",
                "Assisted project managers with risk logs, project status, and resource scheduling for 10 projects.",
                "Managed and updated the CRM with 500+ client records and property listings."
            ],
            "location": "📍 Hyderabad, Telangana, India",
            "skills": ["Quality Management", "Microsoft Excel"],
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [
                {"title": "Overview Intern", "duration": "Apr 2022 - May 2022", "details": "On-site"}
            ],
            "description": [
                "Worked in a government-owned organization specializing in avionics and electronic warfare.",
                "Took responsibility for product management, focusing on the product life cycle of the RWR (Radio Warning Receiver).",
                "Performed quality testing and operated THV (Temperature, Humidity, and Vibration) chambers."
            ],
            "location": "📍 Bengaluru, Karnataka, India",
            "skills": ["Power Electronics Design", "Product Management"],
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [
                {"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "Hybrid"}
            ],
            "description": [
                "Assisted in quality assurance for transformer manufacturing, ensuring ISO 9001 compliance.",
                "Supported project management activities: timeline management, resource allocation, and risk assessment.",
                "Conducted root cause analysis and implemented corrective actions to enhance product quality.",
                "Utilized Microsoft Project and Primavera P6 for project tracking and reporting.",
                "Collaborated with cross-functional teams to streamline workflows and improve efficiency."
            ],
            "location": "📍 Kanpur, Uttar Pradesh, India",
            "skills": ["Project Plans", "Multiple Projects"],
            "logo": "data:image/png;base64,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"
        }
    ]

    # Render each experience entry in a card format with expanders for descriptions
    for exp in experience_entries:
        cols = st.columns([0.5, 9.5])  # Adjusted column ratios to reduce space around the logo
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=60, use_column_width=False)
        with cols[1]:
            st.markdown(f"**{exp['company']}**", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d;'>{exp['location']}</p>", unsafe_allow_html=True)

        # Role entries
        for role in exp["role"]:
            st.markdown(f"**{role['title']}**  \n{role['duration']} | {role['details']}", unsafe_allow_html=True)

        # Expandable description for responsibilities
        with st.expander("Responsibilities and Contributions"):
            for item in exp["description"]:
                st.write(f"- {item}")

        # Key skills presented as tags with basic styling
        st.markdown("**Skills:**")
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

        # Add some space after each experience entry for better separation
        st.markdown("---")

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
