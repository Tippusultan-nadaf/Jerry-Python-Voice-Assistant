import speech_recognition as sr
import webbrowser
import pyttsx3
import songs
 

#  modules
# 1) setuptools
# 2) speech_recognition pyaudio
# 3) pyttsx3

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def process_Command(command):
    if command =="open youtube":
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif command=="open google":
        speak("opening google")
        webbrowser.open("https://www.google.com/")
    elif command=="open whatsapp":
        speak("opening whatspp")
        webbrowser.open("https://www.whatsapp.com/")
    elif command=="open linkedin":
        speak("opening linkedin")
        webbrowser.open("https://www.linkedin.com/")
    elif command=="open naukri":
        speak("opening naukri.com")
        webbrowser.open("https://www.naukri.com/")
    elif command.startswith("play"):
        song=command.split(" ")[1]
        link=songs.music[song]
        webbrowser.open(link)


if __name__ == "__main__":
    
    while True:   
        try:
            with sr.Microphone() as source:
                recognizer.adjust_for_ambient_noise(source, duration=2)
                print("listening....")
                audio=recognizer.listen(source)
            j = recognizer.recognize_google(audio).lower()
            print(j)
            if j =="hey jerry" or j=="hey siri":
                speak("hi this is your personal assistant Jerry, how may i help you")
                with sr.Microphone() as source:
                    recognizer.adjust_for_ambient_noise(source, duration=2)
                    print("listening to command")
                    audio=recognizer.listen(source, timeout=2,phrase_time_limit=2)
                command = recognizer.recognize_google(audio).lower()
                print(command)
                process_Command(command)


                

        except Exception as e:
            print("Error i could not understand")
 