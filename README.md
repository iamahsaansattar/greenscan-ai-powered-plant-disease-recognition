# 🌱 GreenScan — AI-Powered Plant Disease Recognition

GreenScan is a web-based **AI-powered plant disease detection system** that allows users to upload plant images and receive instant disease identification along with actionable treatment recommendations.

The system leverages a pre-trained deep learning model based on the **PlantVillage dataset** and is designed for **farmers**, **gardeners**, and **agriculture enthusiasts**.

---

## 🚀 Key Features

- 📸 Upload plant images for real-time disease detection  
- 🧠 Deep learning–based image classification  
- 🌿 Supports multiple crops and disease types  
- 💊 Provides disease cause and treatment recommendations  
- 🏷️ Displays manufacturer details and logos (when available)  
- 📱 Fully responsive, modern UI with glassmorphism design  
- 🐳 Fully containerized with Docker (zero setup)  

---

## 🧠 AI Model & Dataset

- **Model Type:** Convolutional Neural Network (CNN)  
- **Framework:** TensorFlow / Keras  
- **Dataset:** PlantVillage  
- **Dataset Source:**  
  ```bash
  https://www.tensorflow.org/datasets/catalog/plant_village  
  ```

---

## 🔗 Model Handling (Flexible: Zero Setup or Manual)

Due to GitHub’s file size limitations, the trained AI model is **not included in this repository**. GreenScan supports **two usage modes**, depending on user preference.

### 🟢 Option 1: Zero Setup (Recommended — Docker & Cloud)

When running the application using **Docker**, **Docker Compose**, or deploying to cloud platforms (e.g., Render):

- The application **automatically downloads** the trained model from Google Drive.
- The model is cached locally inside the container.
- Subsequent runs reuse the downloaded model.

✅ No manual steps required.  
✅ Best for end users and deployment.  

### 🟡 Option 2: Manual Model Placement (Local Development)

For users who prefer **not to use Docker** and want full control:

1️⃣ Download the trained model from Google Drive:
```bash
https://drive.google.com/drive/folders/18_uYPdBuxsOmDUCwNQEF_lXPLeloZfHG?usp=sharing
```

2️⃣ Create a `models/` directory in the project root (if it does not exist).

3️⃣ Place the model file exactly at:
```bash
models/plant_disease_recog_model_pwp.keras
```

⚠️ **The application will not run without this file in the correct location**, as required by  `app.py`.

4️⃣ Run the application normally:
```bash
python app.py
```

🔹 If the model file is already present, **the application will not attempt to download it again**.

### 📌 Important Note

The **same application code** supports both modes:

- Manual placement is ideal for:
  - Offline usage
  - Research experiments
  - Development and debugging

- Docker-based execution is recommended for:
  - Zero setup
  - Deployment
  - End users

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
- **Containerization:** Docker, Docker Compose  
- **Data Storage:** JSON  

---

## 🐍 Python Version

- **Recommended:** Python 3.8 – 3.11
- TensorFlow may not support newer Python versions.

---

## 📦 Dependencies

All required dependencies are listed in:
```bash
requirements.txt
```

They are automatically installed when using Docker.

---

## 🐳 Running with Docker (Recommended)

### 1️⃣ Clone the repository
```bash
git clone https://github.com/iamahsaansattar/greenscan-ai-powered-plant-disease-recognition.git
```
```bash
cd greenscan-ai-powered-plant-disease-recognition
```

### 2️⃣ Run using Docker Compose
```bash
docker compose up --build
```

or (older Docker versions):
```bash
docker-compose up --build
```

### 3️⃣ Open in browser
```bash
http://localhost:5000
```

✅ No Python installation  
✅ No dependency installation  
✅ No manual model download  
✅ Works out of the box  

---

## 🐳 Running with Docker (Without Compose)

If you prefer plain Docker:
```bash
docker build -t greenscan .
```
```bash
docker run -p 5000:5000 greenscan
```

---

## 🖥️ Running Without Docker (Optional)

⚠️ Docker is **strongly recommended**.
Use this method only for development or experimentation.

### 1️⃣ Clone the repository

```bash
git clone https://github.com/iamahsaansattar/greenscan-ai-powered-plant-disease-recognition.git
```
```bash
cd greenscan-ai-powered-plant-disease-recognition
```

### 2️⃣ Download & place the AI model

(See **Model Download & Placement** section above)

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Run the application
```bash
python app.py
```
### 5️⃣ Open in browser
```bash
http://127.0.0.1:5000
```

---

## 📌 Important Notes

- The AI model is **pre-trained** — no training required.
- Uploaded images are stored temporarily in the `uploadimages/` directory.
- The application runs entirely on **CPU** (GPU not required).
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

- **Author:** Muhammad Ahsaan Sattar
- **Qualification:** Bachelor of Science in Software Engineering
- **Institution:** The Islamia University of Bahawalpur, Pakistan
- **Email:** itsahsaansattar@gmail.com

GreenScan is developed as a **Final Year Project (FYP)** focused on applying Artificial Intelligence to solve real-world agricultural problems through accessible web technology.

---

## 📜 License

This project is intended for **academic and educational use**.
Reuse or modification should include proper attribution.

---

## 🙌 Acknowledgments

- PlantVillage Dataset
- TensorFlow & Keras
- Docker Community
- Open-source Community