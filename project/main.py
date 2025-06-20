# main.py

import cv2
from ultralytics import YOLO


model = YOLO("yolov8n-face.pt")



# Start webcam capture (0 = default webcam)
cap = cv2.VideoCapture(0)

# Force OpenCV to create a visible window
cv2.namedWindow("YOLOv8 Face Detector", cv2.WINDOW_NORMAL)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame from webcam.")
        break

    # Perform object detection
    results = model(frame)

    # Draw detections
    for r in results:
        for box in r.boxes:
            cls = int(box.cls[0])
            conf = float(box.conf[0])
            
            # Filter only for 'person' class (default YOLO model doesn't do faces)
            if model.names[cls] != "person":
                continue

            # Get bounding box coordinates
            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw rectangle and label
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{model.names[cls]} {conf:.2f}",
                        (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX,
                        0.6, (255, 0, 0), 2)

    # Show the frame in a GUI window
    cv2.imshow("YOLOv8 Face Detector", frame)

    # Exit loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
