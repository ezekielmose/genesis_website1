import streamlit as st

# ======================================
# SERVICES PAGE
# ======================================
def show_services():

    st.title("Our Services")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.subheader("Video Sourcing")

    with col2:
        st.subheader("AI Solutions")

    with col3:
        st.subheader("Data Analysis")
