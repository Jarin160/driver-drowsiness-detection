import cv2
import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
from pygame import mixer
import time

# Initialize pygame mixer
mixer.init()
mixer.music.load("alarm.wav")

# Load TensorFlow model
model = load_model("drowsiness_detection.h5")

# Define class names (same order as training)
class_names = ['Closed Eyes', 'Open Eyes', 'No Yawn', 'Yawn']

# Open webcam
cap = cv2.VideoCapture(0)

# Optional: Haarcascade face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# --- Parameters ---
CLOSED_FRAMES_THRESHOLD = 5   # number of consecutive frames with eyes closed
YAWN_FRAMES_THRESHOLD = 2     # number of consecutive frames with yawning            # seconds before alarm can trigger again

closed_counter = 0
yawn_counter = 0

def play_alarm():
    if not mixer.music.get_busy():
        mixer.music.play(-1)

def stop_alarm():
    if mixer.music.get_busy():
        mixer.music.stop()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        face_roi = frame[y:y+h, x:x+w]
        img = cv2.resize(face_roi, (224, 224))
        img = img / 255.0
        img = np.expand_dims(img, axis=0)

        # Predict
        preds = model.predict(img, verbose=0)
        print(preds)
        class_index = np.argmax(preds)
        label = class_names[class_index]
        print(label)
        confidence = preds[0][class_index]

        # Draw rectangle + label
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        cv2.putText(frame, f"{label} ({confidence:.2f})", (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)

        # --- Improved Drowsiness Logic ---
        if label == 'Closed Eyes':
            closed_counter += 1
        else:
            closed_counter = 0

        if label == 'Yawn':
            yawn_counter += 1
        else:
            yawn_counter = 0

        # Trigger alarm if either counter exceeds threshold and cooldown passed
        current_time = time.time()
        if (closed_counter >= CLOSED_FRAMES_THRESHOLD or yawn_counter >= YAWN_FRAMES_THRESHOLD):
                play_alarm()
        else:
            stop_alarm()

    cv2.imshow("Driver Drowsiness Detection", frame)
    
    # Exit on 'q'
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
mixer.quit()
