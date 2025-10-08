# Driver Drowsiness Detection using Deep Learning

This project implements a **deep learning-based driver drowsiness detection system** that identifies whether a person’s **eyes are open or closed** and whether they are **yawning**.  
It uses **InceptionV3** for image classification and **OpenCV** for real-time deployment via webcam.  
An **alarm system** is also integrated using `pygame.mixer` to alert the user when signs of drowsiness are detected.


## Objective

This project aims to develop a **deep learning-based driver drowsiness detection system** with the following key objectives:

- **Detect eye state:** Classify whether the driver’s **eyes are open or closed** using image classification.  
- **Detect yawning:** Identify if the driver is **yawning**, which is a common sign of fatigue.  
- **Leverage deep learning:** Utilize the **InceptionV3** architecture for accurate feature extraction and classification.  
- **Enable real-time monitoring:** Integrate **OpenCV** to capture and process live video streams from the **webcam**.  
- **Alert system:** Implement an **alarm mechanism** using `pygame.mixer` that triggers when drowsiness is detected.  
- 🚗**Enhance driver safety:** Provide a proactive system to **reduce the risk of accidents** caused by fatigue or inattention.  

---

## Dataset

The project uses the **[Yawn Eye Dataset (New)](https://www.kaggle.com/datasets/serenaraju/yawn-eye-dataset-new)** from Kaggle.

### Dataset Description:
- Contains labeled images of faces showing different states:
  - `Open` — Eyes open  
  - `Closed` — Eyes closed  
  - `yawn` — Person yawning  
  - `no_yawn` — No yawn

  ---

## Model Overview

- **Base Model:** InceptionV3 (Transfer Learning)
- **Framework:** TensorFlow / Keras
- **Input Shape:** (224 × 224 × 3)

---

## ⚙️ Model Training Configuration

| Parameter | Value |
|------------|--------|
| Optimizer | Adam |
| Loss Function | Categorical Crossentropy |
| Epochs | 30 |
| Batch Size | 32 |
| Evaluation Metric | Accuracy |

**Training Strategy:**
- The dataset is split into training, validation, and test sets.  
- The model is trained for 30 epochs.  
- Performance is monitored using accuracy and loss curves.

---

## Model Evaluation

Model evaluation is performed using unseen test data to assess generalization ability.
Visualization tools such as **Matplotlib** are used to plot accuracy and loss trends over training epochs.

---

## The system:
1. Captures frames from webcam  
2. Detects face ROI (Region of Interest)  
3. Classifies eye/yawn state using the trained model  
4. Triggers an **alarm** if eyes remain closed or yawning continues for several frames

---

## Dependencies
- pandas
- numpy
- matplotlib
- tensorflow
- OpenCV
- pygame
  
---
