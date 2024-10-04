import streamlit as st

# Function to initialize the text size if it is not in session_state
def initialize_text_size():
    if 'text_size' not in st.session_state:
        st.session_state['text_size'] = 16  # Default value for text size

# Function to increase text size
def increase_text_size():
    if st.session_state['text_size'] < 24:  # Set an upper limit for text size
        st.session_state['text_size'] += 2

# Function to decrease text size
def decrease_text_size():
    if st.session_state['text_size'] > 10:  # Set a lower limit for text size
        st.session_state['text_size'] -= 2

# Buttons to increase or decrease the text size
st.sidebar.button("Increase Text Size", on_click=increase_text_size)
st.sidebar.button("Decrease Text Size", on_click=decrease_text_size)

# Certifications function with updated text size handling
def Certifications():
    initialize_text_size()  # Initialize the text size if not already done

    # Page header
    st.markdown(
        f"<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px; font-size: {st.session_state['text_size'] + 10}px;'></h1>",
        unsafe_allow_html=True
    )

    # List of certification entries, including ongoing certifications
    certifications_list = [
        {
            "title": "PMI CAPM (Certified Associate in Project Management)",
            "issuer": "PMI",
            "issued_date": "Ongoing",
            "credential_id": "",
            "logo": "data:image/png;base64,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"
        },
        {
            "title": "AIGPE Six Sigma: Lean Six Sigma Green Belt Certification (Accredited)",
            "issuer": "AIGPE",
            "issued_date": "Ongoing",
            "credential_id": "",
            "logo": "data:image/png;base64,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"
        },
        {
            "title": "Microsoft Project: MS Project 2021 2019 2016 Complete - 8 PDUs",
            "issuer": "Udemy",
            "issued_date": "Sep 2024",
            "credential_id": "UC-6abec0b7-e1d4-4999-ae95-12d093a0fe76",
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEf_NHzN2yVQg/company-logo_100_100/company-logo_100_100/0/1723593046388/udemy_logo?e=1735776000&v=beta&t=d4ikIqG_1JZKDor84v02-Hzs4nwufAlMH4Bl7toaalk"
        },
        {
            "title": "Responsible Conduct of Research (RCR) - Basic",
            "issuer": "CITI Program",
            "issued_date": "Sep 2024",
            "credential_id": "53395239",
            "logo": "https://media.licdn.com/dms/image/v2/C560BAQF0C3CTnjBm2w/company-logo_100_100/company-logo_100_100/0/1631314320914?e=1735776000&v=beta&t=isQEPoGFfLziemjS95OI2F0ZyLtHfbaBo9kHRZYIBhg"
        },
        {
            "title": "Advertising on LinkedIn",
            "issuer": "LinkedIn",
            "issued_date": "May 2024",
            "credential_id": "",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
        },
        {
            "title": "How to Generate Marketing Leads with AI",
            "issuer": "LinkedIn",
            "issued_date": "May 2024",
            "credential_id": "",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png"
        },
        {
            "title": "Foundations of Project Management",
            "issuer": "Google",
            "issued_date": "Sep 2023",
            "credential_id": "",
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQHiNSL4Or29cg/company-logo_100_100/company-logo_100_100/0/1631311446380?e=1735776000&v=beta&t=yz54uBYDvTRXVCn3_vT_hG_eEHd-DjkvtVTpzZOZuFE"
        }
    ]

    # Render each certification entry with dynamic font size
    for cert in certifications_list:
        st.markdown(
            f"""
            <div style="margin-bottom: 20px; display: flex; align-items: center; gap: 15px;">
                <img src="{cert['logo']}" style="max-width: 70px; max-height: 70px; width: auto; height: auto;"/>
                <div>
                    <h3 style="color: #2b6cb0; font-size: {st.session_state['text_size'] + 2}px;">{cert['title']}</h3>
                    <p style="font-size: {st.session_state['text_size']}px; color: #6c757d; margin: 0;">{cert['issuer']} - Issued {cert['issued_date']}</p>
                    {"<p style='font-size: " + str(st.session_state['text_size'] - 2) + "px; color: #6c757d; margin: 0;'>Credential ID: " + cert['credential_id'] + "</p>" if 'credential_id' in cert else ""}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Call the function to render the certifications page
if __name__ == "__main__":
    Certifications()
