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

if "d20" not in st.session_state:
    st.session_state.d20 = False

def disable():
    st.session_state.d20= True

if "Question20" not in st.session_state:
    st.session_state["Question20"] = ('')

def update_mc():
    st.session_state["Question20"] = st.session_state["q20"]

if 'score_20' not in st.session_state:
    st.session_state.score_20 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "In most households food waste is the result of…",
    ["Poor purchasing habits", "Unsuitable packaging sizes", 
    "Date label confusion", "All of the above"],index=None,key= "q20",
    on_change=update_mc,
    disabled=st.session_state.d20
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d20)

if Submit_button:
    if st.session_state.q20 == 'All of the above':
        st.session_state.score_20 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("Bravo, you've unlocked the secret of knowledge! Well done! 🗝️")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown('  \nIn many households food waste is somehow linked to all three of these reasons. Poor knowledge about food storage is another reason.')
            
    else:
        st.error("Your crystal ball must be in need of some polish after that response. 🔮")
        st.info('**The correct answer is: All of the above.**  \n  \n In many households food waste is somehow linked to all three of these reasons. Poor knowledge about food storage is another reason.')

st.write(f"You've selected:  **_{st.session_state.Question20}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

modal = Modal("Warning", key="demo-modal")

with col1:
    if st.button('Previous'):
        switch_page('Question 19') 
    
with col5:
    open_modal = st.button('Finish Quiz!')
if open_modal:
    if not st.session_state.Question19:
        with modal.container():
            st.markdown("***Please select an option***")
    else:
            switch_page('Finish Line') 
       
#st.write(st.session_state)
