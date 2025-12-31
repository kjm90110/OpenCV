import cv2
import matplotlib.pyplot as plt

candies = cv2.imread('./images/candies.png', cv2.IMREAD_GRAYSCALE)

"""
    히스토그램이란..
    밝기(또는 색상) 값의 분포를 그래프로 표현
        -> 어떤 픽셀이 0(검정)인지 255(흰색)인지,
            각 값이 몇 개나 있는지 확인
"""
# [candies]: 대상 이미지 리스트
# [0]: 분석할 채널 번호. 만약 컬러라면 (B:0, G:1, R:2) 요런식으로 지정해 줘야 함.
# None: 분석할 영역의 마스크(None: 전체)
# [256]: 히스토그램의 빈 개수
# [0, 255]: 값의 범위
hist1 = cv2.calcHist([candies], [0], None, [256], [0, 255])

plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(hist1, color="gray")

# 컬러로
img2 = cv2.imread('./images/candies.png')
print('img2 shape:', img2.shape)

"""
    b = img2[:, :, 0]
    g = img2[:, :, 1]
    r = img2[:, :, 2]
"""

channels = cv2.split(img2) # B, G, R
# print(channels)

colors = ['b', 'g', 'r']

plt.subplot(1, 2, 2)

for channel, color in zip(channels, colors):
    hist2 = cv2.calcHist([channel], [0], None, [256], [0, 255])
    plt.plot(hist2, color=color, label=color.upper())

plt.show()