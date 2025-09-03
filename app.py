# app.py - Landing Page Estilo Jonty Angarita (CORREGIDO - Video + Imagen Fallback)

from flask import Flask, render_template_string, jsonify
import urllib.parse
import os

app = Flask(__name__)

# ========================================
# CONFIGURACIÓN PERSONALIZABLE DEL ESTUDIO
# ========================================
STUDIO_CONFIG = {
    "studio_name": "Certified Tattoo Studio",
    "artist_name": "Jonty  Angarita",
    "title": "TATTOO ARTIST",
    "main_message": "¿Deseas tatuarte y estás en Medellín?",
    "submessage": "AGENDA UNA ASESORÍA TOTALMENTE GRATIS",
    
    "final_message": "¡Convierte tu cuerpo en la imagen que quieres reflejar!",
    "hero_video": "https://res.cloudinary.com/dweqlnl1w/video/upload/v1756840388/copy_87684891-94AE-4CF6-9E2C-4A9BCD183822_tlqd6g.mov",
    
    # ⭐ NUEVA IMAGEN FALLBACK ESTÁTICA ⭐
    "hero_fallback_image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756840540/image00007_d6qbn7.jpg",  # Tu imagen de fallback
    
    "instagram_handle": "@jontyangarita",
    "instagram_url": "https://www.instagram.com/jontyangarita?igsh=MXdqOXlpeG9pZTRmZA%3D%3D&utm_source=qr",
    "whatsapp_number": "+573504556466",
    "location": "Medellín, Antioquia",
    "about_text": "Soy Jonty Angarita, Artista Tatuador radicado en la ciudad de Medellín-Colombia, cuento con +10 años de experiencia como tatuador y me especializo en los estilos de Realismo, Color, Sombras, y Ornamentales. En estos largos años he tenido la oportunidad de trabajar con clientes nacionales e internacionales, logrando así un portafolio amplio y variado. Mi objetivo es brindar a cada cliente una experiencia única y personalizada, asegurándome de que cada tatuaje sea una obra de arte que refleje su individualidad y estilo personal. Si estás buscando un tatuaje que combine técnica, creatividad y pasión, no dudes en contactarme para agendar tu cita o asesoría gratuita.",
    "google_maps_embed": "Tattoo Shop Medellin / Jonty Angarita",
    "google_ads_id": "G-LLX2T252FL",
}

# ========================================
# ESTILOS DE TATUAJE
# ========================================
tattoo_styles = [
    {
        "name": "SOMBRAS",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756164403/IMG_0942_pkr2pb.jpg",
        "description": "Tortuga ancestral sombras"
    },
    {
        "name": "COLOR",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162609/IMG_4025_gkl0su.jpg", 
        "description": "Zorro full color"
    },
    {
        "name": "ORNAMENTAL",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756170191/IMG_4070_daqhap.jpg",
        "description": "Proyecto manga Ornamental"
    },
    {
        "name": "TRADICIONAL",
        "image": "https://res.cloudinary.com/dweqlnl1w/image/upload/v1756187447/IMG_9280_dzbmwd.jpg",
        "description": "Color Tradicional"
    }
]

def generate_whatsapp_link(message="Hola! Me interesa agendar una asesoría de tatuaje"):
    """Genera enlace de WhatsApp con mensaje preconfigurado"""
    phone = STUDIO_CONFIG["whatsapp_number"].replace("+", "").replace(" ", "")
    encoded_message = urllib.parse.quote(message)
    return f"https://wa.me/{phone}?text={encoded_message}"

@app.route('/')
def index():
    """Página principal - Landing page estilo Jonty Angarita con video corregido"""
    return render_template_string(HTML_TEMPLATE, 
                                config=STUDIO_CONFIG,
                                styles=tattoo_styles,
                                whatsapp_link=generate_whatsapp_link())

