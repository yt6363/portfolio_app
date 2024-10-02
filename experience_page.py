import streamlit as st

def experience():
    # Page title
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0;'>Experience</h1>",
        unsafe_allow_html=True
    )

    # List of experience entries (easy to modify and add/remove content)
    experience_entries = [
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - Present", "details": "Part-time | On-site"},
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Oct 2023", "details": "10 months"}
            ],
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership", "+27 skills"],
            "description": [
                "Assisted faculty members in research and administrative tasks.",
                "Developed course materials for undergraduate classes.",
                "Guided students during lab sessions and provided tutoring assistance."
            ],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "8 mos | Hybrid"}],
            "location": "📍 Hyderabad, Telangana, India",
            "skills": ["Quality Management", "Microsoft Excel", "+11 skills"],
            "description": [
                "Developed standards and processes for marketing operations.",
                "Created over 15 templates and workflows to streamline processes.",
                "Coordinated marketing events to increase outreach."
            ],
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Student Intern", "duration": "Apr 2022 - May 2022", "details": "2 mos | On-site"}],
            "location": "📍 Bengaluru, Karnataka, India",
            "skills": ["Power Electronics Design", "Product Management", "+19 skills"],
            "description": [
                "Worked as an intern under electronic warfare and avionics SBU.",
                "Assisted in power electronics design and testing.",
                "Contributed to the development of electronic warfare systems."
            ],
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "4 mos | Hybrid"}],
            "location": "📍 Kanpur, Uttar Pradesh, India",
            "skills": ["Project Plans", "ISO 9001 Compliance", "Multiple Projects"],
            "description": [
                "Supported quality assurance for transformer manufacturing.",
                "Assisted in ISO 9001 compliance processes and documentation.",
                "Worked on project management tasks for various client projects."
            ],
            "logo": "https://via.placeholder.com/100x100.png"
        }
    ]

    # Render each experience entry in a modern, clean format
    for exp in experience_entries:
        # Card container with modern styling
        st.markdown(
            """
            <div style="
                border-radius: 10px; 
                padding: 20px; 
                margin-bottom: 20px; 
                background-color: #f8f9fa; 
                box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
            ">
            """, unsafe_allow_html=True
        )

        # Company logo and details
        cols = st.columns([1, 8])
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=50)
        with cols[1]:
            st.markdown(f"<h4 style='color: #2b6cb0;'>{exp['role'][0]['title']} @ {exp['company']}</h4>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d;'>{exp['role'][0]['duration']} | {exp['location']}</p>", unsafe_allow_html=True)

        # Role descriptions in bullet points
        st.markdown("<ul>", unsafe_allow_html=True)
        for desc in exp["description"]:
            st.markdown(f"<li style='font-size: 14px; color: #333;'>{desc}</li>", unsafe_allow_html=True)
        st.markdown("</ul>", unsafe_allow_html=True)

        # Skills as tags
        st.markdown("<div style='display: flex; flex-wrap: wrap; gap: 8px; margin-top: 10px;'>", unsafe_allow_html=True)
        for skill in exp["skills"]:
            st.markdown(
                f"""
                <span style="
                    background-color: #007bff; 
                    color: white; 
                    padding: 4px 8px; 
                    border-radius: 5px; 
                    font-size: 12px;
                ">
                    {skill}
                </span>
                """, unsafe_allow_html=True
            )
        st.markdown("</div>", unsafe_allow_html=True)

        # Close card container
        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
