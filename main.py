import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)

# HandDetector [80% of detection is required for it a hand to be detected]
detector = HandDetector(detectionCon=0.8,maxHands=1)

# Find Function
# Distances in pixels (example)
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
# Corresponding distances in centimeters (example)
y = [20, 25, 30, 35, 40,45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x,y,2)  # y = Ax2 + Bx + C

# Loop
while True:
    success , img = cap.read()
    hands , img = detector.findHands(img, draw=False)

    if hands:
        lmList = hands[0]['lmList']
        x, y, w, h = hands[0]['bbox']
        # 5,17 values can be found at website of mediapipe
        x1, y1 , _ = lmList[5]
        x2, y2 , _ = lmList[17]

        distance = int(math.sqrt((x2-x1)**2 + (y2-y1)**2))
        A,B,C = coff
        distanceCM = A*distance**2 + B*distance + C

        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,255),3)
        cvzone.putTextRect(img,f'{int(distanceCM)} cm',(x+5,y-10))


    cv2.imshow("Image",img)
    cv2.waitKey(1)

# We see that the hand remains at the same position but the distance between the coordinates will change despite , which shall not happen
# Thus instead of finding x value , we shall find the diagonal value
# We want to convert distance values in cm , but another problem we face is to find the polynomial function that can accurately provide us with a cm value for the distance [linear]
# the accuracy varies on number of camera , also on the size of the hands for which we can add a multiplier or make a separate function for each