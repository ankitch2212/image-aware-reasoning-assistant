import cv2
import numpy as np

def image_quality_metrics(image_path):
    img = cv2.imread(image_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur_score = cv2.Laplacian(gray, cv2.CV_64F).var()
    brightness = np.mean(cv2.cvtColor(img, cv2.COLOR_BGR2HSV)[:, :, 2])

    return {
        "blur_score": round(blur_score, 2),
        "brightness": round(brightness, 2),
        "is_blurry": bool(blur_score < 100),
        "is_dark": bool(brightness < 80)
    }
