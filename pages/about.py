import streamlit as st

# ======================================
# ABOUT PAGE
# ======================================
def show_about():

    # ======================================
    # ABOUT US
    # ======================================
    st.title("About Us")

    st.write(
        """
        At Genesis Digital we specialize in sourcing and curating
        high-quality digital content to help businesses enhance their
        online presence.

        With a focus on video acquisition, metadata documentation,
        and quality assurance, we deliver engaging, scalable,
        and compliant solutions tailored to meet client needs.

        Backed by a skilled team and innovative strategies,
        we are committed to driving digital impact and delivering
        excellence with every project.
        """
    )

    # ======================================
    # THIN BLUE LINE
    # ======================================
    st.markdown("""
    <div style="
        width:100%;
        height:2px;
        background-color:#0057b8;
        margin-top:25px;
        margin-bottom:25px;
    "></div>
    """, unsafe_allow_html=True)

    # ======================================
    # OUR TEAM TITLE
    # ======================================
    st.markdown("""
    <div style="
        color:#0057b8;
        font-size:34px;
        font-weight:900;
        margin-bottom:25px;
    ">
        Our Team
    </div>
    """, unsafe_allow_html=True)

    # ======================================
    # TEAM MEMBERS
    # ======================================
    team1, team2, team3 = st.columns(3)

    # --------------------------------------
    # TEAM MEMBER 1
    # --------------------------------------
    with team1:

        st.image("assets/aravind.png", width=180)

        st.markdown(
            """
            <div style="text-align:center;">
                <div style="
                    color:#0057b8;
                    font-size:18px;
                    font-weight:600;
                ">
                    Aravind Konnte
                    - Chief Executive Officer
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------
    # TEAM MEMBER 2
    # --------------------------------------
    with team2:

        st.image("assets/havala.png", width=180)

        st.markdown(
            """
            <div style="text-align:center;">
                <div style="
                    color:#0057b8;
                    font-size:18px;
                    font-weight:600;
                ">
                    Dr. Havala Allan
                    - Chief Operations Officer
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # --------------------------------------
    # TEAM MEMBER 3
    # --------------------------------------
    with team3:

        st.image("assets/ezekiel.png", width=180)

        st.markdown(
            """
            <div style="text-align:center;">
                <div style="
                    color:#0057b8;
                    font-size:18px;
                    font-weight:600;
                ">
                    Ezekiel Mose
                    - Head of Analytics
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    # ======================================
    # CONTACT US
    # ======================================
    st.title("Contact Us")

    st.write("📧 aravind@genesisdigital.in")

    st.write("📞 +919731016770")
