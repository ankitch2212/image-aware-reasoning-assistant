from ultralytics import YOLO

model = YOLO("yolov8n.pt")

def detect_objects(image_path):
    results = model(image_path)
    objects = set()

    for r in results:
        for box in r.boxes:
            objects.add(model.names[int(box.cls)])

    return list(objects)
