import streamlit as st

# App title
st.title("📋 Lead Form Application")

# Input Fields
name = st.text_input("Enter your Name")
whatsapp = st.text_input("Enter your WhatsApp Number")
email = st.text_input("Enter your Email ID")

# Submit Button
if st.button("Submit"):
    if name.strip() and whatsapp.strip() and email.strip():
        st.success("✅ Thank you for Registering with us!")
    else:
        st.warning("⚠️ Please fill the Important Fields. Thank you.")
