import streamlit as st
import requests

# ======================================
# FIREBASE CONFIG
# ======================================
# Replace with your Firebase Web API Key
FIREBASE_API_KEY = "YOUR_FIREBASE_WEB_API_KEY"

# ======================================
# FIREBASE ENDPOINTS
# ======================================
SIGNUP_URL = (
    "https://identitytoolkit.googleapis.com/v1/"
    f"accounts:signUp?key={FIREBASE_API_KEY}"
)

LOGIN_URL = (
    "https://identitytoolkit.googleapis.com/v1/"
    f"accounts:signInWithPassword?key={FIREBASE_API_KEY}"
)

# ======================================
# AUTH STATE INIT
# ======================================
def init_auth():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_email" not in st.session_state:
        st.session_state.user_email = None

# ======================================
# SIGN UP FUNCTION
# ======================================
def signup(email: str, password: str):

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(SIGNUP_URL, json=payload)
    data = response.json()

    if response.status_code == 200:
        return True, data
    else:
        error_message = data.get("error", {}).get("message", "Signup failed")
        return False, error_message

# ======================================
# LOGIN FUNCTION
# ======================================
def login(email: str, password: str):

    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }

    response = requests.post(LOGIN_URL, json=payload)
    data = response.json()

    if response.status_code == 200:
        return True, data
    else:
        error_message = data.get("error", {}).get("message", "Login failed")
        return False, error_message

# ======================================
# LOGOUT FUNCTION
# ======================================
def logout():
    st.session_state.logged_in = False
    st.session_state.user_email = None
    st.rerun()
