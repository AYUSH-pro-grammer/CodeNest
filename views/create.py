import streamlit as st




def show_create():
    if not st.session_state.logged_in:
        st.warning("Sign in to create a coding question.")
        return

    st.title("Create question")

    st.write(
        "The question creation form will be added later."
    )


