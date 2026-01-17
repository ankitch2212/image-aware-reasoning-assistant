import argparse
import json

from feature_extraction.object_detection import detect_objects
from feature_extraction.face_detection import detect_faces
from feature_extraction.ocr import extract_text
from feature_extraction.quality_metrics import image_quality_metrics
from llm.reasoning import reason_about_image

def run_pipeline(image_path):
    features = {
        "objects_detected": detect_objects(image_path),
        "faces": detect_faces(image_path),
        "text_detected": extract_text(image_path),
        "quality_metrics": image_quality_metrics(image_path)
    }

    llm_result = reason_about_image(features)

    output = {
        "features": features,
        "llm_decision": llm_result
    }

    return output

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image", required=True)
    args = parser.parse_args()

    result = run_pipeline(args.image)
    print(json.dumps(result, indent=2))
