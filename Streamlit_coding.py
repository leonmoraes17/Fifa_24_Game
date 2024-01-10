### NEEDS TO BE RUN IN BASE ENVIRONMENT ##

import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import numpy as np
from sklearn.pipeline import Pipeline

#loading the saved modela

overall_skill_model = pickle.load(open('trained_model_overall1.sav', 'rb'))

value_model = pickle.load(open('trained_model_value1.sav', 'rb'))
from sklearn.preprocessing import StandardScaler
scaler= StandardScaler()


#sidebar for navigation for choosing the model
import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('soccer.jpeg')  


with st.sidebar:

    selected = option_menu('Choose your Prediction System' ,
                           ['Overall Skill',
                            'Price Category'],
                            icons=['activity', 'currency-euro'], 
                            default_index=0)

#Overall Skill Page

if (selected=="Overall Skill"):
    #page title
    st.title("**Overall Skill using ML**")
    st.markdown("**For eg : Lionel Messi Overall Skill of : 78, we entered the following values :**")
    st.markdown("**Pace:80, Shooting:87, Passing:90, Dribbling: 94, Defending:33, Physic: 64**")
    st.markdown("**Finishing:89, Skill Ability: 96, Sprinting:74**")
    # ['pace_24','shooting_24','passing_24',
    #          'dribbling_24','defending_24','physic_24','attacking_finishing_24','skill_dribbling_24','movement_sprint_speed_24']]
    
    pace = st.number_input('Pace of Player (Denotes the speed of the player)', max_value= 100, min_value=10)
    shooting = st.number_input("Striking Ability",max_value= 100, min_value=10)
    passing = st.number_input("Passing Ability  (Ability to successfully pass the ball with vision)",max_value= 100, min_value=10)
    dribbling = st.number_input("Dribbling Ability \n ( Denotes Ball Control,agility and balance)",max_value= 100, min_value=10)
    defending = st.number_input("Defending Ability",max_value= 100, min_value=10)
    physic = st.number_input("Physic of Player \n ( Denotes Strength and Stamine)",max_value= 100, min_value=10)
    finishing = st.number_input("Finishing Ability (Ability of player to score)",max_value= 100, min_value=10)
    skill = st.number_input("Skill Ability",max_value= 100, min_value=10)
    sprinting = st.number_input("Sprinting Speed (Denotes the Acceleration of the player)",max_value= 100, min_value=10)
    
    # code for Prediction
    overall_diagnosis = ""

    #creating a button for Prediction

    if st.button("Overall Skill Result"):
    #     overall_prediction = overall_skill_model.predict([[pace,shooting,passing,dribbling,defending,physic,finishing,skill,sprinting]])
    #     overall_diagnosis = overall_prediction
    # st.success(overall_diagnosis)



        input_data = (pace,shooting,passing,dribbling,defending,physic,finishing,skill,sprinting)
        input_data_as_numpy_arry = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_arry.reshape(1,-1)
        # input_data_scaled = scaler.fit_transform(input_data_reshaped)
        overall_prediction = overall_skill_model.predict(input_data_reshaped)
        overall_diagnosis= overall_prediction
    st.success(overall_diagnosis)




#Price Category Page

if ( selected == "Price Category"):
    #page title
    st.title("**Price Category using ML**") 
    st.markdown("**Price category in euros: Cheap: 0-1,000,000; Low: 1,000,000 - 2,700,000,**")
    st.markdown("**Average: 2,700,000-20,000,000, Expensive: 20,000,000 - 79,000,000,**")
    st.markdown("**Premium: 79,000,000 and above**")
    st.markdown("**eg. To calculate the Purchase Category of 'Premium' of Lionel Messi, we,**")
    st.markdown("**entered the following values:**")
    st.markdown("**Overall: 90, Wage:23000, Potential Overall: 90, Age: 36, League Level:1, Passing:90,**")
    st.markdown("**Dribbling: 94**")
    # Xv = df_24[['overall_24', 'wage_eur_24', 'potential_24', 'age_24','league_level_24','passing_24', 'dribbling_24' ]]
    overall = st.number_input('Overall Skill of Player',max_value= 100, min_value=10)
    wage = st.number_input("Weekly Wage in euros",max_value= 1000000, min_value=10)
    potential = st.number_input("Potential Overall ( Denotes the ability to increase the players overall skill))",max_value= 100, min_value=10)
    age = st.number_input("Age")
    league_level = st.number_input("League classification",max_value= 5, min_value=1)
    passing = st.number_input("Passing Skill",max_value= 100, min_value=10)
    dribbling = st.number_input("Dribbling Skill ( Denotes Ball Control,agility and balance)",max_value= 100, min_value=10)

 # code for Prediction
    value_diagnosis = "output"

    #creating a button for Prediction

    if st.button("Price Category"):
    #     overall_prediction = overall_skill_model.predict([[pace,shooting,passing,dribbling,defending,physic,finishing,skill,sprinting]])
    #     overall_diagnosis = overall_prediction
    # st.success(overall_diagnosis)



        input_data = (overall, wage, potential, age, league_level, passing, dribbling)
        input_data_as_numpy_arry = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_arry.reshape(1,-1)
        # input_data_scaled = scaler.fit_transform(input_data_reshaped)
        value_prediction = value_model.predict(input_data_reshaped)
        if (value_prediction[0] == 0):
            value_diagnosis = " Cheap Priced Player"
        elif (value_prediction[0] == 1):
            value_diagnosis = " Low Priced Player"
        elif (value_prediction[0] == 2):
            value_diagnosis = " Average Priced Player"
        elif (value_prediction[0] == 3):
            value_diagnosis = " Expensive Player"
        else :
            value_diagnosis= " Premium Player"


        # value_diagnosis= value_prediction
    st.success(value_diagnosis)