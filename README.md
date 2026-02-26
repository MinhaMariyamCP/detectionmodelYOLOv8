# YOLO26 Car Parts Segmentation 🚗

This project demonstrates car part detection and instance segmentation using the YOLO26 segmentation model trained on the CarParts-Seg dataset.

## 🔥 Project Overview
The model detects multiple vehicle components such as:

- Bumpers
- Doors
- Lights
- Mirrors
- Hood
- Wheels

The system can be applied in:
- Insurance damage assessment
- Automated vehicle inspection
- Smart transportation systems

---

## ⚙️ Training

Training performed using Ultralytics YOLO framework:

```bash
yolo segment train data=carparts-seg.yaml model=yolo26n-seg.pt epochs=100 imgsz=640
