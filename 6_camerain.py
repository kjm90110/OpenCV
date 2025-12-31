import cv2
import sys

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('카메라를 열 수 없음')
    sys.exit()

print('카메라 연결 성공!')

width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width) 
print(height) 

fps = cap.get(cv2.CAP_PROP_FPS)
print(fps)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27:
        break

cap.release()