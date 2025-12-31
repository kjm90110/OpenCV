import cv2
import sys

cap = cv2.VideoCapture('./movies/movie.mp4')

if not cap.isOpened():
    print('동영상을 불러올 수 없음')
    sys.exit()

print('동영상을 불러올 수 있음')

# 객체 안에 들어있는 width, height 가져오기
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH) 
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
print(width) 
print(height) 

frame_count = cap.get(cv2.CAP_PROP_FRAME_COUNT)
print(frame_count) # 291.0 

# 1초 동안 몇 개의 프레임이 쓰였나
fps = cap.get(cv2.CAP_PROP_FPS)
print(fps) # 30.0 (30개!)

while True:
    # read: 제일 처음부터 프레임 한 장을 읽어옴
    ret, frame = cap.read() # ret: 제대로 읽어왔는지에 대한 bool data
    # frame: 동영상 제일 처음 순간(이미지)를 nbarray로 읽어옴
    if not ret:
        break

    cv2.imshow('frame', frame)
    if cv2.waitKey(10) == 27: # esc를 누를 때까지 인자로 준 시간 동안 기다림
        break 

cap.release() # 자원 반납
