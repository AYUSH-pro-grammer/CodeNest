import streamlit as st

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

