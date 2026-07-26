from paddleocr import PaddleOCR
import numpy as np

ocr = PaddleOCR(use_angle_cls=True,lang="en")

def extract_text(image):

    image=np.array(image)

    result=ocr.ocr(image)

    blocks=[]

    for line in result[0]:

        box=line[0]
        text=line[1][0]

        blocks.append({

            "text":text,

            "box":box

        })

    return blocks
