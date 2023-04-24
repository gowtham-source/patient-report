import altair as alt
# import pandas as pd  # pip install pandas openpyxl
import plotly.graph_objs as go
import altair as alt
import os
import streamlit as st  # pip install streamlit
import streamlit_authenticator as stauth  # pip install streamlit-authenticator
# import time
import database as db
import update_database as ud
from streamlit_option_menu import option_menu
import base64
import pandas as pd
from firebase import get_image_url
import numpy as np

st.session_state["user_id"] = ""

st.set_page_config(page_title="Home", page_icon="🏠",
                   layout="wide", initial_sidebar_state="collapsed")


def get_img_as_base64(file):
    with open(file, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode()


# img = get_img_as_base64("./assets/bus_bg.jpg")
# st.markdown('''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">''', unsafe_allow_html=True)
st.markdown('''<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">''', unsafe_allow_html=True)


page_bg = f'''
<style>
p{{
    font-family: 'Work Sans', sans-serif;
}}
[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}
[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
'''
st.markdown(page_bg, unsafe_allow_html=True)

css = """
                    <style>
                        .card {
                            padding: 1rem;
                            border-radius: 25px;
                            box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.2);
                            
                            margin-bottom: 20px;
                            width: 400px;
                            height: 300px;
                        }
                    </style>
                """

# Display the CSS style
st.markdown(css, unsafe_allow_html=True)
placeholder = st.empty()

users = db.fetch_all_users()

usernames = [user["key"] for user in users]
names = [user["name"] for user in users]
passwords = [user["password"] for user in users]

credentials = {"usernames": {}}

for un, name, pw in zip(usernames, names, passwords):
    user_dict = {"name": name, "password": pw}
    credentials["usernames"].update({un: user_dict})


placeholder = st.empty()
with placeholder.container():
    selected3 = option_menu(None, ["Sign-in", "Sign-up"],
                            icons=['box-arrow-in-right',
                                   'arrow-right-square-fill'],
                            menu_icon="cast", default_index=0, orientation="horizontal")

st.session_state["user_id"] = ""

authenticator = stauth.Authenticate(
    credentials, 'some_cookie_name', 'some_signature_key', cookie_expiry_days=30)
if selected3 == "Sign-in":
    # name = st.text_input("Name", placeholder='Enter your name')
    # username = st.text_input("Username", placeholder='Enter username')
    # password = st.text_input("password", placeholder='Enter the password')

    name, authentication_status, username = authenticator.login(
        "Login", "main")

    if authentication_status == False:
        st.error("Username/password is incorrect")

    if authentication_status == None:
        st.warning("Please enter your username and password")

    if authentication_status:
        # st.write('Welcome {0}!'.format(name))
        st.session_state["user_id"] = name

        placeholder.empty()
        try:

            df = pd.read_csv('userdata/user_details.csv')
            # name = df.loc[df['username'] == username, 'name'].iloc[0]
            age = df.loc[df['username'] == username, 'age'].iloc[0]
            gender = df.loc[df["username"] == username, 'gender'].iloc[0]
            with st.container():
                col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
                col1.write("### Patient name:")

                col1.write(
                    "### {0}".format(name))
                col2.write("### Age:")
                col2.write("### {0}".format(age))
                col3.write('### Gender:')
                col3.write('### {0}'.format(gender))
                with col4:
                    image_url = get_image_url(name)
                    st.image(image_url, width=200)

                # Define CSS style for the card
                hr = 172
                ox = 82
                st.write("")
                st.write("")
                col6, col7 = st.columns([1, 1])
                with col6:
                    st.write(
                        f'''<div class="card">
                            <h3>Vital:</h3></br><h3><i class="fa-solid fa-heart-pulse fa-beat-fade fa-2xl"></i></h3>
                            <div>
                            <h3>Heart beat rate: {hr}bpm</h3>
                            <h3>Oxygen Level: {ox}%</h3></div></div>''', unsafe_allow_html=True)
                    with st.container():

                      # Generate random patient data
                        np.random.seed(0)
                        age = np.random.randint(18, 90, 100)
                        bp = np.random.randint(60, 200, 100)

                        # Create a dataframe with the patient data
                        df = pd.DataFrame({'age': age, 'blood_pressure': bp})

                        # Add a slider to filter the data by age
                        age_range = st.slider('Age Range', 18, 90, (18, 90))
                        filtered_df = df[(df['age'] >= age_range[0]) & (
                            df['age'] <= age_range[1])]

                        # Create a scatter plot with Altair
                        scatter_plot = alt.Chart(filtered_df).mark_circle().encode(
                            x='age',
                            y='blood_pressure',
                            tooltip=['age', 'blood_pressure']
                        ).properties(
                            width=800,
                            height=400
                        )

                        # Show the scatter plot in Streamlit
                        st.altair_chart(scatter_plot)

                with col7:
                    col1, col2, col3 = st.columns(3)
                    col1.metric("Temperature", "98.6°F", "1.2 °c")
                    col2.metric("Blood Pressure", "120/80 mmHg", "-8%")
                    col3.metric("Glucose level", "86%", "4%")
                    st.write("")
                    st.write("")
                    with st.container():
                        df3 = pd.read_csv('medication.csv')
                        st.write(df3)
                with st.container():
                    np.random.seed(0)
                    n_patients = 50
                    weight = np.random.normal(70, 10, n_patients)
                    height = np.random.normal(170, 10, n_patients)
                    age = np.random.normal(40, 10, n_patients)

                    # Create a Pandas dataframe with the patient data
                    df = pd.DataFrame(
                        {'Weight (kg)': weight, 'Height (cm)': height, 'Age (years)': age})

                    # Create a Plotly bar chart with multiple variables
                    st.bar_chart(df)

                np.random.seed(0)
                n_days = 30
                mental_state = np.random.normal(5, 2, n_days)

                # Create a Pandas dataframe with the patient data
                df = pd.DataFrame(
                    {'Day': range(1, n_days+1), 'Mental State': mental_state})

                # Create a Vega-Lite chart with size and color indicating mental state
                st.vega_lite_chart(df, {
                    'mark': {'type': 'circle', 'tooltip': True},
                    'encoding': {
                        'x': {'field': 'Day', 'type': 'quantitative', 'title': 'Day'},
                        'y': {'field': 'Mental State', 'type': 'quantitative', 'title': 'Mental State'},
                        'size': {'field': 'Mental State', 'type': 'quantitative', 'scale': {'range': [10, 200]}, 'title': 'Mental State'},
                        'color': {'field': 'Mental State', 'type': 'quantitative', 'scale': {'range': ['green', 'yellow', 'red']}, 'title': 'Mental State'},
                    },
                    'width': 500,
                    'height': 400,
                    'title': 'Patient Mental State over Time'
                })

        except Exception as e:
            print(e)
            pass


if selected3 == "Sign-up":
    name = st.text_input("Name", placeholder='Enter your name')
    username = st.text_input("Username", placeholder='Enter username')
    password = st.text_input("password", placeholder='Enter the password')
    age = st.text_input("Age", placeholder='Enter your age')
    ph_no = st.text_input(
        "Phone Number", placeholder='Enter your phone number')
    mail_id = st.text_input("Email ID", placeholder='Enter your email id')
    gender = st.selectbox('Select the gender here', ('Male', 'Female'))
    if st.button('submit'):
        ud.signup(name, username, password)
        age = int(age)
        data = [[name, username, ph_no, mail_id, age, gender]]
        columns = ['name', 'username', 'ph_no', 'mail_id', 'age', 'gender']
        df = pd.DataFrame(data, columns=columns)
        output_path = 'userdata/user_details.csv'
        df.to_csv(output_path, mode='a', index=False,
                  header=not os.path.exists(output_path))
        st.session_state["user_id"] = name
        st.write('Welcome', name)

        with st.container():
            col1, col2, col3 = st.columns([1, 1, 1])

authenticator.logout("Logout", "sidebar")
