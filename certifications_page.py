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
        f"<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px; font-size: {st.session_state['text_size'] + 10}px;'>Certifications</h1>",
        unsafe_allow_html=True
    )

    # List of certification entries, including ongoing certifications
    certifications_list = [
        {
            "title": "PMI CAPM (Certified Associate in Project Management)",
            "issuer": "PMI",
            "issued_date": "11/02/2024",
            "credential_id": "3969140",
            "logo": "https://ccrs.pmi.org/image/providerlogo/1000000003",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "AIGPE Six Sigma: Lean Six Sigma Green Belt Certification (Accredited)",
            "issuer": "AIGPE",
            "issued_date": "11/07/2024",
            "credential_id": "ZSSGB121154025",
            "logo": "https://gaqm.org/uploads/cert_logos/logo_5442.png",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "AWS Flash - Introduction to Cost Management for SaaS",
            "issuer": "Amazon Web Services (AWS)",
            "issued_date": "Nov 2024",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "AWS Flash - SaaS Business Fundamentals",
            "issuer": "Amazon Web Services (AWS)",
            "issued_date": "Nov 2024",
            "logo": "https://upload.wikimedia.org/wikipedia/commons/9/93/Amazon_Web_Services_Logo.svg",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "PMI Talking to AI: Prompt Engineering for Project Managers",
            "issuer": "PMI",
            "issued_date": "Nov 2024",
            "logo": "https://ccrs.pmi.org/image/providerlogo/1000000003",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "PMI: Data Landscape of GenAI for Project Managers",
            "issuer": "PMI",
            "issued_date": "Nov 2024",
            "logo": "https://ccrs.pmi.org/image/providerlogo/1000000003",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "PMI: Generative AI Overview for Project Managers",
            "issuer": "PMI",
            "issued_date": "Nov 2024",
            "logo": "https://ccrs.pmi.org/image/providerlogo/1000000003",
            "logo_style": "max-width: 95px; max-height: 95px; width: auto; height: auto;"
        },
        {
            "title": "Microsoft Project: MS Project 2021 2019 2016 Complete - 8 PDUs",
            "issuer": "Udemy",
            "issued_date": "Sep 2024",
            "credential_id": "UC-6abec0b7-e1d4-4999-ae95-12d093a0fe76",
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEf_NHzN2yVQg/company-logo_100_100/company-logo_100_100/0/1723593046388/udemy_logo?e=1735776000&v=beta&t=d4ikIqG_1JZKDor84v02-Hzs4nwufAlMH4Bl7toaalk",
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
                    {"<p style='font-size: " + str(st.session_state['text_size'] - 2) + "px; color: #6c757d; margin: 0;'>Credential ID: " + cert['credential_id'] + "</p>" if cert.get('credential_id') else ""}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

# Call the function to render the certifications page
if __name__ == "__main__":
    Certifications()
