# -*- coding: utf-8 -*-
"""
Created on Tue May 18 14:40:39 2021

@author: neeraj
"""

import cv2
import mediapipe as mp

class handTracker():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def findHands(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.result = self.hands.process(imgRGB)
    
        if self.result.multi_hand_landmarks:
            for handLms in self.result.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img
    
    def findLocation(self, img, draw=True, handNo=0):  
        lmList = []
        if self.result.multi_hand_landmarks:
            hand = self.result.multi_hand_landmarks[handNo]
            for id, lm in enumerate(hand.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x * w), int(lm.y * h)
                lmList.append([id, cx, cy])
                
                if draw:
                    cv2.circle(img, (cx,cy), 5, (255,255,0), cv2.FILLED)
        return lmList
            
    

##    cap = cv2.VideoCapture(0)
#    while True:
#        success, img = cap.read()
#        detector = handTracker()
#        img = detector.findHands(img)
#        lmList = detector.findLocation(img)
#        
#        if len(lmList) != 0:
#            print(lmList[5])
        
        
#        cv2.imshow("preview",img)
#        key = cv2.waitKey(1)
 #       if key == 27: # exit on ESC
#           break
#   cv2.destroyWindow("preview")

#if __name__== "__main__":
#    main()