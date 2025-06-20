# main.py

import cv2
from ultralytics import YOLO
from deepface import DeepFace

# Load YOLOv8 face detector
model = YOLO("yolov8n.pt")  # Make sure this file is in the same folder

# Start webcam
cap = cv2.VideoCapture(0)
cv2.namedWindow("Face & Emotion Detector", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)

    for r in results:
        for box in r.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            x1, y1, x2, y2 = max(0, x1), max(0, y1), min(frame.shape[1], x2), min(frame.shape[0], y2)

            face = frame[y1:y2, x1:x2]

            # Emotion detection on the cropped face
            try:
                analysis = DeepFace.analyze(face, actions=['emotion'], enforce_detection=False)
                emotion = analysis[0]['dominant_emotion']
                confidence = analysis[0]['emotion'][emotion]
                label = f"{emotion} ({confidence:.2f}%)"
            except Exception:
                label = "Error"

            # Draw rectangle and emotion label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Face & Emotion Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
