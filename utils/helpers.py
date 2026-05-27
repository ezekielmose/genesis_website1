import urllib.parse

# ======================================
# GENERAL HELPERS
# ======================================

def build_google_search_url(query: str) -> str:
    """
    Returns a Google search URL for the given query.
    """
    return "https://www.google.com/search?q=" + urllib.parse.quote(query)


def safe_get_session_value(key: str, default=""):
    """
    Safely get a value from Streamlit session_state.
    """
    import streamlit as st
    return st.session_state.get(key, default)


def format_file_size(bytes_size: int) -> str:
    """
    Convert bytes to MB string.
    """
    try:
        mb = bytes_size / (1024 * 1024)
        return f"{mb:.2f} MB"
    except:
        return "0 MB"
