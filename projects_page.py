import streamlit as st

def projects():
    st.header("Academic & Personal Projects")
    st.write("Here are some of the projects I've worked on:")

    st.subheader("Health Insurance Company Database")
    st.write("""
    - Developed a SQL database for health insurer record management, handling 300+ patient profiles.
    - Included demographics, physician, and insurance ID data for comprehensive record-keeping.
    - Enhanced targeted marketing capabilities through detailed patient information analysis.
    """)

    st.subheader("EV Charging Management System")
    st.write("""
    - Developed priority-based scheduling algorithms to optimize electric vehicle charging and minimize wait times.
    - Pioneered the design of an SQL database for metadata analysis on electric vehicle catalogs and tariffs.
    - Crafted mathematical models for prioritization and ROI to steer strategic decisions.
    """)

    
    st.subheader("Dripper Design and Manufacturing Project")
    st.write("""
    - Excelled in project management, leading the design-to-manufacturing lifecycle of a high-quality dripper on time.
    - Demonstrated product management expertise by engineering a micro-irrigation dripper tailored to agricultural needs.
    - Employed **Primavera P6** for superior project timeline coordination and task execution.
    """)

    st.subheader("Keurig Dr. Pepper's Alcoholic Beverage Project")
    st.write("""
    - Oversaw Keurig Dr. Pepper's alcoholic beverage project, blending project and marketing management.
    - Conducted detailed market analysis, informing strategic direction and partnership selection.
    - Utilized **Primavera P6** for meticulous project timeline management.
    - Crafted and deployed a marketing plan, aligning with consumer trends and business goals.
    """)
    
    st.subheader("Streamlit Web Application for Data Calculators")
    st.write("""
    - Built an interactive data application using **Streamlit**.
    - Utilized **Python** for backend calculations.
    - Deployed the app on **Streamlit Sharing**, showcasing skills in **deployment** and **continuous integration**.
    - Developed models and calculators based on **Gann** and **Astronomy Methodologies** for financial and astronomical analysis
    - Implemented features such as **stock price calculators**, **planetary ingress date generators**, and **gravitational plotter**.
    - Technologies used: **Streamlit**, **Matplotlib**, **Plotly**, **SQL**, **Git/GitHub**, and **Vercel**.
    """)

# Call the function to render the projects page
if __name__ == "__main__":
    projects()
