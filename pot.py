import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Page config
st.set_page_config(page_title="Zwi Portfolio", page_icon="🚀", layout="wide")

# --- Helper function for Lottie ---
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# --- Header with animation ---
lottie_hero = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_tfb3estd.json")
st_lottie(lottie_hero, speed=1, height=250, key="hero")

st.markdown("<h1 style='text-align:center; color:#00FFAA;'>👾 Zwi | Developer from the Future</h1>", unsafe_allow_html=True)
st.markdown("<hr>", unsafe_allow_html=True)

# --- Profile Section ---
col1, col2 = st.columns([1,2])
with col1:
    uploaded_profile = st.file_uploader("Upload Profile Image", type=["png","jpg","jpeg"])
    if uploaded_profile:
        st.image(uploaded_profile, width=250)
with col2:
    st.subheader("About Me")
    st.write("""
    I am Zwi, a forward-thinking developer blending web, AI, and Python expertise.
    I craft interactive apps, futuristic tools, and smart solutions that make life simpler.
    """)

# --- Skills Section ---
st.subheader("💻 Skills & Proficiency")
skill_cols = st.columns(4)
skills = {
    "HTML/CSS": 95,
    "JavaScript": 90,
    "Python": 95,
    "PHP": 85,
    "React.js": 80,
    "MySQL": 85,
    "Streamlit": 90,
    "AI/ML": 75
}
for i, (skill, level) in enumerate(skills.items()):
    with skill_cols[i % 4]:
        st.write(f"**{skill}**")
        st.progress(level)

# --- Projects Section ---
st.subheader("🚀 Projects")
projects = [
    {
        "title": "Technosol Inventory System",
        "description": "Device and inventory tracking system for companies.",
        "image": None,  # can upload or use URL
        "link": "#"
    },
    {
        "title": "AutoSphere Car Marketplace",
        "description": "Online platform to buy and sell cars.",
        "image": None,
        "link": "#"
    },
    {
        "title": "AI Chatbot Portfolio",
        "description": "Customizable AI chatbot powered by OpenAI API.",
        "image": None,
        "link": "#"
    }
]

for project in projects:
    st.markdown("---")
    col1, col2 = st.columns([1,2])
    with col1:
        uploaded_project_img = st.file_uploader(f"Upload image for {project['title']}", type=["png","jpg","jpeg"], key=project['title'])
        if uploaded_project_img:
            st.image(uploaded_project_img, use_column_width=True)
    with col2:
        st.markdown(f"### {project['title']}")
        st.write(project['description'])
        st.markdown(f"[View Project]({project['link']})")

# --- Lottie Animation for Footer ---
lottie_footer = load_lottieurl("https://assets6.lottiefiles.com/packages/lf20_jcikwtux.json")
st_lottie(lottie_footer, speed=1, height=150, key="footer")

# --- Contact Section ---
st.markdown("<hr>", unsafe_allow_html=True)
st.subheader("📬 Contact Me")
st.write("Email: futuristic.dev@example.com")
st.write("LinkedIn: [Connect](https://linkedin.com)")
st.write("GitHub: [Explore](https://github.com)")

# Optional: Dark theme styling
st.markdown("""
<style>
body {
    background-color: #0A0A0A;
    color: #00FFAA;
}
</style>
""", unsafe_allow_html=True)
