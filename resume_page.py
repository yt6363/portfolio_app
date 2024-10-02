import streamlit as st
import os
import fitz  # PyMuPDF

def resume():
    st.header("Resume")
    st.write("Here's a quick overview of my educational and professional background.")

    # Path to the local resume file
    resume_path = "Yashwanth sai Tatineni Resume.pdf"

    # Check if the file exists
    if os.path.exists(resume_path):
        # Provide a download button for the resume
        with open(resume_path, "rb") as pdf_file:
            st.download_button(
                label="Download Resume",
                data=pdf_file,
                file_name="Yashwanth_sai_Tatineni_Resume.pdf",
                mime="application/pdf"
            )

        # Render PDF pages as high-resolution images
        try:
            with fitz.open(resume_path) as pdf_document:
                num_pages = pdf_document.page_count
                st.write(f"Preview of Resume ({num_pages} pages):")

                for page_number in range(num_pages):
                    page = pdf_document.load_page(page_number)

                    # Use a higher scaling factor to improve image quality
                    zoom_x = 2.0  # Increase to make the resolution higher (2.0 means 200%)
                    zoom_y = 2.0
                    matrix = fitz.Matrix(zoom_x, zoom_y)

                    # Get high-resolution image of the page
                    image = page.get_pixmap(matrix=matrix)
                    img_bytes = image.tobytes(output="png")

                    # Display image of the page in Streamlit
                    st.image(img_bytes, caption=f"Page {page_number + 1}", use_column_width=True)
        except Exception as e:
            st.error("An error occurred while trying to display the resume.")
            st.write(e)
    else:
        st.error("Resume file not found. Please ensure the file is in the correct location.")
