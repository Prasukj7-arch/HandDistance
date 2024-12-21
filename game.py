import cv2
from cvzone.HandTrackingModule import HandDetector
import math
import numpy as np
import cvzone
import random
import time
import pygame  # Import pygame for music

# Initialize pygame mixer
pygame.mixer.init()

# Load music and sound effects
pygame.mixer.music.load("background.mp3")
pygame.mixer.music.play(-1)
hit_sound = pygame.mixer.Sound("hit_sound.wav")  # Replace with your hit sound effect file

# Webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

# HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Polynomial coefficients for distance calibration
x = [300, 245, 200, 170, 145, 130, 112, 103, 93, 87, 80, 75, 70, 67, 62, 59, 57]
y = [20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100]
coff = np.polyfit(x, y, 2)  # y = Ax^2 + Bx + C

# Game variables
cx, cy = (250, 250)
color = (255, 0, 255)
counter = 0
score = 0
timeStart = time.time()
totalTime = 20

# Game loop
while True:
    success, img = cap.read()
    hands, img = detector.findHands(img, draw=False)

    if time.time() - timeStart < totalTime:
        if hands:
            lmList = hands[0]['lmList']
            x, y, w, h = hands[0]['bbox']
            x1, y1, _ = lmList[5]
            x2, y2, _ = lmList[17]

            distance = int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))
            A, B, C = coff
            distanceCM = A * distance ** 2 + B * distance + C

            if distanceCM < 40:
                if x < cx < x + w and y < cy < y + h:
                    counter = 1

            cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 255), 3)
            cvzone.putTextRect(img, f'{int(distanceCM)} cm', (x + 5, y - 10))

        if counter:
            counter += 1
            color = (0, 255, 0)
            if counter == 3:
                cx = random.randint(100, 1100)
                cy = random.randint(100, 600)
                color = (255, 0, 255)
                score += 1
                counter = 0
                hit_sound.play()  # Play hit sound

        # Draw target
        cv2.circle(img, (cx, cy), 30, color, cv2.FILLED)
        cv2.circle(img, (cx, cy), 10, (255, 255, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 20, (255, 255, 255), 2)
        cv2.circle(img, (cx, cy), 30, (50, 50, 50), 2)

        # Game HUD
        cvzone.putTextRect(img, f'Time: {int(totalTime - (time.time() - timeStart))}', (1000, 75), scale=3, offset=20)
        cvzone.putTextRect(img, f'Score: {str(score).zfill(2)}', (60, 75), scale=3, offset=20)

    else:
        cvzone.putTextRect(img, 'Game Over', (400, 400), scale=5, offset=30, thickness=7)
        cvzone.putTextRect(img, f'Your Score: {score}', (450, 500), scale=3, offset=20, thickness=7)
        cvzone.putTextRect(img, 'Press R to restart', (460, 575), scale=2, offset=10)

    cv2.imshow("Image", img)
    key = cv2.waitKey(1)

    if key == ord('r'):
        timeStart = time.time()
        score = 0

pygame.mixer.quit()

# We see that the hand remains at the same position but the distance between the coordinates will change despite , which shall not happen
# Thus instead of finding x value , we shall find the diagonal value
# We want to convert distance values in cm , but another problem we face is to find the polynomial function that can accurately provide us with a cm value for the distance [linear]
# the accuracy varies on number of camera , also on the size of the hands for which we can add a multiplier or make a separate function for each.
# We need to delay a little so that a person can see the change in colour , for 1 to 2 iterations we keep the colour same. Delay a little and then change the location
# Not delay with time , but use counter on basis of how many frames have passed by.
