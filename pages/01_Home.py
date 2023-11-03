import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_space import space
from st_pages import add_page_title
import base64

# Setting the page's background image and sidebar's image using a local 'png' image file
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_1 = get_img_as_base64("Background_1_4.png")
img_2 = get_img_as_base64("Background_2.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_1}");
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

# Initializing the session state; it is intended to not allow the user to return to the 'Food Storage Wizards!'page
# once it clicks the button
if "intro" not in st.session_state:
   st.session_state["intro"] = False

# Adds the title to the current page, but not the icon
space(lines=3) 
add_page_title(add_icon=False)

# Text to be displayed in the page
st.write("**👋🪄 Welcome to the enchanted quiz on food waste!**  \n  \n**Food waste is a pressing issue that has significant environmental, social and economic consequences.**  \n  \n**_Did you know that nearly 59 million tonnes of food waste are produced every year in the EU (around 131 kg per person), more than half of which comes from households?_**   \n  \n**Take the quiz, assess your knowledge of food waste, and learn some wizardly tips to make your home more sustainable. 🌱♻️**  \n  \n**By following these practical tips, you’ll be on your way to becoming a true Food Waste Wizard, dedicated to saving money and preserving your food and our magical planet! 🌍**")
st.markdown("<h1 style='text-align: center; color: white;'>  \n  \n_**What are you waiting for? Gather your wands, put on your wizarding hats, and get ready to test your magical knowledge of food waste.**_</h1>", unsafe_allow_html=True)

# Creating a "Create your profile" button; when is pressed it changes to next page - 'Let's begin!' page
col1, col2, col3 = st.columns([1,1,1])

with col2:
    if st.button("Create your profile!"):
        st.session_state["intro"] = True
        if st.session_state["intro"]:
            switch_page("Let's_begin!") 
