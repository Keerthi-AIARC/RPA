import streamlit as st

# Set page title
st.set_page_config(page_title="Twin-D Digital Marketing Agency")

# Title
st.title("👋 Welcome to Twin-D Digital Marketing Agency")

# Ask user if they want to explore services
st.subheader("Are you really interested in exploring our services?")

# Radio buttons with no default selection
choice = st.radio("Choose one:", options=["", "Yes", "No"], index=0, format_func=lambda x: "Select..." if x == "" else x)

# If Yes is selected
if choice == "Yes":
    st.markdown("### 🚀 All Digital Marketing Services:")
    st.markdown("- 📣 Meta / Facebook Ads")
    st.markdown("- 🔍 Google Ads")
    st.markdown("- 🌐 Website Development")
    st.markdown("- 📈 SEO (Search Engine Optimization)")
    st.markdown("- 🧠 Branding & Identity")
    st.markdown("- 🤖 AI Automation Solutions")
    st.markdown("- 📍 Google My Business (GMB) Optimization")

    # Button to book appointment
    if st.button("📅 Book Your Appointment"):
        st.success("✅ Thank you for contacting us, We will get back to you shortly.")

# If No is selected
elif choice == "No":
    st.info("📨 Keep in Touch, We Will Work Together in Future.")
