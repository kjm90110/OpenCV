import cv2
import numpy as np

oldx = oldy = 0

def on_mouse(event, x, y, flags, param):
    global oldx, oldy
    print("x: ", x, "y:", y)
    print('flags:', flags)

    if event == cv2.EVENT_LBUTTONDBLCLK: # 좌클릭
        print('마우스 왼쪽 버튼 클릭')
        oldx, oldy = x, y
    elif event == cv2.EVENT_LBUTTONUP:
        print('마우스 왼쪽 버튼이 떼짐')
    elif event == cv2.EVENT_MOUSEMOVE:
        print('마우스 이동 중')
        if flags:
            print('드래그 중')
            cv2.line(img, (oldx, oldy), (x, y), (255, 51, 255), 3)
            cv2.imshow('img', img)
            oldx, oldy = x, y



img = np.ones((500, 500, 3), dtype=np.uint8) * 255
cv2.rectangle(img, (50, 200, 150, 100), (0, 255, 0), 3) # x축 시작점, y축 시작점, w, h / 3: 두께
cv2.rectangle(img, (300, 200, 150, 100), (255, 0, 0), -1) # -1을 주면 배경색을 칠함
cv2.circle(img, (150, 400), 50, (255, 255, 0), 3)
cv2.putText(img, '2026', (50, 200), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 0, 0)) # 0.7: 원래 글자 크기의 70%


cv2.imshow('img', img)

cv2.setMouseCallback('img', on_mouse)

cv2.waitKey()