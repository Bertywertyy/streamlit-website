import streamlit as st
from pathlib import Path
from PIL import Image

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital Introduction | Wilbert Marvin Tiono"
PAGE_ICON = ":wave:"

# --- CLASSES ---
class SocialMedia:
    def __init__(self, platform, link):
        self.platform = platform
        self.link = link

    def display(self):
        return f"[{self.platform}]({self.link})"


class Competition:
    def __init__(self, title, link):
        self.title = title
        self.link = link

    def display(self):
        return f"[{self.title}]({self.link})"


class Profile:
    def __init__(self, name, description, email, phone, profile_pic):
        self.name = name
        self.description = description
        self.email = email
        self.phone = phone
        self.profile_pic = profile_pic
        self.social_media = []
        self.competitions = []

    def add_social_media(self, platform, link):
        self.social_media.append(SocialMedia(platform, link))

    def add_competition(self, title, link):
        self.competitions.append(SocialMedia(title, link))

    def display_profile(self):
        col1, col2 = st.columns(2, gap="small")
        with col1:
            st.image(self.profile_pic, width=230)

        with col2:
            st.title(self.name)
            st.write(self.description)
            st.write("☎️", self.phone)
            st.write("📫", self.email)

    def display_social_media(self):
        cols = st.columns(len(self.social_media))
        for index, sm in enumerate(self.social_media):
            cols[index].write(sm.display())

    def display_competitions(self):
        st.subheader("Accomplishments")
        st.write("---")
        for comp in self.competitions:
            st.write(comp.display())


# --- SET PAGE CONFIG ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "main.css"
profile_pic = current_dir / "profile-pic.png"

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
profile_pic = Image.open(profile_pic)

# --- PROFILE INSTANCE ---
profile = Profile(
    name="Wilbert Marvin Tiono 🇮🇩",
    description="Athletic high school student with an enthusiasm for coding ✨",
    email="marvinwilbert4@gmail.com",
    phone="(+62) 815 8690 9537",
    profile_pic=profile_pic,
)

# --- ADD SOCIAL MEDIA ---
social_links = {
    "YouTube": "https://www.youtube.com/@GWilbert",
    "Instagram": "https://www.instagram.com/wilbert.tiono/",
    "GitHub": "https://github.com/Bertywertyy",
    "Codecademy": "https://www.codecademy.com/profiles/g808Wilbert3931277717",
}

for platform, link in social_links.items():
    profile.add_social_media(platform, link)

# --- ADD COMPETITIONS ---
competition_links = {
    "🏆 2023 Indonesia GreenMech R4M Contest Second Place 🥈": "https://ibb.co/rtcqyFs",
    "🏆 2023 World GreenMech Contest Third Place 🥉": "https://ibb.co/TKhbtyY",
    "🏆 1130310 梯次全國高級中等學校閱讀心得寫作比賽－甲等": " ",
    "🏆 Sololearn Python Developer Completer": "https://api2.sololearn.com/v2/certificates/CC-QEP7COTQ/image/jpg",
}

for title, link in competition_links.items():
    profile.add_competition(title, link)

# --- DISPLAY PROFILE ---
profile.display_profile()

# --- SOCIAL LINKS ---
st.write('\n')
profile.display_social_media()

# --- LANGUAGES ---
st.write('\n')
st.subheader("Languages")
st.write(
    """
- ✔️ English 
- ✔️ Chinese
- ✔️ Indonesian
- ✔️ Taiwanese
- ✔️ Japanese
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Skills")
st.write(
    """
- 👩‍💻 Programming: Python, C++ 
- 🎵 Music Instruments: Guitar, Piano, Drum
- 💪 Sports: Basketball, Badminton, Soccer, Gym
- 🎤 Professional High Schooler MC
"""
)

# --- CODING HISTORY ---
# --- PROFILE SECTIONS WITH IMAGES AND LINKS ---

# 🎸 Side Quest | Mastering the Guitar
st.markdown("### 🎸 Side Quest | Mastering the Guitar")
st.write("**2023 March - July**")
st.write("I've always had a desire to learn instruments beyond the piano, and the guitar quickly caught my attention. I began by mastering basic chords, then progressed to barre chords and solos. With the support of my teachers and friends, I had the opportunity to perform my favorite songs at the talent show, creating unforgettable memories along the way!")
guitar_img = Image.open('guitar_performance.png')  # Replace with the correct image path
st.image(guitar_img, caption="Guitar Performance")
st.markdown("[View the PowerPoint](https://docs.google.com/presentation/d/1KmGS3T-ktMpbJn_gYj8aI7V_aNDvhbKuVnqqFCrnVB4/edit?usp=sharing)")

# 🚀 C++ & Kotlin | Arduino & Android Studio Code
st.markdown("### 🚀 C++ & Kotlin | Arduino & Android Studio Code")
st.write("**2023 October - December**")
st.write("I had the opportunity to participate in a summer camp organized by the Asia Eastern University of Science and Technology. During the camp, I delved into the fundamentals of building Android applications using Android Studio. Additionally, I explored the intriguing world of machine learning, focusing specifically on Arduino. Engaging with machine learning was particularly enjoyable and added an exciting dimension to my learning experience.")
android_img = Image.open('android_studio_ui.png')  # Replace with the correct image path
st.image(android_img, caption="Android Studio UI")
st.markdown("[View CODES & VIDEOS](https://drive.google.com/drive/folders/1oBFK5lrnFQ8N7uUqWmrUaKHGkha6q5zG?usp=sharing)")

# 🤖 Robotics Competition | National & International
st.markdown("### 🤖 Robotics Competition | National & International")
st.write("**2023 January - June**")
st.write("As part of our school robotics team, I had the chance to compete nationally, where we placed third. This allowed us to represent Indonesia in a global competition, where we secured another third-place finish. The experience was eye-opening, pushing me to improve both my programming skills and teamwork abilities, while also igniting my passion for technology even further.")
robotics_img = Image.open('robotics_competition.png')  # Replace with the correct image path
st.image(robotics_img, caption="Robotics Competition")
st.markdown("[View Competition Highlights](https://drive.google.com/drive/folders/1jK83hG_Competition_Folder?usp=sharing)")

# 🎓 Graduation Project | AI-powered Learning Platform
st.markdown("### 🎓 Graduation Project | AI-powered Learning Platform")
st.write("**2024 January - April**")
st.write("For my high school graduation project, I developed an AI-powered learning platform designed to help students practice math and science topics through interactive problem-solving. The platform leverages machine learning to tailor the questions based on the student's progress and areas of improvement, offering a personalized learning experience. This project not only honed my coding skills but also deepened my understanding of AI technology.")
ai_project_img = Image.open('ai_learning_platform.png')  # Replace with the correct image path
st.image(ai_project_img, caption="AI-powered Learning Platform")
st.markdown("[View Project Demo & Code](https://drive.google.com/drive/folders/1abcAI_Project_Folder?usp=sharing)")

# --- DISPLAY COMPETITIONS ---
profile.display_competitions()
