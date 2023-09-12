import cv2
filename='Baidu_0001.jpeg'

img=cv2.imread(filename,1)

cv2.namedWindow("Baidu_0001.jpeg",0)

b,g,r = cv2.split(img)

merged=cv2.merge([r,g,b])

height,width,channel=img.shape

img_cropped=img[0:560,0:560]

cv2.imshow("merged",img_cropped)

cv2.imwrite("Baidu_0001_cut.jpeg",img_cropped)

'''
flip0=cv2.flip(img,0)
flip1=cv2.flip(img,1)
flip2=cv2.flip(img,-1)

cv2.imwrite('Baidu_0001_change1.jpeg',flip0)
cv2.imwrite('Baidu_0001_change2.jpeg',flip1)
cv2.imwrite('Baidu_0001_change3.jpeg',flip2)
'''
cv2.waitKey(0)
