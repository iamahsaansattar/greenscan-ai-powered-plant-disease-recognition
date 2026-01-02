# 🌱 GreenScan — AI-Powered Plant Disease Recognition

GreenScan is a web-based **AI-powered plant disease detection system** that allows users to upload plant images and receive instant disease identification along with actionable treatment recommendations.

The system leverages a pre-trained deep learning model based on the **PlantVillage dataset** and is designed for farmers, gardeners, and agriculture enthusiasts.

---

## 🚀 Key Features

- 📸 Upload plant images for real-time disease detection  
- 🧠 Deep learning–based image classification  
- 🌿 Supports multiple crops and disease types  
- 💊 Provides disease cause and treatment recommendations  
- 🏷️ Displays manufacturer details and logos (when available)  
- 📱 Fully responsive, modern UI with glassmorphism design  

---

## 🧠 AI Model & Dataset

- **Model Type:** Convolutional Neural Network (CNN)  
- **Framework:** TensorFlow / Keras  
- **Dataset:** PlantVillage  
- **Dataset Source:**  
  ```bash
  https://www.tensorflow.org/datasets/catalog/plant_village  
  ```

The trained model is stored locally at:
```bash
models/plant_disease_recog_model_pwp.keras
```

---

## 🔗 Model Download (Required)

Due to GitHub’s file size limitations, the trained AI model is not included in this repository.

### ➡️ Download the model from Google Drive:
```bash
https://drive.google.com/drive/folders/18_uYPdBuxsOmDUCwNQEF_lXPLeloZfHG?usp=sharing
```

---

## 📂 Model Placement

After downloading:

**1:** Extract the file (if zipped).
**2:** Place the model file inside the following directory:
```bash
models/plant_disease_recog_model_pwp.keras
```

⚠️ **The application will not run without this file in the correct location**, as required by  `app.py`.

---

## 📄 Disease & Treatment Data

All plant disease and treatment metadata is maintained in:
```bash
plant_disease.json
```

Each entry may include:
- Plant name  
- Disease name (raw and proper)  
- Disease cause  
- Recommended cure  
- Manufacturer name  
- Manufacturer logo path  
- Additional disease details  

The backend safely handles optional or missing fields.

---

## 🖥️ Tech Stack

- **Backend:** Python, Flask  
- **Frontend:** HTML5, CSS3, Bootstrap  
- **AI / ML:** TensorFlow, Keras, NumPy  
- **Data Storage:** JSON  

---

## ▶️ How to Run the Project

### 1️⃣ Prerequisites
Ensure Python **3.8 or higher** is installed.

### 2️⃣ Install dependencies
```bash
pip install flask tensorflow numpypy
```

### 3️⃣ Run the application
```bash
python app.py
```
### 4️⃣ Open in browser

```bash
http://127.0.0.1:5000
```

---

## 📌 Important Notes

- The AI model is **pre-trained** — no training required to run the app.
- Uploaded images are stored temporarily in the `uploadimages/` directory.
- This project is intended for **educational and research purposes**.
- Treatment recommendations should **not replace professional agricultural advice**.

---

## 🎯 Project Objective

The objective of GreenScan is to:

- Assist farmers and gardeners in early plant disease detection.
- Reduce crop losses through timely intervention.
- Demonstrate real-world application of Artificial Intelligence in agriculture.
- Provide an accessible and easy-to-use plant health diagnostic platform.

---

## 👨‍💻 Author & Project Context

**Author:** Muhammad Ahsaan Sattar
**Qualification:** Bachelor of Science in Software Engineering
**Institution:** The Islamia University of Bahawalpur, Pakistan
**Email:** itsahsaansattar@gmail.com

GreenScan is developed as a Final Year Project (FYP) focused on applying Artificial Intelligence to solve real-world agricultural problems through accessible web technology.

---

## 📜 License

This project is intended for **academic and educational use**.
Reuse or modification should include proper attribution.

---

## 🙌 Acknowledgments

- PlantVillage Dataset
- TensorFlow & Keras
- Open-source community