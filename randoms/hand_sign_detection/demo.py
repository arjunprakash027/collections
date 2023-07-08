import mediapipe as mp
import cv2
import numpy as np

#capturing the output from webcam
mpHands  = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils
hands = mpHands.Hands(max_num_hands=1, min_detection_confidence=0.7)

cap = cv2.VideoCapture(0)
while True:
    # Read each frame from the webcam
    _, frame = cap.read()
    x , y, c = frame.shape

    # Flip the frame vertically
    frame = cv2.flip(frame, 1)
    # Show the final output
    cv2.imshow("Output", frame)

    framergb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Get hand landmark prediction
    result = hands.process(framergb)

    className = ''

    # post process the result
    if result.multi_hand_landmarks:
        landmarks = []
        for handslms in result.multi_hand_landmarks:
            for lm in handslms.landmark:
                # print(id, lm)
                
                #qprint(lm.x,lm.y)
                lmx = int(lm.x * x)
                lmy = int(lm.y * y)

                landmarks.append([lmx, lmy])
            mpDraw.draw_landmarks(frame, handslms,mpHands.HAND_CONNECTIONS)
        #print(landmarks)
        for landmark in handslms.landmark:
                x, y, z = landmark.x, landmark.y, landmark.z
                cv2.circle(frame, (int(x), int(y)), 3, (0, 0, 255), -1)

            # Drawing landmarks on frames
            
    
    if cv2.waitKey(1) == ord('s'):
          print(landmarks)

    if cv2.waitKey(1) == ord('q'):
                break
cap.release()
cv2.destroyAllWindows()

#drawing annotations





