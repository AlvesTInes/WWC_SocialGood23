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

if "d13" not in st.session_state:
    st.session_state.d13 = False

def disable():
    st.session_state.d13= True

if "Question13" not in st.session_state:
    st.session_state["Question13"] = ('')

def update_mc():
    st.session_state["Question13"] = st.session_state["q13"]

if 'score_13' not in st.session_state:
    st.session_state.score_13 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    "Which one of these food storage tip is correct?",
    ["Meat should be at the top shelf of the fridge", "Tomatoes and onions should be stored in the fridge, never at room temperature or in a cool pantry", 
    "Dairy products should be at the back of the fridge", "You should wash your fruits and vegetables as soon as you come home from the grocery store"],index=None,key= "q13",
    on_change=update_mc,
    disabled=st.session_state.d13
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d13)

if Submit_button:
    if st.session_state.q13 == 'Dairy products should be at the back of the fridge':
        st.session_state.score_13 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("Your answer is pure wizardry – truly enchanting! Well done! ✨")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown("  \nIt is crucial to keep dairy products at the back of the fridge, where it's coldest.")
            
    else:
        st.error("Your crystal ball must be in need of some polish after that response. 🔮")
        st.info("**The correct answer is: Dairy products should be at the back of the fridge.**  \n  \n It is crucial to keep dairy products at the back of the fridge, where it's coldest.")

st.write(f"You've selected:  **_{st.session_state.Question13}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

modal = Modal("Warning", key="demo-modal")

with col1:
    if st.button('Previous'):
        switch_page('Question 12') 
    
with col5:
    open_modal = st.button('Next')
if open_modal:
    if not st.session_state.Question13:
        with modal.container():
            st.markdown("***Please select an option***")
    else:
            switch_page('Question 14')  
       
# st.write(st.session_state)
