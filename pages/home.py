import streamlit as st
import streamlit.components.v1 as components

# ======================================
# IMPORT COMPONENTS
# ======================================
from components.hero_slider import hero_slider_html
from components.partners_slider import partners_slider_html
from components.numbers_section import numbers_section_html

# ======================================
# HOME PAGE
# ======================================
def show_home():

    # ======================================
    # HERO SLIDER
    # ======================================
    components.html(hero_slider_html, height=420)

    # ======================================
    # SECTION TITLES
    # ======================================
    st.markdown(
        '<div class="home-subtitle">OUR EDGE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-title">Why Genesis Digital Stands Out</div>',
        unsafe_allow_html=True
    )

    st.markdown("---")

    # ======================================
    # FIRST ROW CARDS
    # ======================================
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="card">
            <div class="card-title">Art Meets Technology</div>
            <div class="card-text">
                We fuse creative storytelling with cutting-edge digital infrastructure.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="card">
            <div class="card-title">Industry Expertise</div>
            <div class="card-text">
                Deep domain knowledge across hospitality, travel, and digital media.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ======================================
    # SECOND ROW CARDS
    # ======================================
    col3, col4 = st.columns(2)

    with col3:
        st.markdown("""
        <div class="card">
            <div class="card-title">Client-Centric Approach</div>
            <div class="card-text">
                Every project is custom-architected to your needs.
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown("""
        <div class="card">
            <div class="card-title">Scalable Execution</div>
            <div class="card-text">
                From small to large scale video production seamlessly.
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ======================================
    # PARTNERS TITLE
    # ======================================
    st.markdown("""
    <div style="
        text-align:center;
        color:#0057b8;
        font-size:34px;
        font-weight:900;
        margin-top:40px;
        margin-bottom:25px;
    ">
        Our Partners
    </div>
    """, unsafe_allow_html=True)

    # ======================================
    # PARTNERS SLIDER
    # ======================================
    components.html(partners_slider_html, height=160)

    # ======================================
    # NUMBERS SECTION
    # ======================================
    components.html(
        numbers_section_html,
        height=1000,
        scrolling=True
    )
