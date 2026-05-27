import streamlit as st
import pandas as pd

# ======================================
# GOOGLE SHEET CONFIG
# ======================================
SHEET_ID = "1gh2QMj4vngL-JLf6SPmWvjSuCgl9uItTAMteY3acVNg"
SHEET_GID = "204054788"

SHEET_URL = (
    f"https://docs.google.com/spreadsheets/d/"
    f"{SHEET_ID}/export?format=csv&gid={SHEET_GID}"
)

# ======================================
# LOAD SHEET (CACHED)
# ======================================
@st.cache_data
def load_sheet():
    try:
        return pd.read_csv(SHEET_URL, dtype=str)
    except Exception as e:
        st.error(f"Failed to load sheet: {e}")
        return pd.DataFrame()

# ======================================
# CLEAN ID HELPER
# ======================================
def clean_id(value):
    return str(value).strip().lower() if value else ""
