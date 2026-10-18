import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
cap = cv2.VideoCapture(0)
while cv2.waitKey(1) != ord("q"):
    _, frame = cap.read()
    result = model(frame, classes=[0], verbose=False)
    cv2.imshow("autumn", result[0].plot())
cap.release()
cv2.destroyAllWindows()
