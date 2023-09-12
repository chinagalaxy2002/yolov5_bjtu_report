import cv2

filename = 'Baidu_0001.jpeg'
img = cv2.imread(filename)
img = cv2.resize(img,(180,120))
cv2.imwrite('Baidu_0001_small.jpeg',img)
cv2.namedWindow("Baidu_0001",0)
cv2.imshow("Baidu_0001",img)
height,width,channel = img.shape
print('size == ', img.shape)

cv2.waitKey(0)

