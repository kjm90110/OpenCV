import cv2
import matplotlib.pyplot as plt

# 이진화: 영상을 흑백(0 또는 255)으로 변환하여 특정 임계값 이상인 픽셀을 흰색으로, 
#           이하인 픽셀을 검은색으로 변환

# 객체 검출, OCR(광학 문자 인식), 엣지 검출 등의 전처리 과정에서 매우 중요한 역할

# 오츠 이진화: OpenCV에서 제공하는 자동 임계값 결정 기법.
#             영상의 히스토그램을 분석하여 객체와 배경을 
#             가장 잘 구분할 수 있는 최적의 임계값을 찾음 


img = cv2.imread('./images/cells.png', cv2.IMREAD_GRAYSCALE)
hist = cv2.calcHist([img], [0], None, [256], [0, 255])

# 픽셀값이 임계값(100)을 넘으면 최대값(255)으로 설정하고 넘지 못하면 0으로 설정
a, dst1 = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

b, dst2 = cv2.threshold(img, 210, 255, cv2.THRESH_BINARY)
c, dst3 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# threshold값
print(a, b, c) # 100.0 210.0

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)

plt.plot(hist)
plt.show()
cv2.waitKey()