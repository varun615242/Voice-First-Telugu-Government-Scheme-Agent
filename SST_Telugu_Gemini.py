import base64
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyBRWST5R3JJee7QH2v1KeYt_BP7wEZ3aac")

model = genai.GenerativeModel("models/gemini-3-flash-preview")

def transcribe_telugu_gemini(audio_path: str) -> str:
    """
    Telugu Speech-to-Text using Gemini Audio understanding.
    """

    with open(audio_path, "rb") as f:
        audio_bytes = f.read()

    audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")

    response = model.generate_content([
        {
            "mime_type": "audio/mp4",
            "data": audio_base64
        },
        "Please accurately transcribe the above Telugu audio. and give the telugu output in english phonetics"
    ])

    return response.text


# -------------------------------
# Example Run
# -------------------------------
if __name__ == "__main__":
    audio_file = "audios/a1.mp4"
    text = transcribe_telugu_gemini(audio_file)

    print("Telugu Transcription:")
    print(text)