import streamlit as st

def projects():
    # Custom CSS for project card and styling
    st.markdown("""
        <style>
        /* Card container styling */
        .project-card {
            padding: 10px;
            margin-bottom: 15px;
            background-color: #ffffff;
            border-radius: 10px;
            border: 1px solid #e0e0e0; /* Light border to define each card */
        }

        /* Project title styling */
        .project-title {
            color: #2b6cb0;
            font-size: 22px;
            margin-bottom: 5px;
        }

        /* Project list styling */
        .project-list {
            color: #4a5568;
            font-size: 14px;
            line-height: 1.3;
            margin-left: 20px;
            padding-left: 20px;
            margin-top: 10px;
        }

        /* Mobile-specific styling for compactness */
        @media only screen and (max-width: 768px) {
            .project-card {
                padding: 8px;
                margin-bottom: 10px;
            }
            .project-title {
                font-size: 18px;
            }
            .project-list {
                font-size: 13px;
                line-height: 1.2;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # List of project entries
    project_entries = [
        {
            "title": "Health Insurance Company Database",
            "description": """
                <ol class="project-list">
                    <li>Developed a SQL database for health insurer record management, handling 300+ patient profiles.</li>
                    <li>Included demographics, physician, and insurance ID data for comprehensive record-keeping.</li>
                    <li>Enhanced targeted marketing capabilities through detailed patient information analysis.</li>
                </ol>
            """
        },
        {
            "title": "EV Charging Management System",
            "description": """
                <ol class="project-list">
                    <li>Developed priority-based scheduling algorithms to optimize electric vehicle charging and minimize wait times.</li>
                    <li>Pioneered the design of an SQL database for metadata analysis on electric vehicle catalogs and tariffs.</li>
                    <li>Crafted mathematical models for prioritization and ROI to steer strategic decisions.</li>
                </ol>
            """
        },
        {
            "title": "Dripper Design and Manufacturing Project",
            "description": """
                <ol class="project-list">
                    <li>Excelled in project management, leading the design-to-manufacturing lifecycle of a high-quality dripper on time.</li>
                    <li>Demonstrated product management expertise by engineering a micro-irrigation dripper tailored to agricultural needs.</li>
                    <li>Employed Primavera P6 for superior project timeline coordination and task execution.</li>
                </ol>
            """
        },
        {
            "title": "Keurig Dr. Pepper's Alcoholic Beverage Project",
            "description": """
                <ol class="project-list">
                    <li>Oversaw Keurig Dr. Pepper's alcoholic beverage project, blending project and marketing management.</li>
                    <li>Conducted detailed market analysis, informing strategic direction and partnership selection.</li>
                    <li>Utilized Primavera P6 for meticulous project timeline management.</li>
                    <li>Crafted and deployed a marketing plan, aligning with consumer trends and business goals.</li>
                </ol>
            """
        },
        {
            "title": "Streamlit Web Application for Data Calculators",
            "description": """
                <ol class="project-list">
                    <li>Built an interactive data application using Streamlit.</li>
                    <li>Utilized Python for backend calculations.</li>
                    <li>Deployed the app on Streamlit Sharing, showcasing skills in deployment and continuous integration.</li>
                    <li>Developed models and calculators based on Gann and Astronomy Methodologies for financial and astronomical analysis.</li>
                    <li>Implemented features such as stock price calculators, planetary ingress date generators, and gravitational plotter.</li>
                    <li>Technologies used: Streamlit, Matplotlib, Plotly, SQL, Git/GitHub, and Vercel.</li>
                </ol>
            """
        }
    ]

    # Render each project entry in a card format without box shadows
    for project in project_entries:
        st.markdown(
            f"""
            <div class="project-card">
                <h3 class="project-title">{project['title']}</h3>
                {project['description']}
            </div>
            """,
            unsafe_allow_html=True
        )

# Call the function to render the projects page
if __name__ == "__main__":
    projects()
