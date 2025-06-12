import streamlit as st
from saving_account import SavingsAccount

st.set_page_config(page_title = "Savings Account", layout ="centered")

savings = SavingsAccount(20000)

with st.form("savings_form"):
    amount = st.number_input("Enter Amount")
    operations = st.sidebar("Deposit or withdraw")
    submit = st.form_submit_button("Submit")

if submit and operations == "withdraw":
    with  st.spinner("processing..."):
        savings.withdraw(amount)
        print(savings.balance)


