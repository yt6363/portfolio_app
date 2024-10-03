import streamlit as st

def Certifications():
    # Page header
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Certifications</h1>",
        unsafe_allow_html=True
    )

    # List of certification entries, including ongoing certifications
    certifications_list = [
        {
            "title": "PMI CAPM (Certified Associate in Project Management)",
            "issuer": "PMI",
            "issued_date": "Ongoing"
        },
        {
            "title": "AIGPE Six Sigma: Lean Six Sigma Green Belt Certification (Accredited)",
            "issuer": "AIGPE",
            "issued_date": "In-Progress"
        },
        {
            "title": "Microsoft Project: MS Project 2021 2019 2016 Complete - 8 PDUs",
            "issuer": "Udemy",
            "issued_date": "Sep 2024",
            "credential_id": "UC-6abec0b7-e1d4-4999-ae95-12d093a0fe76"
        },
        {
            "title": "Responsible Conduct of Research (RCR) - Basic",
            "issuer": "CITI Program",
            "issued_date": "Sep 2024",
            "credential_id": "53395239"
        },
        {
            "title": "Advertising on LinkedIn",
            "issuer": "LinkedIn",
            "issued_date": "May 2024"
        },
        {
            "title": "How to Generate Marketing Leads with AI",
            "issuer": "LinkedIn",
            "issued_date": "May 2024"
        },
        {
            "title": "Foundations of Project Management",
            "issuer": "Google",
            "issued_date": "Sep 2023"
        }
    ]

    # Render each certification entry
    for cert in certifications_list:
        st.markdown(
            f"""
            <div style="margin-bottom: 20px;">
                <h3 style="color: #2b6cb0;">{cert['title']}</h3>
                <p style="font-size: 14px; color: #6c757d; margin: 0;">{cert['issuer']} - Issued {cert['issued_date']}</p>
                {"<p style='font-size: 12px; color: #6c757d; margin: 0;'>Credential ID: " + cert['credential_id'] + "</p>" if 'credential_id' in cert else ""}
            </div>
            """,
            unsafe_allow_html=True
        )

# Call the function to render the certifications page
if __name__ == "__main__":
    Certifications()
