# ChainPay

ChainPay style blockchain payment gateway.ChainPay is a blockchain-based payment platform that collects payment requests through Streamlit, processes them using FastAPI, executes secure transactions via Solidity smart contracts, stores transaction records in a database, and provides insights through an analytics dashboard. It offers secure, transparent, automated, and efficient payment processing while ensuring reliable record management and real-time monitoring.

## Install

pip install -r requirements.txt

## Run

uvicorn app.main:app --reload



## Dashboard

streamlit run dashboard/streamlit_app.py
