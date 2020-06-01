import numpy as np
import cv2

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
# Load an color image in grayscale
file_path = "rtsp://203.178.139.239:8080/h264_ulaw.sdp"

while True:
    cam = cv2.VideoCapture(file_path)
    # img = cv2.imread('/home/h-kz/Pictures/PK2019112402100117_size0.jpg',1)
    ret, img = cam.read()
    print(img)

    cv2.imshow('image',img)
    cv2.waitKey(100)
cv2.destroyAllWindows()