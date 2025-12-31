import cv2
import numpy as np

img_gray = cv2.imread('./images/dog.bmp', cv2.IMREAD_GRAYSCALE)

print('img_gray type: ', type(img_gray)) # <class 'numpy.ndarray'>
print('img_gray shape:', img_gray.shape) # (364, 548) 가로, 세로
print('img_gray dtype:', img_gray.dtype) # uint8


img_color = cv2.imread('./images/dog.bmp')
print('img_color type: ', type(img_color)) # <class 'numpy.ndarray'>
print('img_color shape:', img_color.shape) # (364, 548, 3) 가로, 세로, 채널
print('img_color dtype:', img_color.dtype) # uint8

h, w = img_color.shape[:2]
print(f'이미지 사이즈: {w} * {h}')

if len(img_gray.shape) == 3:
    print('컬러 영상')
elif len(img_gray.shape) == 2:
    print('흑백 영상')

img1 = np.zeros((240, 320, 3), dtype=np.uint8)
img2 = np.empty((240, 320), dtype=np.uint8) # empty: 아무 값이나 넣어줌
img3 = np.ones((240, 320), dtype=np.uint8) * 120
img4 = np.full((240, 320, 3), (255, 102, 255), dtype=np.uint8)

img2 = cv2.cvtColor(img2, cv2.COLOR_GRAY2BGR)
h, w = img2.shape[:2]

# height만큼 반복
# for x in range(h):
#     for y in range(w):
#         # img2[x, y] = img2[x][y]
#         img2[x, y] = (255, 102, 255)

img2[:, :] = (255, 102, 255) # 한 줄로 끝남

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('img3', img3)
cv2.imshow('img4', img4)

cv2.imshow('img_gray', img_gray)
cv2.imshow('img_color', img_color)


# keyboard event
while True:
    keyvalue = cv2.waitKey()
    print(keyvalue)
    if keyvalue == 27: # esc
        break
    elif keyvalue == ord('i') or keyvalue == ord('I'):
        img_color = ~img_color # 값 반전
        cv2.imshow('img_color', img_color)