import cv2
import mediapipe as mp
import pickle
import time
import pyttsx3
import collections

# 🔊 Voice setup
engine = pyttsx3.init()
engine.setProperty('rate', 150)

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

# Mediapipe setup
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

# Camera
cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

# Variables
sentence = ""
last_letter = ""
last_time = 0

# Stability filter
history = collections.deque(maxlen=10)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)

    img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    current_letter = ""

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            row = []
            for lm in handLms.landmark:
                row.append(lm.x)
                row.append(lm.y)

            pred = model.predict([row])[0]

            # Add to history for smoothing
            history.append(pred)

            # Get most common prediction
            current_letter = max(set(history), key=history.count)

    # Add letter to sentence (delay to avoid spam)
    current_time = time.time()
    if current_letter != "" and current_letter != last_letter:
        if current_time - last_time > 1:
            sentence += current_letter
            last_letter = current_letter
            last_time = current_time

    # Keyboard controls
    key = cv2.waitKey(1)

    if key == ord('c'):   # clear text
        sentence = ""

    if key == ord(' '):   # add space
        sentence += " "

    if key == ord('v'):   # 🔊 speak
        engine.say(sentence)
        engine.runAndWait()

    # Display
    cv2.putText(frame, f"Letter: {current_letter}", (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.putText(frame, f"Text: {sentence}", (10,100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255,0,0), 2)

    cv2.imshow("ANNA Sign Language AI", frame)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
