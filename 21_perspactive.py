import cv2
import numpy as np


# 투시 변환(Perspective Transform)
# 영상에서 원근감을 조절하거나, 사각형을 반듯하게 펴주는 변환
img = cv2.imread('./images/pic.jpg')

srcQuad = np.array([
    [370, 175],
    [1230, 160],
    [1420, 850],
    [210, 850]
], np.float32)

dstQuad = np.array([
    [0, 0],
    [600, 0],
    [600, 400],
    [0, 400]
], np.float32)

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad) 
dst = cv2.warpPerspective(img, pers, (600, 400))

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.waitKey()