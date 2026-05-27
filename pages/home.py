import streamlit as st

from components.hero_slider import render_hero_slider
from components.partners_slider import render_partners_slider
from components.numbers_section import render_numbers

def show_home():

    render_hero_slider()

    st.markdown(
        '<div class="home-subtitle">OUR EDGE</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="home-title">Why Genesis Digital Stands Out</div>',
        unsafe_allow_html=True
    )

    render_partners_slider()

    render_numbers()
