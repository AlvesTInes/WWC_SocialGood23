import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from streamlit_space import space
from streamlit_modal import Modal
from streamlit_gsheets import GSheetsConnection
from st_pages import add_page_title
from PIL import Image
import base64

space(lines=10)

add_page_title()

@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_4 = get_img_as_base64("Background_3.png")
img_2 = get_img_as_base64("Background_2.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_4}");
background-size: cover;
background-position: top-left;
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
    
st.session_state.avatar = st.session_state.avatar

images=[
    Image.open(r"Avatar_1.jpg"),
    Image.open(r"Avatar_2.jpg"),
    Image.open(r"Avatar_3.jpg"),
    Image.open(r"Avatar_4.jpg")
    ]

st.sidebar.title('Wizard '+ st.session_state.user_id+ '!')    
st.sidebar.image(images[st.session_state.avatar])

# Establishing a Google Sheets Connection
#conn= st.connection("gsheets", type=GSheetsConnection)

# Fetch existing data
#existing_data= conn.read(worksheet="FoodWasteWizards",ttl=5)
#existing_data=existing_data.dropna(how='all')
#st.dataframe(existing_data)

if "d2" not in st.session_state:
    st.session_state.d2 = False

def disable():
    st.session_state.d2= True

if "Question2" not in st.session_state:
    st.session_state["Question2"] = ('')

def update_mc():
    st.session_state["Question2"] = st.session_state["q2"]

if 'score_2' not in st.session_state:
    st.session_state.score_2 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "Can you eat eggs past their expiration date?",
    ["No, you should not eat eggs after their expiration date", "Yes, you can unless they are cracked or broken", 
    "Yes, but only in baking or dishes where they will be throroughly cooked", "Options B and C"],index=None,key= "q2",
    on_change=update_mc,
    disabled=st.session_state.d2
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d2)

if Submit_button:
    if st.session_state.q2 == "Options B and C":
        st.session_state.score_2 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("You've cast a spell of brilliance with your answer. Well done, wizard! 🎇")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown("  \nEggs can be eaten after their expiry date. Make sure they look normal and are odourless, and use them for boiling or baking. Boiled eggs should be stored in the fridge and consumed within 2 days.")
            
    else:
        st.error("Wand-erful effort, but the spell of accuracy eluded you this time. 🪄")
        st.info('**The correct answer is: Options B and C.**  \n  \n Eggs can be eaten after their expiry date. Make sure they look normal and are odourless, and use them for boiling or baking. Boiled eggs should be stored in the fridge and consumed within 2 days.')

st.write(f"You've selected:  **_{st.session_state.Question2}_**")

st.markdown('***')
# Defining the st.button's layout; once it's clicked (on_click callback) it disables (disabled)
# and chances to the previous page ('Question 1') or the next page ('Question 3')
col1, col2, col3, col4, col5 = st.columns(5)

modal = Modal("Warning", key="demo-modal")

with col1:
    if st.button('Previous'):
        switch_page('Question 1') 
    
with col5:
    open_modal = st.button('Next')
if open_modal:
    if not st.session_state.Question2:
        with modal.container():
            st.markdown("***Please select an option***")
    else:
            switch_page('Question 3') 
       
# st.write(st.session_state)



