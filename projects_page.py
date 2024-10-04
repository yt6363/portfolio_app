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
            box-shadow: none;
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

        /* Link icon styling */
        .link-icons {
            display: flex;
            align-items: center;
            gap: 15px;
            margin-top: 15px;
        }

        .link-icons img {
            width: 30px;
            height: 30px;
            cursor: pointer;
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
            .link-icons {
                gap: 8px;
            }
        }
        </style>
    """, unsafe_allow_html=True)

    # List of project entries
    project_entries = [
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

        # Add GitHub and Website links if available
        link_icons = []
        if 'github_link' in project:
            link_icons.append(
                f"<a href='{project['github_link']}' target='_blank'><img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' alt='GitHub Link'></a>"
            )
        
        if 'website_link' in project:
            link_icons.append(
                f"<a href='{project['website_link']}' target='_blank'><img src='https://upload.wikimedia.org/wikipedia/commons/d/db/Internet-web-browser.svg' alt='Website Link'></a>"
            )

        if link_icons:
            st.markdown(
                f"<div class='link-icons'>{''.join(link_icons)}</div>",
                unsafe_allow_html=True
            )

# Call the function to render the projects page
if __name__ == "__main__":
    projects()
