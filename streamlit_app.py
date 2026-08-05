import streamlit as st
import requests
import pandas as pd
import hashlib
from datetime import datetime

# ==================================
# CONFIG
# ==================================

API_URL = "http://127.0.0.1:8000"

st.set_page_config(
    page_title="ChainPay",
    page_icon="⛓️",
    layout="wide"
)

# ==================================
# SESSION STATE
# ==================================

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "user" not in st.session_state:
    st.session_state.user = None

if "token" not in st.session_state:
    st.session_state.token = None

if "transactions" not in st.session_state:
    st.session_state.transactions = []

if "ledger" not in st.session_state:
    st.session_state.ledger = [
        {
            "index": 0,
            "hash": "GENESIS_BLOCK",
            "previous_hash": "NONE"
        }
    ]

# ==================================
# LOGIN / REGISTER PAGE
# ==================================

if not st.session_state.logged_in:

    st.title("⛓️ ChainPay")
    st.subheader("Blockchain Payment System")

    login_tab, register_tab = st.tabs(
        ["Login", "Register"]
    )

    # LOGIN

    with login_tab:

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

            try:

                response = requests.post(
                    f"{API_URL}/auth/login",
                    json={
                        "email": login_email,
                        "password": login_password
                    }
                )

                if response.status_code == 200:

                    data = response.json()

                    st.session_state.logged_in = True
                    st.session_state.user = data["user"]
                    st.session_state.token = data["token"]

                    st.success(
                        "Login Successful"
                    )

                    st.rerun()

                else:

                    st.error(
                        "Invalid Email or Password"
                    )

            except Exception as e:

                st.error(
                    f"Backend Error: {e}"
                )

    # REGISTER

    with register_tab:

        register_email = st.text_input(
            "Email Address",
            key="register_email"
        )

        register_password = st.text_input(
            "Password",
            type="password",
            key="register_password"
        )

        confirm_password = st.text_input(
            "Confirm Password",
            type="password",
            key="confirm_password"
        )

        if st.button("Register"):

            if register_password != confirm_password:

                st.error(
                    "Passwords do not match"
                )

            else:

                try:

                    response = requests.post(
                        f"{API_URL}/auth/register",
                        json={
                            "email": register_email,
                            "password": register_password
                        }
                    )

                    if response.status_code == 200:

                        st.success(
                            "Account created successfully"
                        )

                    else:

                        st.error(
                            response.json()["detail"]
                        )

                except Exception as e:

                    st.error(
                        f"Backend Error: {e}"
                    )

    st.stop()

# ==================================
# SIDEBAR
# ==================================

st.sidebar.title("⛓️ ChainPay")

st.sidebar.write(
    f"👤 {st.session_state.user}"
)

if st.sidebar.button("Logout"):

    st.session_state.clear()
    st.rerun()

# ==================================
# HEADER
# ==================================

st.title("⛓ Blockchain Payment Gateway")

st.success(
    f"Welcome {st.session_state.user}"
)

# ==================================
# WALLET
# ==================================

col1, col2 = st.columns(2)

with col1:

    st.info(
        """
Wallet Address

0x71f3be9c7fd3aa743210ab34c56
"""
    )

with col2:

    st.metric(
        "Wallet Balance",
        "$12,845.22",
        "+4.5%"
    )

st.divider()

# ==================================
# SEND PAYMENT
# ==================================

st.subheader("💸 Send Payment")

with st.form("send_payment"):

    receiver = st.text_input(
        "Receiver Name / Wallet"
    )

    amount = st.number_input(
        "Amount",
        min_value=0.0
    )

    currency = st.selectbox(
        "Currency",
        [
            "ETH",
            "BTC",
            "USDT"
        ]
    )

    submit = st.form_submit_button(
        "Send Payment"
    )

    if submit:

        tx_string = (
            f"{st.session_state.user}"
            f"{receiver}"
            f"{amount}"
            f"{currency}"
            f"{datetime.now()}"
        )

        tx_hash = hashlib.sha256(
            tx_string.encode()
        ).hexdigest()

        st.session_state.transactions.append(
            {
                "Sender": st.session_state.user,
                "Receiver": receiver,
                "Amount": f"{amount} {currency}",
                "Status": "Completed",
                "Hash": tx_hash[:18]
            }
        )

        previous_hash = (
            st.session_state.ledger[-1]["hash"]
        )

        st.session_state.ledger.append(
            {
                "index": len(
                    st.session_state.ledger
                ),
                "hash": tx_hash,
                "previous_hash": previous_hash
            }
        )

        st.success(
            f"""
Payment Submitted

Receiver: {receiver}

Amount: {amount} {currency}
"""
        )

st.divider()

# ==================================
# TRANSACTION HISTORY
# ==================================

st.subheader("📜 Transaction History")

if st.session_state.transactions:

    tx_df = pd.DataFrame(
        st.session_state.transactions
    )

    st.dataframe(
        tx_df,
        use_container_width=True
    )

else:

    st.info(
        "No transactions available."
    )

st.divider()

# ==================================
# BLOCKCHAIN LEDGER
# ==================================

st.subheader("🔗 Blockchain Ledger")

for block in reversed(
    st.session_state.ledger
):

    st.info(
        f"""
Block #{block['index']}

Hash:
{block['hash'][:35]}...

Previous Hash:
{block['previous_hash'][:35]}...
"""
    )

st.divider()

st.caption(
    "ChainPay • Blockchain Payment Gateway"
)