import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from streamlit_space import space
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

if "d16" not in st.session_state:
    st.session_state.d16 = False

def disable():
    st.session_state.d16= True

if "Question16" not in st.session_state:
    st.session_state["Question16"] = ('')

def update_mc():
    st.session_state["Question16"] = st.session_state["q16"]

if 'score_16' not in st.session_state:
    st.session_state.score_16 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "What should you do if your freezer stops working?",
    ["Open the door immediately to check the food", "Leave the food inside with the door shut, if it is likely to be working within 24 hours", 
    "All frozen food should be trown out", "None of the above"],index=None,key= "q16",
    on_change=update_mc,
    disabled=st.session_state.d16
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d16)

if Submit_button:
    if st.session_state.q16 == 'Leave the food inside with the door shut, if it is likely to be working within 24 hours':
        st.session_state.score_16 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("You've cast a spell of brilliance with your answer. Well done, wizard! 🎇")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown('  \nThe freezer plays an important role in household management. If it stops, you should not open the door to check the food. If you do, the temperature will rise. If its likely to be working within 24 hours it is best to leave the food inside with the door closed. When the freezer is working, you should check each food item individually. As a general rule, defrosted food should not be refrozen and should be eaten immediately, otherwise it may have to be thrown away.')
            
    else:
        st.error("Looks like your broomstick took an unexpected turn with that response. 🧹")
        st.info('**The correct answer is: Leave the food inside with the door shut, if it is likely to be working within 24 hours.**  \n  \n The freezer plays an important role in household management. If it stops, you should not open the door to check the food. If you do, the temperature will rise. If its likely to be working within 24 hours it is best to leave the food inside with the door closed. When the freezer is working, you should check each food item individually. As a general rule, defrosted food should not be refrozen and should be eaten immediately, otherwise it may have to be thrown away.')

st.write(f"You've selected:  **_{st.session_state.Question16}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button('Previous'):
        switch_page('Question 15') 
    
with col5:
    if st.button('Next'):
        switch_page('Question 17') 
       
# st.write(st.session_state)
