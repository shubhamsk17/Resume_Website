import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime
import base64
from config import PERSONAL_INFO, EDUCATION, CERTIFICATIONS, SKILLS, PROJECTS, STATS

# Page configuration
st.set_page_config(
    page_title=f"{PERSONAL_INFO['name']} - {PERSONAL_INFO['title']}",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Clear cache to ensure fresh data
if hasattr(st, 'cache_data'):
    st.cache_data.clear()

# Custom CSS
def load_css():
    st.markdown("""
    <style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global Styles */
    .main {
        padding-top: 0rem;
    }
    
    .stApp {
        background: linear-gradient(135deg, #000000 0%, #1a1a1a 50%, #ffffff 100%);
        font-family: 'Inter', sans-serif;
    }
    
    /* Header Styles */
    .header-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        text-align: center;
        border: 2px solid #000000;
    }
    
    
    /* Logo Styles */
    .logo-container {
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 1rem;
    }
    
    .logo-circle {
        width: 80px;
        height: 80px;
        border-radius: 50%;
        background: linear-gradient(135deg, #000000, #333333);
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 1rem;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .logo-text {
        font-size: 2.5rem;
        font-weight: 700;
        color: #ffffff;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    }
    
    .logo-name {
        font-size: 1.8rem;
        font-weight: 600;
        color: #000000;
        letter-spacing: 2px;
    }
    
    .name-title {
        font-size: 3rem;
        font-weight: 700;
        color: #000000;
        margin-bottom: 0.5rem;
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.1);
    }
    
    .subtitle {
        font-size: 1.5rem;
        color: #333333;
        margin-bottom: 1rem;
        font-weight: 400;
    }
    
    .description {
        font-size: 1.1rem;
        color: #666666;
        max-width: 600px;
        margin: 0 auto;
        line-height: 1.6;
    }
    
    /* Section Styles */
    .section-container {
        background: rgba(255, 255, 255, 0.98);
        backdrop-filter: blur(15px);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.2);
        border: 1px solid #000000;
    }
    
    .section-title {
        font-size: 2rem;
        font-weight: 600;
        color: #000000;
        margin-bottom: 1.5rem;
        border-bottom: 3px solid #000000;
        padding-bottom: 0.5rem;
    }
    
    /* Card Styles */
    .card {
        background: white;
        border-radius: 15px;
        padding: 1.5rem;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
        border-left: 4px solid #000000;
        border: 1px solid #e0e0e0;
    }
    
    .card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3);
    }
    
    .card-title {
        font-size: 1.3rem;
        font-weight: 600;
        color: #000000;
        margin-bottom: 0.5rem;
    }
    
    .card-subtitle {
        font-size: 1rem;
        color: #333333;
        margin-bottom: 0.5rem;
        font-weight: 500;
    }
    
    .card-content {
        color: #333333;
        line-height: 1.6;
    }
    
    /* Skill Tags */
    .skill-tag {
        display: inline-block;
        background: linear-gradient(135deg, #000000, #333333);
        color: white;
        padding: 0.5rem 1rem;
        border-radius: 25px;
        margin: 0.25rem;
        font-size: 0.9rem;
        font-weight: 500;
        border: 1px solid #000000;
    }
    
    /* Contact Icons */
    .contact-icon {
        font-size: 1.5rem;
        margin-right: 0.5rem;
        color: #000000;
    }
    
    /* Navigation */
    .nav-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(15px);
        border-radius: 15px;
        padding: 1rem;
        margin: 1rem 0;
        text-align: center;
        border: 1px solid #000000;
    }
    
    .nav-link {
        display: inline-block;
        padding: 0.8rem 1.5rem;
        margin: 0 0.5rem;
        color: #000000;
        text-decoration: none;
        border-radius: 8px;
        transition: all 0.3s ease;
        font-weight: 600;
        border: 2px solid #000000;
        background: rgba(255, 255, 255, 0.9);
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    }
    
    .nav-link:hover {
        background: #000000;
        color: white;
        text-decoration: none;
        border: 2px solid #000000;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
        transform: translateY(-2px);
    }
    
    /* Stats Cards */
    .stats-container {
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        margin: 2rem 0;
    }
    
    .stat-card {
        background: linear-gradient(135deg, #000000, #333333);
        color: white;
        padding: 1.5rem;
        border-radius: 15px;
        text-align: center;
        margin: 0.5rem;
        min-width: 150px;
        border: 2px solid #000000;
        box-shadow: 0 4px 15px rgba(0, 0, 0, 0.3);
    }
    
    .stat-number {
        font-size: 2rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
    }
    
    .stat-label {
        font-size: 0.9rem;
        opacity: 0.9;
    }
    
    /* Responsive Design */
    @media (max-width: 768px) {
        .name-title {
            font-size: 2rem;
        }
        
        .subtitle {
            font-size: 1.2rem;
        }
        
        .stats-container {
            flex-direction: column;
            align-items: center;
        }
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    load_css()
    
    # Navigation
    st.markdown("""
    <div class="nav-container">
        <a href="#about" class="nav-link">About</a>
        <a href="#education" class="nav-link">Education</a>
        <a href="#skills" class="nav-link">Skills</a>
        <a href="#projects" class="nav-link">Projects</a>
        <a href="#contact" class="nav-link">Contact</a>
    </div>
    """, unsafe_allow_html=True)
    
    # Header Section
    name = PERSONAL_INFO['name']
    title = PERSONAL_INFO['title']
    description = PERSONAL_INFO['description']
    initials = name.split()[0][0] + name.split()[-1][0]
    
    st.markdown(f"""
    <div class="header-container">
        <div class="logo-container">
            <div class="logo-circle">
                <div class="logo-text">{initials}</div>
            </div>
            <div class="logo-name">{name}</div>
        </div>
        
        <h1 class="name-title">{name}</h1>
        <h2 class="subtitle">{title}</h2>
        <p class="description">
            {description}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Stats Section
    st.markdown(f"""
    <div class="stats-container">
        <div class="stat-card">
            <div class="stat-number">{STATS['experience']}</div>
            <div class="stat-label">Years Experience</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{STATS['projects']}</div>
            <div class="stat-label">Projects Completed</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{STATS['certifications']}</div>
            <div class="stat-label">Certifications</div>
        </div>
        <div class="stat-card">
            <div class="stat-number">{STATS['satisfaction']}</div>
            <div class="stat-label">Client Satisfaction</div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # About Section
    st.markdown('<div id="about"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">About Me</h2>
        <div class="card">
            <div class="card-content">
                <p>I am a dedicated data engineer with a strong foundation in statistical analysis, and data engineering. 
                My passion lies in extracting meaningful insights from complex datasets and translating them into actionable business strategies.</p>
                
                <p>With expertise in Python, Javascript and SQL, I have successfully delivered numerous 
                data-driven solutions that have improved operational efficiency and decision-making processes across different industries.</p>
                
                <p>I am constantly learning and staying updated with the latest trends in data science, artificial intelligence, and cloud technologies 
                to provide cutting-edge solutions to complex business problems.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Education Section
    st.markdown('<div id="education"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Education & Certifications</h2>
    """, unsafe_allow_html=True)
    
    # Education entries
    for edu in EDUCATION:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{edu['degree']}</div>
            <div class="card-subtitle">{edu['institution']}, {edu['period']}</div>
            <div class="card-content">
                {edu['description']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # Certifications
    cert_list = "".join([f"<li>{cert}</li>" for cert in CERTIFICATIONS])
    st.markdown(f"""
        <div class="card">
            <div class="card-title">Professional Certifications</div>
            <div class="card-content">
                <ul>
                    {cert_list}
                </ul>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Skills Section
    st.markdown('<div id="skills"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Technical Skills</h2>
    """, unsafe_allow_html=True)
    
    # Skills by category
    for category, skills in SKILLS.items():
        skill_tags = "".join([f'<span class="skill-tag">{skill}</span>' for skill in skills])
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{category}</div>
            <div class="card-content">
                {skill_tags}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Projects Section
    st.markdown('<div id="projects"></div>', unsafe_allow_html=True)
    st.markdown("""
    <div class="section-container">
        <h2 class="section-title">Featured Projects</h2>
    """, unsafe_allow_html=True)
    
    # Projects
    for project in PROJECTS:
        st.markdown(f"""
        <div class="card">
            <div class="card-title">{project['title']}</div>
            <div class="card-subtitle">{project['technologies']}</div>
            <div class="card-content">
                {project['description']}
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Contact Section
    st.markdown('<div id="contact"></div>', unsafe_allow_html=True)
    st.markdown(f"""
    <div class="section-container">
        <h2 class="section-title">Get In Touch</h2>
        
        <div class="card">
            <div class="card-content">
                <p style="font-size: 1.1rem; margin-bottom: 1.5rem;">
                    I'm always interested in new opportunities and exciting projects. 
                    Let's connect and discuss how we can work together!
                </p>
                
                <div style="display: flex; flex-wrap: wrap; gap: 1rem; margin: 1rem 0;">
                    <div style="flex: 1; min-width: 200px;">
                        <h4 style="color: #000000; margin-bottom: 0.5rem;">📧 Email</h4>
                        <p>{PERSONAL_INFO['email']}</p>
                    </div>
                    <div style="flex: 1; min-width: 200px;">
                        <h4 style="color: #000000; margin-bottom: 0.5rem;">📱 Phone</h4>
                        <p>{PERSONAL_INFO['phone']}</p>
                    </div>
                    <div style="flex: 1; min-width: 200px;">
                        <h4 style="color: #000000; margin-bottom: 0.5rem;">📍 Location</h4>
                        <p>{PERSONAL_INFO['location']}</p>
                    </div>
                </div>
                
                <div style="margin-top: 2rem;">
                    <h4 style="color: #000000; margin-bottom: 1rem;">Connect with me</h4>
                    <div style="display: flex; gap: 1rem; flex-wrap: wrap;">
                        <a href="{PERSONAL_INFO.get('linkedin', '#')}" target="_blank" 
                           style="color: #000000; text-decoration: none; font-weight: 500; border: 1px solid #000000; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s ease;">
                            🔗 LinkedIn
                        </a>
                        <a href="{PERSONAL_INFO.get('github', '#')}" target="_blank" 
                           style="color: #000000; text-decoration: none; font-weight: 500; border: 1px solid #000000; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s ease;">
                            🐙 GitHub
                        </a>
                        <a href="{PERSONAL_INFO.get('twitter', '#')}" target="_blank" 
                           style="color: #000000; text-decoration: none; font-weight: 500; border: 1px solid #000000; padding: 0.5rem 1rem; border-radius: 5px; transition: all 0.3s ease;">
                            🐦 Twitter
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # Footer
    st.markdown(f"""
    <div style="text-align: center; padding: 2rem; color: white; opacity: 0.8;">
        <p>© 2024 {PERSONAL_INFO['name']}. Built with ❤️ using Streamlit</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()