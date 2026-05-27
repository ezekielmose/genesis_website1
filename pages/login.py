import streamlit as st
import requests

# ======================================
# FIREBASE CONFIG
# ======================================
# REPLACE WITH YOUR FIREBASE WEB API KEY
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
# LOGIN PAGE
# ======================================
def show_login():

    # ======================================
    # PAGE TITLE
    # ======================================
    st.markdown("""
    <div style="
        text-align:center;
        color:#0057b8;
        font-size:42px;
        font-weight:900;
        margin-top:20px;
        margin-bottom:10px;
    ">
        Genesis Digital
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div style="
        text-align:center;
        color:black;
        font-size:18px;
        margin-bottom:40px;
    ">
        Secure Login Portal
    </div>
    """, unsafe_allow_html=True)

    # ======================================
    # CENTERED LOGIN BOX
    # ======================================
    left, center, right = st.columns([1, 2, 1])

    with center:

        # ======================================
        # AUTH MODE
        # ======================================
        auth_mode = st.radio(
            "Choose Action",
            ["Login", "Create Account"],
            horizontal=True
        )

        # ======================================
        # FORM BOX
        # ======================================
        st.markdown("""
        <style>

        .auth-box {
            background: rgba(255,255,255,0.92);
            padding: 35px;
            border-radius: 18px;
            box-shadow: 0 8px 25px rgba(0,0,0,0.08);
            border: 1px solid rgba(0,0,0,0.05);
        }

        </style>
        """, unsafe_allow_html=True)

        st.markdown('<div class="auth-box">', unsafe_allow_html=True)

        # ======================================
        # INPUTS
        # ======================================
        email = st.text_input(
            "Email Address",
            placeholder="Enter your email"
        )

        password = st.text_input(
            "Password",
            placeholder="Enter your password",
            type="password"
        )

        # ======================================
        # CREATE ACCOUNT
        # ======================================
        if auth_mode == "Create Account":

            confirm_password = st.text_input(
                "Confirm Password",
                placeholder="Confirm password",
                type="password"
            )

            if st.button("Create Account"):

                # VALIDATION
                if not email or not password:

                    st.warning(
                        "⚠️ Please fill all fields."
                    )

                elif password != confirm_password:

                    st.error(
                        "❌ Passwords do not match."
                    )

                elif len(password) < 6:

                    st.warning(
                        "⚠️ Password must be at least 6 characters."
                    )

                else:

                    payload = {
                        "email": email,
                        "password": password,
                        "returnSecureToken": True
                    }

                    try:

                        response = requests.post(
                            SIGNUP_URL,
                            json=payload
                        )

                        data = response.json()

                        if response.status_code == 200:

                            st.success(
                                "✅ Account created successfully!"
                            )

                            st.info(
                                "You can now login."
                            )

                        else:

                            error_message = (
                                data.get("error", {})
                                .get("message", "Signup failed")
                            )

                            st.error(
                                f"❌ {error_message}"
                            )

                    except Exception as e:

                        st.error(
                            f"Error: {e}"
                        )

        # ======================================
        # LOGIN
        # ======================================
        else:

            if st.button("Login"):

                if not email or not password:

                    st.warning(
                        "⚠️ Please fill all fields."
                    )

                else:

                    payload = {
                        "email": email,
                        "password": password,
                        "returnSecureToken": True
                    }

                    try:

                        response = requests.post(
                            LOGIN_URL,
                            json=payload
                        )

                        data = response.json()

                        if response.status_code == 200:

                            st.session_state.logged_in = True

                            st.session_state.user_email = email

                            st.success(
                                "✅ Login successful!"
                            )

                            st.rerun()

                        else:

                            error_message = (
                                data.get("error", {})
                                .get("message", "Login failed")
                            )

                            st.error(
                                f"❌ {error_message}"
                            )

                    except Exception as e:

                        st.error(
                            f"Error: {e}"
                        )

        st.markdown("</div>", unsafe_allow_html=True)
