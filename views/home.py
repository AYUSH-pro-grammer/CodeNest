import streamlit as st


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

