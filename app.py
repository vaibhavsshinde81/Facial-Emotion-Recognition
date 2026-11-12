import streamlit as st
import numpy as np
import cv2
from PIL import Image
from deepface import DeepFace

st.set_page_config(
    page_title="Facial Emotion Recognition",
    page_icon="😊",
    layout="centered"
)

st.title("😊 Facial Emotion Recognition")
st.write("Upload a face photo or take a picture with your camera to estimate the facial expression.")

st.info(
    "Demo note: This app predicts an emotion from a still image. "
    "It is an AI estimate, not a reliable measure of a person's actual feelings."
)

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)
camera_file = st.camera_input("Or take a photo")

image_file = camera_file if camera_file is not None else uploaded_file

if image_file is not None:
    try:
        image = Image.open(image_file).convert("RGB")
        image_array = np.array(image)

        st.image(image, caption="Image selected", use_container_width=True)

        if st.button("Analyze emotion", type="primary"):
            with st.spinner("Loading the AI model and analyzing the face..."):
                # DeepFace expects an image array. The first run may take longer
                # because the emotion model needs to be downloaded.
                results = DeepFace.analyze(
                    img_path=image_array,
                    actions=["emotion"],
                    detector_backend="opencv",
                    enforce_detection=True,
                    silent=True
                )

                if isinstance(results, dict):
                    results = [results]

                annotated = cv2.cvtColor(image_array, cv2.COLOR_RGB2BGR)

                st.subheader("Analysis result")
                for index, result in enumerate(results, start=1):
                    emotion = result.get("dominant_emotion", "Unknown")
                    scores = result.get("emotion", {})
                    area = result.get("region", result.get("facial_area", {}))

                    x = int(area.get("x", 0))
                    y = int(area.get("y", 0))
                    w = int(area.get("w", 0))
                    h = int(area.get("h", 0))

                    if w > 0 and h > 0:
                        cv2.rectangle(annotated, (x, y), (x + w, y + h), (0, 180, 255), 2)
                        cv2.putText(
                            annotated, emotion, (x, max(25, y - 10)),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 180, 255), 2
                        )

                    st.markdown(f"**Face {index}: {emotion.title()}**")
                    if scores:
                        st.write("Emotion scores (model estimates):")
                        st.bar_chart(scores)

                st.image(
                    cv2.cvtColor(annotated, cv2.COLOR_BGR2RGB),
                    caption="Detected face(s) and predicted emotion(s)",
                    use_container_width=True
                )

    except ValueError as error:
        st.error("No clear face was detected. Try a front-facing photo with good lighting.")
        st.caption(str(error))
    except Exception as error:
        st.error("Analysis failed. Please try another image or retry in a moment.")
        st.caption(f"Technical detail: {type(error).__name__}: {error}")

st.divider()
st.caption("Built with Python, Streamlit, OpenCV and DeepFace.")
