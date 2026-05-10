import streamlit as st
import requests

API_URL = "http://localhost:8000/chat"

st.title("🏦 Banking AI Support Agent")

session_id = st.text_input(
    "Session ID",
    value="user123"
)

message = st.text_area(
    "Enter Message"
)

if st.button("Send"):

    response = requests.post(
        API_URL,
        json={
            "session_id": session_id,
            "message": message
        }
    )

    data = response.json()

    st.write("### Classification")
    st.write(data["category"])

    st.write("### Response")
    st.write(data["response"])