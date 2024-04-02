import speech_recognition as sr
import pyttsx3

# Initialize recognizer class (for recognizing speech)
recognizer = sr.Recognizer()

# Initialize pyttsx3 engine for speech output
engine = pyttsx3.init()

# Set properties for speech output (optional)
engine.setProperty('rate', 150)  # Speed of speech

# Reading Microphone as source
# Listening to the speech and storing it in the audio_text variable
with sr.Microphone() as source:
    print("Talk")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    audio_text = recognizer.listen(source, timeout=5)  # Set a timeout of 5 seconds

    # Recognize speech using Google Speech Recognition
    try:
        print("Recognizing...")
        text = recognizer.recognize_google(audio_text)
        print("You said:", text)

        # Convert recognized text to speech
        engine.say("You said: " + text)
        engine.runAndWait()
    except sr.UnknownValueError:
        print("Sorry, I did not understand what you said")
        engine.say("Sorry, I did not understand what you said")
        engine.runAndWait()
    except sr.RequestError:
        print("Sorry, I'm unable to access the Google Speech Recognition API")
        engine.say("Sorry, I'm unable to access the Google Speech Recognition API")
        engine.runAndWait()
