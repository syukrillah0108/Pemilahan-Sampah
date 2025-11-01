import cv2
import numpy as np
import requests
import time
import subprocess
import tensorflow as tf  # gunakan tensorflow, bukan tflite_runtime

# --- Konfigurasi ---
URL = "http://127.0.0.1:8080/?action=snapshot"
""" Class Labels:
  0: Organic
  1: botol plastik
  2: kaca
  3: kardus
  4: kertas
  5: metal
  6: plastic
"""
Classes = ["Organic", "botol plastik", "kaca", "kardus", "kertas", "metal", "plastic"]
# --- Load model ---
interpreter = tf.lite.Interpreter(model_path="./v1/model.tflite")
interpreter.allocate_tensors()
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()

def get_frame():
    try:
        response = requests.get(URL, timeout=3)
        response.raise_for_status()
        img_array = np.frombuffer(response.content, np.uint8)
        frame = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        if frame is None:
            raise ValueError("Frame kosong / gagal decode")
        return frame
    except Exception as e:
        print(f"⚠️  Gagal ambil frame: {e}")
        return None

def predict(frame, conf_threshold=0.5):
    img = cv2.resize(frame, (320, 320))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = np.expand_dims(img, axis=0).astype(np.float32) / 255.0

    interpreter.set_tensor(input_details[0]['index'], img)
    interpreter.invoke()

    output_data = interpreter.get_tensor(output_details[0]['index'])[0]

    detections = []
    for det in output_data:
        if len(det) < 6:
            continue
        x, y, w, h, conf, cls_id = det[:6]
        if conf > conf_threshold:
            cls_id = int(cls_id)
            label = Classes[cls_id] if cls_id < len(Classes) else f"class_{cls_id}"
            detections.append((label, float(conf)))

    if len(detections) == 0:
        return "no_object", 0.0

    detections.sort(key=lambda x: x[1], reverse=True)
    return detections[0]

print("🚀 Mulai deteksi (TensorFlow) dan kirim ke MQTT")
retry_count = 0
try:
    while True:
        frame = get_frame()
        if frame is None:
            retry_count += 1
            print(f"🔄 MJPEG belum aktif... percobaan ke-{retry_count}")
            time.sleep(2)
            continue

        label, conf = predict(frame)
        print(f"📦 Deteksi: {label} ({conf:.2f})")

        retry_count = 0
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\n🛑 Program dihentikan oleh user")
