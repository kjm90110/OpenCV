import cv2

cap1 = cv2.VideoCapture('./movies/322220_tiny.mp4')
cap2 = cv2.VideoCapture('./movies/movie.mp4')

w = int(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))

# frame count, fps는 서로 다를 수 있기 때문에 따로따로 할당
frame_count1 = int(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_count2 = int(cap2.get(cv2.CAP_PROP_FRAME_COUNT))

fps1 = cap1.get(cv2.CAP_PROP_FPS)
fps2 = cap2.get(cv2.CAP_PROP_FPS)

print(w, h)
print(frame_count1, frame_count2)
print(fps1, fps2)

'''
    fourcc = FOUR Character Code

    'DIVX' = 비디오 압축 방식(코덱) 이름

    *'DIVX' → 'D','I','V','X' 로 쪼개서 전달
'''
fourcc = cv2.VideoWriter.fourcc(*'DIVX')

# 결과물을 저장
out = cv2.VideoWriter('./movies/mix.avi', fourcc, fps1, (w, h))

for i in range(frame_count1):
    
    ret, frame = cap1.read()
    
    cv2.imshow('output', frame)
    
    # 이미지 삽입
    out.write(frame)
    
    if cv2.waitKey(10) == 27:
        break


for i in range(frame_count2):

    ret, frame = cap2.read()
    
    cv2.imshow('output', frame)
    
    # 이미지 삽입
    out.write(frame)
    
    if cv2.waitKey(10) == 27:
        break