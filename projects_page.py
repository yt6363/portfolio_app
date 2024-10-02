import streamlit as st

def projects():
    # Header for the projects section
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'></h1>",
        unsafe_allow_html=True
    )

    # List of project entries
    project_entries = [
        {
            "title": "Health Insurance Company Database",
            "description": """
                <ol style="color: #4a5568;">
                    <li>Developed a SQL database for health insurer record management, handling 300+ patient profiles.</li>
                    <li>Included demographics, physician, and insurance ID data for comprehensive record-keeping.</li>
                    <li>Enhanced targeted marketing capabilities through detailed patient information analysis.</li>
                </ol>
            """
        },
        {
            "title": "EV Charging Management System",
            "description": """
                <ol style="color: #4a5568;">
                    <li>Developed priority-based scheduling algorithms to optimize electric vehicle charging and minimize wait times.</li>
                    <li>Pioneered the design of an SQL database for metadata analysis on electric vehicle catalogs and tariffs.</li>
                    <li>Crafted mathematical models for prioritization and ROI to steer strategic decisions.</li>
                </ol>
            """
        },
        {
            "title": "Dripper Design and Manufacturing Project",
            "description": """
                <ol style="color: #4a5568;">
                    <li>Excelled in project management, leading the design-to-manufacturing lifecycle of a high-quality dripper on time.</li>
                    <li>Demonstrated product management expertise by engineering a micro-irrigation dripper tailored to agricultural needs.</li>
                    <li>Employed <strong>Primavera P6</strong> for superior project timeline coordination and task execution.</li>
                </ol>
            """
        },
        {
            "title": "Keurig Dr. Pepper's Alcoholic Beverage Project",
            "description": """
                <ol style="color: #4a5568;">
                    <li>Oversaw Keurig Dr. Pepper's alcoholic beverage project, blending project and marketing management.</li>
                    <li>Conducted detailed market analysis, informing strategic direction and partnership selection.</li>
                    <li>Utilized <strong>Primavera P6</strong> for meticulous project timeline management.</li>
                    <li>Crafted and deployed a marketing plan, aligning with consumer trends and business goals.</li>
                </ol>
            """
        },
        {
            "title": "Streamlit Web Application for Data Calculators",
            "description": """
                <ol style="color: #4a5568;">
                    <li>Built an interactive data application using <strong>Streamlit</strong>.</li>
                    <li>Utilized <strong>Python</strong> for backend calculations.</li>
                    <li>Deployed the app on <strong>Streamlit Sharing</strong>, showcasing skills in deployment and continuous integration.</li>
                    <li>Developed models and calculators based on <strong>Gann</strong> and <strong>Astronomy Methodologies</strong> for financial and astronomical analysis.</li>
                    <li>Implemented features such as <strong>stock price calculators</strong>, <strong>planetary ingress date generators</strong>, and <strong>gravitational plotter</strong>.</li>
                    <li>Technologies used: <strong>Streamlit</strong>, <strong>Matplotlib</strong>, <strong>Plotly</strong>, <strong>SQL</strong>, <strong>Git/GitHub</strong>, and <strong>Vercel</strong>.</li>
                </ol>
            """
        }
    ]

    # Render each project entry in a card format
    for project in project_entries:
        st.markdown(
            """
            <div style="
                padding: 15px; 
                margin-bottom: 15px; 
                background-color: #ffffff;
                border-radius: 10px;
            ">
            """, unsafe_allow_html=True
        )
        
        # Project title
        st.markdown(f"<h3 style='color: #2b6cb0;'>{project['title']}</h3>", unsafe_allow_html=True)

        # Project description with ordered list
        st.markdown(f"{project['description']}", unsafe_allow_html=True)

        # Close card container
        st.markdown("</div>", unsafe_allow_html=True)

# Call the function to render the projects page
if __name__ == "__main__":
    projects()
