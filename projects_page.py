import streamlit as st

def projects():
    # Header for the projects section
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'>Projects</h1>",
        unsafe_allow_html=True
    )
    
    # Custom CSS for the project section styling
    st.markdown("""
        <style>
        /* Custom styles for project cards */
        .project-card {
            padding: 10px;
            margin-bottom: 20px;
            background-color: #ffffff;
            border-radius: 8px;
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

        /* Link styling */
        .project-link img {
            width: 32px;  /* Increased size from 24px to 32px */
            height: 32px;  /* Increased size from 24px to 32px */
            margin-right: 10px;
            vertical-align: middle;
        }
        </style>
    """, unsafe_allow_html=True)

    # List of project entries with GitHub and website links
    project_entries = [
        {
            "title": "Health Insurance Company Database",
            "description": [
                "Developed a SQL database for health insurer record management, handling 300+ patient profiles.",
                "Included demographics, physician, and insurance ID data for comprehensive record-keeping.",
                "Enhanced targeted marketing capabilities through detailed patient information analysis."
            ],
            "github_link": "https://github.com/yt6363/Health-Insurance-Company-Database"
        },
        {
            "title": "EV Charging Management System",
            "description": [
                "Developed priority-based scheduling algorithms to optimize electric vehicle charging and minimize wait times.",
                "Pioneered the design of an SQL database for metadata analysis on electric vehicle catalogs and tariffs.",
                "Crafted mathematical models for prioritization and ROI to steer strategic decisions."
            ],
            "github_link": "https://github.com/yt6363/V-Charging-Management-System"
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
            "title": "Personal Portfolio Web Application",
            "description": [
                "Developed a responsive, interactive portfolio application using Streamlit to showcase experience, projects, resume, and contact information.",
                "Designed and implemented a top navigation bar and a two-column layout for experience and project sections to create a structured and user-friendly interface.",
                "Optimized the app for both desktop and mobile viewing, addressing zoom levels and rendering issues.",
                "Integrated a contact form using Formspree for easy communication.",
                "Added features like PDF resume preview and download, utilizing high-resolution image rendering for text clarity.",
                "Utilized custom CSS for styling to give a sleek and modern user experience."
            ],
            "github_link": "https://github.com/yt6363/portfolio_app",
            "website_link": "https://yashwanthtatineni.streamlit.app/"
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
            ],
            "website_link": "https://1133633.streamlit.app/"
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
            """,
            unsafe_allow_html=True
        )

        # Add GitHub link if available
        if 'github_link' in project:
            st.markdown(
                f"<a href='{project['github_link']}' target='_blank' class='project-link'><img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' alt='GitHub Link'></a>",
                unsafe_allow_html=True
            )

        # Add Website link if available
        if 'website_link' in project:
            st.markdown(
                f"<a href='{project['website_link']}' target='_blank' class='project-link'><img src='https://e7.pngegg.com/pngimages/722/126/png-clipart-web-development-computer-icons-world-wide-web-logo-symmetry.png' alt='Website Link'></a>",
                unsafe_allow_html=True
            )

        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to render the projects page
if __name__ == "__main__":
    projects()
