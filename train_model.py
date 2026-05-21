import os
import cv2
import mediapipe as mp
from sklearn.ensemble import RandomForestClassifier
import pickle

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

data = []
labels = []

print("Training started...")

for label in os.listdir("dataset"):
    for file in os.listdir(f"dataset/{label}"):

        img = cv2.imread(f"dataset/{label}/{file}")
        if img is None:
            continue

        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(img_rgb)

        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                row = []
                for lm in handLms.landmark:
                    row.append(lm.x)
                    row.append(lm.y)

                data.append(row)
                labels.append(label)

model = RandomForestClassifier()
model.fit(data, labels)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained successfully")
