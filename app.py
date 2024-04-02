import streamlit as st
import speech_recognition as sr
import pyttsx3

# Initialize recognizer class (for recognizing speech)
recognizer = sr.Recognizer()

# Initialize pyttsx3 engine for speech output
engine = pyttsx3.init()

# Set properties for speech output (optional)
engine.setProperty('rate', 150)  # Speed of speech

# Function to recognize speech and display result
def recognize_speech():
    with sr.Microphone() as source:
        st.write("Listening...")
        recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
        audio_text = recognizer.listen(source, timeout=5)  # Set a timeout of 5 seconds

        try:
            st.write("Recognizing...")
            text = recognizer.recognize_google(audio_text)
            st.success("You said: " + text)

            # Convert recognized text to speech
            engine.say("You said: " + text)
            engine.runAndWait()
        except sr.UnknownValueError:
            st.error("Sorry, I did not understand what you said")
            engine.say("Sorry, I did not understand what you said")
            engine.runAndWait()
        except sr.RequestError:
            st.error("Sorry, I'm unable to access the Google Speech Recognition API")
            engine.say("Sorry, I'm unable to access the Google Speech Recognition API")
            engine.runAndWait()

# Streamlit app layout
st.title("Voice Recognition App")
st.write("Speak into your microphone:")
recognize_button = st.button("Recognize Speech")

# Event handler for the Recognize Speech button
if recognize_button:
    recognize_speech()
