import cv2
import matplotlib.pyplot as plt

dog = cv2.imread('./images/dog.jpg')
square = cv2.imread('./images/square.bmp')

dst1 = cv2.add(dog, square)

# 가중치 합성: 두 이미지를 비율로 섞음
dst2 = cv2.addWeighted(dog, 0.5, square, 0.5, 0)
dst3 = cv2.subtract(dog, square)

# 절대 차이: 두 이미지 간의 절대 차이값 abs(dog(x, y) - square(x, y))
dst4 = cv2.absdiff(dog, square)

img = {'dog':dog, 'square': square, 'dst1':dst1, 'dst2':dst2, 'dst3':dst3, 'dst4':dst4}
for i, (k, v) in enumerate(img.items()):
    plt.subplot(2, 3, i+1)
    plt.imshow(v[:, :, ::-1])
    plt.title(k)
plt.show()