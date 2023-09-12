import cv2

filename = 'Baidu_0001.jpeg'
img = cv2.imread(filename)
cv2.namedWindow("Baidu_0001.jpeg",0)
cv2.imshow("Baidu_0001.jpeg",img)
print('size == ', img.shape)
cv2.waitKey(0)

