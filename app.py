import streamlit as st
import pandas as pd
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

df = pd.read_csv("comptes.csv")


credentials = {'usernames': {}}
for _, row in df.iterrows():
    credentials['usernames'][row['name']] = {
        'name': row['name'],
        'password': str(row['password']),
        'email': row['email'],
        'failed_login_attemps': int(row['failed_login_attemps']),
        'logged_in': bool(row['logged_in']),
        'role': row['role']
    }

authenticator = stauth.Authenticate(credentials, "cookie", "key", 30)
authenticator.login(location='main')


if st.session_state["authentication_status"]:
    username = st.session_state["username"]
    
    with st.sidebar:
        st.write(f"### Bienvenue {username}")
        selection = option_menu(
            menu_title=None,
            options=["Accueil", "Photos de Russie"],
            icons=["house", "camera"]
        )
        authenticator.logout('Déconnexion', 'sidebar')

    if selection == "Accueil":
        st.title("Bienvenue sur ma page d'accueil")
        
        st.image("https://mf.b37mrtl.ru/rbthmedia/images/2021.11/original/6193a80615e9f94cad681737.jpg", caption="Bienvenue en Russie")
    
    elif selection == "Photos de Russie":
        st.title("Mes photos de Russie")
        
        # CSS
        st.markdown("""
            <style>
            [data-testid="stImage"] img {
                height: 450px; 
                object-fit: cover;
                width: 100%;
                border-radius: 10px;
            }
            </style>
            """, unsafe_allow_html=True)

        c1, c2, c3 = st.columns(3)
        with c1: st.image("https://images.unsplash.com/photo-1513326738677-b964603b136d?w=800")
        with c2: st.image("https://www.shutterstock.com/image-photo/high-buildings-moscowcity-moskva-river-260nw-2536606723.jpg")
        with c3: st.image("https://mf.b37mrtl.ru/rbthmedia/images/2020.10/original/5f9a99c015e9f95df179f254.jpg")

elif st.session_state["authentication_status"] is False:
    st.error("Username/password incorrect")
elif st.session_state["authentication_status"] is None:
    st.warning('Veuillez vous connecter')

    st.markdown("""
---
### Test accounts  
- **Username :** `zilya`  
- **Password :** `123`
""")
