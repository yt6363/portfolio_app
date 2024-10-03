import streamlit as st

def Certifications():
    # Page header
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Certifications</h1>",
        unsafe_allow_html=True
    )

    # Header for ongoing certifications
    st.markdown(
        "<p style='text-align: center; font-size: 16px;'>"
        "PMI CAPM (Certified Associate in Project Management) (Ongoing), "
        "AIGPE Six Sigma: Lean Six Sigma Green Belt Certification (Accredited) (In-Progress)"
        "</p>",
        unsafe_allow_html=True
    )

    # List of certification entries
    certifications_list = [
        {
            "title": "Microsoft Project: MS Project 2021 2019 2016 Complete - 8 PDUs",
            "issuer": "Udemy",
            "issued_date": "Sep 2024",
            "credential_id": "UC-6abec0b7-e1d4-4999-ae95-12d093a0fe76",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/e/ea/Udemy_logo.png"
        },
        {
            "title": "Responsible Conduct of Research (RCR) - Basic",
            "issuer": "CITI Program",
            "issued_date": "Sep 2024",
            "credential_id": "53395239",
            "logo": "https://upload.wikimedia.org/wikipedia/en/2/2d/CITI_Program_Logo.png"
        },
        {
            "title": "Advertising on LinkedIn",
            "issuer": "LinkedIn",
            "issued_date": "May 2024",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
        },
        {
            "title": "How to Generate Marketing Leads with AI",
            "issuer": "LinkedIn",
            "issued_date": "May 2024",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
        },
        {
            "title": "Foundations of Project Management",
            "issuer": "Google",
            "issued_date": "Sep 2023",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/2/2f/Google_2015_logo.svg"
        }
    ]

    # Render each certification entry without extra div tags or shadows
    for cert in certifications_list:
        # Build the certification display card
        st.markdown(
            f"""
            <div style="display: flex; align-items: center; padding: 10px 0;">
                <img src="{cert['logo']}" style="width: 50px; height: 50px; margin-right: 15px;">
                <div style="flex-grow: 1;">
                    <h4 style="margin: 0; color: #2b6cb0;">{cert['title']}</h4>
                    <p style="margin: 0; color: #6c757d; font-size: 14px;">{cert['issuer']} - Issued {cert['issued_date']}</p>
                    {"<p style='margin: 0; color: #6c757d; font-size: 12px;'>Credential ID: " + cert['credential_id'] + "</p>" if 'credential_id' in cert else ""}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Call the function to render the certifications page
if __name__ == "__main__":
    Certifications()
