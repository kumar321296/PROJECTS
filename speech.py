import speech_recognition as sr
import pyttsx3
import subprocess
import os
import webbrowser

engine = pyttsx3.init()
recognizer = sr.Recognizer()
opened = set()  # Track opened apps/websites

def speak(text):
    print(f"Vani: {text}")
    engine.say(text)
    engine.runAndWait()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio).lower()
        print(f"You said: {query}")
        return query
    except:
        speak("Sorry, I didn't catch that.")
        return ""

def open_app(command):
    user = os.getlogin()

    apps = {
        "notepad": "notepad.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vscode": fr"C:\Users\{user}\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "spotify": fr"C:\Users\{user}\AppData\Roaming\Spotify\Spotify.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe"
    }

    for app in apps:
        if f"open {app}" in command:
            if app in opened:
                speak(f"{app.capitalize()} is already opened.")
            else:
                try:
                    subprocess.Popen(apps[app])
                    speak(f"Opening {app}")
                    opened.add(app)
                except:
                    speak(f"Sorry, I can't open {app}")
            return True

    # Websites
    if "open youtube" in command:
        if "youtube" in opened:
            speak("YouTube is already opened.")
        else:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube")
            opened.add("youtube")
        return True

    if "open google" in command:
        if "google" in opened:
            speak("Google is already opened.")
        else:
            webbrowser.open("https://www.google.com")
            speak("Opening Google")
            opened.add("google")
        return True

    return False

def main():
    speak("Hello! I am Vani. How can I help you?")
    while True:
        command = listen()

        if command == "":
            continue

        if "exit" in command or "quit" in command or "stop" in command:
            speak("Goodbye!")
            break

        if not open_app(command):
            speak("I can only open apps or websites. Try saying 'open notepad' or 'open Chrome'.")

if __name__ == "__main__":
    main()
