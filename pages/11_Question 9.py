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

if "d9" not in st.session_state:
    st.session_state.d9 = False

def disable():
    st.session_state.d9= True

if "Question9" not in st.session_state:
    st.session_state["Question9"] = ('')

def update_mc():
    st.session_state["Question9"] = st.session_state["q9"]

if 'score_9' not in st.session_state:
    st.session_state.score_9 = 0
    
st.caption('Please select one of the options below:')

question = st.radio(
    "Which one of these refrigerated foods has the longest shelf life?",
    ["Margarine", "Butter", 
    "Fruit juices", "Ricotta cheese"],index=None,key= "q9",
    on_change=update_mc,
    disabled=st.session_state.d9
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d9)

if Submit_button:
    if st.session_state.q9 == 'Margarine':
        st.session_state.score_9 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("Your answer is pure wizardry – truly enchanting! Well done! ✨")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown("  \nFoods labelled 'keep refrigerated' should be stored in the fridge to keep it safe. Margarine stored in the fridge lasts up to 6 months, butter 8 weeks, fruit juices 7-14 days and ricotta cheese 10 days. Uncooked poultry, meat, seafood and crustaceans have the shortest shelf life, just 3-5 days.")
            
    else:
        st.error('Oh, wizardry gone astray! That answer missed the mark. 🪄')
        st.info("**The correct answer is: Margarine.**  \n  \n Foods labelled 'keep refrigerated' should be stored in the fridge to keep it safe. Margarine stored in the fridge lasts up to 6 months, butter 8 weeks, fruit juices 7-14 days and ricotta cheese 10 days. Uncooked poultry, meat, seafood and crustaceans have the shortest shelf life, just 3-5 days.")

st.write(f"You've selected:  **_{st.session_state.Question9}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button('Previous'):
        switch_page('Question 8') 
    
with col5:
    if st.button('Next'):
        switch_page('Question 10') 
       
# st.write(st.session_state)
