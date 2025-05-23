# Traffic Sign Detection API

This project provides a RESTful API for traffic sign detection using a pre-trained deep learning model. The API is built with Flask and TensorFlow, allowing users to upload images and receive predictions for traffic sign classes.

## Features

- Accepts image uploads via HTTP POST requests.
- Predicts traffic sign classes: `crosswalk`, `speedlimit`, `stop`, `trafficlight`.
- Returns the predicted class and confidence score in JSON format.

## Project Structure

```
traffic-sign-detection/
├── app.py
├── requirements.txt
├── model/
│   └── traffic-sign-model.h5
├── test-image/
│   └── crosswalk.jpg
│   └── speedlimit.jpg
│   └── trafficlight.jpg
└── readme.md
```

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
   - Ensure the pre-trained model file `traffic-sign-model.h5` is placed in the `model/` directory.

4. **Run the API server:**
   ```bash
   python app.py
   ```

   The server will start at `http://127.0.0.1:5000/`.

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

- Success:  
  ```json
  {
    "prediction": "stop",
    "confidence": 0.987654
  }
  ```
- Error (no image uploaded):  
  ```json
  {
    "error": "No image uploaded"
  }
  ```

## Model Details

- Input size: 64x64 RGB images.
- Output classes:  
  - `crosswalk`
  - `speedlimit`
  - `stop`
  - `trafficlight`

## Notes

- The model must be trained separately and saved as `traffic-sign-model.h5`.
- For best results, use clear images of traffic signs.

## License

This project is for educational purposes.

