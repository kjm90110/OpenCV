# ROI(Region Of Interest): 관심 영역
import cv2

img = cv2.imread('./images/sun.jpg')

x = 183
y = 25
w = 120
h = 110

roi = img[y:y+h, x:x+w]
roi = roi.copy()

img[y:y+h, x+w:x+w+w] = roi

cv2.rectangle(img, (x, y), (x+w+w, y+h), (0, 255, 0), 3)

cv2.imshow("img", img)
cv2.imshow("roi", roi)
cv2.waitKey()
