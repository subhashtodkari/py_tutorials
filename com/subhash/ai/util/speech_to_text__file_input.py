import speech_recognition as sr


if __name__ == "__main__":
    print(sr.__version__)
    r = sr.Recognizer()
    file = "cache/harvard.wav"
    harvard = sr.AudioFile(file)
    with harvard as source:
        audio = r.record(source)
        text = r.recognize_google(audio)
        print(file + " >> " + text)
