import streamlit as st
import requests

def contact():
    st.markdown(
        "<h1 style='text-align: center; color: #2b6cb0; padding-bottom: 20px;'> </h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<p style='text-align: center;'>Feel free to reach out via the form below:</p>",
        unsafe_allow_html=True
    )

    # Contact Form
    with st.form(key='contact_form'):
        name = st.text_input("Name", placeholder="Enter your name here")
        email = st.text_input("Email", placeholder="Enter your email address")
        message = st.text_area("Message", placeholder="Write your message here", height=150)
        submit_button = st.form_submit_button("Send Message")

        # Form Submission Handling
        if submit_button:
            if not name.strip() or not email.strip() or not message.strip():
                st.error("All fields are required. Please fill in all fields before submitting.")
            else:
                # Post the data to Formspree
                formspree_url = "https://formspree.io/f/mgvewwkr"
                data = {
                    'name': name,
                    'email': email,
                    'message': message
                }

                try:
                    response = requests.post(formspree_url, data=data)

                    if response.status_code == 200:
                        st.success("Thank you! Your message has been sent.")
                    else:
                        st.error("There was an error sending your message. Please try again later.")
                except requests.exceptions.RequestException as e:
                    st.error("There was an error connecting to the server. Please try again later.")
                    st.write(e)

# Call the function to render the contact page
if __name__ == "__main__":
    contact()
