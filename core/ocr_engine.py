from paddleocr import PaddleOCR

ocr=PaddleOCR(
    use_angle_cls=True,
    lang="en"
)

def extract_text(image):

    result=ocr.ocr(image)

    output=[]

    for line in result[0]:

        output.append({

            "text":line[1][0],

            "box":line[0]

        })

    return output
