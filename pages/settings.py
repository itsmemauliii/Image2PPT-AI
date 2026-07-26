import streamlit as st

st.title("Settings")

st.checkbox("Preserve Colours",True)

st.checkbox("Preserve Fonts",True)

st.checkbox("Detect Shapes",True)

st.checkbox("Enhance Image",True)

st.selectbox(
    "Slide Size",
    [
        "16:9",
        "4:3"
    ]
)
