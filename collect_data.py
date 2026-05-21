import cv2
import os

label = "C"   # change later

path = f"dataset/{label}"
os.makedirs(path, exist_ok=True)

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)
count = 0

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    cv2.putText(frame, f"{label}: {count}", (10,50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Collect Data", frame)

    key = cv2.waitKey(1)

    if key == ord('s'):   # press S to save
        cv2.imwrite(f"{path}/{count}.jpg", frame)
        count += 1

    elif key == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()
