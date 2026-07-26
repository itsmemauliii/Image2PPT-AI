import streamlit as st
import os

st.title("History")

folder="output"

if os.path.exists(folder):

    files=os.listdir(folder)

    if len(files)==0:

        st.info("No presentations yet.")

    for file in files:

        st.write(file)
