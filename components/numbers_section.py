# ======================================
# NUMBERS SECTION COMPONENT (HTML)
# ======================================

numbers_section_html = """
<!DOCTYPE html>
<html>

<head>

<style>

/* SECTION */
.numbers-section {
    width: 100%;
    padding-top: 30px;
    padding-bottom: 40px;
    margin-top: 50px;
    background: transparent;
}

/* TITLE */
.numbers-title {
    text-align: center;
    color: #0057b8;
    font-size: 32px;
    font-weight: 800;
    margin-bottom: 35px;
    font-family: Arial, sans-serif;
    letter-spacing: 1px;
}

/* ROW */
.numbers-row {
    display: flex;
    justify-content: center;
    gap: 45px;
    flex-wrap: wrap;
}

/* CARD */
.number-card {
    width: 230px;
    height: 290px;
    border-radius: 24px;
    position: relative;
    overflow: hidden;
    background: linear-gradient(145deg, #050505 0%, #101010 45%, #1a1a1a 100%);
    border: 1px solid rgba(255,255,255,0.08);
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.45s ease;
    box-shadow: 0 10px 35px rgba(0,0,0,0.45), 0 0 20px rgba(0,87,184,0.08);
    cursor: pointer;
}

/* TOP GLOW */
.number-card::before {
    content: "";
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 4px;
    background: linear-gradient(90deg, #0057b8, #00c6ff, #0057b8);
    box-shadow: 0 0 18px rgba(0,198,255,0.8);
}

/* HOVER */
.number-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 18px 45px rgba(0,0,0,0.6), 0 0 30px rgba(0,87,184,0.18);
}

/* CONTENT */
.number-content {
    position: relative;
    z-index: 5;
    text-align: center;
    color: white;
}

/* VALUE */
.number-value {
    font-size: 62px;
    font-weight: 800;
    line-height: 1;
    margin-bottom: 14px;
    font-family: Arial Black, sans-serif;
    color: white;
    text-shadow: 0 0 12px rgba(0,198,255,0.35), 0 0 30px rgba(0,87,184,0.22);
}

/* LABEL */
.number-label {
    font-size: 22px;
    line-height: 1.5;
    font-family: Arial, sans-serif;
}

/* MOBILE */
@media only screen and (max-width: 768px) {
    .numbers-title { font-size: 24px; }
    .number-card { width: 220px; height: 330px; }
    .number-value { font-size: 62px; }
    .number-label { font-size: 18px; }
}

</style>

</head>

<body>

<div class="numbers-section">

    <div class="numbers-title">
        THE NUMBERS DON'T LIE
    </div>

    <div class="numbers-row">

        <!-- CARD 1 -->
        <div class="number-card">
            <div class="number-content">
                <div class="number-value" id="videosShared">0</div>
                <div class="number-label">Videos<br>Shared</div>
            </div>
        </div>

        <!-- CARD 2 -->
        <div class="number-card">
            <div class="number-content">
                <div class="number-value" id="videosApproved">0</div>
                <div class="number-label">Videos<br>Approved</div>
            </div>
        </div>

        <!-- CARD 3 -->
        <div class="number-card">
            <div class="number-content">
                <div class="number-value">80%</div>
                <div class="number-label">Approval<br>Rate</div>
            </div>
        </div>

    </div>
</div>

<script>
function animateValue(id, start, end, duration, suffix="") {

    let obj = document.getElementById(id);
    let current = start;
    let increment = 0.1;
    let stepTime = duration / ((end - start) / increment);

    let timer = setInterval(function() {

        current += increment;
        current = Math.round(current * 10) / 10;

        obj.innerHTML = current.toFixed(1) + suffix;

        if (current >= end) {
            obj.innerHTML = end + suffix;
            clearInterval(timer);
        }

    }, stepTime);
}

animateValue("videosShared", 0, 28, 12000, "k+");
animateValue("videosApproved", 0, 19.7, 14000, "k+");
</script>

</body>
</html>
"""
