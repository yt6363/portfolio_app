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
            "description": [
                "Assist faculty in special projects.",
                "Laboratory instruction.",
                "Grading assignments for 140 undergraduate students."
            ],
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        # Add more experiences as needed...
    ]

    # Render each experience entry
    for exp in experience_entries:
        cols = st.columns([0.5, 9.5])  # Adjusted column ratios for proper spacing
        with cols[0]:
            if exp["logo"]:
                st.image(exp["logo"], width=50, use_column_width=False)
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

        # Key skills presented as simple tags without extra styling
        st.markdown("**Skills:**")
        st.write(", ".join(exp["skills"]))

        # Add some space after each experience entry for better separation
        st.markdown("---")

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
