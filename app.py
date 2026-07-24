import streamlit as st


st.set_page_config(
    page_title="CodeNest",
    page_icon="CodeNest",
    layout="wide",
)


def show_sidebar():
    st.sidebar.title("CodeNest")


    if st.sidebar.button(
        "Home",
        use_container_width=True,
    ):
        st.session_state.page = "home"
        st.rerun()


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




def show_home():
    st.title("CodeNest")

    st.write(
        "Solve coding problems, test your code and create "
        "your own programming challenges."
    )

    st.subheader("Public questions")

    st.info("Coding questions will appear here soon.")


def show_signin():
    st.title("Sign in")

    st.write(
        "Sign in to solve questions and track your progress."
    )

    email = st.text_input(
        "Email",
        placeholder="you@example.com",
    )

    password = st.text_input(
        "Password",
        type="password",
    )


    if st.button(
        "Sign in",
        use_container_width=True,
    ):
        st.info(
            "The login system will be connected later."
        )


def show_signup():
    st.title("Create account")

    st.write(
        "Create an account to join CodeNest."
    )

    username = st.text_input(
        "Username",
        placeholder="your username",
    )

    email = st.text_input(
        "Email",
        placeholder="you@example.com",
    )


    password = st.text_input(
        "Password",
        type="password",
    )

    confirm_password = st.text_input(
        "Confirm password",
        type="password",
    )

    if st.button(
        "Create account",
        use_container_width=True,
    ):
        st.info(
            "The signup system will be connected later."
        )


setup_session()
show_sidebar()


page = st.session_state.page

if page == "signin":
    show_signin()

elif page == "signup":
    show_signup()

else:
    show_home()

