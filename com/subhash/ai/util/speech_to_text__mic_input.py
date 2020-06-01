import speech_recognition as sr
from speech_recognition import UnknownValueError


mic_idx = 1
mic_name = "Eva"
r = sr.Recognizer()
mic = sr.Microphone()   # sr.Microphone(device_index=mic_idx)


def listen():
    with mic as source:
        try:
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text_options = r.recognize_google(audio, show_all=True)
            if len(text_options) == 0:
                raise UnknownValueError()

            if len(text_options['alternative']) > 1:
                print("")
                print("I am confused between below options but I will go with first one:")
                print("")
                i = 0
                for option in text_options['alternative']:
                    print(i + 1, ". ", option['transcript'])
                    i += 1
                print("")

            transcript = text_options['alternative'][0]['transcript']
            print(" >> " + transcript)

            return transcript

        except UnknownValueError:
            print("Could not recognize what you have said, would you please come again?")


if __name__ == "__main__":
    print(sr.__version__)
    '''
    print("Microphones available: ")
    i = 0
    mics = sr.Microphone.list_microphone_names()
    for mic_name in mics:
        print(i, " - ", mic_name)
        i += 1
    print("")
    '''

    text = listen()
    print("You said: ", text)
