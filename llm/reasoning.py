def reason_about_image(features):
    issues = []

    if features["faces"]["has_face"]:
        issues.append("human face detected")

    if features["quality_metrics"]["is_blurry"]:
        issues.append("image blur")

    if features["quality_metrics"]["is_dark"]:
        issues.append("low lighting")

    score = 1.0 - (0.1 * len(issues))

    return {
        "image_quality_score": round(score, 2),
        "issues_detected": issues,
        "final_verdict": (
            "Not suitable for professional e-commerce use"
            if issues else
            "Suitable for professional e-commerce use"
        ),
        "reasoning_summary": "Decision derived from extracted visual quality signals.",
        "confidence": 0.85
    }

