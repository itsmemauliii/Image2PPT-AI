import streamlit as st
from PIL import Image
import os

from core.converter import convert_image

st.title("📊 Image2PPT AI")

st.write("Convert images into editable PowerPoint presentations.")

uploaded = st.file_uploader(
    "Upload Image",
    type=["png","jpg","jpeg"]
)

if uploaded:

    image = Image.open(uploaded)

    st.image(image,use_container_width=True)

    if st.button("Generate PPT"):

        with st.spinner("Processing..."):

            ppt = convert_image(image)

        with open(ppt,"rb") as f:

            st.download_button(
                "Download PPT",
                data=f,
                file_name="presentation.pptx"
            )
