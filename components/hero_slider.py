# ======================================
# HERO SLIDER COMPONENT (HTML)
# ======================================

hero_slider_html = """
<!DOCTYPE html>
<html>

<head>

<style>

/* MAIN SLIDER */
.hero-slider {
    width: 100%;
    height: 420px;
    overflow: hidden;
    position: relative;
    border-radius: 18px;
    box-shadow: 0 8px 24px rgba(0,0,0,0.12);
}

/* TRACK */
.hero-track {
    display: flex;
    width: 300%;
    height: 100%;
    animation: slideHero 45s infinite;
}

/* EACH SLIDE */
.hero-slide {
    width: 100%;
    height: 420px;
    position: relative;
    overflow: hidden;
    flex-shrink: 0;
}

/* IMAGE */
.hero-slide img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    animation: zoomImage 15s ease-in-out infinite alternate;
}

/* OVERLAY */
.hero-overlay {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0,0,0,0.45);
    display: flex;
    flex-direction: column;
    justify-content: center;
    padding-left: 70px;
    padding-right: 70px;
}

/* TITLE */
.hero-heading {
    color: white;
    font-size: 44px;
    font-weight: 900;
    margin-bottom: 18px;
}

/* TEXT */
.hero-text {
    color: white;
    font-size: 20px;
    max-width: 700px;
    line-height: 1.8;
}

/* ANIMATION */
@keyframes slideHero {
    0% { transform: translateX(0%); }
    30% { transform: translateX(0%); }
    33% { transform: translateX(-100%); }
    63% { transform: translateX(-100%); }
    66% { transform: translateX(-200%); }
    96% { transform: translateX(-200%); }
    100% { transform: translateX(0%); }
}

@keyframes zoomImage {
    0% { transform: scale(1); }
    100% { transform: scale(1.12); }
}

/* MOBILE */
@media only screen and (max-width: 768px) {
    .hero-slider { height: 280px; }
    .hero-slide { height: 280px; }
    .hero-overlay { padding-left: 25px; padding-right: 25px; }
    .hero-heading { font-size: 28px; }
    .hero-text { font-size: 15px; }
}

</style>

</head>

<body>

<div class="hero-slider">

    <div class="hero-track">

        <!-- SLIDE 1 -->
        <div class="hero-slide">
            <img src="https://images.unsplash.com/photo-1522202176988-66273c2fd55f?q=80&w=1600&auto=format&fit=crop">
            <div class="hero-overlay">
                <div class="hero-heading">Who We Are</div>
                <div class="hero-text">
                    Genesis Digital is a next-generation creative and AI-powered company focused on digital transformation and analytics solutions.
                </div>
            </div>
        </div>

        <!-- SLIDE 2 -->
        <div class="hero-slide">
            <img src="https://images.unsplash.com/photo-1516321318423-f06f85e504b3?q=80&w=1600&auto=format&fit=crop">
            <div class="hero-overlay">
                <div class="hero-heading">What We Do</div>
                <div class="hero-text">
                    We provide AI solutions, media sourcing, hospitality intelligence, and digital infrastructure.
                </div>
            </div>
        </div>

        <!-- SLIDE 3 -->
        <div class="hero-slide">
            <img src="https://images.unsplash.com/photo-1552664730-d307ca884978?q=80&w=1600&auto=format&fit=crop">
            <div class="hero-overlay">
                <div class="hero-heading">What Makes Us Different</div>
                <div class="hero-text">
                    We combine creativity, automation, operational excellence, and scalable execution.
                </div>
            </div>
        </div>

    </div>

</div>

</body>
</html>
"""
