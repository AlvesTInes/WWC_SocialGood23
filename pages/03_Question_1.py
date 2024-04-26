import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from streamlit_extras.let_it_rain import rain
from streamlit_space import space
from st_pages import add_page_title
from PIL import Image
import base64

# THIS COMMENTS APPLY FROM PAGE 'QUESTION 1' TO 'QUESTION 20'

space(lines=10)
# Adds the title and icon to the current page
add_page_title()

# Setting the page's background image and sidebar's image using a local 'png' image file
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

# This allows us to display the avatar in the current page
st.session_state.avatar = st.session_state.avatar

images=[
    Image.open(r"Avatar_1.jpg"),
    Image.open(r"Avatar_2.jpg"),
    Image.open(r"Avatar_3.jpg"),
    Image.open(r"Avatar_4.jpg")
    ]
# Displaying the message 'Welcome + chosen user_id' as the sidebar title and the chosen avatar as the image
st.sidebar.title('Welcome '+ st.session_state.user_id+ '!')    
st.sidebar.image(images[st.session_state.avatar])

# Initializing a session state variable called 'd1' to False; pass the former to the st.button's 'd1' parameter
if "d1" not in st.session_state:
    st.session_state.d1 = False
# Disable the st.radio once the st.button is clicked
def disable():
    st.session_state.d1= True

# The multiselect options will persist by updating the default value, but the default value needs to be initialized
if "Question1" not in st.session_state:
    st.session_state["Question1"] = ('')
# Updates the "non-widget session state key value" to be the same as the "widget session state key value"; on_change
def update_mc():
    st.session_state["Question1"] = st.session_state["q1"]
#Initializing a session state variable called 'score_1' to 0
if 'score_1' not in st.session_state:
    st.session_state.score_1 = 0
# Text to be displayed after the page's title
st.caption('Please select one of the options below:')
# Displays a radio button widget; we have a question and 4 possible options for the answer
question = st.radio(
    "Which option would allow you to reduce food waste in your kitchen?",
    ["Plan your meals", "Buying 'ugly' foods", 
    "Good food storage knowledge and behaviours", "All of the above"],index=None,key= "q1", # The index = None, no option is preselected
    on_change=update_mc,
    disabled=st.session_state.d1
    )
# Once an answer is clicked, it disables; meaning the user only has one chance to answer the question
Submit_button=st.button('Submit',disabled=st.session_state.d1)
# Once the submit_button is clicked: if the correct option is chosen, the 'score_1' updates and is equal to 1
# a sucess message is displayed, as well as a +1 message; additionaly some feedback is also provided
if Submit_button: 
if st.session_state.q1 == "All of the above":
    st.session_state.score_1 +=1
    col1, col2=st.columns([6,1])
    with col1:
        st.success("Bravo, you've unlocked the secret of knowledge! Well done! 🗝️")
        with col2:
            st.warning('&nbsp;&nbsp;&nbsp;**+1** 🌟')
            rain(emoji="✨", font_size=70, falling_speed=2,animation_length=2)
            with st.expander('**📖 Feedback**:'):
                st.markdown('  \nAll the options are valuable tips for avoiding food waste at home! ')
# If the wrong option is selected the 'score_1' is 0, a error message is display as well as the correct option and some feedback            
else:
    st.error('Oh, wizardry gone astray! That answer missed the mark. 🪄')
    st.info('**The correct answer is: All of the above**  \n  \n All the options are valuable tips for avoiding food waste at home!')
# The option that the user selected is displayed
st.write(f"You've selected:  **_{st.session_state.Question1}_**")

st.markdown('***')
# Defining the st.button's layout; once the submit_button it's clicked (on_click callback) it disables (disabled)
# and chances to the next page ('Question 2')
col1, col2, col3 = st.columns([2,1,2])

with col2:
    if st.button('Next'):
        if not st.session_state.Question1:
            st.warning ("Please select an option") 
        else:
            switch_page('Question 2')

# Read the value of the items in Session State
# st.write(st.session_state)






