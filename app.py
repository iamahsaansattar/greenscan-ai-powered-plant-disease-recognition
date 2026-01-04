from flask import Flask, render_template, request, redirect, send_from_directory, url_for
import numpy as np
import json
import uuid
import tensorflow as tf
import os
import gdown

app = Flask(__name__)

@app.context_processor
def inject_active_page():
    return dict(active_page=request.endpoint)

# ===================== MODEL AUTO-DOWNLOAD =====================
MODEL_DIR = "models"
MODEL_NAME = "plant_disease_recog_model_pwp.keras"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

# 🔁 Replace with your actual Google Drive file ID
MODEL_URL = "https://drive.google.com/uc?id=1NOL9LXLWbvv-8wBfWfBkNWrxRS5ZYTZD"

os.makedirs(MODEL_DIR, exist_ok=True)

if not os.path.exists(MODEL_PATH):
    print("⬇️ Model not found. Downloading from Google Drive...")
    gdown.download(MODEL_URL, MODEL_PATH, quiet=False)
else:
    print("✅ Model already exists. Skipping download.")

# Load trained model
model = tf.keras.models.load_model(MODEL_PATH)

# ===================== LOAD DISEASE INFO =====================
with open("plant_disease.json", "r", encoding="utf-8") as f:
    plant_disease = json.load(f)

# ===================== UPLOADS =====================
UPLOAD_FOLDER = "uploadimages"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Store last prediction temporarily
last_prediction = {}

def get_safe_value(item, key, default=None):
    """Safely fetch optional JSON fields"""
    return item.get(key, default)

# ===================== ROUTES =====================
@app.route("/")
def home():
    return render_template("home.html", active_page="home")

@app.route("/about")
def about():
    return render_template("about.html", active_page="about")

@app.route("/upload", methods=["GET", "POST"])
def upload():
    global last_prediction

    if request.method == "POST":
        image = request.files["img"]

        filename = f"{uuid.uuid4().hex}_{image.filename}"
        filepath = os.path.join(UPLOAD_FOLDER, filename)
        image.save(filepath)

        # Preprocess image
        img = tf.keras.utils.load_img(filepath, target_size=(160, 160))
        img = tf.keras.utils.img_to_array(img)
        img = np.expand_dims(img, axis=0)

        # Predict
        prediction = model.predict(img)
        predicted_index = prediction.argmax()

        disease_info = plant_disease[predicted_index]

        plant_name = disease_info["plant_name"]
        raw_disease_name = disease_info["disease_name"]

        last_prediction = {
            "imagepath": f"/uploadimages/{filename}",
            "plant_name": plant_name,
            "disease_name": get_safe_value(
                disease_info, "disease_proper_name", raw_disease_name
            ),
            "disease_cause": get_safe_value(
                disease_info, "disease_cause", None
            ),
            "disease_cure": get_safe_value(
                disease_info,
                "disease_cure",
                "Maintain good cultural practices for optimal health."
            ),
            "cure_manufacturer": get_safe_value(
                disease_info, "cure_manufacturer", None
            ),
            "cure_manufacturer_logo": get_safe_value(
                disease_info, "cure_manufacturer_logo", None
            ),
            "disease_details": get_safe_value(
                disease_info, "disease_details", None
            ),
        }

        return redirect(url_for("result"))

    return render_template("upload.html", active_page="upload")

@app.route("/result")
def result():
    if not last_prediction:
        return redirect(url_for("upload"))

    return render_template(
        "result.html",
        imagepath=last_prediction["imagepath"],
        plant_name=last_prediction["plant_name"],
        disease_name=last_prediction["disease_name"],
        disease_cause=last_prediction["disease_cause"],
        disease_cure=last_prediction["disease_cure"],
        cure_manufacturer=last_prediction["cure_manufacturer"],
        cure_manufacturer_logo=last_prediction["cure_manufacturer_logo"],
        disease_details=last_prediction["disease_details"],
    )

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        comment = request.form.get("comment")

        print("📩 New Contact Message")
        print("Name:", name)
        print("Email:", email)
        print("Comment:", comment)

        return redirect(url_for("contact"))

    return render_template("contact.html", active_page="contact")

@app.route("/uploadimages/<path:filename>")
def uploaded_images(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ===================== ENTRY POINT =====================
if __name__ == "__main__":
    app.run(debug=True)
