from flask import Flask, request, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import firebase_admin
from firebase_admin import credentials, firestore
import random

app = Flask(__name__)

# Inisialisasi Firebase Admin (Firestore)
cred = credentials.Certificate("./firebaseServiceAccountKey")  # Ganti path sesuai file firebaseServiceAccountKey.json kamu
firebase_admin.initialize_app(cred)
db = firestore.client()

# Load model
model = load_model("model/traffic-sign-model.h5")

# Label kelas
labels = ['crosswalk', 'speedlimit', 'stop', 'trafficlight']

def preprocess_image(image):
    if image.mode != 'RGB':
        image = image.convert("RGB")
    image = image.resize((64, 64))
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)
    return image

def get_random_fact(label):
    doc_ref = db.collection('facts').document(label)
    doc = doc_ref.get()
    if doc.exists:
        facts_dict = doc.to_dict()
        if facts_dict:
            return random.choice(list(facts_dict.values()))
    return "Tidak ada fakta ditemukan."

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    image_file = request.files['image']
    image = Image.open(image_file)
    processed_image = preprocess_image(image)

    prediction = model.predict(processed_image)
    class_index = np.argmax(prediction)
    class_label = labels[class_index]
    confidence = float(np.max(prediction))

    fact = get_random_fact(class_label)

    return jsonify({
        'prediction': class_label,
        'confidence': confidence,
        'fact': fact
    })

if __name__ == '__main__':
    app.run(debug=True)
