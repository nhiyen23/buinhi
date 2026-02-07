import streamlit as st

# ===== PAGE CONFIG =====
st.set_page_config(
    page_title="Yen Nhi - Portfolio",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===== CUSTOM CSS =====
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Lato:wght@300;400;700&display=swap');
    
    [data-testid="stSidebar"] {display: none !important;}
    #MainMenu, footer, .stDeployButton, header {visibility: hidden;}
    
    html {scroll-behavior: smooth;}
  
    [data-testid="stAppViewContainer"] {
    background-color: #FDF8F5 !important;
    }
 
    [data-testid="stHeader"] {
    background-color: rgba(0,0,0,0) !important;
    }
    
    .block-container {
        padding: 2rem 2% !important;
        max-width: 90% !important;
        margin-left: 0px !important;
        margin-right: 0px !important;
    }
    
    h1, h2, h3 {
        font-family: 'Playfair Display';
        color: #2B1E4B;
        margin-bottom: 40px !important;
    }
    
    p, li {
        font-family: 'Montserrat';
        color: #666666;
        font-size: 4rem;
        line-height: 1.8;
    }
    
    .nav-bar {
        background: #FDF8F5;
        padding: 1.5rem 0;
        text-align: center;
        border-bottom: 1px solid rgba(43, 30, 75, 0.1);
        position: sticky;
        top: 0;
        z-index: 1000;
        margin: 0 -8%;
        padding-left: 8%;
        padding-right: 8%;
    }
    
    .nav-bar a {
        font-family: 'Montserrat';
        font-weight: 500;
        color: #2B1E4B;
        text-decoration: none;
        margin: 0 1.5rem;
        font-size: 1.2rem;
        transition: color 0.3s;
    }
    
    .nav-bar a:hover {color: #FFB6C1;}
    
    .hero {
        text-align: center;
        padding: 8rem 2rem 6rem;
        margin: 0 -8%;
        background: #FDF8F5;
    }
    
    .hero-subtitle {
        font-family: 'Montserrat';
        font-size: 2rem;
        letter-spacing: 6px;
        color: #FFB6C1;
        margin-bottom: 1.5rem;
    }
    
    .hero-title {
        font-family: 'Playfair Display';
        font-size: 10rem;
        font-weight: 900;
        color: #2B1E4B;
        margin: 1.5rem 0;
        line-height: 1;
    }

    .hero-con {
        font-family: 'Playfair Display';
        font-size: 4rem;
        font-weight: 800;
        color: #2B1E4B;
        margin: 1.5rem 0;
        line-height: 1;
    }

    .hero-con2 {
        font-family: 'Playfair Display';
        font-size: 4rem;
        font-weight: 800;
        color: #F5E1A8;
        margin: 1.5rem 0;
        line-height: 1;
    }

    .hero-con3 {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        font-weight: 600;
        color: #E8B9B9;
        font-style: italic;
        margin: 1.5rem 0;
        line-height: 1;
    }

    .hero-con4 {
        font-family: 'Montserrat';
        font-size: 1.2rem;
        font-weight: 500;
        color: #666666;
        margin: 1.5rem 0;
        line-height: 1;
    }

    .hero-role {
        font-family: 'Playfair Display';
        font-size: 3rem;
        color: #666666;
        font-style: italic;
        margin: 2rem 0 1rem;
    }
    
    .hero-location {
        font-family: 'Montserrat';
        font-size: 1.5rem;
        color: #666666;
        letter-spacing: 4px;
    }
    
    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: 4rem;
        font-weight: 700;
        color: #2B1E4B;
        margin: 3rem 0 2rem 0;
        position: relative;
        display: inline-block;
    }
    
    .section-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 100px;
        height: 3px;
        background: #FFB6C1;
    }
    
    .content-box {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    }
    
    .vision-box {
        background: #2B1E4B;
        padding: 4rem;
        border-radius: 25px;
        margin: 3rem 0;
    }
    
    .vision-title {
        font-size: 3.5rem;
        color: #FFE5B4;
        margin-bottom: 2rem;
        position: relative;
        display: inline-block;
    }
    
    .vision-title::after {
        content: '';
        position: absolute;
        bottom: -10px;
        left: 0;
        width: 80px;
        height: 3px;
        background: #FFB6C1;
    }
    
    .vision-text {
        color: white !important;
        font-size: 4rem;
        line-height: 2;
    }
    
    .exp-card {
        background: white;
        padding: 3rem;
        border-radius: 20px;
        margin: 2rem 0;
        border-left: 5px solid #FFB6C1;
        box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    }
    
    .stImage {border-radius: 15px;}
    
    @media (max-width: 768px) {
        .block-container {padding: 1rem 4% !important;}
        .hero-title {font-size: 4rem;}
        .section-title {font-size: 2.5rem;}
        .nav-bar, .hero {margin: 0 -4%;}
    }
