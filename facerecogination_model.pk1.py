import cv2
import joblib
import numpy as np
from skimage.feature import hog

# Load trained model
clf = joblib.load("facerecogination_model.pkl")

# OpenCV Face Detector
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

# Emotion Labels
emotion_dict = {0: "Angry", 1: "Disgust", 2: "Fear", 3: "Happy", 4: "Sad", 5: "Surprise", 6: "Neutral"}

# Start Webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in faces:
        face_roi = gray[y:y+h, x:x+w]
        face_roi = cv2.resize(face_roi, (48, 48))  # Ensure correct size

        # Extract HOG features (Ensure same as training: 1764 features)
        features = hog(face_roi, pixels_per_cell=(4, 4), cells_per_block=(2, 2))

        if len(features) == 1764:  # Ensure correct feature count
            prediction = clf.predict([features])[0]
            label = emotion_dict.get(prediction, "Unknown")
        else:
            label = "Feature Mismatch"

        # Draw rectangle and label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"Expression: {label}", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

    cv2.imshow("Face Expression Recognition", frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
