import cv2
import matplotlib.pyplot as plt

man = cv2.imread('./images/man.jpg')
turkey = cv2.imread('./images/turkey.jpg')

# 그냥 덧셈을 할 경우 0 ~ 255 값을 벗어나면
#  256으로 나눈 나머지가 되어버려서 픽셀이 깨짐
dst1 = man + turkey

# 0 ~ 255를 벗어나도 0 또는 255 값으로 보정
dst2 = cv2.add(man, turkey)

img = {'man':man, 'turkey':turkey, 'dst1':dst1, 'dst2':dst2}

for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 2, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()