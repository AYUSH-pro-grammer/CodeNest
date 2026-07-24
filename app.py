import streamlit as st

from config import APP_NAME

from views.create import show_create
from views.home import show_home
from views.profile import show_profile
from views.signin import show_signin
from views.signup import show_signup



st.set_page_config(
    page_title=APP_NAME,
    page_icon="CodeNest",
    layout="wide",
)




def show_sidebar():
    st.sidebar.title(APP_NAME)

    if st.sidebar.button(
        "Home",
        use_container_width=True,
    ):
        st.session_state.page = "home"
        st.rerun()


    if st.session_state.logged_in:
        st.sidebar.write(
            f"Signed in as {st.session_state.username}"
        )


        if st.sidebar.button(
            "Create question",
            use_container_width=True,
        ):
            st.session_state.page = "create"
            st.rerun()


        if st.sidebar.button(
            "Profile",
            use_container_width=True,
        ):
            st.session_state.page = "profile"
            st.rerun()


        if st.sidebar.button(
            "Logout",
            use_container_width=True,
        ):
            logout()


    else:
        if st.sidebar.button(
            "Sign in",
            use_container_width=True,
        ):
            st.session_state.page = "signin"
            st.rerun()


        if st.sidebar.button(
            "Sign up",
            use_container_width=True,
        ):
            st.session_state.page = "signup"
            st.rerun()



def setup_session():
    if "page" not in st.session_state:
        st.session_state.page = "home"

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "user_id" not in st.session_state:
        st.session_state.user_id = None

    if "username" not in st.session_state:
        st.session_state.username = None



def logout():
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = None
    st.session_state.page = "home"

    st.rerun()






setup_session()
show_sidebar()


page = st.session_state.page

if page == "signin":
    show_signin()

elif page == "signup":
    show_signup()

elif page == "create":
    show_create()

elif page == "profile":
    show_profile()


else:
    show_home()

