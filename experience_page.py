import streamlit as st
from PIL import Image

def experience():
    # Header for the experience section
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'></h1>",
        unsafe_allow_html=True
    )

    # List of experience entries
    experience_entries = [
        {
            "company": "Pennsylvania State University",
            "role": [
                {"title": "Graduate Wage Associate & Teaching Assistant", "duration": "Jan 2023 - Present", "details": ""}
            ],
            "description": """
                <ul>
                    <li>Conducted a comprehensive feasibility analysis of a potential Dr Pepper product line expansion into distilleries, wineries, and RTD beverages, using market research and financial modeling to validate product-market fit, projected a 15% increase in annual revenue.</li>
                    <li>Optimized grading processes by implementing an automated data upload solution, cutting turnaround time by 50% and ensuring timely delivery of submission milestones.</li>
                    <li>Managed an iterative curriculum development project, gathering feedback from over 150 stakeholders (students and faculty) and refining course modules, resulting in a 25% increase in overall engagement.</li>
                </ul>
            """,
            "location": "Pennsylvania, United States",
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Assistant Project Manager", "duration": "May 2022 - Dec 2022", "details": "Hybrid"}],
            "location": "Hyderabad, Telangana, India",
            "description": """
                <ul>
                    <li>Managed resource scheduling for 10 projects valued over $33M+ as evidenced by on-time project completions by assisting project managers with risk logs, project status updates, and resource allocation.</li>
                    <li>Improved customer relationship management data accuracy by 20% as measured by reduced data errors by managing and updating over 500 client records.</li>
                    <li>Boosted team efficiency by 30% as measured by internal performance metrics by creating 15 workflow templates.</li>
                </ul>
            """,
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Project Intern", "duration": "Apr 2022 - May 2022", "details": "On-site"}],
            "location": "Bengaluru, Karnataka, India",
            "description": """
                <ul>
                    <li>Ensured project compliance with industry standards as measured by successful audits by reviewing and coordinating avionics and electronic warfare projects as an overview engineer.</li>
                    <li>Increased RWR (Radar Warning Receivers) reliability by 15% as indicated by performance data by guiding product management and implementing life cycle extensions.</li>
                    <li>Achieved 100% product compliance and durability as confirmed by passing all quality tests by performing quality testing on Temperature, Humidity, and Vibration (THV) chamber.</li>
                </ul>
            """,
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "Hybrid"}],
            "location": "Kanpur, Uttar Pradesh, India",
            "description": """
                <ul>
                    <li>Achieved ISO 9001 and ISO 18095:2018 compliance through external audits by assisting in quality assurance for transformer manufacturing, decreased defects by 30% through root cause analysis and corrective actions.</li>
                    <li>Reduced project time by 20% by streamlining schedules, resources, and risk management.</li>
                    <li>Improved tracking accuracy by 25% using Microsoft Project and Primavera P6 for reporting.</li>
                </ul>
            """,
            "logo": "https://img.freepik.com/premium-vector/high-voltage-electrical-transformer-icon_609277-5895.jpg?w=1800"
        }
    ]

    # Render each experience entry in a two-column layout
    cols = st.columns(2)
    for idx, exp in enumerate(experience_entries):
        col = cols[idx % 2]  # Alternates between columns
        with col:
            details = exp['role'][0].get('details', '')
            st.markdown(
                f"""
                <div style="margin-bottom: 20px;">
                    <div style="display: flex; align-items: center; gap: 15px;">
                        <img src="{exp['logo']}" style="width: 60px; height: 60px; object-fit: contain;"/>
                        <div>
                            <h3 style="margin: 0; color: #2b6cb0;">{exp['company']}</h3>
                            <p style="font-size: 13px; color: #6c757d; margin: 0;">{exp['location']}</p>
                        </div>
                    </div>
                    <h5 style="color: #333; margin: 10px 0;">{exp['role'][0]['title']}</h5>
                    <p style="font-size: 13px; color: #6c757d;">{exp['role'][0]['duration']}{' | ' + details if details else ''}</p>
                    <div style="font-size: 13px; color: #4a5568; margin-top: 10px;">{exp['description']}</div>\n                </div>
                """,
                unsafe_allow_html=True
            )

# Call the function to render the experience page
if __name__ == "__main__":
    experience()
