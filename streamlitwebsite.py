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
    "🏆 2023 Indonesia GreenMech R4M Contest Second Place 🥈": "https://im.ge/i/WhatsApp-Image-2024-09-24-at-22-56-58-3991fd96.kOZVGz",
    "🏆 2023 World GreenMech Contest Third Place 🥉": "https://im.ge/i/WhatsApp-Image-2024-09-24-at-22-53-42-e05bfa37.kOZk76",
    "🏆 1130310 梯次全國高級中等學校閱讀心得寫作比賽－甲等": "https://im.ge/i/D2689801-38B3-4D1C-BB41-9F3B12D9A2A2.kOZJ6X",
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
st.write('\n')
st.subheader("Coding History")
st.write("---")

st.write("🚀", "**codecademy.com | Python 2**")
st.write("2022 October - December")
st.image("https://i.im.ge/2024/03/17/RPZW5D.WhatsApp-Image-2024-02-21-at-22-02-13-7308a444-3.jpeg", width=600)
st.markdown('[Tap me for PowerPoint](https://docs.google.com/presentation/d/1gO3TiF6HdYTqyM5ak7bD_DiMCHI0IC4C3h1sLWPnN58/edit?usp=sharing)')
st.write(
    """
- ► Embarking on my coding journey, I chose Codecademy for its free lessons and Python for its beginner-friendly language. 
  Through Codecademy, I mastered key concepts like string manipulation, variable usage, and conditional statements. 
  I'm eager to explore advanced subjects and enhance my programming skills further.
"""
)

st.write('\n')
st.write("🚀", "**C++ & Kotlin | Arduino & Android Studio Code**")
st.write("2023 October - December")
st.image("https://i.im.ge/2024/03/17/RPZZg4.Android-Studio-UI-2.png", width=600)
st.markdown('[Tap me for CODES & VIDEOS](https://drive.google.com/drive/folders/1oBFK5lrnFQ8N7uUqWmrUaKHGkha6q5zG?usp=sharing)')
st.write(
    """
- ► I participated in a summer camp organized by Asia Eastern University of Science and Technology. 
  I explored the fundamentals of building Android applications and machine learning with Arduino, adding an exciting dimension to my learning experience.
"""
)

st.write('\n')
st.write("🚀", "**Harvard's CS50P | Python Fundamentals**")
st.write("2024 February")
st.image("https://i.im.ge/2024/03/17/RPZzJP.Screenshot-2024-03-17-162600-5.png", width=600)
st.markdown('[Tap me for CODES](https://drive.google.com/drive/folders/1tk4eW_ImJviEn380W4FlWtlAHXVFi0ha)')
st.write(
    """
- ► To solidify my Python skills, I enrolled in David Malan's Harvard CS50 course. 
  I revisited Python fundamentals and explored more advanced concepts like loops, dictionaries, and unit tests.
"""
)

st.write('\n')
st.write("🎸", "**Side Quest | Mastering the Guitar**")
st.write("2023 March - July")
st.image("https://i.im.ge/2024/03/17/RP84rz.Screenshot-2024-03-17-172811.png", width=600)
st.markdown('[Tap me for POWERPOINT](https://docs.google.com/presentation/d/1KmGS3T-ktMpbJn_gYj8aI7V_aNDvhbKuVnqqFCrnVB4/edit#slide=id.gba05e71233_1_0)')
st.write(
    """
- ► I began learning guitar and mastered basic chords, progressing to solos. 
  I had the opportunity to perform at the talent show, creating unforgettable memories along the way!
"""
)


# --- DISPLAY COMPETITIONS ---
profile.display_competitions()
