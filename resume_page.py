import streamlit as st
import os
import fitz  # PyMuPDF
import base64

def resume():
    st.header("")
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

                    # Use a moderate scaling factor to improve image quality while keeping it manageable
                    zoom_x = 2.0  # Set zoom for balance between clarity and screen fitting
                    zoom_y = 2.0
                    matrix = fitz.Matrix(zoom_x, zoom_y)

                    # Get high-resolution image of the page
                    image = page.get_pixmap(matrix=matrix)
                    img_bytes = image.tobytes(output="png")

                    # Convert image bytes to base64
                    img_base64 = base64.b64encode(img_bytes).decode()

                    # Display image of the page in Streamlit with improved styling for mobile
                    st.markdown(
                        f"""
                        <div style="text-align: center; margin-bottom: 20px;">
                            <img src="data:image/png;base64,{img_base64}" 
                                 style="width: 90%; max-width: 800px; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);" />
                            <p style="font-size: 14px;">Page {page_number + 1}</p>
                        </div>
                        """,
                        unsafe_allow_html=True
                    )
        except Exception as e:
            st.error("An error occurred while trying to display the resume.")
            st.write(e)
    else:
        st.error("Resume file not found. Please ensure the file is in the correct location.")

# Call the function to render the resume page
if __name__ == "__main__":
    resume()
