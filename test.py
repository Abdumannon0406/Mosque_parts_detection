from ultralytics import YOLO

model=YOLO("runs/detect/train/weights/best.pt")

results=model.predict("testing_folders",save=True)