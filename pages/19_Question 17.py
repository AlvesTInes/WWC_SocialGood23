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

if "d17" not in st.session_state:
    st.session_state.d17 = False

def disable():
    st.session_state.d17= True

if "Question17" not in st.session_state:
    st.session_state["Question17"] = ('')

def update_mc():
    st.session_state["Question17"] = st.session_state["q17"]

if 'score_17' not in st.session_state:
    st.session_state.score_17 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "What can you put in your food waste recycling bin?",
    ["Fruits and vegetables", "Meat, poultry and fish, including bones", 
    "Tea bags and coffee grinds", "All of the above"],index=None,key= "q17",
    on_change=update_mc,
    disabled=st.session_state.d17
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d17)

if Submit_button:
    if st.session_state.q17 == 'All of the above':
        st.session_state.score_17 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("You've just brewed up a potion of success with your answer. Well done, wizard! 🧪")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown('  \nYou can put all these items in your food waste recycling bin. Later these, will be taken by a waste collector to a composting facility, where they will be used to produce a high-quality compost.')
            
    else:
        st.error('Oh, wizardry gone astray! That answer missed the mark. 🪄')
        st.info('**The correct answer is: All of the above.**  \n  \n You can put all these items in your food waste recycling bin. Later these, will be taken by a waste collector to a composting facility, where they will be used to produce a high-quality compost.')

st.write(f"You've selected:  **_{st.session_state.Question17}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button('Previous'):
        switch_page('Question 16') 
    
with col5:
    if st.button('Next'):
        switch_page('Question 18') 
       
# st.write(st.session_state)
