import cv2
import mediapipe as mp
import pyautogui
import time

pyautogui.FAILSAFE = False

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

screen_w, screen_h = pyautogui.size()

last_click_time = 0   # 👈 IMPORTANT

while True:
    success, img = cap.read()
    if not success:
        break

    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

            landmarks = handLms.landmark

            x = int(landmarks[8].x * screen_w)
            y = int(landmarks[8].y * screen_h)

            pyautogui.moveTo(x, y)

            # 👉 CLICK LOGIC (FIXED)
            if landmarks[8].y > landmarks[6].y:
                current_time = time.time()

                if current_time - last_click_time > 1:   # 1 sec delay
                    pyautogui.click()
                    last_click_time = current_time

                    cv2.putText(img, "CLICK", (10, 50),
                                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)
            else:
                cv2.putText(img, "MOVE", (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("ANNA Control", img)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()
       
            
      
                
               
