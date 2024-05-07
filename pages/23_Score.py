import streamlit as st
import pandas as pd
from streamlit_gsheets import GSheetsConnection
from st_pages import add_page_title
from streamlit_space import space
import base64

space(lines=4)

# Setting the page's background image and sidebar's image using a local 'png' image file
@st.cache_data
def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()

img_5 = get_img_as_base64("Background_1_4.png")
img_2 = get_img_as_base64("Background_2.png")

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-image: url("data:image/png;base64,{img_5}");
background-size: cover;
background-position: top left;
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
# Adds the title and icon to the current page
add_page_title() 

# Establishing a Google Sheets Connection
#conn= st.connection("gsheets", type=GSheetsConnection)

#Create an empty dataframe
#df= pd.DataFrame(columns=['user_id','age', 'continent', 'country','gender_id', 'score_1','score_2','score_3','score_4','score_5','score_6','score_7','score_8','score_9','score_10','score_11','score_12','score_13','score_14','score_15','score_16','score_17','score_18','score_19','score_20', 'rating'])
#excel_data=conn.update(worksheet="FoodWasteWizards", data=df)

# Fetch existing data
#existing_data= conn.read(worksheet="FoodWasteWizards",usecols=['user_id','age', 'continent', 'country','gender_id', 'score_1','score_2','score_3','score_4','score_5','score_6','score_7','score_8','score_9','score_10','score_11','score_12','score_13','score_14','score_15','score_16','score_17','score_18','score_19','score_20', 'rating', 'total_score', 'user_opinion'], ttl=5)
#existing_data= conn.read(worksheet="FoodWasteWizards",usecols=list(range(28)), ttl=5)
#existing_data=existing_data.dropna(how='all')
#existing_data=conn.update(worksheet="FoodWasteWizards", data=existing_data)

#st.dataframe(existing_data)

# Calculate the total score of the user, by summing all of the session state scores
total_score = st.session_state.score_1 + st.session_state.score_2 + st.session_state.score_3 + st.session_state.score_4 + st.session_state.score_5 + st.session_state.score_6 + st.session_state.score_7 + st.session_state.score_8 + st.session_state.score_9 + st.session_state.score_10 + st.session_state.score_11 + st.session_state.score_12 + st.session_state.score_13 + st.session_state.score_14 + st.session_state.score_15 + st.session_state.score_16 + st.session_state.score_17 + st.session_state.score_18 + st.session_state.score_19 + st.session_state.score_20
# Initializing a session state variable called 'total_score' to total_score
if 'total_score' not in st.session_state:
    st.session_state.total_score = total_score
# Displaying the final score value
st.header(f'Your final score is: {st.session_state.total_score}')
# If the total score value falls within one of the three possible levels, a message is displayed
# according to the level
if  total_score in range(0,6):
    st.error("Alas, your crystal ball of knowledge seems a bit cloudy today!")
    
elif total_score in range(6,15):
    st.warning("The spell seemed promising, but the incantation missed the target!")

elif total_score in range(15,21):
    st.success("Your wisdom shines like a wizard's staff. Well done, my magical friend!")

# Text to be displayed in bottom of the page
st.write("👏 **Bravo, aspiring Food Waste Wizard!**  \n  \n**You’ve embarked on this magical journey, and now it’s time to conclude our quest for food waste wisdom. We hope you’ve uncovered the secrets and knowledge you need to become a true sustainability wizard in your home.**  \n  \n**Now, go forth and share your newfound wisdom with your family and friends.**")
st.markdown("<h1 style='text-align: center; color: white;'>  \n  \n_**Farewell, Food Waste Wizard, until we meet again for our next mystical quest!**_</h1>", unsafe_allow_html=True)

# Additional info 
space(lines=1)
st.write("_**Should you seek to unravel more mystical knowledge, you're welcome to explore these enchanted portals**_")
col1, col2, col3 =st.columns([1,1,1])
with col1:
 st.link_button('eufic.org',"https://www.eufic.org/en/")
with col2:
 st.link_button('fao.org',"https://www.fao.org/home/en/")
with col3:
 st.link_button('wwf.panda.org',"https://wwf.panda.org/discover/our_focus/food_practice/?gclid=EAIaIQobChMI5J2nrumJggMVCL3VCh1I4Qk9EAAYAyAAEgILCPD_BwE")

# Give rating
if "rate" not in st.session_state:
    st.session_state.rate = False
def disable():
    st.session_state.rate= True

# The multiselect options will persist by updating the default value, but the default value needs to be initialized
if "star" not in st.session_state:
    st.session_state["star"] = ()
# Updates the "non-widget session state key value" to be the same as the "widget session state key value"; on_change
def update_star_rating():
    st.session_state["star"] = st.session_state["rating"]

space(lines=3)
col1, col2, col3 = st.columns([1,6,1])
with col2:
 st.write("**We value your feedback. Please take a moment to rate our app!**")
 rating = st.radio("label",[1, 2, 3, 4, 5],index=None, horizontal=True,label_visibility="collapsed",captions=["⭐","⭐⭐","⭐⭐⭐","⭐⭐⭐⭐","⭐⭐⭐⭐⭐"],key='rating', on_change=update_star_rating, disabled=st.session_state.rate)

space(lines=2)
# Create a test input for user opinion
user_opinion=st.text_input('**Please let us know what you think of our app!**', disabled=st.session_state.rate)

# Initializing the session state keys 'user_opinion'
def initialize_user_opinion():
    if ('user_opinion' not in st.session_state) and (user_opinion != ''):
        st.session_state.user_opinion = user_opinion
        
def update_opinion():
    if'user_opinion' in st.session_state:
        st.write()
  
initialize_user_opinion()
update_opinion() 

space(lines=2)
col1,col2,col3 = st.columns([2,1,2])
with col2:
 End_button=st.button('Finish Quiz!',on_click=disable, disabled=st.session_state.rate) 

col1,col2,col3 = st.columns([1,5,1])
with col2:
 if End_button:
     #player_data = pd.DataFrame([{"user_id": st.session_state.user_id,"age": st.session_state.age,"continent": st.session_state.continent,"country": st.session_state.country,"gender_id": st.session_state.gender_id,
                                   "score_1": st.session_state.score_1, "score_2": st.session_state.score_2,"score_3": st.session_state.score_3,"score_4": st.session_state.score_4,"score_5": st.session_state.score_5,
                                   "score_6": st.session_state.score_6,"score_7": st.session_state.score_7,"score_8": st.session_state.score_8,"score_9": st.session_state.score_9,"score_10": st.session_state.score_10,
                                   "score_11": st.session_state.score_11,"score_12": st.session_state.score_12,"score_13": st.session_state.score_13,"score_14": st.session_state.score_14,"score_15": st.session_state.score_15,
                                   "score_16": st.session_state.score_16,"score_17": st.session_state.score_17,"score_18": st.session_state.score_18,"score_19": st.session_state.score_19,"score_20": st.session_state.score_20,
                                   "rating": st.session_state.rating,"total_score": st.session_state.total_score,"user_opinion": st.session_state.user_opinion,}])
     #updated_df=pd.concat([existing_data, player_data], ignore_index=True)
     #conn.update(worksheet="FoodWasteWizards", data=updated_df)
     col1,col2,col3 = st.columns([2,1,2])
     with col2:
         st.warning('Thank you!')
         
# Read the value of the items in Session State
#st.write(st.session_state)
