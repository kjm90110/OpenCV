import cv2

cap = cv2.VideoCapture('./movies/woman.mp4')

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print('width:', w)
print('height:', h)
# width: 1280
# height: 720