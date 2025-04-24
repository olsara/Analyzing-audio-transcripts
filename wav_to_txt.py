import os
import speech_recognition as sr

def convert_wav_to_txt(folder_path):
    recognizer = sr.Recognizer()

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".wav"):
            filepath = os.path.join(folder_path, filename)
            print(f"Transcribing: {filename}")

            with sr.AudioFile(filepath) as source:
                audio = recognizer.record(source)

                try:
                    # You can also try recognizer.recognize_google_cloud(), .recognize_sphinx(), etc.
                    text = recognizer.recognize_google(audio)
                    txt_filename = filename.replace(".wav", ".txt")
                    txt_filepath = os.path.join(folder_path, txt_filename)

                    with open(txt_filepath, "w", encoding="utf-8") as f:
                        f.write(text)

                    print(f"Saved transcription to: {txt_filepath}")
                except sr.UnknownValueError:
                    print("Could not understand audio")
                except sr.RequestError as e:
                    print(f"API request error: {e}")

if __name__ == "__main__":
    folder = input("Enter the path to the folder with .wav files: ").strip()
    if os.path.isdir(folder):
        convert_wav_to_txt(folder)
    else:
        print("Invalid folder path.")
