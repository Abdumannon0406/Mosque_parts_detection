from ultralytics import YOLO

model=YOLO('yolo11n.pt')

results=model.train(data="Mosque_parts_detection/data.yaml")