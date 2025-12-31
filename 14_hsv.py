import cv2

img = cv2.imread('./images/candies.png')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# HSV
# 색을 표현하는 한 방식. 이미지 처리와 색상 추출에 매우 자주 사용됨
# H: 색상을 숫자로 높낮이에 따라서 표현 
# S: 채도(색의 선명도)
# V: 명도(밝기)

'''
색상 H 값 (OpenCV 기준)     
빨강 (Red) 0 또는 179   
주황 (Orange) 10~20   
노랑 (Yellow) 20~30   
초록 (Green) 40~85   
파랑 (Blue) 90~130   
보라 (Violet) 130~160

채도: 150 ~ 255
명도: 0 ~ 255
'''

dst = cv2.inRange(hsv, (90, 150, 0), (130, 255, 255))

airplane = cv2.imread('./images/airplane.bmp')
# mask: 원래 추출하고자 하는 오브젝트(ROI)에 대하여 흰색 또는 검정색으로 표현하고 배경색을 반전시키는 것
mask = cv2.imread('./images/mask_plane.bmp')
field = cv2.imread('./images/field.bmp')

# copyTo: 마스크를 이용한 선택적 복사
temp = cv2.copyTo(airplane, mask) # mask에 있는 ROI를 떼서 temp에 할당
cv2.copyTo(airplane, mask, field) # airplane의 mask를 떼서 field에 붙여라

cv2.imshow('img', img)
cv2.imshow('dst', dst)
cv2.imshow('field', field)

cv2.waitKey()
