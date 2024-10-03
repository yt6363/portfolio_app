import streamlit as st

def Certifications():
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Certifications</h1>",
        unsafe_allow_html=True
    )

    # Add the ongoing certifications at the top
    st.markdown(
        """
        <div style="text-align: center; padding-bottom: 20px;">
            <strong>PMI CAPM (Certified Associate in Project Management) (On-going)</strong><br>
            <strong>AIGPE Six Sigma: Lean Six Sigma Green Belt Certification (Accredited) (In-Progress)</strong>
        </div>
        """,
        unsafe_allow_html=True
    )

    # List of other certification entries
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
            "logo": "https://www.citiprogram.org/media/logo.png"
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
            "logo": "https://upload.wikimedia.org/wikipedia/commons/4/4a/Logo_of_Google_%282013-2015%29.png"
        }
    ]

    for cert in certifications_list:
        st.markdown(
            """
            <div style="
                display: flex; 
                align-items: center; 
                gap: 15px; 
                padding: 15px; 
                margin-bottom: 15px; 
                background-color: #ffffff; 
                border-radius: 10px;
            ">
                <img src="{logo}" style="width: 50px; height: 50px;">
                <div>
                    <h4 style="margin: 0; color: #2b6cb0;">{title}</h4>
                    <p style="margin: 0; color: #6c757d; font-size: 14px;">{issuer} - Issued {issued_date}</p>
                    {credential_info}
                </div>
            </div>
            """.format(
                logo=cert['logo'],
                title=cert['title'],
                issuer=cert['issuer'],
                issued_date=cert['issued_date'],
                credential_info=f"<p style='margin: 0; color: #6c757d; font-size: 12px;'>Credential ID: {cert['credential_id']}</p>" if 'credential_id' in cert else ""
            ),
            unsafe_allow_html=True
        )

# Call the function to render the certifications page
if __name__ == "__main__":
    certifications()
