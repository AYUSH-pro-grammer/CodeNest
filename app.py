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



def show_create():
    if not st.session_state.logged_in:
        st.warning("Sign in to create a coding question.")
        return

    st.title("Create question")

    st.write(
        "The question creation form will be added later."
    )


def show_profile():
    if not st.session_state.logged_in:
        st.warning("Sign in to view your profile.")
        return

    st.title("Profile")

    st.write(f"Username: {st.session_state.username}")

    st.metric(
        "Points",
        0,
    )

    st.metric(
        "Questions solved",
        0,
    )



def logout():
    st.session_state.logged_in = False
    st.session_state.user_id = None
    st.session_state.username = None
    st.session_state.page = "home"

    st.rerun()


def show_home():
    st.title("CodeNest")

    if st.session_state.logged_in:
        st.write(
            f"Welcome back, {st.session_state.username}."
        )
    else:
        st.write(
            "Solve coding problems, test your code and create "
            "your own programming challenges."
        )


    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Public questions",
            0,
        )

    with col2:
        st.metric(
            "Users",
            0,
        )

    with col3:
        st.metric(
            "Submissions",
            0,
        )


    st.subheader("Public questions")

    st.info(
        "Coding questions will appear here soon."
    )




def show_signin():
    st.title("Sign in")

    st.write(
        "Sign in to solve questions and track "
        "your progress."
    )

    with st.form("signin_form"):
        email = st.text_input(
            "Email",
            placeholder="you@example.com",
        )


        password = st.text_input(
            "Password",
            type="password",
        )

        submitted = st.form_submit_button(
            "Sign in",
            use_container_width=True,
        )


    if submitted:
        email = email.strip().lower()

        if not email:
            st.error("Enter your email.")
            return

        if not password:
            st.error("Enter your password.")
            return


        st.session_state.logged_in = True
        st.session_state.user_id = "temporary-user"

        st.session_state.username = (
            email.split("@")[0]
        )

        st.session_state.page = "home"

        st.rerun()





def show_signup():
    st.title("Create account")

    st.write(
        "Create an account to join CodeNest."
    )

    with st.form("signup_form"):
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

        submitted = st.form_submit_button(
            "Create account",
            use_container_width=True,
        )


    if submitted:
        username = username.strip()
        email = email.strip().lower()

        if not username:
            st.error("Enter a username.")
            return

        if not email:
            st.error("Enter an email.")
            return


        if "@" not in email:
            st.error("Enter a valid email.")
            return

        if len(password) < 6:
            st.error(
                "Password must contain at least "
                "6 characters."
            )
            return


        if password != confirm_password:
            st.error("Passwords do not match.")
            return

        st.success("Account form is valid.")

        st.session_state.page = "signin"


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

