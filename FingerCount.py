import cv2
import time
import handtraking as ht

wcam, hcam = 640, 480
cap=cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)

ptime = 0

detector = ht.handTracker()

tipId = [4, 8, 12, 16, 20]

while True:
    success,img = cap.read()

    img = detector.findHands(img)
    lmList = detector.findLocation(img, draw=False)

    if len(lmList)!=0:
        fingers = []

        #Thumb
        if lmList[tipId[0]][1] > lmList[tipId[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #Fingers
        for id in range(1,5):
            if lmList[tipId[id]][2] < lmList[tipId[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalFingers = sum(fingers)

        cv2.putText(img, f'Total: {int(totalFingers)}', (50,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,255,0), 3)


    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv2.putText(img, f'FPS: {int(fps)}', (400,70), 
               cv2.FONT_HERSHEY_PLAIN, 2, (255,0,0), 2)

    cv2.imshow("preview",img)
    key = cv2.waitKey(1)
    if key==27:
        break

cap.release()
cv2.destroyWindow("preview")
