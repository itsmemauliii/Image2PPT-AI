import streamlit as st
from PIL import Image
import os

from core.ocr import extract_text
from core.ppt_generator import create_ppt

st.set_page_config(
    page_title="Image2PPT AI",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Image2PPT AI")
st.caption("Convert images into editable PowerPoint slides")

uploaded = st.file_uploader(
    "Upload Image",
    type=["png","jpg","jpeg"]
)

if uploaded:

    image = Image.open(uploaded)

    st.image(image,use_container_width=True)

    if st.button("Generate PowerPoint"):

        with st.spinner("Reading image..."):

            text_blocks = extract_text(image)

            output_path = create_ppt(image,text_blocks)

        with open(output_path,"rb") as f:

            st.download_button(
                "Download PPT",
                f,
                file_name="presentation.pptx"
            )
