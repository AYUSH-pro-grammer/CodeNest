import streamlit as st




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


