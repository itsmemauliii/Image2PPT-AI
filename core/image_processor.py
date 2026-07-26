import cv2
import numpy as np

def preprocess(image):

    img=np.array(image)

    gray=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)

    gray=cv2.GaussianBlur(gray,(3,3),0)

    return gray
