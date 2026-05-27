# ======================================
# TEAM SECTION COMPONENT (HTML)
# ======================================

team_section_html = """
<!DOCTYPE html>
<html>

<head>

<style>

/* TEAM SECTION WRAPPER */
.team-section {
    width: 100%;
    padding: 40px 20px;
    text-align: center;
}

/* TITLE */
.team-title {
    color: #0057b8;
    font-size: 34px;
    font-weight: 900;
    margin-bottom: 30px;
}

/* GRID */
.team-grid {
    display: flex;
    justify-content: center;
    gap: 30px;
    flex-wrap: wrap;
}

/* CARD */
.team-card {
    background: rgba(255,255,255,0.9);
    border-radius: 14px;
    padding: 18px;
    min-width: 220px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}

.team-card:hover {
    transform: translateY(-8px);
}

/* IMAGE */
.team-card img {
    width: 170px;
    height: 170px;
    object-fit: cover;
    border-radius: 12px;
    margin-bottom: 12px;
}

/* NAME */
.team-name {
    font-size: 18px;
    font-weight: 800;
    color: #0057b8;
    margin-bottom: 5px;
}

/* ROLE */
.team-role {
    font-size: 14px;
    color: #444;
}

/* MOBILE */
@media only screen and (max-width: 768px) {
    .team-card {
        width: 90%;
    }
}

</style>

</head>

<body>

<div class="team-section">

    <div class="team-title">
        Our Team
    </div>

    <div class="team-grid">

        <!-- MEMBER 1 -->
        <div class="team-card">
            <img src="assets/aravind.png">
            <div class="team-name">Aravind Konnte</div>
            <div class="team-role">Chief Executive Officer</div>
        </div>

        <!-- MEMBER 2 -->
        <div class="team-card">
            <img src="assets/havala.png">
            <div class="team-name">Dr. Havala Allan</div>
            <div class="team-role">Chief Operations Officer</div>
        </div>

        <!-- MEMBER 3 -->
        <div class="team-card">
            <img src="assets/ezekiel.png">
            <div class="team-name">Ezekiel Mose</div>
            <div class="team-role">Head of Analytics</div>
        </div>

    </div>

</div>

</body>
</html>
"""
