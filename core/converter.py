from core.image_processor import preprocess
from core.ocr_engine import extract_text
from core.ppt_builder import build_ppt


def convert_image(image):

    processed = preprocess(image)

    text = extract_text(processed)

    ppt = build_ppt(image,text)

    return ppt
