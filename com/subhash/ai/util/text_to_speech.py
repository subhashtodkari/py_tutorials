from pathlib import Path

from gtts import gTTS
from playsound import playsound


def speak_word_by_word(text, lang='en'):
    cache_dir = Path("cache")
    if not cache_dir.is_dir():
        cache_dir.mkdir()

    tokens = text.split()
    for token in tokens:
        file_name = ''.join(e for e in token if e.isalnum())
        file_name = "cache/" + file_name.lower() + ".mp3"
        if not Path(file_name).is_file():
            print("requesting gTTS...")
            audio = gTTS(text=token, lang=lang, slow=False)
            audio.save(file_name)

    for token in tokens:
        file_name = ''.join(e for e in token if e.isalnum())
        file_name = "cache/" + file_name.lower() + ".mp3"
        playsound(file_name)


def speak_whole_sentence(text, lang='en'):
    cache_dir = Path("cache")
    if not cache_dir.is_dir():
        cache_dir.mkdir()

    file_name = ''.join(e for e in text if e.isalnum())
    file_name = "cache/" + file_name.lower() + ".mp3"
    if not Path(file_name).is_file():
        print("requesting gTTS...")
        audio = gTTS(text=text, lang=lang, slow=False)
        audio.save(file_name)
    playsound(file_name)


def speak(text, lang='en'):
    speak_whole_sentence(text, lang)


if __name__ == "__main__":
    message = "Hello World! Hello World!"
    speak(message)
    countDown = 15
    speak("Counting down from " + str(countDown))
    while countDown > 0:
        speak(str(countDown))
        countDown -= 1
    speak("Done!")
    speak("Good bye!")
