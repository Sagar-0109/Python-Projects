import cv2
import numpy as np
from deepface import DeepFace
# Initialize the webcam
cap = cv2.VideoCapture(0)

# Load OpenCV face detection model
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

    for (x, y, w, h) in faces:
        # Extract the face ROI
        face = frame[y:y+h, x:x+w]

        try:
            # Predict age using DeepFace
            analysis = DeepFace.analyze(face, actions=["age"], enforce_detection=False)
            predicted_age = analysis[0]['age']

            # Draw rectangle around face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

            # Display predicted age
            cv2.putText(frame, f"Age: {predicted_age}", (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

        except Exception as e:
            print(f"Error in age prediction: {e}")

    # Display the frame
    cv2.imshow("Age Prediction", frame)

    # Press 'q' to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
