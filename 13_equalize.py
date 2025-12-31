import cv2
import matplotlib.pyplot as plt


img1 = cv2.imread('./images/Hawkes.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('./images/field.bmp')

# 히스토그램 평활화
# 이미지의 전체 밝기 분포를 고르게 퍼뜨려 명암 대비를 향상
dst1 = cv2.equalizeHist(img1)

# YCrCb
# Y: 밝기(명도), Cr: 빨강 계열 색상 정보, Cb: 파랑 계열 색상 정보
dst2 = cv2.cvtColor(img2, cv2.COLOR_BGR2YCrCb)
dst2[:, :, 0] = cv2.equalizeHist(dst2[:, :, 0])
dst2 = cv2.cvtColor(dst2, cv2.COLOR_YCrCb2BGR)

# normalize: 정규화
# img1: 원본 이미지, None: 출력
# None: 배열(None이면 새로 생성)
# 0: 정규화 후 최소값
# 255: 정규화 후 최대값
# cv2.NORM_MINMAX: 정규화 방식
dst3 = cv2.normalize(img1, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)


hist1 = cv2.calcHist([img1], [0], None, [256], [0, 255])
hist2 = cv2.calcHist([dst1], [0], None, [256], [0, 255])
hist3 = cv2.calcHist([dst2], [0], None, [256], [0, 255])
hist4 = cv2.calcHist([dst3], [0], None, [256], [0, 255])


hists = {'hist1': hist1, 'hist2': hist2, 'hist3': hist3, 'hist4': hist4}

plt.figure(figsize=(15, 8))
for i, (k, v) in enumerate(hists.items()):
    plt.subplot(2, 2, i+1)
    plt.title(k)
    plt.plot(v)
plt.show()