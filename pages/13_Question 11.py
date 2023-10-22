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

if "d11" not in st.session_state:
    st.session_state.d11 = False

def disable():
    st.session_state.d11= True

if "Question11" not in st.session_state:
    st.session_state["Question11"] = ('')

def update_mc():
    st.session_state["Question11"] = st.session_state["q11"]

if 'score_11' not in st.session_state:
    st.session_state.score_11 = 0

st.caption('Please select one of the options below:')

question = st.radio(
    " Which of the following options refers to the reuse of food that would otherwise be discarded?",
    ["Use what you have", "Avoid serving too much", 
    "Pick up food from restaurants and stores", "None of the above"],index=None,key= "q11",
    on_change=update_mc,
    disabled=st.session_state.d11
    )

Submit_button=st.button('Submit',on_click=disable, disabled=st.session_state.d11)

if Submit_button:
    if st.session_state.q11 == 'Pick up food from restaurants and stores':
        st.session_state.score_11 +=1
        col1, col2=st.columns([6,1])
        with col1:
            st.success("You've just brewed up a potion of success with your answer. Well done, wizard! 🧪")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
        rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
        with st.expander('**📖 Feedback**:'):
            st.markdown('  \nRepurposing waste whenever possible is another valuable tip to help you reduce food waste. Picking food from stores and restaurants that would otherwise be discarded is one very good tip, keeping a food waste diary and writring down creative ways to stop wasting food is another great way to repurpose food scraps. All the other options are also good for reducing food waste.')
            
    else:
        st.error("Wand-erful effort, but the spell of accuracy eluded you this time. 🪄")
        st.info('**The correct answer is: Pick up food from restaurants and stores.**  \n  \n Repurposing waste whenever possible is another valuable tip to help you reduce food waste. Picking food from stores and restaurants that would otherwise be discarded is one very good tip, keeping a food waste diary and writring down creative ways to stop wasting food is another great way to repurpose food scraps. All the other options are also good for reducing food waste.')

st.write(f"You've selected:  **_{st.session_state.Question11}_**")

st.markdown('***')

col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    if st.button('Previous'):
        switch_page('Question 10') 
    
with col5:
    if st.button('Next'):
        switch_page('Question 12') 
       
# st.write(st.session_state)