</style>
""", unsafe_allow_html=True)

# ===== NAVIGATION =====
st.markdown("""
<div class='nav-bar'>
    <a href='#home'>Home</a>
    <a href='#about'>About</a>
    <a href='#vision'>Vision</a>
    <a href='#education'>Education</a>
    <a href='#skills'>Skills</a>
    <a href='#experience'>Experience</a>
    <a href='#projects'>Projects</a>
</div>
""", unsafe_allow_html=True)

# ===== HOME =====
st.markdown("""
<div id='home' class='hero'>
    <div class='hero-subtitle'>PORTFOLIO</div>
    <div class='hero-title'>YEN NHI</div>
    <div class='hero-role'>Graphic Designer Intern</div>
    <div class='hero-location'>HA NOI</div>
</div>
""", unsafe_allow_html=True)

# ===== ABOUT =====
st.markdown("<div id='about'>", unsafe_allow_html=True)
st.markdown("<div class='hero-con'>About Me</div>", unsafe_allow_html=True)

col1, col2 = st.columns([1.2, 1])

with col1:
    st.write("Hello, I'm Yen Nhi, a passionate Graphic Design Intern candidate with a strong interest in visual communication and creative storytelling. I have hands-on experience in designing posters, banners, and digital content for student organizations and educational projects.")
    st.write("With a background in Marketing and Communication activities, I understand not only how to design visually appealing products but also how to deliver messages effectively to target audiences. I enjoy transforming ideas into meaningful visuals and continuously improving my design skills through practice and real projects.")
    st.write("I am currently seeking an internship opportunity where I can contribute my creativity, learn from professionals, and grow into a well-rounded graphic designer.")
   
with col2:
    # Image path for Streamlit Cloud - place image in /images/ folder
    st.image("images/anh_nhi.jpg", use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== VISION =====
st.markdown("<div id='vision'>", unsafe_allow_html=True)

st.markdown("""
<div class='vision-box'>
    <div class='hero-con2'>Vision</div>
    <p class='vision-text'>
        My vision is to become a professional graphic designer who creates impactful visual experiences that connect brands with people.
    </p>
    <p class='vision-text'>
        I aim to develop strong design thinking, master industry-standard tools, and continuously explore new trends in digital design. In the long term, I hope to work in creative teams where collaboration, innovation, and storytelling play key roles in building meaningful products and campaigns.
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== EDUCATION =====
st.markdown("<div id='education'>", unsafe_allow_html=True)
st.markdown("<div class='hero-con'>Education</div>", unsafe_allow_html=True)

