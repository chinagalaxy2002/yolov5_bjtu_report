import cv2

filename = 'Baidu_0001.jpeg'

img = cv2.imread(filename,1)



img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

cv2.imwrite('Baidu_0001_small_grey.jpeg',img)
cv2.namedWindow("Baidu_0001",0)
cv2.imshow("Baidu_0001",img)

print('size == ', img.shape)

cv2.waitKey(0)

