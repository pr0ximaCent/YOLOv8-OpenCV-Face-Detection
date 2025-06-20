

### ✅ `README.md`

````markdown
# 🧠 Real-Time Face & Emotion Detection

This project uses **YOLOv8** for face detection and **DeepFace** for emotion classification in real-time via a webcam feed. It's built with Python, OpenCV, and modern deep learning tools to provide an intelligent, interactive experience.

---

## 🔍 Features

- 🚀 **YOLOv8n-face** model for fast and accurate face detection
- 😊 **DeepFace** for recognizing 7 core emotions: `angry`, `disgust`, `fear`, `happy`, `sad`, `surprise`, `neutral`
- 🖼️ Real-time video processing via webcam
- 📦 Simple to run locally in a virtual environment

---

## 🧰 Tech Stack

- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
- [DeepFace](https://github.com/serengil/deepface)
- OpenCV
- Python 3.8+

---

## ⚙️ Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/face-emotion-detector.git
cd face-emotion-detector
````

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, you can install manually:

```bash
pip install ultralytics opencv-python deepface
```

### 4. Download YOLOv8 Face Model

Download `yolov8n-face.pt` from this repo:
🔗 [https://github.com/derronqi/yolov8-face/releases](https://github.com/derronqi/yolov8-face/releases)

Place it in the root project directory.

---

## 🚀 Run the Project

```bash
python main.py
```

A webcam window will open, showing bounding boxes around detected faces with predicted emotions labeled in real time.

---

## 📂 Project Structure

```
.
├── main.py                  # Main app script
├── yolov8n-face.pt          # Face detection model (download separately)
├── requirements.txt         # Python dependencies
└── README.md                # You're here!
```

---

## 📸 Example Output

![demo](https://i.imgur.com/your-sample-frame.jpg)
*(Replace this with a real screenshot if you like)*

---

## 🧠 Future Ideas

* Blur faces for privacy
* Add snapshot saving when emotions are detected
* Deploy with Streamlit or Gradio
* Add gender and age estimation

---

## 👤 Author

**Sabik Aftahee**
📫 \[sabikaftahee01@gmail.com]
🌐 \[Portfolio](https://tinyurl.com/Sabik-Aftahee)]

---

## 📝 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

```


