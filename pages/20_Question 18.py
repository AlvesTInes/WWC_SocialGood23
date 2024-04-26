import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from streamlit_space import space
from streamlit_modal import Modal
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

if "d18" not in st.session_state:
    st.session_state.d18 = False

def disable():
    st.session_state.d18= True

if "Question18" not in st.session_state:
    st.session_state["Question18"] = ('')

def update_mc():
    st.session_state["Question18"] = st.session_state["q18"]

if 'score_18' not in st.session_state:
    st.session_state.score_18 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "What can't you put in your food waste recycling bin?",
    ["Cooking oils", "Food soiled paper napkins and paper towels", 
    "Rice, pasta and cereals", "Leftover food from your plate and dishes"],index=None,key= "q18",
    on_change=update_mc,
    disabled=st.session_state.d18
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d18)

if Submit_button:
    if st.session_state.q18 == 'Cooking oils':
        st.session_state.score_18 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("You've conjured up the correct answer from the depths of your wizard's hat. Well done! 🧙")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown('  \nCooking oils should not be placed in the food waste recycling bin. Putting contents that should not go in your food waste recycling bin will contaminate the load and will not compost.')
            
    else:
        st.error("Your knowledge spell needs a little more enchantment, my friend. 🪄")
        st.info('**The correct answer is: Cooking oils.**  \n  \n Cooking oils should not be placed in the food waste recycling bin. Putting contents that should not go in your food waste recycling bin will contaminate the load and will not compost.')

st.write(f"You've selected:  **_{st.session_state.Question18}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

modal = Modal("Warning", key="demo-modal")

with col1:
    if st.button('Previous'):
        switch_page('Question 17') 
    
with col5:
    open_modal = st.button('Next')
if open_modal:
    if not st.session_state.Question18:
        with modal.container():
            st.markdown("***Please select an option***")
    else:
            switch_page('Question 19') 
       
# st.write(st.session_state)
