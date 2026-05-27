import streamlit as st
import pandas as pd
import tempfile
import requests
import urllib.parse

# ======================================
# IMPORT HELPERS
# ======================================
from utils.sheets import load_sheet, clean_id

# ======================================
# AI ANALYZER PAGE
# ======================================
def show_ai_analyzer():

    # ======================================
    # CUSTOM BUTTON CSS
    # ======================================
    st.markdown("""
    <style>

    /* BUTTON STYLE */
    div.stButton > button {
        background-color: #0057b8 !important;
        color: white !important;
        font-size: 16px !important;
        font-weight: bold !important;
        border-radius: 12px !important;
        border: none !important;
        width: 120% !important;
        height: 50px !important;
        margin-bottom: 20px !important;
        transition: 0.3s !important;
    }

    /* BUTTON TEXT */
    div.stButton > button p {
        color: white !important;
    }

    /* HOVER EFFECT */
    div.stButton > button:hover {
        background-color: red !important;
        color: white !important;
    }

    div.stButton > button:hover p {
        color: white !important;
    }

    </style>
    """, unsafe_allow_html=True)

    st.write("Choose an AI Tool Below")

    # ======================================
    # LAYOUT
    # ======================================
    left_col, right_col = st.columns([1, 3])

    # ======================================
    # LEFT SIDE BUTTONS
    # ======================================
    with left_col:

        if st.button("A Profile Finder"):
            st.session_state.active_tool = "profile"

        if st.button("Analyze a Video"):
            st.session_state.active_tool = "video"

    # ======================================
    # RIGHT SIDE CONTENT
    # ======================================
    with right_col:

        # ======================================
        # PROFILE FINDER
        # ======================================
        if st.session_state.get("active_tool") == "profile":

            st.subheader("Hotel Profiles Analyzer")

            st.write(
                "Find the best matching Instagram profile for a hotel."
            )

            # ======================================
            # AUTO FILL SECTION
            # ======================================
            st.subheader("Auto Fill from Item ID")

            item_id = st.text_input(
                "Item ID",
                placeholder="e.g. 846e9ee4-e5e4-434d-b6ac-ef67c301b3e8"
            )

            if st.button("Auto Fill"):

                if item_id:

                    try:
                        df = load_sheet()

                        id_column = df.iloc[:, 1].apply(clean_id)

                        input_id = clean_id(item_id)

                        match = df[id_column == input_id]

                        if not match.empty:

                            st.session_state.hotel_name = str(
                                match.iloc[0, 2]
                            ).strip()

                            st.session_state.city = str(
                                match.iloc[0, 3]
                            ).strip()

                            st.session_state.country = str(
                                match.iloc[0, 4]
                            ).strip()

                            st.success("✅ Auto-filled successfully!")

                        else:
                            st.error("❌ Item ID not found in sheet.")

                    except Exception as e:
                        st.error(f"Error loading sheet: {e}")

                else:
                    st.warning("⚠️ Please enter an Item ID.")

            # ======================================
            # INPUT FIELDS
            # ======================================
            hotel_name = st.text_input(
                "Hotel Name",
                value=st.session_state.get("hotel_name", "")
            )

            city = st.text_input(
                "City",
                value=st.session_state.get("city", "")
            )

            country = st.text_input(
                "Country",
                value=st.session_state.get("country", "")
            )

            # ======================================
            # INSTAGRAM SEARCH BUTTON
            # ======================================
            if st.button("Instagram Page"):

                if hotel_name:

                    query = (
                        f"{hotel_name} {city} "
                        f"{country} Instagram"
                    ).strip()

                    instagram_link = None

                    try:

                        SERPAPI_KEY = (
                            "YOUR_SERPAPI_KEY"
                        )

                        params = {
                            "engine": "google",
                            "q": query,
                            "api_key": SERPAPI_KEY
                        }

                        response = requests.get(
                            "https://serpapi.com/search.json",
                            params=params
                        )

                        data = response.json()

                        for result in data.get(
                            "organic_results",
                            []
                        ):

                            link = result.get("link", "")

                            if "instagram.com" in link:
                                instagram_link = link
                                break

                    except Exception as e:
                        st.warning(f"SerpAPI failed: {e}")

                    # ======================================
                    # OUTPUT RESULTS
                    # ======================================
                    if instagram_link:

                        st.success(
                            "Instagram Profile Found 🎯"
                        )

                        st.markdown(
                            f"""
                            <a href="{instagram_link}"
                               target="_blank"
                               style="
                                   color:#0057b8;
                                   font-size:18px;
                                   font-weight:bold;
                                   text-decoration:none;
                               ">
                               Open Instagram Profile
                            </a>
                            """,
                            unsafe_allow_html=True
                        )

                    else:

                        google_url = (
                            "https://www.google.com/search?q="
                            + urllib.parse.quote(query)
                        )

                        st.warning(
                            "No Instagram profile found."
                        )

                        st.markdown(
                            f"""
                            <a href="{google_url}"
                               target="_blank"
                               style="
                                   color:#0057b8;
                                   font-size:18px;
                                   font-weight:bold;
                                   text-decoration:none;
                               ">
                               Search on Google
                            </a>
                            """,
                            unsafe_allow_html=True
                        )

                else:
                    st.warning(
                        "⚠️ Please fill in hotel details first."
                    )

        # ======================================
        # VIDEO ANALYZER
        # ======================================
        elif st.session_state.get("active_tool") == "video":

            st.subheader("🎬 Analyze a Video")

            st.write(
                "Upload a video from your device for analysis."
            )

            # ======================================
            # VIDEO CSS
            # ======================================
            st.markdown("""
            <style>

            [data-testid="stFileUploaderDropzone"] {
                background-color: white !important;
                border: 2px dashed black !important;
                border-radius: 12px !important;
                color: black !important;
            }

            [data-testid="stFileUploaderDropzone"] * {
                color: black !important;
            }

            [data-testid="stFileUploaderDropzone"] button {
                background-color: #0057b8 !important;
                color: white !important;
                border: none !important;
                border-radius: 10px !important;
                font-weight: bold !important;
                padding: 10px 18px !important;
            }

            [data-testid="stFileUploaderDropzone"] button:hover {
                background-color: #004494 !important;
                color: white !important;
            }

            [data-testid="stVideo"] {
                max-width: 320px;
            }

            [data-testid="stVideo"] video {
                max-width: 320px !important;
                max-height: 500px !important;
                border-radius: 12px !important;
            }

            </style>
            """, unsafe_allow_html=True)

            # ======================================
            # VIDEO UPLOADER
            # ======================================
            uploaded_video = st.file_uploader(
                "Upload Video",
                type=["mp4", "mov"],
                help="Upload a video file for analysis"
            )

            # ======================================
            # PROCESS VIDEO
            # ======================================
            if uploaded_video is not None:

                st.success(
                    "✅ Video uploaded successfully!"
                )

                temp_video = tempfile.NamedTemporaryFile(
                    delete=False,
                    suffix=".mp4"
                )

                temp_video.write(uploaded_video.read())

                video_path = temp_video.name

                temp_video.close()

                # ======================================
                # PLAY VIDEO
                # ======================================
                st.video(video_path)

                # ======================================
                # VIDEO INFO
                # ======================================
                file_size = (
                    uploaded_video.size / (1024 * 1024)
                )

                st.markdown("### 📊 Video Info")

                st.write(
                    f"**File Name:** "
                    f"{uploaded_video.name}"
                )

                st.write(
                    f"**Size:** "
                    f"{file_size:.2f} MB"
                )

                # ======================================
                # ANALYZE BUTTON
                # ======================================
                if st.button("Analyze the Video"):

                    st.write("UNDER DEVELOPMENT")
