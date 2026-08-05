import streamlit as st
import requests

st.set_page_config(
    page_title="ChainPay Login"
)

tab1, tab2 = st.tabs(
    ["Login", "Register"]
)

with tab1:

    st.subheader("Login")

    login_email = st.text_input(
        "Email",
        key="login_email"
    )

    login_password = st.text_input(
        "Password",
        type="password",
        key="login_password"
    )

    if st.button("Login"):

        response = requests.post(
            "http://localhost:8000/auth/login",
            json={
                "email": login_email,
                "password": login_password
            }
        )

        if response.status_code == 200:

            data = response.json()

            st.session_state.logged_in = True

            st.session_state.user = (
                data["company_name"]
            )

            st.session_state.token = (
                data["access_token"]
            )

            st.success(
                "Login Success"
            )

            st.rerun()

        else:
            st.error(
                "Invalid Credentials"
            )

with tab2:

    st.subheader("Register")

    company = st.text_input(
        "Company Name"
    )

    reg_email = st.text_input(
        "Email"
    )

    reg_password = st.text_input(
        "Password",
        type="password"
    )

    if st.button("Register"):

        response = requests.post(
            "http://localhost:8000/auth/register",
            json={
                "company_name": company,
                "email": reg_email,
                "password": reg_password
            }
        )

        if response.status_code == 200:

            st.success(
                "Registration Successful"
            )

        else:

            st.error(
                response.json()["detail"]
            )