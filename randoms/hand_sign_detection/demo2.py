import cv2
import mediapipe as mp
import time
import numpy as np
from math import hypot

wcam, hcam = 640,480
plocX, plocY = 0,0  #previous location of x & y
clocX, clocY = 0,0  #current location of x & y
#these codes are imported from the cvzone handtracking module from cvzone.HandTrackingModule import HandDetector
#I did this for customization of the detectionbox

class HandDetector:
    """
    Finds Hands using the mediapipe library. Exports the landmarks
    in pixel format. Adds extra functionalities like finding how
    many fingers are up or the distance between two fingers. Also
    provides bounding box info of the hand found.
    """

    def __init__(self, mode=False, maxHands=1, detectionCon=0.5, minTrackCon=0.5):
        """
        :param mode: In static mode, detection is done on each image: slower
        :param maxHands: Maximum number of hands to detect
        :param detectionCon: Minimum Detection Confidence Threshold
        :param minTrackCon: Minimum Tracking Confidence Threshold
        """
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.minTrackCon = minTrackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(static_image_mode=self.mode, max_num_hands=self.maxHands,
                                        min_detection_confidence=self.detectionCon,
                                        min_tracking_confidence=self.minTrackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.tipIds = [4, 8, 12, 16, 20]
        self.fingers = []
        self.lmList = []

    def findHands(self, img, draw=True, flipType=True):
        """
        Finds hands in a BGR image.
        :param img: Image to find the hands in.
        :param draw: Flag to draw the output on the image
        :return: Image with or without drawings
        """
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        allHands = []
        height = 0
        dbox = (0,0)
        h, w, c = img.shape
        if self.results.multi_hand_landmarks:
            for handType, handLms in zip(self.results.multi_handedness, self.results.multi_hand_landmarks):
                myHand = {}
                ## lmList
                mylmList = []
                xList = []
                yList = []
                for id, lm in enumerate(handLms.landmark):
                    px, py, pz = int(lm.x * w), int(lm.y * h), int(lm.z * w)
                    mylmList.append([px, py, pz])
                    xList.append(px)
                    yList.append(py)

                ## bbox
                xmin, xmax = min(xList), max(xList)
                ymin, ymax = min(yList), max(yList)
                boxW, boxH = xmax - xmin, ymax - ymin
                bbox = xmin, ymin, boxW, boxH
                cx, cy = bbox[0] + (bbox[2] // 2), \
                         bbox[1] + (bbox[3] // 2)

                myHand["lmList"] = mylmList
                myHand["bbox"] = bbox
                myHand["center"] = (cx, cy)

                if flipType:
                    if handType.classification[0].label == "Right":
                        myHand["type"] = "Left"
                    else:
                        myHand["type"] = "Right"
                else:
                    myHand["type"] = handType.classification[0].label
                allHands.append(myHand)

                ## draw
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms,
                                               self.mpHands.HAND_CONNECTIONS)
                    cv2.rectangle(img, (bbox[0] - 20, bbox[1] - 20),
                                  (bbox[0] + bbox[2] + 20, bbox[1] + bbox[3] + 20),
                                  (108,47,0), 2)
                    cv2.putText(img, myHand["type"], (bbox[0] - 30, bbox[1] - 30), cv2.FONT_HERSHEY_PLAIN,
                                2, (255, 255, 0), 2)
                    #cv2.putText(img,f"distance : {distance_find(f, H, h)}", (bbox[0]+80, bbox[1]-30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)
                    height = (bbox[3] + 20)
                    dbox = (bbox[0]+80, bbox[1]-30)
                    #print(dbox)
        if draw:
            
            return allHands, img, height, dbox
        else:
            return allHands
    
    def fingersUp(self, myHand):
        """
        Finds how many fingers are open and returns in a list.
        Considers left and right hands separately
        :return: List of which fingers are up
        """
        myHandType = myHand["type"]
        myLmList = myHand["lmList"]
        if self.results.multi_hand_landmarks:
            fingers = []
            # Thumb
            if myHandType == "Right":
                if myLmList[self.tipIds[0]][0] > myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)
            else:
                if myLmList[self.tipIds[0]][0] < myLmList[self.tipIds[0] - 1][0]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            # 4 Fingers
            for id in range(1, 5):
                if myLmList[self.tipIds[id]][1] < myLmList[self.tipIds[id] - 2][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
        return fingers

    def findPosition(self, img, handNo=0, draw=True):
        xList = []
        yList = []
        bbox = []
        self.lmList = []
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(img, (cx, cy), 5, (108,47,0), cv2.FILLED)
 
            xmin, xmax = min(xList), max(xList)
            ymin, ymax = min(yList), max(yList)
            bbox = xmin, ymin, xmax, ymax
 
            if draw:
                cv2.rectangle(img, (xmin - 20, ymin - 20), (xmax + 20, ymax + 20),
                              (0, 255, 0), 2)
 
        return self.lmList, bbox


#average FPS  = 35.93436293436294
#average FPS when detecting hands  = 19.258928571428573
#approximatley 16 FPS drops when hand detection is called

detector = HandDetector(detectionCon=0.8, maxHands=2)

avgfps = []
cap = cv2.VideoCapture(0)
cap.set(3,wcam)
cap.set(4,hcam)
pTime = 0

thres = 70
#calculate focal length and distance
#distance -> the initial distance through which the focal length is found
'''H -> initial height of the face/object detectionbox when 
placed in the initial distance found by measuring the height
of the detectionbox in pixel at initial distance and converting
the pixel value to cm by multiplying with `0.02645(constant)'''


#dei..distance config width vechi paniruka..change that to height again configure pannu
#find_hands la height nu return panadhu width..20/12/22 changed return value of height to height

distance = 50
H = 4.62875

def focal(h,distance,H):
    f = (h * distance) / H
    print(f)
    return f

f = 45 #this is found by facing the hand at 50cm distance and measuring the height of the detectionbox and passing it to the focal function

def distance_find(f,H,h):
    #print(h)
    if h==0:
        return 0
    else:
        d = int((H * f) / h)
        return d

'''distance tracking using the height of the detectionbox has some errors.
If the object which is being tracked in dynamic or changes forms, then the 
distance calculated will be false. Hence need to try another method by calculating 
the distance of the 2 points in hand detection from pinky finger to index finger'''

def main(pTime):
    plocX, plocY = 0,0
    clocX, clocY = 0,0

    while True:
        success, img = cap.read()
        hands, img, height, dbox = detector.findHands(img) 
        lmlist, bbox = detector.findPosition(img)

        pixel = height
        h = float(pixel * 0.02645)
        #print(h)
        #res = focal(h,distance,H)
        #print(res)q

        #detect fingers
        if hands:
            hand = hands[0]
            #print(hand)
            fingers = detector.fingersUp(hand)
            print(fingers)

        #detect and calculate FPS
        cTime = time.time()
        fps = int(1 / (cTime - pTime))
        pTime = cTime
        avgfps.append(fps)
        #display FPS
        cv2.putText(img, f"FPS : {fps}",(10,25),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
        cv2.putText(img,f"{distance_find(f, H, h)} cm", dbox, cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 2)
        cv2.putText(img,"GCC 2.0",(250,30),cv2.FONT_HERSHEY_DUPLEX,1, (0,0,128), 2)
        cv2.imshow("test",img)
        if cv2.waitKey(1) == ord('q'):
            break
    cv2.destroyAllWindows()
main(pTime)