import cv2
import matplotlib.pyplot as plt
img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./images/dog.bmp', cv2.IMREAD_COLOR)
img_color = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
# RGB로 변환하지 않으면 색상이 이상하게 나옴
# RGB -> BGR 순서로 저장되기 때문
plt.subplot(121)
plt.axis('off')
plt.imshow(img_gray, cmap='gray')
plt.subplot(122)
plt.axis('off')
plt.imshow(img_color)
plt.show()
cv2.imshow('Gray Image', img_gray)
cv2.imshow('Color Image', img2)
cv2.waitKey(0) # 창 안 닫히게