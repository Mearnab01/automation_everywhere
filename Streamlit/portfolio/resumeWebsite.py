import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image
from pathlib import Path


#---INITIALIZING----
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir/"style"/"style.css"
profile_pic = current_dir/"profile-pic.png" #paste your profile pic at same folder
st.set_page_config(page_title="My Webpage", page_icon=":wave:",layout="wide")

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
profile_pic = Image.open(profile_pic)

# ---- LOAD ASSETS ----
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


#-------HEADER-----
with st.container():
    left_column , right_column = st.columns((2,1))
    with left_column:
        st.subheader("Hi, I am <Your Name> :wave:")
        st.title("A Data Analyst From Germany")
        st.write(
            "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
        )
        st.write("[Learn More >](https://linkOfYourWebsite.com)")
    with right_column:
        st.image(profile_pic , width=230)

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel....
            """
        )
        st.write("[YouTube Channel >](https://yourYtChannelLink)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")


# ---- PROJECTS ----

# Define a list of projects, each with a name, image URL, description, and link
projects = [
    {
        "name": "Project 1",
        "image": "",
        "description": "Description for Project 1 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 2",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 3",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 4",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 5",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 6",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 7",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    },
    {
        "name": "Project 8",
        "image": "",
        "description": "Description for Project 2 goes here. You can provide details about this project.",
        "link": "",
    }
    
]

# Create a layout with two rows and four columns
cols = st.columns(4)

# Loop through the projects and generate content for each project
for i,project in enumerate(projects):
    with cols[i % 4]:  # Cycle through the four columns
        st.write("---")
        st.header(project["name"])
        st.write("##")
        st.image(project["image"], use_column_width=True)
        st.subheader(f"{project['name']} Description")
        st.write(project["description"])
        st.markdown(f"[{project['name']} Link]({project['link']})")

#---------CONTACT------------
st.header(":mailbox: Get in touch with me!")
contact_form = """
<form action="" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name.." required>
     <input type="email" name="email" placeholder="Your email.." required>
     <textarea name="message" placeholder="Your messge here.."></textarea>
     <input type="file" name="attachment" accept="image/png, image/jpeg pdf">
     <button type="submit">Send</button>
</form>
"""
st.markdown(contact_form , unsafe_allow_html=True)

#SOCIAL MEDIA 
SOCIAL_MEDIA = {
    "Instagram": "https://instagram.com",
    "LinkedIn": "https://linkedin.com",
    "GitHub": "https://github.com",
    "Whatsapp": "https://web.whatsapp.com/",
    
}
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

