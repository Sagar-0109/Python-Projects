import cv2
import time

# Load Haar Cascade classifiers
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

cap = cv2.VideoCapture(0)
smile_count = 0  # Counter for smiles

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))  # Resize frame for faster processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        smiles = smile_cascade.detectMultiScale(roi_gray, scaleFactor=1.5, minNeighbors=15, minSize=(25, 25))

        if len(smiles) > 0:
            cv2.putText(frame, "Smiling!", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            smile_count += 1
            
            # Save a snapshot of the smile
            timestamp = time.strftime("%Y%m%d-%H%M%S")
            cv2.imwrite(f"smile_{timestamp}.jpg", frame)
        else:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

    # Display smile count
    cv2.putText(frame, f"Smiles: {smile_count}", (20, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    
    cv2.imshow("Smile Detector", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
