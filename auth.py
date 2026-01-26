import streamlit as st

# Simple users database (you can change usernames/passwords)
users = {
    "student": "stu123",
    "priya": "priya123"
}

def login():
    st.title("Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in users and users[username] == password:
            st.session_state["logged_in"] = True
            st.success("Login successful")
            st.rerun()
        else:
            st.error("Invalid username or password")


def logout():
    st.session_state["logged_in"] = False
    st.rerun()