st.markdown("""
<div class='content-box'>
    <div class='hero-con3'>Second-year student in Economics</div>
    <div class='hero-con4'>Foreign Trade University (FTU)</div>
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='hero-con3'>Relevant Coursework</div>", unsafe_allow_html=True)
st.write("• Marketing Fundamentals")
st.write("• Digital Communication")
st.write("• Consumer Behavior")
st.write("• Branding Basics")

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("<div class='hero-con3'>Additional Learning</div>", unsafe_allow_html=True)
st.write("• Self-study Graphic Design via online courses and practice projects")
st.write("• Experience in club media teams and event communication")

st.markdown("</div>", unsafe_allow_html=True)

# ===== SKILLS =====
st.markdown("<div id='skills'>", unsafe_allow_html=True)
st.markdown("<div class='hero-con'>Personal Skills</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='hero-con3'>Hard Skills</div>", unsafe_allow_html=True)
    st.write("• Graphic Design: Canva, Adobe Illustrator, Photoshop")
    st.write("• Layout Design for posters, banners, social media posts")
    st.write("• Basic UI/Visual thinking for web content")
    st.write("• Branding fundamentals")
    st.write("• Content visualization")
    st.write("• Basic HTML/CSS")

with col2:
    st.markdown("<div class='hero-con3'>Soft Skills</div>", unsafe_allow_html=True)
    st.write("• Creativity and visual storytelling")
    st.write("• Strong sense of responsibility")
    st.write("• Time management and deadline awareness")
    st.write("• Teamwork and communication")
    st.write("• Willingness to learn and adapt")
    st.write("• Attention to detail")

st.markdown("<br>", unsafe_allow_html=True)

# Skills Images
cols = st.columns(3)
skill_images = [
    "images/slide4.png",
    "images/skill_2.png",
    "images/skill_3.png"
]
for col, img in zip(cols, skill_images):
    with col:
        st.image(img, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== EXPERIENCE =====
st.markdown("<div id='experience'>", unsafe_allow_html=True)
st.markdown("<div class='hero-con'>Experience</div>", unsafe_allow_html=True)

st.markdown("""
<div class='exp-card'>
    <div class='hero-con3'>IPC Organizations</div>
    <div class='hero-con4'>Media & Marketing Member</div>
    <p style='color: #999999; font-size: 1rem; font-style: italic; margin-bottom: 0px;'>[2024 – 2025]</p>
</div>
""", unsafe_allow_html=True)

st.write("• Designed posters, banners, and social media visuals for events and campaigns")
st.write("• Collaborated with marketing teams to develop creative concepts")
st.write("• Supported branding activities for workshops and seminars")
st.write("• Assisted in content planning and visual direction")
st.write("• Delivered designs under tight deadlines while maintaining quality")

st.markdown("<br>", unsafe_allow_html=True)

# IPC Images
cols = st.columns(3)
ipc_images = [
    "images/ipc_1.jpg",
    "images/ipc_2.jpg",
    "images/ipc_3.jpg"
]
for col, img in zip(cols, ipc_images):
    with col:
        st.image(img, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# ===== PROJECTS =====
st.markdown("<div id='projects'>", unsafe_allow_html=True)
st.markdown("<div class='hero-con'>Projects</div>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

# Project 1: IP Day
with col1:
    st.markdown("<div class='hero-con3'>Event Promotion Design – IP Day</div>", unsafe_allow_html=True)
    st.image("images/ipday.jpg", use_container_width=True)
    st.write("Designed poster and digital banners for Intellectual Property Day. Created visual identity aligned with event theme and produced social media posts for promotion.")
    st.markdown("<p style='background: #FFF5F7; padding: 1rem; border-radius: 10px; border-left: 4px solid #FFB6C1;'><strong>Outcome:</strong> Increased event visibility and engagement</p>", unsafe_allow_html=True)

# Project 2: Glowbies
with col2:
    st.markdown("<div class='hero-con3'>Community Project – Glowbies</div>", unsafe_allow_html=True)
    st.image("images/glowbies.jpg", use_container_width=True)
    st.write("Designed branding materials for children-focused community project. Created posters and fundraising visuals while supporting storytelling through warm color palettes and friendly layouts.")

st.markdown("</div>", unsafe_allow_html=True)

# ===== FOOTER =====
st.markdown("""
<div style='text-align: center; padding: 3rem 2rem; margin-top: 4rem; border-top: 1px solid rgba(43, 30, 75, 0.1);'>
    <p style='font-family: Lato, sans-serif; color: #666666; margin: 0;'>
        © 2026 Yen Nhi - Graphic Designer Portfolio
    </p>
</div>
""", unsafe_allow_html=True)
