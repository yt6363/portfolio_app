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
            "logo": "https://ccrs.pmi.org/image/providerlogo/1000000003",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "AIGPE Six Sigma: Lean Six Sigma Green Belt Certification (Accredited)",
            "issuer": "AIGPE",
            "issued_date": "Ongoing",
            "credential_id": "",
            "logo": "https://gaqm.org/uploads/cert_logos/logo_5442.png",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "Microsoft Project: MS Project 2021 2019 2016 Complete - 8 PDUs",
            "issuer": "Udemy",
            "issued_date": "Sep 2024",
            "credential_id": "UC-6abec0b7-e1d4-4999-ae95-12d093a0fe76",
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEf_NHzN2yVQg/company-logo_100_100/company-logo_100_100/0/1723593046388/udemy_logo?e=1735776000&v=beta&t=d4ikIqG_1JZKDor84v02-Hzs4nwufAlMH4Bl7toaalk",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "Responsible Conduct of Research (RCR) - Basic",
            "issuer": "CITI Program",
            "issued_date": "Sep 2024",
            "credential_id": "53395239",
            "logo": "https://media.licdn.com/dms/image/v2/C560BAQF0C3CTnjBm2w/company-logo_100_100/company-logo_100_100/0/1631314320914?e=1735776000&v=beta&t=isQEPoGFfLziemjS95OI2F0ZyLtHfbaBo9kHRZYIBhg",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "Advertising on LinkedIn",
            "issuer": "LinkedIn",
            "issued_date": "May 2024",
            "credential_id": "",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "How to Generate Marketing Leads with AI",
            "issuer": "LinkedIn",
            "issued_date": "May 2024",
            "credential_id": "",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "Foundations of Project Management",
            "issuer": "Google",
            "issued_date": "Sep 2023",
            "credential_id": "",
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQHiNSL4Or29cg/company-logo_100_100/company-logo_100_100/0/1631311446380?e=1735776000&v=beta&t=yz54uBYDvTRXVCn3_vT_hG_eEHd-DjkvtVTpzZOZuFE",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        }
    ]

    # Render each certification entry with dynamic font size
    for cert in certifications_list:
        st.markdown(
            f"""
            <div style="margin-bottom: 20px; display: flex; align-items: center; gap: 15px;">
                <img src="{cert['logo']}" style="{cert['logo_style']}"/>
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
