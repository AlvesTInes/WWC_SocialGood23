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

if "d6" not in st.session_state:
    st.session_state.d6 = False

def disable():
    st.session_state.d6= True

if "Question6" not in st.session_state:
    st.session_state["Question6"] = ('')

def update_mc():
    st.session_state["Question6"] = st.session_state["q6"]

if 'score_6' not in st.session_state:
    st.session_state.score_6 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "Which fruit and vegetables should not be stored together to prevent them from spoiling quickly?",
    ["Citrus fruit and Nectarine", "Eggplant and Artichoke", 
    "Berries and Kiwi", "Bell pepper and Carrot"],index=None,key= "q6",
    on_change=update_mc,
    disabled=st.session_state.d6
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d6)

if Submit_button:
    if st.session_state.q6 == 'Citrus fruit and Nectarine':
        st.session_state.score_6 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("You've just brewed up a potion of success with your answer. Well done, wizard! 🧪")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown('  \nSome vegetables and fruit, such as nectarines, produce a high amount of ethylene gas, which is linked to the ripening process of fruit and vegetables. Citrus fruits and other fruits and vegetables are more sensitive to ethylene gas, which causes them to spoil more quickly. You should never combine fruits and vegetables that produce a large amount of ethylene with fruits and vegetables that are sensitive to ethylene.')
            
    else:
        st.error("Your crystal ball must be in need of some polish after that response. 🔮")
        st.info('**The correct answer is: Citrus fruit and Nectarine.**  \n  \n Some vegetables and fruit, such as nectarines, produce a high amount of ethylene gas, which is linked to the ripening process of fruit and vegetables. Citrus fruits and other fruits and vegetables are more sensitive to ethylene gas, which causes them to spoil more quickly. You should never combine fruits and vegetables that produce a large amount of ethylene with fruits and vegetables that are sensitive to ethylene.')

st.write(f"You've selected:  **_{st.session_state.Question6}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5) 

modal = Modal("Warning", key="demo-modal")

with col1:
    if st.button('Previous'):
        switch_page('Question 5') 
    
with col5:
    open_modal = st.button('Next')
if open_modal:
    if not st.session_state.Question6:
        with modal.container():
            st.markdown("***Please select an option***")
    else:
            switch_page('Question 7') 
       
# st.write(st.session_state)
