import streamlit as st

# ======================================
# GLOBAL CSS LOADER
# ======================================
def load_css():

    st.markdown("""
    <style>

    /* ======================================
       GLOBAL BACKGROUND
    ====================================== */
    .stApp {
        background: linear-gradient(
            135deg,
            #d9d9d9 0%,
            #eeeeee 40%,
            #ffffff 100%
        );
    }

    /* HIDE STREAMLIT DEFAULTS */
    #MainMenu, footer, header {
        visibility: hidden;
    }

    .block-container {
        padding-top: 0.5rem;
    }

    /* GLOBAL TEXT */
    p, label, div {
        color: black;
    }

    /* ======================================
       HOME TITLES
    ====================================== */
    .home-title {
        text-align: center;
        color: #0057b8;
        font-weight: 900;
    }

    .home-subtitle {
        text-align: center;
        color: #0057b8;
        font-size: 28px;
        font-weight: 800;
        letter-spacing: 1px;
    }

    a {
        color: blue !important;
    }

    /* ======================================
       CARD STYLE
    ====================================== */
    .card {
        border: 2px solid #0dcfff;
        background: rgba(255,255,255,0.88);
        backdrop-filter: blur(10px);
        padding: 30px 25px;
        border-radius: 14px;
        min-height: 260px;
        margin-bottom: 20px;
        box-shadow: 0 4px 18px rgba(0,0,0,0.08);
    }

    .card-title {
        color: #0057b8 !important;
        font-size: 28px;
        font-weight: bold;
        margin-bottom: 18px;
    }

    .card-text {
        font-size: 18px;
        line-height: 1.8;
    }

    /* ======================================
       HEADER TABS
    ====================================== */
    div[data-baseweb="tab-list"] {
        background: transparent !important;
        border: none !important;
        gap: 45px;
        padding-top: 15px;
        padding-bottom: 10px;
        margin-top: 18px;
        justify-content: center !important;
        display: flex !important;
        width: 100%;
    }

    button[role="tab"] {
        background: transparent !important;
        border: none !important;
        color: black !important;
        font-size: 18px !important;
        font-weight: 900 !important;
        padding: 10px 0px !important;
        transition: 0.3s ease;
    }

    button[role="tab"]:hover {
        color: red !important;
    }

    button[aria-selected="true"] {
        color: black !important;
        border-bottom: 3px solid red !important;
    }

    /* ======================================
       FOOTER
    ====================================== */
    .footer {
        position: fixed;
        bottom: 0;
        left: 0;
        width: 100%;
        background-color: #0057b8;
        color: white;
        text-align: center;
        padding: 10px;
        font-size: 13px;
        z-index: 999;
    }

    </style>
    """, unsafe_allow_html=True)
