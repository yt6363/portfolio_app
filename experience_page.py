import streamlit as st

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

    # Render each experience entry
    for exp in experience_entries:
        # Company logo and name
        cols = st.columns([1, 4])
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=60)
        with cols[1]:
            st.subheader(exp["company"])
            st.write(f"{exp['location']}")

        # Role entries
        for role in exp["role"]:
            st.markdown(f"**{role['title']}**")
            st.write(f"{role['duration']}  |  {role['details']}")

        # Additional Description (Optional)
        if "description" in exp:
            st.write(f"*{exp['description']}*")

        # Key skills and others
        st.write(f"**Skills:** {exp['skills']}")
        st.markdown("---")


# Call the function to render the experience page
if __name__ == "__main__":
    experience()
