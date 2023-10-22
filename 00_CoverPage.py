import streamlit as st
from st_pages import Page, Section, show_pages
from streamlit_space import space
import base64

#Defining the name and icon of the pages shown inside of the sidebar (st_pages)
show_pages(
    [
      Page("pages/01_Home.py", "Food Waste Wizards!", "👉"),
      Page("pages/02_Let's_begin!.py", "Let's begin!", "🪄"),
      Section(name='Questions',icon="📜"), #Pages after the 'Section' will be indented
      Page("pages/03_Question_1.py", "Question 1", "❓"),
      Page("pages/04_Question 2.py", "Question 2", "❓"),
      Page("pages/05_Question 3.py", "Question 3", "❓"),
      Page("pages/06_Question 4.py", "Question 4", "❓"),
      Page("pages/07_Question 5.py", "Question 5", "❓"),
      Page("pages/08_Question 6.py", "Question 6", "❓"),
      Page("pages/09_Question 7.py", "Question 7", "❓"),
      Page("pages/10_Question 8.py", "Question 8", "❓"),
      Page("pages/11_Question 9.py", "Question 9", "❓"),
      Page("pages/12_Question 10.py", "Question 10", "❓"),
      Page("pages/13_Question 11.py", "Question 11", "❓"),
      Page("pages/14_Question 12.py", "Question 12", "❓"),
      Page("pages/15_Question 13.py", "Question 13", "❓"),
      Page("pages/16_Question 14.py", "Question 14", "❓"),
      Page("pages/17_Question 15.py", "Question 15", "❓"),
      Page("pages/18_Question 16.py", "Question 16", "❓"),
      Page("pages/19_Question 17.py", "Question 17", "❓"),
      Page("pages/20_Question 18.py", "Question 18", "❓"),
      Page("pages/21_Question 19.py", "Question 19", "❓"),
      Page("pages/22_Question 20.py", "Question 20", "❓"),
      Page("pages/23_Score.py", "Finish Line", "🏅", in_section=False), #The last page, it will not be indented
     
      ]
    )

# Setting the page's background image and sidebar's image using a local 'png' image file
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img = get_img_as_base64("Background_0.png")
img_2 = get_img_as_base64("Background_2.png")


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img}");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}} 

[data-testid="stSidebar"] > div:first-child {{
background-image: url("data:image/png;base64,{img_2}");
background-position: top left; 
background-repeat: no-repeat;
background-attachment: fixed;
}}

</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

# Text to be displayed in the page
space(lines=19) # Creating an empty portion of the app
st.markdown("**Are you ready to explore the realm of food waste and sustainability?  Join us as we embark on this mystical journey to reduce food waste.**")
st.markdown("<h1 style='text-align: center; color: white;'>  \n  \n**Go to _👉Food Waste Wizards_ in the sidebar and let the quiz begin!**</h1>", unsafe_allow_html=True)