# ========================================
# TEMPLATE HTML CORREGIDO
# ========================================
HTML_TEMPLATE = '''
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ config.artist_name }} - {{ config.title }}</title>
    
    <!-- SEO Meta Tags -->
    <meta name="description" content="Artista tatuador especializado en Realismo, Color y Ornamentales en {{ config.location }}. Agenda tu asesoría completamente Gratis.">
    <meta name="keywords" content="tatuajes, {{ config.location.lower() }}, realismo, color, ornamentales, artista tatuador">
    
    <!-- Open Graph Meta Tags -->
    <meta property="og:title" content="Jonty Angarita - Tattoo Artist Medellín | Realismo y Color">
    <meta property="og:description" content="Especialista en realismo, color, sombras y ornamentales. +10 años de experiencia. Agenda tu asesoría completamente GRATIS en Medellín.">
    <meta property="og:type" content="website">
    <meta property="og:url" content="https://jontyangaritatattooshop.onrender.com">
    <meta property="og:image" content="{{ config.hero_fallback_image }}">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:site_name" content="Top Artists Medellin">
    <meta property="og:locale" content="es_CO">

    <!-- Twitter Cards -->
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:title" content="Jonty Angarita - Tattoo Artist Medellín | Realismo y Color">
    <meta name="twitter:description" content="Especialista en realismo, color, sombras y ornamentales. +10 años de experiencia. Agenda tu asesoría completamente GRATIS.">
    <meta name="twitter:image" content="{{ config.hero_fallback_image }}">
    
    <!-- Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:wght@300;400;500;700;900&family=Oswald:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <!-- Font Awesome -->
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <style>
    /* MISMO CSS QUE ANTES - NO CAMBIAR */
    :root {
        --orange-primary: #FF4B35;
        --orange-hover: #e55a2b;
        --orange-light: #ff8660;
        --bg-dark: #1a1a1a;
        --bg-darker: #0a0a0a;
        --bg-light: #161616;
        --text-white: #333333;
        --text-dark: #ffffff;
        --text-gray: #cccccc;
        --border-gray: #333333;
    }
    
    * {
        margin: 0;
        padding: 0;
        box-sizing: border-box;
    }
    
    html {
        scroll-behavior: smooth;
    }
    
    body {
        font-family: 'Roboto', sans-serif;
        line-height: 1.6;
        overflow-x: hidden;
    }
    
    /* HEADER NAVIGATION */
    .header {
        background: var(--bg-light);
        padding: 1rem 0;
        box-shadow: 0 2px 10px rgba(255,255,255,0.1);
        position: fixed;
        width: 100%;
        top: 0;
        z-index: 1000;
    }
    
    .nav-container {
        max-width: 1200px;
        margin: 0 auto;
        padding: 0 2rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .logo {
        font-family: 'Oswald', sans-serif;
        font-size: 1.8rem;
        font-weight: 700;
        color: var(--text-dark);
        text-decoration: none;
        letter-spacing: 2px;
    }
    
    /* MENÚ HAMBURGUESA */
    .hamburger-menu {
        display: flex;
        flex-direction: column;
        cursor: pointer;
        padding: 10px;
        background: var(--orange-primary);
        border-radius: 8px;
        transition: all 0.3s ease;
        position: relative;
        z-index: 1001;
    }
    
    .hamburger-menu:hover {
        background: var(--orange-hover);
        transform: scale(1.05);
    }
    
    .hamburger-line {
        width: 25px;
        height: 3px;
        background: white;
        margin: 3px 0;
        transition: all 0.3s ease;
        border-radius: 2px;
    }
    
    .hamburger-menu.active .hamburger-line:nth-child(1) {
        transform: rotate(45deg) translate(6px, 6px);
    }
    
    .hamburger-menu.active .hamburger-line:nth-child(2) {
        opacity: 0;
    }
    
    .hamburger-menu.active .hamburger-line:nth-child(3) {
        transform: rotate(-45deg) translate(6px, -6px);
    }
    
    .mobile-menu {
        position: fixed;
        top: 0;
        right: -100%;
        width: 100%;
        height: 100vh;
        background: var(--bg-light);
        transition: right 0.3s ease;
        z-index: 1000;
        display: flex;
        flex-direction: column;
        padding: 100px 2rem 2rem;
    }
    
    .mobile-menu.active {
        right: 0;
    }
    
    .mobile-menu-item {
        display: block;
        padding: 1.5rem 0;
        color: var(--orange-primary);
        text-decoration: none;
        font-size: 1.8rem;
        font-weight: 600;
        font-family: 'Oswald', sans-serif;
        text-transform: uppercase;
        letter-spacing: 2px;
        border-bottom: 2px solid var(--border-gray);
        transition: all 0.3s ease;
    }
    
    .mobile-menu-item:hover {
        color: var(--orange-hover);
        padding-left: 1rem;
    }
    
    .mobile-menu-item:last-child {
        border-bottom: none;
    }
    
    .mobile-menu-instagram {
        display: flex;
        align-items: center;
        gap: 1rem;
        margin-top: 2rem;
        padding: 1rem 0;
    }
    
    .mobile-menu-instagram i {
        font-size: 2rem;
        color: var(--text-dark);
    }
    
    .mobile-menu-instagram:hover i {
        color: var(--orange-primary);
    }
    
    .menu-overlay {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        height: 100vh;
        background: rgba(0, 0, 0, 0.5);
        z-index: 999;
        opacity: 0;
        visibility: hidden;
        transition: all 0.3s ease;
    }
    
    .menu-overlay.active {
        opacity: 1;
        visibility: visible;
    }
    
    /* ⭐ HERO SECTION CORREGIDO CON VIDEO MEJORADO ⭐ */
    .hero {
        min-height: 100vh;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
        color: white;
        position: relative;
        padding-top: 100px;
        overflow: hidden;
        /* ⭐ IMAGEN DE FONDO COMO FALLBACK ⭐ */
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                    url('{{ config.hero_fallback_image }}') center/cover no-repeat;
    }
    
    .hero-video {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: cover;
        z-index: 1;
        /* ⭐ OCULTO POR DEFECTO, SE MUESTRA CUANDO EL VIDEO CARGA ⭐ */
        opacity: 0;
        transition: opacity 0.5s ease;
    }
    
    .hero-video.loaded {
        opacity: 1;
    }
    
    .hero::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        background: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6));
        z-index: 2;
    }
    
    .hero-content {
        max-width: 800px;
        padding: 2rem;
        position: relative;
        z-index: 3;
    }
    
    .hero-subtitle {
        font-family: 'Oswald', sans-serif;
        font-size: 1.5rem;
        font-weight: 400;
        letter-spacing: 3px;
        margin-bottom: 1rem;
        color: var(--orange-primary);
    }
    
    .hero-title {
        font-family: 'Oswald', sans-serif;
        font-size: clamp(3rem, 8vw, 6rem);
        font-weight: 700;
        margin-bottom: 2rem;
        letter-spacing: 12px;
        line-height: 1.1;
    }
    
    .hero-message {
        font-size: 2.3rem;
        margin-bottom: 1rem;
        font-weight: 400;
    }
    
    .hero-submessage {
        font-size: 1.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
        color: var(--orange-primary);
    }
    
    .hero-description {
        font-size: 1.1rem;
        margin-bottom: 1rem;
        opacity: 0.9;
    }
    
    .hero-final {
        font-size: 1.2rem;
        font-weight: 600;
        margin-bottom: 2rem;
        color: var(--orange-light);
    }
    
    .cta-button {
        background: var(--orange-primary);
        color: white;
        padding: 1.2rem 3rem;
        border: none;
        border-radius: 5px;
        font-size: 1.2rem;
        font-weight: 700;
        text-transform: uppercase;
        text-decoration: none;
        display: inline-block;
        transition: all 0.3s ease;
        letter-spacing: 1px;
        box-shadow: 0 4px 15px rgba(255, 107, 53, 0.3);
    }
    
    .cta-button:hover {
        background: var(--orange-hover);
        transform: translateY(-3px);
        box-shadow: 0 6px 20px rgba(255, 107, 53, 0.4);
    }
    
    /* REST OF CSS REMAINS THE SAME - ESTILOS, ABOUT, MAP, REVIEWS, FOOTER */
    .styles-section {
        padding: 5rem 2rem;
        background: var(--bg-light);
    }
    
    .section-container {
        max-width: 1200px;
        margin: 0 auto;
        text-align: center;
    }
    
    .section-title {
        font-family: 'Oswald', sans-serif;
        font-size: 2.5rem;
        color: var(--text-dark);
        margin-bottom: 3rem;
        position: relative;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 50%;
        transform: translateX(-50%);
        width: 80px;
        height: 3px;
        background: var(--orange-primary);
    }
    
    .styles-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 2rem;
        margin-bottom: 3rem;
    }
    
    .style-card {
        background: var(--bg-dark);
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0 5px 20px rgba(255,255,255,0.1);
        transition: transform 0.3s ease;
    }
    
    .style-card:hover {
        transform: translateY(-10px);
    }
    
    .style-image {
        width: 100%;
        height: 400px;
        object-fit: cover;
        aspect-ratio: 3/4;
    }
    
    .style-content {
        padding: 2rem;
    }
    
    .style-name {
        font-family: 'Oswald', sans-serif;
        font-size: 1.8rem;
        color: var(--orange-primary);
        margin-bottom: 1rem;
        font-weight: 600;
    }
    
    .style-button {
        background: var(--orange-primary);
        color: white;
        border: none;
        padding: 0.8rem 2rem;
        border-radius: 25px;
        font-weight: 600;
        text-transform: uppercase;
        cursor: pointer;
        transition: background 0.3s ease;
        font-size: 0.9rem;
    }
    
    .style-button:hover {
        background: var(--orange-hover);
    }
    
    .about-section {
        background: var(--orange-primary);
        padding: 4rem 2rem;
        color: white;
    }
    
    .about-container {
        max-width: 1200px;
        margin: 0 auto;
        display: grid;
        grid-template-columns: 2fr 1fr;
        gap: 3rem;
        align-items: center;
    }
    
    .about-content h2 {
        font-family: 'Oswald', sans-serif;
        font-size: 2.5rem;
        margin-bottom: 2rem;
        color: white;
    }
    
    .about-text {
        font-size: 1rem;
        line-height: 1.8;
        margin-bottom: 2rem;
        text-align: justify;
    }
    
    .about-button {
        background: var(--bg-darker);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 5px;
        font-weight: 600;
        text-transform: uppercase;
        cursor: pointer;
        transition: background 0.3s ease;
    }
    
    .about-button:hover {
        background: #333;
    }
    
    .about-image {
        text-align: center;
    }
    
    .about-photo {
        width: 300px;
        height: 400px;
        object-fit: cover;
        border-radius: 15px;
        border: 5px solid white;
    }
    
    .map-section {
        padding: 0;
        height: 400px;
    }
    
    .map-container {
        width: 100%;
        height: 100%;
    }
    
    .map-container iframe {
        width: 100%;
        height: 100%;
        border: none;
    }
    
    .reviews-section {
        background: var(--bg-darker);
        color: var(--text-dark);
        padding: 4rem 2rem;
        text-align: center;
    }
    
    .reviews-title {
        font-family: 'Oswald', sans-serif;
        font-size: 2.5rem;
        color: var(--orange-primary);
        margin-bottom: 1rem;
    }
    
    .reviews-subtitle {
        font-size: 1.2rem;
        margin-bottom: 1rem;
        font-weight: 600;
        color: var(--text-dark);
    }
    
    .reviews-text {
        margin-bottom: 2rem;
        color: var(--text-gray);
    }
    
    .stars {
        font-size: 2rem;
        color: #ffd700;
        margin-bottom: 2rem;
    }
    
    .reviews-button {
        background: var(--orange-primary);
        color: white;
        padding: 1rem 2rem;
        border: none;
        border-radius: 25px;
        font-weight: 600;
        text-transform: uppercase;
        cursor: pointer;
        transition: background 0.3s ease;
        text-decoration: none;
        display: inline-block;
    }
    
    .reviews-button:hover {
        background: var(--orange-hover);
    }
    
    .footer {
        background: var(--bg-darker);
        color: var(--text-dark);
        padding: 2rem;
        text-align: center;
    }
    
    .footer-content {
        max-width: 1200px;
        margin: 0 auto;
        display: flex;
        justify-content: space-between;
        align-items: center;
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .footer-links {
        display: flex;
        gap: 2rem;
        flex-wrap: wrap;
    }
    
    .footer-links a {
        color: var(--orange-primary);
        text-decoration: none;
        transition: color 0.3s ease;
    }
    
    .footer-links a:hover {
        color: var(--orange-light);
    }
    
    .footer-social a {
        color: var(--text-dark);
        font-size: 1.5rem;
        margin: 0 0.5rem;
        transition: color 0.3s ease;
    }
    
    .footer-social a:hover {
        color: var(--orange-primary);
    }
    
    .copyright {
        margin-top: 1rem;
        color: var(--text-gray);
        font-size: 0.9rem;
    }
    
    .whatsapp-float {
        position: fixed;
        bottom: 2rem;
        right: 2rem;
        background: #25d366;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        color: white;
        font-size: 1.8rem;
        text-decoration: none;
        box-shadow: 0 4px 20px rgba(37, 211, 102, 0.3);
        z-index: 1000;
        transition: all 0.3s ease;
    }
    
    .whatsapp-float:hover {
        transform: scale(1.1);
        box-shadow: 0 8px 30px rgba(37, 211, 102, 0.4);
    }
    
    /* RESPONSIVE DESIGN */
    @media (max-width: 768px) {
        .nav-container {
            padding: 0 1rem;
        }
        
        .logo {
            font-size: 1.4rem;
        }
        
        .mobile-menu-item {
            font-size: 1.5rem;
        }
        
        .styles-grid {
            grid-template-columns: 1fr;
            gap: 1.5rem;
        }
        
        .about-container {
            grid-template-columns: 1fr;
            text-align: center;
        }
        
        .about-photo {
            width: 250px;
            height: 320px;
        }
        
        .footer-content {
            flex-direction: column;
            text-align: center;
        }
        
        .footer-links {
            justify-content: center;
        }
    }
    
    @media (max-width: 480px) {
        .hero-content {
            padding: 1rem;
        }
        
        .section-container {
            padding: 0 1rem;
        }
        
        .about-container {
            padding: 0 1rem;
        }
        
        .about-photo {
            width: 200px;
            height: 280px;
        }
        
        .whatsapp-float {
            bottom: 1rem;
            right: 1rem;
            width: 50px;
            height: 50px;
            font-size: 1.5rem;
        }
        
        .mobile-menu {
            padding: 80px 1rem 1rem;
        }
        
        .mobile-menu-item {
            font-size: 1.3rem;
            padding: 1rem 0;
        }
    }
    
    .fade-in {
        opacity: 0;
        transform: translateY(30px);
        transition: all 0.8s ease;
    }
    
    .fade-in.active {
        opacity: 1;
        transform: translateY(0);
    }
    </style>
    
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={{ config.google_ads_id }}"></script>
    <script>
        window.dataLayer = window.dataLayer || [];
        function gtag(){dataLayer.push(arguments);}
        gtag('js', new Date());
        gtag('config', '{{ config.google_ads_id }}');
    </script>
    
    <!-- Google tag (gtag.js) event - delayed navigation helper -->
    <script>
      // Helper function to delay opening a URL until a gtag event is sent.
      // Call it in response to an action that should navigate to a URL.
      function gtagSendEvent(url) {
        var callback = function () {
          if (typeof url === 'string') {
            window.location = url;
          }
        };
        gtag('event', 'whatsapp_float', {
          'event_callback': callback,
          'event_timeout': 2000,
          // <event_parameters>
        });
        return false;
      }
    </script>
</head>
<body>
    <!-- HEADER -->
    <header class="header">
        <nav class="nav-container">
            <a href="#" class="logo">{{ config.studio_name }}</a>
            <div class="hamburger-menu" id="hamburgerMenu">
                <div class="hamburger-line"></div>
                <div class="hamburger-line"></div>
                <div class="hamburger-line"></div>
            </div>
        </nav>
    </header>

    <div class="menu-overlay" id="menuOverlay"></div>

    <nav class="mobile-menu" id="mobileMenu">
        <a href="#inicio" class="mobile-menu-item">Inicio</a>
        <a href="#estilos" class="mobile-menu-item">Mi Portafolio</a>
        <a href="#sobre-mi" class="mobile-menu-item">Sobre el Artista</a>
        <a href="#contacto" class="mobile-menu-item">Contacto</a>
        <a href="{{ config.instagram_url }}" target="_blank" class="mobile-menu-item mobile-menu-instagram">
            <i class="fab fa-instagram"></i>
            Instagram
        </a>
    </nav>

    <!-- ⭐ HERO SECTION CORREGIDO ⭐ -->
    <section class="hero" id="inicio">
        <!-- ⭐ VIDEO CON MÚLTIPLES FORMATOS Y MEJOR CONFIGURACIÓN ⭐ -->
        <video class="hero-video" id="heroVideo" muted loop playsinline preload="metadata">
            <source src="{{ config.hero_video }}" type="video/mp4">
            <source src="{{ config.hero_video }}" type="video/mov">
            <source src="{{ config.hero_video }}" type="video/webm">
            <!-- Más tipos de video para compatibilidad -->
        </video>
        
        <div class="hero-content">
            <div class="hero-subtitle">{{ config.title }}</div>
            <h1 class="hero-title">{{ config.artist_name }}</h1>
            <p class="hero-message">{{ config.main_message }}</p>
            <p class="hero-submessage">{{ config.submessage }}</p>
            <p class="hero-final">{{ config.final_message }}</p>
            <a href="{{ whatsapp_link }}" class="cta-button" target="_blank" onclick="return gtagSendEvent('{{ whatsapp_link }}')">
                AGENDA TU CITA
            </a>
        </div>
    </section>

    <!-- REST OF CONTENT REMAINS THE SAME -->
    <section class="styles-section" id="estilos">
        <div class="section-container">
            <h2 class="section-title">Mi Portafolio</h2>
            <div class="styles-grid">
                {% for style in styles %}
                <div class="style-card fade-in">
                    <img src="{{ style.image }}" alt="{{ style.name }}" class="style-image">
                    <div class="style-content">
                        <h3 class="style-name">{{ style.name }}</h3>
                        <button class="style-button" onclick="openInstagram()">
                            VER MAS
                        </button>
                    </div>
                </div>
                {% endfor %}
            </div>
        </div>
    </section>

    <section class="about-section" id="sobre-el-artista">
        <div class="about-container">
            <div class="about-content">
                <h2>SOBRE EL ARTISTA</h2>
                <p class="about-text">{{ config.about_text }}</p>
                <button class="about-button" onclick="openInstagram()">
                    AGENDA AHORA
                </button>
            </div>
            <div class="about-image">
                <img src="https://res.cloudinary.com/dweqlnl1w/image/upload/v1756162692/image00007_hs638b.jpg" alt="{{ config.artist_name }}" class="about-photo">
            </div>
        </div>
    </section>

    <section class="map-section" id="contacto">
        <div class="map-container">
            <iframe 
                src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d991.5145179063718!2d-75.58418833048293!3d6.256080432726896!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e4429d888310d0b%3A0x21d15470e7091326!2sTattoo%20Shop%20Medellin%20%2F%20Jonty%20Angarita!5e0!3m2!1sen!2sco!4v1756185107388!5m2!1sen!2sco"
                width="100%" 
                height="100%" 
                style="border:0;" 
                allowfullscreen="" 
                loading="lazy" 
                referrerpolicy="no-referrer-when-downgrade">
            </iframe>
        </div>
    </section>

    <section class="reviews-section">
        <div class="section-container">
            <h2 class="reviews-title">REVIEWS Y OPINIONES</h2>
            <p class="reviews-subtitle">CONOCE LA OPINIÓN DE MIS CLIENTES</p>
            <p class="reviews-text">Puedes ver más opiniones reales y conocer sus experiencias (Pregunta las dudas que tengas!) </p>
            <div class="stars">
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
                <i class="fas fa-star"></i>
            </div>
            <a href="https://maps.app.goo.gl/5tutFQQHQfYuxmRc7" target="_blank" class="reviews-button">
                HAZ CLIC AQUÍ PARA VER TODAS
            </a>
        </div>
    </section>

    <footer class="footer">
        <div class="footer-content">
            <div class="footer-links">
                <a href="#inicio">Inicio</a>
                <a href="#estilos">Mi Portafolio</a>
                <a href="#sobre-el-artista">Sobre el Artista</a>
            </div>
            <div class="footer-social">
                <a href="{{ config.instagram_url }}" target="_blank">
                    <i class="fab fa-instagram"></i>
                </a>
            </div>
            <div class="copyright">
                <p>Todos los derechos reservados</p>
            </div>
        </div>
    </footer>

    <a href="{{ whatsapp_link }}" class="whatsapp-float" target="_blank" aria-label="Contactar por WhatsApp" onclick="return gtagSendEvent('{{ whatsapp_link }}')">
        <i class="fab fa-whatsapp"></i>
    </a>

    <!-- ⭐ JAVASCRIPT CORREGIDO CON VIDEO MEJORADO ⭐ -->
    <script>
    // ========================================
    // MENÚ HAMBURGUESA FUNCTIONALITY
    // ========================================
    const hamburgerMenu = document.getElementById('hamburgerMenu');
    const mobileMenu = document.getElementById('mobileMenu');
    const menuOverlay = document.getElementById('menuOverlay');
    const mobileMenuItems = document.querySelectorAll('.mobile-menu-item');

    hamburgerMenu.addEventListener('click', toggleMenu);
    menuOverlay.addEventListener('click', closeMenu);

    mobileMenuItems.forEach(item => {
        item.addEventListener('click', (e) => {
            if (!item.hasAttribute('target')) {
                closeMenu();
            }
        });
    });

    function toggleMenu() {
        hamburgerMenu.classList.toggle('active');
        mobileMenu.classList.toggle('active');
        menuOverlay.classList.toggle('active');
        
        if (mobileMenu.classList.contains('active')) {
            document.body.style.overflow = 'hidden';
        } else {
            document.body.style.overflow = '';
        }
    }

    function closeMenu() {
        hamburgerMenu.classList.remove('active');
        mobileMenu.classList.remove('active');
        menuOverlay.classList.remove('active');
        document.body.style.overflow = '';
    }

    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && mobileMenu.classList.contains('active')) {
            closeMenu();
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth > 768 && mobileMenu.classList.contains('active')) {
            closeMenu();
        }
    });

    // ========================================
    // ⭐ VIDEO MANAGEMENT CORREGIDO ⭐
    // ========================================
    const heroVideo = document.getElementById('heroVideo');
    
    if (heroVideo) {
        console.log('🎬 Iniciando carga del video...');
        
        // ⭐ MEJORADO: Múltiples eventos para asegurar que el video cargue ⭐
        heroVideo.addEventListener('loadedmetadata', () => {
            console.log('📹 Video metadata cargado');
            tryPlayVideo();
        });
        
        heroVideo.addEventListener('canplaythrough', () => {
            console.log('✅ Video listo para reproducir');
            tryPlayVideo();
        });
        
        heroVideo.addEventListener('loadeddata', () => {
            console.log('📊 Video data cargado');
            tryPlayVideo();
        });
        
        // ⭐ FUNCIÓN MEJORADA PARA REPRODUCIR VIDEO ⭐
        function tryPlayVideo() {
            heroVideo.play()
                .then(() => {
                    console.log('🎬 Video reproduciéndose correctamente');
                    heroVideo.classList.add('loaded');
                    
                    // ⭐ TRACKING: Video exitoso ⭐
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'video_play_success', {
                            'event_category': 'media',
                            'event_label': 'hero_video'
                        });
                    }
                })
                .catch(error => {
                    console.warn('⚠️ Video no puede reproducirse, usando imagen de fallback:', error);
                    
                    // ⭐ EL VIDEO SE MANTIENE OCULTO, LA IMAGEN DE FONDO SE MANTIENE VISIBLE ⭐
                    // No necesitamos cambiar nada porque ya está configurado en CSS
                    
                    // ⭐ TRACKING: Video falló ⭐
                    if (typeof gtag !== 'undefined') {
                        gtag('event', 'video_play_failed', {
                            'event_category': 'media',
                            'event_label': 'hero_video',
                            'custom_parameters': {
                                'error': error.name || 'unknown'
                            }
                        });
                    }
                });
        }
        
        // ⭐ OPTIMIZACIÓN: Pausar video cuando no está visible ⭐
        const videoObserver = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    if (heroVideo.paused) {
                        tryPlayVideo();
                    }
                } else {
                    heroVideo.pause();
                }
            });
        }, { threshold: 0.5 });
        
        videoObserver.observe(heroVideo);
        
        // ⭐ INTENTAR CARGAR INMEDIATAMENTE ⭐
        heroVideo.load();
    }
    
    // ========================================
    // SMOOTH SCROLLING Y OTRAS FUNCIONALIDADES
    // ========================================
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };
    
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
            }
        });
    }, observerOptions);
    
    document.querySelectorAll('.fade-in').forEach(el => {
        observer.observe(el);
    });
    
    function openInstagram() {
        window.open('{{ config.instagram_url }}', '_blank');
        
        if (typeof gtag !== 'undefined') {
            gtag('event', 'instagram_click', {
                'event_category': 'engagement',
                'event_label': 'style_button'
            });
        }
    }
    
    // ⭐ TRACKING MEJORADO ⭐
    document.querySelectorAll('a[href*="wa.me"]').forEach(btn => {
        btn.addEventListener('click', () => {
            if (typeof gtag !== 'undefined') {
                gtag('event', 'whatsapp_click', {
                    'event_category': 'conversion',
                    'event_label': 'contact_button'
                });
            }
        });
    });
    
    console.log('🎨 {{ config.artist_name }} - Landing page CORREGIDA cargada');
    console.log('📱 Instagram: {{ config.instagram_handle }}');
    console.log('💬 WhatsApp: {{ config.whatsapp_number }}');
    console.log('🎬 Video URL: {{ config.hero_video }}');
    console.log('🖼️ Imagen fallback: {{ config.hero_fallback_image }}');
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 5001)))
