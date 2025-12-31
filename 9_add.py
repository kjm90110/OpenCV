import cv2

img1 = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./images/dog.bmp')

dst1_add = cv2.add(img1, 100)
dst2_add = cv2.add(img2, (100, 100, 100))
dst3_subtract = cv2.subtract(img1, 100)
dst4_multiply= cv2.multiply(img1, 10)
dst5_divide = cv2.divide(img1, 10)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1_add)
cv2.imshow('dst2', dst2_add)
cv2.imshow('dst3', dst3_subtract)
cv2.imshow('dst3', dst4_multiply)
cv2.imshow('dst3', dst5_divide)

cv2.waitKey()