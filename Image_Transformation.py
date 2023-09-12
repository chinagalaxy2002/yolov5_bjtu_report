import cv2
filename='Baidu_0001.jpeg'

img=cv2.imread(filename,1)

b,g,r=cv2.split(img)

cv2.namedWindow("Baidu_0001.jpeg",0)

merged=cv2.merge([r,g,b])

flip0=cv2.flip(img,0)
flip1=cv2.flip(img,1)
flip2=cv2.flip(img,-1)

cv2.imshow("flip0",flip0)
cv2.imshow("flip1",flip1)
cv2.imshow("flip2",flip2)

cv2.imwrite('Baidu_0001_change1.jpeg',flip0)
cv2.imwrite('Baidu_0001_change2.jpeg',flip1)

cv2.imwrite('Baidu_0001_change3.jpeg',flip2)

cv2.waitKey(0)
