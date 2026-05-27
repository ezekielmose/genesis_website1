import streamlit as st

# ======================================
# IMPORT STYLES
# ======================================
from styles.global_css import load_css

# ======================================
# IMPORT COMPONENTS
# ======================================
from components.header import show_header
from components.footer import show_footer

# ======================================
# IMPORT PAGES
# ======================================
from pages.home import show_home
from pages.ai_analyzer import show_ai_analyzer
from pages.services import show_services
from pages.about import show_about


st.set_page_config(
    page_title="Genesis Digital",
    page_icon="🌐",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# HIDE SIDEBAR COMPLETELY
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# ======================================
# PAGE CONFIGURATION
# ======================================
st.set_page_config(
    page_title="Genesis Digital",
    page_icon="🌐",
    layout="wide"
)

# ======================================
# LOAD GLOBAL CSS
# ======================================
load_css()

# ======================================
# HEADER
# ======================================
tabs = show_header()

# ======================================
# HOME PAGE
# ======================================
with tabs[0]:
    show_home()

# ======================================
# AI ANALYZER PAGE
# ======================================
with tabs[1]:
    show_ai_analyzer()

# ======================================
# SERVICES PAGE
# ======================================
with tabs[2]:
    show_services()

# ======================================
# ABOUT PAGE
# ======================================
with tabs[3]:
    show_about()

# ======================================
# FOOTER
# ======================================
show_footer()
