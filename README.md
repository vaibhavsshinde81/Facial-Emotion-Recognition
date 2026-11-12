---
title: Facial Emotion Recognition
emoji: 😊
colorFrom: blue
colorTo: purple
sdk: docker
app_port: 7860
---

# Facial Emotion Recognition — Web Demo

This version adapts the original webcam-only OpenCV script into a browser app.

## Features
- Upload a JPG/PNG photo.
- Take a photo using the browser camera.
- Detect faces and estimate facial emotion with DeepFace.
- Display the predicted emotion and model scores.

> This is a still-image demo, not continuous real-time video. Emotion predictions are estimates and should not be treated as facts about someone's internal feelings.

## Run locally (Windows)

1. Install Python 3.11 (64-bit).
2. Extract this folder.
3. Open Command Prompt in this folder.
4. Create and activate a virtual environment:

   ```bash
   py -3.11 -m venv .venv
   .venv\\Scripts\\activate
   ```

5. Install packages:

   ```bash
   python -m pip install --upgrade pip
   pip install -r requirements.txt
   ```

6. Start the app:

   ```bash
   streamlit run app.py
   ```

7. Open the local URL shown in the terminal (usually http://localhost:8501).

The first analysis may take longer because DeepFace downloads its model weights.

## Deploy publicly with Hugging Face Spaces

1. Create/sign in to an account at https://huggingface.co/.
2. Open https://huggingface.co/new-space.
3. Enter a Space name such as `facial-emotion-recognition`.
4. For SDK, choose **Docker** (Hugging Face currently recommends Docker for Streamlit deployments because the built-in Streamlit SDK is deprecated).
5. Set visibility to **Public** and choose an available CPU hardware option.
6. Create the Space.
7. Upload all files from this folder: `app.py`, `requirements.txt`, `Dockerfile`, and this `README.md`.
8. Wait for the build to finish. Open the **App** tab.
9. Your public URL will look like `https://YOUR-USERNAME-facial-emotion-recognition.hf.space`.

If the build fails due to memory or dependency limits, check the build logs first. DeepFace/TensorFlow is relatively heavy; a larger CPU instance may be needed. Do not upload private or sensitive face images to a public demo.
