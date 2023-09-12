"'import time
import os
import cv2
import sys

#want to open a video in Pc,use below
capin = cv2.VideoCapture(sys.argv[1])

#want to open a camera in Pc,use below
#capin = cv2.VideoCapture(0)

fps = int(capin.get(cv2.CAP_PROP_FPS))


if capin.isOpened():
    width = capin.get(cv2.CAP_PROP_FRAME_WIDTH)
    height = capin.get(cv2.CAP_PROP_FRAME_HEIGHT)
    print("The video's content is: "+str(width)+" * "+str(height))
'''
cv2.namedWindow("1",0)
while True:
    t1 = time.time()
    flag,frame = capin.read()
    if flag == False:
        break
    cv2.imshow("1",frame)
    k = cv2.waitKey(10)
    if k == ord('q'):
        break
'''

#write
neww = 426
newh = int(neww*float(height)/float(width))
videoout = cv2.VideoWriter(sys.argv[2],cv2.VideoWriter_fourcc('M','P','4','V'),fps,(neww,newh))
while True:
    t1 = time.time()
    ret, frame = capin.read()
    if ret == False:
        break

    newframe = cv2.resize(frame,(neww,newh))
    videoout.write(newframe)

capin.release()
cv2.destroyAllWindows()




    

