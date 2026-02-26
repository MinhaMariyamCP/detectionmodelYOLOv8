from ultralytics import YOLO
import cv2

# Load trained YOLO26 segmentation model
model = YOLO("weights/best.pt")   # path to trained weights

# Image for prediction
image_path = "test.jpg"

# Run inference
results = model.predict(
    source=image_path,
    save=True,
    conf=0.25
)

print("✅ Detection completed. Check outputs folder.")
