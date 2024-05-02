import streamlit as st
import pandas as pd
from streamlit_extras.switch_page_button import switch_page
from streamlit_space import space
from streamlit_image_select import image_select
from streamlit_gsheets import GSheetsConnection
from st_pages import add_page_title
from PIL import Image
import base64

space(lines=3) 
# Adds the title and icon to the current page
add_page_title()

# Setting the page's background image and sidebar's image using a local 'png' image file
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_3 = get_img_as_base64("Background_3.png")
img_2 = get_img_as_base64("Background_2.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_3}");
background-size: 100%;
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
  
# Text to be displayed under the page's title
st.markdown("<h1 style='text-align: center; color: white;'>  \n  \n_**Hello, aspiring Food Waste Wizard!**_  \n  \n_**Let's unlock the mysteries of reducing food waste, transforming your home into a magical realm of eco-consciousness**_</h1>", unsafe_allow_html=True)

# Establishing a Google Sheets Connection
conn= st.connection("gsheets", type=GSheetsConnection)

# Fetch existing data
#existing_data= conn.read(worksheet="FoodWasteWizards",usecols=list(range(26)), ttl=5)
#existing_data=existing_data.dropna(how='all')
#st.dataframe(existing_data)

# Initializing a session state variable called 'quiz' to False; pass the former to the st.button's 'quiz' parameter
if "quiz" not in st.session_state:
    st.session_state.quiz = False
# Disable the age slider, gender selectbox and st.button after it's clicked
def disable():
    st.session_state.quiz= True
# Because a "widget session state key" has the value of the current selection; store the selection as a default
# session state key and then on each page refresh assign that as the default; the on_change callback
# updates the "non-widget session state key value" to be the same as the "widget session state key value"
def update_age():
    st.session_state.age = st.session_state["slider"]
def update_continent():
    st.session_state.continent = st.session_state["select_boxcontinent"]
def update_country():
    st.session_state.country = st.session_state["select_boxcountry"]
def update_gender_id():
    st.session_state.gender_id = st.session_state["select_boxage"]

# Displaying a single-line text input widget, where the user must insert their user identification
user_id= st.text_input('**Please create an User ID:**', disabled=st.session_state.quiz)
space(lines=1)
# Displaying a range slider widget, where the user should choose their age (from 13, minimum, to 100, maximum)
age= st.slider('**How old are you?**', 13,100, key='slider', on_change=update_age, disabled=st.session_state.quiz) # Once the user selects their age, this value will be stored under the key 'age'
space(lines=1)
# Displaying a select widget, where the user should choose their continent and country
data = 'https://raw.githubusercontent.com/AlvesTInes/WWC_SocialGood23/main/Countries%20by%20continents.csv'
df = pd.read_csv(data)
continent_data = df['Continent'].drop_duplicates()
continent = st.selectbox('**Please select a Continent:**', continent_data, index=None, placeholder="Select a continent", key='select_boxcontinent',
                         on_change=update_continent, disabled=st.session_state.quiz)
space(lines=1)
df1 = df.loc[df.Continent == continent]
df2 = df1.Country
country = st.selectbox('**Please select a Country:**', df2, index=None, placeholder="Select a country", key='select_boxcountry',
                         on_change=update_country, disabled=st.session_state.quiz)
space(lines=1)
# Displaying a select widget, where the user should choose from the options presented their gender identity
gender_id= st.selectbox('**Please select your gender identity:**', ['Female','Trans Female','Male','Trans Male','Genderqueer','Non-binary','Prefer not to say'],
                        index=None, placeholder="Select your gender identiy", key='select_boxage', 
                        on_change=update_gender_id, # Once the user selects their gender identity, it will store that value under the key 'gender_id'
                        disabled=st.session_state.quiz)
space(lines=1)
st.markdown("**Please select your avatar:**")
# Displaying an image select component, where the user must choose 1 of the 4 available avatars to represent them
avatar = image_select(
    label=(),
    images=[
        Image.open(r"Avatar_1.jpg"), # The images are a local 'png' file
        Image.open(r"Avatar_2.jpg"),
        Image.open(r"Avatar_3.jpg"),
        Image.open(r"Avatar_4.jpg")
        ], key='avatar'
    )
# Initializing the session state keys 'user_id', 'age', 'gender_id' and 'avatar'
def initialize_session_state():
    if ('user_id' not in st.session_state) and (user_id != ''):
        st.session_state.user_id = user_id
    if 'age' not in st.session_state:
        st.session_state.age = ()
    if 'gender_id' not in st.session_state:
        st.session_state.gender_id = ('')
    if 'avatar' not in st.session_state:
        st.session_state.avatar = avatar

def update_user():
    if'user_id' in st.session_state:
        st.write()
    if 'avatar' in st.session_state:
        st.write()

initialize_session_state()
update_user()

space(lines=2)

# Defining the st.button's layout; once it's clicked (on_click callback) it disables (disabled)
# and chances to the next page ('Question 1')
col1, col2, col3 = st.columns([2,1,2])

with col2:
    if st.button("Let's go!", on_click=disable, disabled=st.session_state.quiz):
        df= pd.DataFrame(columns=['user_id','age', 'continent', 'country','gender_id', 'score_1','score_2','score_3','score_4','score_5','score_6','score_7','score_8','score_9','score_10','score_11','score_12','score_13','score_14','score_15','score_16','score_17','score_18','score_19','score_20', 'rating'])
        existing_data=conn.create(worksheet="FoodWasteWizards", data=df)
        #user_data = pd.DataFrame([{"user_id": st.session_state.user_id,"age": st.session_state.age,"continent": st.session_state.continent,"country": st.session_state.country,"gender_id": st.session_state.gender_id,}])
        #updated_df = pd.concat([existing_data, user_data], ignore_index=True)
        #conn.update(worksheet="FoodWasteWizards", data=updated_df)
        switch_page('Question 1')

# Read the value of the items in Session State
# st.write(st.session_state)

  
