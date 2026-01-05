import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('./images/dog.bmp')

# 이동을 수행하는 affine 행렬

# [ a  b  tx ]
# [ c  d  ty ]
#
# x' = a*x + b*y + tx
# y' = c*x + d*y + ty
#
# a=1, d=1 → 크기 변화 없음
# b=0, c=0 → 회전/기울임 없음
# tx=150   → x축으로 +150 픽셀 이동 (오른쪽)
# ty=100   → y축으로 +100 픽셀 이동 (아래)

aff = np.array([
    [1, 0, 150],
    [0, 1, 100]
], dtype=np.float32)

# cv2.warpAffine(원본, 변환행렬, 출력이미지크기)
dst1 = cv2.warpAffine(img, aff, (0, 0))

# interploation(보간법): 픽셀을 어떻게 채울지 결정
# INTER_NEAREST: 최근법 이웃(속도 빠름. 품질 낮음), 계단 현상이나 노이즈가 생길 수 있음
# INTER_CUBIC: 4차 보간법(속도 느림, 품질 좋음), 주변 16개 픽셀을 사용하여 곡선으로 예측,
#               이미지를 부드럽게 확대/축소
dst2 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_NEAREST)
dst3 = cv2.resize(img, (1280, 1024), interpolation=cv2.INTER_CUBIC)

# 가운데 지점
cp = (img.shape[1] / 2, img.shape[0] / 2)
rot = cv2.getRotationMatrix2D(cp, 30, 0.7)
dst4 = cv2.warpAffine(img, rot, (0, 0))

cv2.imshow('img', img)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.imshow('dst3', dst3)
cv2.imshow('dst4', dst4)
cv2.waitKey()