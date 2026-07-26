from core.image_processor import preprocess
from core.ocr_engine import detect_text
from core.layout_detector import detect_layout
from core.ppt_builder import build_ppt

def convert(image):

    processed=preprocess(image)

    text=detect_text(processed)

    layout=detect_layout(processed)

    ppt=build_ppt(image,text,layout)

    return ppt
