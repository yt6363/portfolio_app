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
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - Present", "details": "Part-time | On-site"},
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Oct 2023", "details": "10 months"}
            ],
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership", "+27 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "8 mos | Hybrid"}],
            "location": "📍 Hyderabad, Telangana, India",
            "description": "Developed standards and processes for marketing operations, including 15 templates and workflows.",
            "skills": ["Quality Management", "Microsoft Excel", "+11 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Student Intern", "duration": "Apr 2022 - May 2022", "details": "2 mos | On-site"}],
            "location": "📍 Bengaluru, Karnataka, India",
            "description": "Worked as an intern under electronic warfare and avionics SBU.",
            "skills": ["Power Electronics Design", "Product Management", "+19 skills"],
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "4 mos | Hybrid"}],
            "location": "📍 Kanpur, Uttar Pradesh, India",
            "description": "Supported quality assurance for transformer manufacturing and ISO 9001 compliance.",
            "skills": ["Project Plans", "Multiple Projects", "+2 skills"],
            "logo": "https://via.placeholder.com/100"
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
        cols = st.columns([1, 8])
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=50, use_column_width=False)
        with cols[1]:
            st.markdown(f"<h3 style='margin-bottom: 5px; color: #2b6cb0;'>{exp['company']}</h3>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 15px; color: #6c757d;'>{exp['location']}</p>", unsafe_allow_html=True)

        # Role entries
        for role in exp["role"]:
            st.markdown(f"<h5 style='color: #333; margin-bottom: 5px;'>{role['title']}</h5>", unsafe_allow_html=True)
            st.markdown(f"<p style='font-size: 14px; color: #6c757d; margin-top: -10px;'>{role['duration']} | {role['details']}</p>", unsafe_allow_html=True)

        # Additional Description (Optional)
        if "description" in exp:
            st.markdown(f"<p style='font-size: 15px; color: #4a5568; margin-top: 10px;'>{exp['description']}</p>", unsafe_allow_html=True)

        # Key skills as horizontally aligned tags
        if "skills" in exp:
            tags = "".join(
                f"""
                <span style="
                    background-color: #007bff; 
                    color: white; 
                    padding: 5px 10px; 
                    border-radius: 5px; 
                    font-size: 13px;
                    margin-right: 5px;
                    margin-bottom: 5px;
                    display: inline-block;
                ">
                    {skill}
                </span>
                """ for skill in exp["skills"]
            )
            st.markdown(f"<div style='margin-top: 10px;'>{tags}</div>", unsafe_allow_html=True)

        # Close card container
        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
