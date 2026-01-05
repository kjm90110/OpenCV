import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('./images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)

# 전역 자동 이진화
a, dst1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

# 지역 자동 이진화
dst2 = np.zeros(img.shape, np.uint8)
bw = img.shape[1] // 4
bh = img.shape[0] // 4  # 위아래 코드 해서 16등분

# 쪼갠 개수 만큼 돌면서 그 영역마다 각각 자동 이진화 시킴
for y in range(4):
    for x in range(4):
        img_ = img[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        dst_ = dst2[y*bh: (y+1)*bh, x*bw: (x+1)*bw]
        cv2.threshold(img_, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU, dst_)



# 적응형 이진화(Adaptive Thresholding): 
#   조명 변화가 심한 영상에서도 적절한 임계값을
#   적용하여 이진화를 수행하는 방법.
#   영상의 작은 영역마다 서로 다른 임계값을 계산해서

"""
9: 이웃 블록 크기. 현재 픽셀 주변에서 얼마 만큼의 영역을 고려할지 설정.
   클 수록 더 넓은 영역을 평균 -> 조명에 덜 민감하지만 부드러움

5: 임계값 보정 상수. 평균 또는 가중 평균에서 얼마나 빼줄지 결정. 클 수록
    픽셀이 어두워야 흰색이 됨(임계값을 낮추거나 높이기 위한 튜닝용 파라미터)
"""
# ADAPTIVE_THRESH_MEAN_C: 해당 픽셀 주변의 평균값을 기준으로 임계값 설정
dst3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, 
                             cv2.THRESH_BINARY, 9, 5)

# ADAPTIVE_THRESH_GAUSSIAN_C: 주변 픽셀에 가중치를 곱한 평균값을 기준으로 임계값 설정
dst4 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                             cv2.THRESH_BINARY, 9, 5)


# 이미지 묶기
images = {
    'Original': img,
    'OTSU': dst1,
    'OTSU_LOCAL': dst2,
    'Adaptive Thresholding - MEAN_C': dst3,
    'Adaptive Thresholding - GAUSSIAN_C': dst4
}

plt.figure(figsize=(6, 6))

for i, (title, image) in enumerate(images.items()):
    plt.subplot(3, 2, i + 1)
    plt.imshow(image, cmap='gray')
    plt.title(title)
    plt.axis('off')

plt.tight_layout()
plt.show()