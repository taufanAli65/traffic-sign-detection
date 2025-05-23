# Traffic Sign Detection API

A RESTful API for detecting traffic signs in images using a pre-trained deep learning model. Built with Flask and TensorFlow, this API allows users to upload images and receive predictions for traffic sign classes, along with educational facts fetched from Firebase Firestore.

---

## Features

- Accepts image uploads via HTTP POST requests.
- Predicts traffic sign classes: `crosswalk`, `speedlimit`, `stop`, `trafficlight`.
- Returns the predicted class, confidence score, and a random educational fact in JSON format.
- Integrates with Firebase Firestore for dynamic fact retrieval.

---

## Table of Contents

- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [API Usage](#api-usage)
- [Model Details](#model-details)
- [Firestore Integration & Random Fact](#firestore-integration--random-fact)
- [Troubleshooting](#troubleshooting)
- [Notes](#notes)
- [License](#license)
- [Credits](#credits)

---

## Project Structure

```
traffic-sign-detection/
├── app.py
├── requirements.txt
├── model/
│   └── traffic-sign-model.h5
├── test-image/
│   ├── crosswalk.jpg
│   ├── speedlimit.jpg
│   └── trafficlight.jpg
├── firebaseServiceAccountKey.json
└── readme.md
```

---

## Prerequisites

- Python 3.7+
- [pip](https://pip.pypa.io/en/stable/)
- A trained Keras model (`traffic-sign-model.h5`)
- Firebase project with Firestore enabled
- Firebase service account key (`firebaseServiceAccountKey.json`)

---

## Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/taufanAli65/traffic-sign-detection.git
   cd traffic-sign-detection
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Model file:**
   - Place your pre-trained model file `traffic-sign-model.h5` in the `model/` directory.

4. **Firebase setup:**
   - Download your Firebase service account key as `firebaseServiceAccountKey.json` and place it in the project root.

5. **Run the API server:**
   ```bash
   python app.py
   ```
   The server will start at `http://127.0.0.1:5000/`.

---

## API Usage

### Endpoint

- **POST** `/predict`

### Request

- Content-Type: `multipart/form-data`
- Parameter: `image` (the image file to be classified)

#### Example using `curl`:

```bash
curl -X POST -F image=@path_to_image.jpg http://127.0.0.1:5000/predict
```

### Response

- **Success:**
  ```json
  {
    "prediction": "stop",
    "confidence": 0.987654,
    "fact": "The stop sign was standardized in 1922."
  }
  ```
- **Error (no image uploaded):**
  ```json
  {
    "error": "No image uploaded"
  }
  ```

---

## Model Details

- **Input size:** 64x64 RGB images.
- **Output classes:**
  - `crosswalk`
  - `speedlimit`
  - `stop`
  - `trafficlight`

---

## Firestore Integration & Random Fact

This project integrates with [Firebase Firestore](https://firebase.google.com/docs/firestore) to provide an educational fact about each predicted traffic sign.

### How it works

- The API connects to Firestore using a service account key (`firebaseServiceAccountKey.json`).
- For each traffic sign class, create a Firestore document in the `facts` collection, named after the class label (e.g., `crosswalk`, `speedlimit`, etc.), each containing multiple facts as key-value pairs.
- When a prediction is made, the API retrieves a random fact from the corresponding Firestore document and returns it in the JSON response.
- If no fact is available, the API returns `"Tidak ada fakta ditemukan."`.

### Firestore Setup

1. Create a Firebase project and Firestore database.
2. Download your service account key as `firebaseServiceAccountKey.json` and place it in the project root.
3. In Firestore, create a collection named `facts` with documents named after each class label (`crosswalk`, `speedlimit`, etc.), each containing several facts as fields.

### Additional Requirements

- The `firebase_admin` Python package is required (see `requirements.txt`).

---

## Troubleshooting

- **Model not found:** Ensure `traffic-sign-model.h5` is in the `model/` directory.
- **Firebase errors:** Check that `firebaseServiceAccountKey.json` is present and valid, and that your Firestore rules allow read access.
- **Missing facts:** Make sure the `facts` collection and documents exist in Firestore for each class label.

---

## Notes

- The model must be trained separately and saved as `traffic-sign-model.h5`.
- For best results, use clear images of traffic signs.
- The API is intended for educational and demonstration purposes.

---

## License

This project is for educational purposes.

---

## Credits

- [TensorFlow](https://www.tensorflow.org/)
- [Flask](https://flask.palletsprojects.com/)
- [Firebase Admin SDK](https://firebase.google.com/docs/admin/setup)

