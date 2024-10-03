import streamlit as st

def projects():
    # Custom CSS for the project section styling
    st.markdown("""
        <style>
        /* Custom styles for project cards */
        .project-card {
            padding: 10px;
            margin-bottom: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: none;  /* No box shadow */
        }

        /* Project title styling */
        .project-title {
            color: #2b6cb0;
            font-size: 22px;
            margin-bottom: 10px;
        }

        /* Project list styling */
        .project-list {
            color: #4a5568;
            font-size: 16px;
            line-height: 1.6;
        }

        .project-list li {
            margin-bottom: 8px;
        }

        /* Mobile-specific styling for compactness */
        @media only screen and (max-width: 768px) {
            .project-card {
                padding: 8px;
                margin-bottom: 15px;
            }
            .project-title {
                font-size: 20px;
                text-align: center;
            }
            .project-list {
                font-size: 14px;
                line-height: 1.4;
                margin-left: 15px;
                padding-left: 15px;
            }
            .project-list li {
                margin-bottom: 5px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # List of project entries
    project_entries = [
        {
            "title": "Health Insurance Company Database",
            "description": [
                "Developed a SQL database for health insurer record management, handling 300+ patient profiles.",
                "Included demographics, physician, and insurance ID data for comprehensive record-keeping.",
                "Enhanced targeted marketing capabilities through detailed patient information analysis."
            ]
        },
        {
            "title": "EV Charging Management System",
            "description": [
                "Developed priority-based scheduling algorithms to optimize electric vehicle charging and minimize wait times.",
                "Pioneered the design of an SQL database for metadata analysis on electric vehicle catalogs and tariffs.",
                "Crafted mathematical models for prioritization and ROI to steer strategic decisions."
            ]
        },
        {
            "title": "Dripper Design and Manufacturing Project",
            "description": [
                "Excelled in project management, leading the design-to-manufacturing lifecycle of a high-quality dripper on time.",
                "Demonstrated product management expertise by engineering a micro-irrigation dripper tailored to agricultural needs.",
                "Employed Primavera P6 for superior project timeline coordination and task execution."
            ]
        },
        {
            "title": "Keurig Dr. Pepper's Alcoholic Beverage Project",
            "description": [
                "Oversaw Keurig Dr. Pepper's alcoholic beverage project, blending project and marketing management.",
                "Conducted detailed market analysis, informing strategic direction and partnership selection.",
                "Utilized Primavera P6 for meticulous project timeline management.",
                "Crafted and deployed a marketing plan, aligning with consumer trends and business goals."
            ]
        },
        {
            "title": "Streamlit Web Application for Data Calculators",
            "description": [
                "Built an interactive data application using Streamlit.",
                "Utilized Python for backend calculations.",
                "Deployed the app on Streamlit Sharing, showcasing skills in deployment and continuous integration.",
                "Developed models and calculators based on Gann and Astronomy Methodologies for financial and astronomical analysis.",
                "Implemented features such as stock price calculators, planetary ingress date generators, and gravitational plotter.",
                "Technologies used: Streamlit, Matplotlib, Plotly, SQL, Git/GitHub, and Vercel."
            ]
        }
    ]

    # Render each project entry
    for project in project_entries:
        st.markdown(
            f"""
            <div class="project-card">
                <h3 class="project-title">{project['title']}</h3>
                <ul class="project-list">
                    {''.join([f"<li>{item}</li>" for item in project['description']])}
                </ul>
            </div>
            """,
            unsafe_allow_html=True
        )

# Call the function to render the projects page
if __name__ == "__main__":
    projects()
