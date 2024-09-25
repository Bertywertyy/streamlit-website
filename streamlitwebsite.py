import streamlit as st

# --- Define Profile Class ---
class Profile:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.social_media_links = {}
        self.competitions = {}

    def add_social_media(self, platform, link):
        self.social_media_links[platform] = link

    def add_competition(self, title, link=""):
        self.competitions[title] = link

    def display_profile(self):
        st.title(self.name)
        st.write(self.description)

    def display_social_media(self):
        for platform, link in self.social_media_links.items():
            st.markdown(f"- [{platform}]({link})")

    def display_competitions(self):
        st.subheader("Competitions and Certifications")
        for title, link in self.competitions.items():
            if link:
                st.markdown(f"- [{title}]({link})")
            else:
                st.write(f"- {title}")


# --- PROFILE DATA ---
profile = Profile("Student Name", "Profile Description Goes Here")

# --- ADD SOCIAL MEDIA LINKS ---
social_links = {
    "LinkedIn": "https://www.linkedin.com/in/your-profile",
    "GitHub": "https://github.com/your-profile",
    "Codecademy": "https://www.codecademy.com/profiles/your-profile",
}

for platform, link in social_links.items():
    profile.add_social_media(platform, link)

# --- ADD PRESENTATION & CODES LINKS ---
st.subheader("Additional Resources")
st.markdown('[PowerPoint](https://docs.google.com/presentation/d/1gO3TiF6HdYTqyM5ak7bD_DiMCHI0IC4C3h1sLWPnN58/edit?usp=sharing)')
st.markdown('[CODES & VIDEOS](https://drive.google.com/drive/folders/1oBFK5lrnFQ8N7uUqWmrUaKHGkha6q5zG?usp=sharing)')

# --- ADD COMPETITIONS ---
competitions = {
    "🏆 2023 Indonesia GreenMech R4M Contest Second Place 🥈": "https://ibb.co/rtcqyFs",
    "🏆 2023 World GreenMech Contest Third Place 🥉": "https://ibb.co/TKhbtyY",
    "🏆 1130310 梯次全國高級中等學校閱讀心得寫作比賽－甲等": "",
    "🏆 Sololearn Python Developer completer": "https://api2.sololearn.com/v2/certificates/CC-QEP7COTQ/image/jpg",
}

for title, link in competitions.items():
    profile.add_competition(title, link)

# --- DISPLAY PROFILE ---
profile.display_profile()

# --- DISPLAY SOCIAL MEDIA LINKS ---
st.subheader("Social Media")
profile.display_social_media()

# --- DISPLAY COMPETITIONS ---
profile.display_competitions()
