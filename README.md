# Driver Drowsiness Detection using Deep Learning

This project implements a **deep learning-based driver drowsiness detection system** that identifies whether a person’s **eyes are open or closed** and whether they are **yawning**.  
It uses **InceptionV3** for image classification and **OpenCV** for real-time deployment via webcam.  
An **alarm system** is also integrated using `pygame.mixer` to alert the user when signs of drowsiness are detected.

---

## Dataset

The project uses the **[Yawn Eye Dataset (New)](https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new)** from Kaggle.

### Dataset Description:
- Contains labeled images of faces showing different states:
  - `Open` — Eyes open  
  - `Closed` — Eyes closed  
  - `Yawn` — Person yawning  
  - `No_yawn` — No yawn

  ---

## Model Overview

- **Base Model:** InceptionV3 (Transfer Learning)
- **Framework:** TensorFlow / Keras
- **Input Shape:** (224 × 224 × 3)
- **Output Classes:**  
  1. Eyes Open  
  2. Eyes Closed  
  3. Yawn  
  4. No Yawn

---

## The system:
1. Captures frames from webcam  
2. Detects face ROI (Region of Interest)  
3. Classifies eye/yawn state using the trained model  
4. Triggers an **alarm** if eyes remain closed or yawning continues for several frames
