import streamlit as st

from styles.global_css import load_css
from components.header import render_header
from components.footer import render_footer

from pages.home import show_home
from pages.services import show_services
from pages.about import show_about
from pages.ai_analyzer import show_ai_analyzer

# PAGE CONFIG
st.set_page_config(
    page_title="Genesis Digital",
    page_icon="🌐",
    layout="wide"
)

# LOAD CSS
load_css()

# HEADER
tabs = render_header()

# PAGES
with tabs[0]:
    show_home()

with tabs[1]:
    show_services()

with tabs[2]:
    show_about()

# AI PAGE ONLY AFTER LOGIN
if st.session_state.logged_in:
    with tabs[3]:
        show_ai_analyzer()

# FOOTER
render_footer()
