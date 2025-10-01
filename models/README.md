
# 🧠 Models Directory – StrayMate AI System

Welcome to the **Models** directory of **StrayMate**, the intelligent stray animal detection and assistance system.  
This folder contains the *core machine learning and deep learning components* that power the project’s capabilities — from **computer vision** and **natural language processing** to intelligent decision-making.

---

## 📂 Directory Overview

| File / Folder | Type | Description |
|---------------|------|-------------|
| `injury_detector_resnet50.pth` | 🧠 Trained Model | Pre-trained **ResNet-50** model fine-tuned to classify stray animals as **Healthy** or **Injured**. |
| `labels.json` | 📄 Metadata | JSON mapping of model output indices to their respective classes. |
| `tokenizer.pkl` | 🔤 NLP Preprocessor | Tokenizer object used to preprocess text for the chatbot NLP model. |
| `chatbot_model.joblib` | 🤖 NLP Model | Trained text classification model that powers the StrayMate assistance chatbot. |
| `train_injury_detector.py` | 🛠️ Training Script | Python script used to train or retrain the vision model on a custom dataset. |
| `fine_tune_chatbot.ipynb` | 📓 Jupyter Notebook | Interactive notebook showcasing training, validation, and evaluation of the NLP model. |
| `README.md` | 📘 Documentation | You’re here — documentation describing all model components in detail. |

---

## 🧠 1. Vision Model – `injury_detector_resnet50.pth`

**Purpose:**  
Detects whether a stray animal (e.g., dog or cat) is **healthy** or **injured** from an input image. This powers the automatic **SOS alert system** in StrayMate.

**Model Details:**

| Property | Value |
|---------|-------|
| Architecture | ResNet-50 (Transfer Learning) |
| Framework | PyTorch |
| Input | 224×224 RGB image |
| Output | `0: Healthy`, `1: Injured` |
| Accuracy | ~93% (Validation) |
| Dataset | Custom dataset (~5,000+ annotated images) |

**Usage Example:**

```python
import torch
from torchvision import transforms
from PIL import Image

model = torch.load("models/injury_detector_resnet50.pth")
model.eval()

img = Image.open("test_image.jpg")
preprocess = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor()
])

input_tensor = preprocess(img).unsqueeze(0)
output = model(input_tensor)
pred = torch.argmax(output, dim=1).item()

print("Injured" if pred == 1 else "Healthy")
````

---

## 🔤 2. NLP Model – `chatbot_model.joblib` & `tokenizer.pkl`

**Purpose:**
Enables natural language understanding for the **StrayMate Assistance Chatbot**, allowing users to ask questions like:

* “How do I report an injured dog?”
* “Where is the nearest animal shelter?”
* “What should I feed a stray puppy?”

**Model Details:**

| Property    | Value                                 |
| ----------- | ------------------------------------- |
| Algorithm   | Logistic Regression (TF-IDF features) |
| Framework   | scikit-learn                          |
| Dataset     | ~2,000 Q&A pairs (custom-curated)     |
| Performance | 89% accuracy (test set)               |

**Usage Example:**

```python
import joblib

tokenizer = joblib.load("models/tokenizer.pkl")
chatbot_model = joblib.load("models/chatbot_model.joblib")

user_input = "How do I help an injured dog?"
X = tokenizer.transform([user_input])
response_class = chatbot_model.predict(X)[0]

print("Predicted intent:", response_class)
```

---

## 📊 3. Metadata – `labels.json`

A simple mapping of class indices to their respective labels, used by the vision model for decoding outputs.

```json
{
  "0": "Healthy",
  "1": "Injured"
}
```

---

## 🧪 4. Training Utilities

* **`train_injury_detector.py`** – Script for training the ResNet model from scratch or fine-tuning it on a new dataset. Includes data augmentation, checkpoint saving, and evaluation logic.
* **`fine_tune_chatbot.ipynb`** – Interactive notebook for retraining the NLP model. Useful for experiments, dataset improvements, or intent expansion.

---

## 🧭 Suggested Workflow

1. 📥 Collect and preprocess image/text data
2. 🧠 Use `train_injury_detector.py` or `fine_tune_chatbot.ipynb` to train models
3. 📦 Save trained models in this directory
4. 🚀 Load and integrate them into the main StrayMate pipeline

---

## 📌 Best Practices & Notes

* 🚫 **Do not commit large models (>100 MB)** directly. Use [Git LFS](https://git-lfs.github.com/) or store them externally (e.g., Google Drive, Hugging Face) and link them in this README.
* 🧪 Always version-control your models (e.g., `injury_detector_v2.pth`) when experimenting.
* 📚 Add training logs, confusion matrices, and evaluation reports in `docs/` for transparency.

---

## 🏁 Conclusion

This `models/` directory represents the **intelligence core of StrayMate** — combining **Computer Vision** and **Natural Language Processing** to make the system autonomous, responsive, and capable of real-world decision-making.

Each file here plays a vital role in transforming data into action, enabling StrayMate to *see, understand, and assist*.

---

✍️ **Author:** Swarnendu Bhattacharjee
📅 **Last Updated:** September 2025
🔗 **Project Repository:** [StrayMate – AI for Stray Animal Welfare](../)

```

---
