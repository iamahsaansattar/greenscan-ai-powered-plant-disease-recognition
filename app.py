from flask import (
    Flask,
    render_template,
    request,
    redirect,
    send_from_directory,
    url_for,
    flash
)
import numpy as np
import json
import uuid
import tensorflow as tf
import os
import gdown
import sqlite3
from datetime import datetime

app = Flask(__name__)
app.secret_key = "greenscan-secret-key"

@app.context_processor
def inject_active_page():
    return dict(active_page=request.endpoint)

# ===================== DATABASE (SQLite) =====================
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "contact_messages.db")

os.makedirs(DB_DIR, exist_ok=True)

def get_db_connection():
    conn = sqlite3.connect(DB_PATH, timeout=10)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            comment TEXT NOT NULL,
            created_at TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

# Initialize database on app start
init_db()

# ===================== MODEL AUTO-DOWNLOAD =====================
MODEL_DIR = "models"
MODEL_NAME = "plant_disease_recog_model_pwp.keras"
MODEL_PATH = os.path.join(MODEL_DIR, MODEL_NAME)

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

        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute(
                """
                INSERT INTO messages (name, email, comment, created_at)
                VALUES (?, ?, ?, ?)
                """,
                (name, email, comment, datetime.utcnow().isoformat())
            )

        flash(
            "Your message has been sent successfully. We’ll get back to you soon!",
            "success"
        )

        return redirect(url_for("contact"))

    return render_template("contact.html", active_page="contact")

@app.route("/uploadimages/<path:filename>")
def uploaded_images(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

# ===================== ENTRY POINT =====================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
