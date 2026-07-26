import cv2
import numpy as np

def preprocess(image):

    img=np.array(image)

    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    gray=cv2.GaussianBlur(gray,(3,3),0)

    thresh=cv2.adaptiveThreshold(
        gray,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    return thresh
