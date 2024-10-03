import streamlit as st

def experience():
    st.markdown("""
        <style>
        /* Experience page styling */
        .experience-container {
            display: flex;
            flex-wrap: wrap;
            justify-content: space-between;
        }
        .experience-card {
            width: 48%;
            background-color: #ffffff;
            margin-bottom: 15px;
        }
        .experience-card h3 {
            color: #2b6cb0;
            margin-bottom: 5px;
        }
        .experience-card h5 {
            color: #333;
        }
        .experience-card p {
            font-size: 14px;
            color: #6c757d;
        }
        .skills-container {
            margin-top: 10px;
        }
        .skill-tag {
            background-color: #f0f0f0;
            color: #333;
            padding: 5px 10px;
            border-radius: 5px;
            font-size: 12px;
            margin-right: 5px;
            margin-bottom: 5px;
            display: inline-block;
        }
        </style>
    """, unsafe_allow_html=True)

    # Experience entries
    experience_entries = [
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Graduate Wage Assistant", "duration": "Oct 2023 - Present", "details": "Part-time | On-site"}
            ],
            "description": """
                <ul>
                    <li>Assist faculty in special projects</li>
                    <li>Laboratory instruction</li>
                    <li>Grading assignments for 140 undergraduate students</li>
                </ul>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Penn State Harrisburg",
            "role": [
                {"title": "Teaching Assistant", "duration": "Jan 2023 - Oct 2023", "details": ""}
            ],
            "description": """
                <ul>
                    <li>Assisted students in Digital Design, Electrical Communication course and developed course modules.</li>
                    <li>Led hands-on sessions and expedited grading for junior engineers in Control Systems and Electromagnetism, enhancing learning and practical skills.</li>
                </ul>
            """,
            "location": "📍 Pennsylvania, United States",
            "skills": ["Project Plans", "Professional Skills", "Leadership"],
            "logo": "https://media.licdn.com/dms/image/v2/C4D0BAQFUE0Km4XXSBQ/company-logo_100_100/company-logo_100_100/0/1631332415612?e=1735776000&v=beta&t=R4qboXMy84-qxVFO3cD7Uo1xnfXI_3p9fuHaTDAmLmQ"
        },
        {
            "company": "Incredible India Projects Pvt Ltd.",
            "role": [{"title": "Marketing Operations Intern", "duration": "May 2022 - Dec 2022", "details": "Hybrid"}],
            "description": """
                <ul>
                    <li>Develop standards and processes for marketing operations, including 15 templates and workflows.</li>
                    <li>Assist project managers with risk logs, project status, and resource scheduling for 10 projects and a team of 25.</li>
                    <li>Manage and update the CRM with 500+ client records with their property listings.</li>
                </ul>
            """,
            "location": "📍 Hyderabad, Telangana, India",
            "skills": ["Quality Management", "Microsoft Excel"],
            "logo": "https://media.licdn.com/dms/image/v2/C4E0BAQGpTI5Hv69-RQ/company-logo_100_100/company-logo_100_100/0/1631315747746?e=1735776000&v=beta&t=ye059Rt3avH1IxHGOpazL9yi0ak68CUMU0Vz3i3hrVY"
        },
        {
            "company": "Bharat Electronics Limited",
            "role": [{"title": "Overview Intern", "duration": "Apr 2022 - May 2022", "details": "On-site"}],
            "description": """
                <ul>
                    <li>Worked in a government-owned organization specializing in avionics and electronic warfare.</li>
                    <li>Took responsibility for product management, focusing on the product life cycle of RWR (Radio warning receiver).</li>
                    <li>Performed quality testing and operated THV (temperature, humidity, and vibration) chamber.</li>
                </ul>
            """,
            "location": "📍 Bengaluru, Karnataka, India",
            "skills": ["Power Electronics Design", "Product Management"],
            "logo": "https://media.licdn.com/dms/image/v2/D560BAQEoT1DsKihRxQ/company-logo_100_100/company-logo_100_100/0/1725596070207/bharat_electronics_limited_logo?e=1735776000&v=beta&t=j77_3BJFaVrjoJ-eUh96puYmDlvvMnwvEyw-gisX1SI"
        },
        {
            "company": "New Tech Transformers Pvt Ltd.",
            "role": [{"title": "Quality and Project Management Intern", "duration": "May 2021 - Aug 2021", "details": "Hybrid"}],
            "description": """
                <ul>
                    <li>Assisted in quality assurance for transformer manufacturing, ensuring ISO 9001 compliance.</li>
                    <li>Supported project management activities: timeline management, resource allocation, and risk assessment.</li>
                    <li>Conducted root cause analysis and implemented corrective actions to enhance product quality.</li>
                    <li>Utilized Microsoft Project and Primavera P6 for project tracking & reporting.</li>
                    <li>Collaborated with cross-functional teams to streamline workflows and improve efficiency.</li>
                </ul>
            """,
            "location": "📍 Kanpur, Uttar Pradesh, India",
            "skills": ["Project Plans", "Multiple Projects"],
            "logo": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAMwAAADACAMAAAB/Pny7AAAAq1BMVEX///8AAAD09PQgICDJyclZWVliYmL7+/umpqb4+PiSkpIMDAyqqqqXl5ejo6M2Njbj4+PPz8/8sEArKyu/v7+2trYVFRUwMDCFhYXs7OwbGxtPT0/V1dU/Pz/b29t5eXlGRkZtbW39rTf0vWr+/O/89+T///jv7ubw26/vxn7x1qD789r2vWD568Lws0j22an0xXf11ZfzpyT66sr5tlTxsDvt3LfyyYr2sEZvCYKfAAAKL0lEQVR4nO1daWOyuBZmV0S2sstuq7fr223a+v9/2ZAElCXMFGwozs3zxapwTh6znIWTlGEoKCgoKCgoKCgoKCgoKCgoKCgozoWtmlOpElSbrIIoZkODrIoKRsjGEVENS5dlfaIajvBZ1l0S1WDwLBsnRFWUSGKW5QkPghXLsnmyIKuEYRZJXihakVajsACaTFKHrEElCkkdEBKL2JDsnDXSIRFUAZEgPUSHc8KXSkhPTrXUU4xnQnQMOC8hVDIajjiS2SylgIQCTlryU5Ex2ROILDZqTYFAQkEd8UmXTmCgGTX58c+Lb0Go/XIEfAF/yo5hGP2kLfvx5SbJah3/08I7kGtcCHRNvWNYnahlBsjr6jIhMIKAK3CWXhlICApRQlaXnv9Um3sRsB0oVpzlZwxwIc9iqyuWJbL0N+Fj1BZYjfZvFiu8xClCDcPFKOb9M+KoyOcxIt0pgsCF2lXs29w5Ijkb090q8TgDoG7XABTfPIsKAGf6SlNqPE10
