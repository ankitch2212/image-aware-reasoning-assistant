# 🧠 Image-Aware Reasoning Assistant  
Mini Multimodal Intelligence System

---

## 📌 Overview

This project implements an **Image-Aware Reasoning Assistant** that evaluates whether an image is suitable for **professional e-commerce usage**.

The goal of this task is **not UI or deployment**, but to demonstrate:
- Multimodal ML thinking
- Pre-LLM intelligence
- Explainable decision making
- Engineering judgment and trade-offs

The system explicitly **does NOT send raw images directly to an LLM**.  
Instead, it extracts meaningful visual signals first and then reasons over them.

---

## 🎯 Problem Statement

> Given an image, assess whether it is suitable for use as a **primary e-commerce product image**, and explain why.

---

## 🧱 System Architecture

┌──────────────┐
│  Image Input │
└──────┬───────┘
       │
       ▼
┌────────────────────────────┐
│ Visual Feature Extraction  │
│ (Pre-LLM Intelligence)     │
│                            │
│ • Object Detection (YOLO)  │
│ • Face Detection (OpenCV)  │
│ • OCR (Tesseract)          │
│ • Blur Score               │
│ • Brightness               │
└──────────┬─────────────────┘
           │
           ▼
┌────────────────────────────┐
│ Feature Aggregation        │
│ (Structured JSON)          │
└──────────┬─────────────────┘
           │
           ▼
┌────────────────────────────┐
│ Reasoning Layer            │
│ (LLM or Rule-based)        │
│                            │
│ • No raw image input       │
│ • Uses extracted features │
└──────────┬─────────────────┘
           │
           ▼
┌────────────────────────────┐
│ Final Explainable Output   │
│                            │
│ • Quality score            │
│ • Issues detected          │
│ • Final verdict            │
│ • Confidence               │
└────────────────────────────┘

## 🔍 Pre-LLM Features Extracted

| Feature | Why it Matters |
|------|---------------|
| Object detection | Detects products vs clutter / hands |
| Face detection | Faces imply lifestyle / informal images |
| OCR | Detects branding or packaging text |
| Blur score | Measures image sharpness |
| Brightness | Measures lighting quality |

These signals are **objective, interpretable, and fast**.

---

## 🤖 Reasoning Layer

The reasoning layer:
- Receives **only structured features**
- Makes **non-trivial judgments**
- Produces **machine-readable output**

If LLM quota is unavailable, a **rule-based fallback** is used to ensure the pipeline still works end-to-end.

---

## 📦 Example Output

```json
{
  "image_quality_score": 0.74,
  "issues_detected": [
    "human face detected",
    "low lighting",
    "image blur"
  ],
  "final_verdict": "Not suitable for PRIMARY e-commerce product image",
  "confidence": 0.85
}

⚙️ How to Run (Local – VS Code)
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run pipeline

python pipeline.py --image sample_images/image_test.jpg

