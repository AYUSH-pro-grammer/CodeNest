import streamlit as st



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

