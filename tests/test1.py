import cv2
from ultralytics import YOLO
model = YOLO("yolov8n.pt")
#loads this yolo model
cap = cv2.VideoCapture(0)
#initializes the webcam video capture 
while cv2.waitKey(1) != ord("q"):
 #starts a while loop which pauses every 1 milisecond to check if q has been pressed
    _, frame = cap.read()
    # _,checks if the frame was sucessfully read then stores it in the variable frame
    result = model(frame, classes=[0], verbose=False)
    #looks for classification 0 in the frame and hides the verbose output
    cv2.imshow("autumn", result[0].plot())
    #opens and indicates the winfdow name and labels and draws bounding boxes around the detected objects
cap.release()
#safely turns off the camera
cv2.destroyAllWindows()
#closes all cv2 windows