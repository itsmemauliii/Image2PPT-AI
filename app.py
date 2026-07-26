import streamlit as st

st.set_page_config(
    page_title="Image2PPT AI",
    page_icon="📊",
    layout="wide"
)

home = st.Page("pages/upload.py", title="Upload", icon="📤")
history = st.Page("pages/history.py", title="History", icon="🕘")
settings = st.Page("pages/settings.py", title="Settings", icon="⚙️")

pg = st.navigation([home, history, settings])

pg.run()
