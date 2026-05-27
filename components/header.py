import streamlit as st

# ======================================
# HEADER COMPONENT (TABS NAVIGATION)
# ======================================
def show_header():

    col1, col2 = st.columns([1, 8])

    # ======================================
    # LOGO
    # ======================================
    with col1:
        st.image("assets/logo.png", width=120)

    # ======================================
    # TABS MENU
    # ======================================
    with col2:
        tabs = st.tabs([
            "Home",
            "AI Analyzer",
            "Our Services",
            "About Us"
        ])

    return tabs
