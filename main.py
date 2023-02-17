import handtraking as hd
import cv2

def main():
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        detector = hd.handTracker()
        img = detector.findHands(img)
        lmList = detector.findLocation(img)
        
        if len(lmList) != 0:
            print(lmList)
            if lmList[8]:
                cv2.putText(img,'1',(20,20),cv2.FONT_HERSHEY_SIMPLEX,1, 
                (0, 255, 255), 
                2, 
                cv2.LINE_4)
        
        
        cv2.imshow("preview",img)
        key = cv2.waitKey(1)
        if key == 27: # exit on ESC
           break
    cv2.destroyWindow("preview")

if __name__=="__main__":
    main()

