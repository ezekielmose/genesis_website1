# ======================================
# PARTNERS SLIDER COMPONENT (HTML)
# ======================================

partners_slider_html = """
<!DOCTYPE html>
<html>

<head>

<style>

/* MAIN CONTAINER */
.partners-slider {
    width: 100%;
    overflow: hidden;
    position: relative;
    padding-top: 10px;
    padding-bottom: 20px;
}

/* MOVING TRACK */
.partners-track {
    display: flex;
    align-items: center;
    gap: 60px;
    width: max-content;
    animation: scrollPartners 35s linear infinite;
}

/* LOGO CARD */
.partner-logo {
    width: 180px;
    height: 90px;
    background: white;
    border-radius: 14px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 15px;
    box-shadow: 0 4px 14px rgba(0,0,0,0.08);
    flex-shrink: 0;
}

/* LOGO IMAGE */
.partner-logo img {
    max-width: 100%;
    max-height: 100%;
    object-fit: contain;
}

/* ANIMATION */
@keyframes scrollPartners {
    0% { transform: translateX(0); }
    100% { transform: translateX(-50%); }
}

/* MOBILE */
@media only screen and (max-width: 768px) {
    .partner-logo {
        width: 130px;
        height: 70px;
    }

    .partners-track {
        gap: 30px;
    }
}

</style>

</head>

<body>

<div class="partners-slider">

    <div class="partners-track">

        <!-- PARTNER 1 -->
        <div class="partner-logo">
            <img src="assets/unravel.JPG">
        </div>

        <!-- PARTNER 2 -->
        <div class="partner-logo">
            <img src="assets/booking.JPG">
        </div>

        <!-- PARTNER 3 -->
        <div class="partner-logo">
            <img src="assets/yafreeka.JPG">
        </div>

        <!-- PARTNER 4 -->
        <div class="partner-logo">
            <img src="assets/airtel.JPG">
        </div>

        <!-- DUPLICATES FOR LOOP -->
        <div class="partner-logo">
            <img src="assets/unravel.JPG">
        </div>

        <div class="partner-logo">
            <img src="assets/booking.JPG">
        </div>

        <div class="partner-logo">
            <img src="assets/yafreeka.JPG">
        </div>

        <div class="partner-logo">
            <img src="assets/airtel.JPG">
        </div>

    </div>

</div>

</body>
</html>
"""
