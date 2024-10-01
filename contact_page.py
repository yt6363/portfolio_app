import streamlit as st

def contact():
    st.header("Contact Me")
    st.write("Feel free to reach out via the form below:")

    with st.form(key='contact_form'):
        name = st.text_input("Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit_button = st.form_submit_button("Send")

        if submit_button:
            st.success("Thank you! Your message has been sent.")
