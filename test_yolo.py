from ultralytics import YOLO
import cv2
from datetime import datetime

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("video.mp4")

while True:
    ret, frame = cap.read()

    if not ret:
        break

    results = model.track(frame, persist=True)

    boxes = results[0].boxes
    person_count = 0

    if boxes is not None:
        for box in boxes:
            cls = int(box.cls[0])

            if cls == 0:
                person_count += 1

    annotated = results[0].plot()

    cv2.putText(
        annotated,
        f"People Count: {person_count}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )

    if person_count >= 4:
        current_time = datetime.now().strftime("%H:%M:%S")
        event = f"{current_time} - Crowd Alert! Count={person_count}"

        print(event)

        with open("events.txt", "a") as f:
            f.write(event + "\n")

    cv2.imshow("Purplle Store Intelligence", annotated)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()