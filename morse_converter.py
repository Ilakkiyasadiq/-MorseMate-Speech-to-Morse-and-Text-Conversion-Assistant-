import speech_recognition as sr

# Function to convert text to Morse code
def convert_morse(code):
    morse_dict = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".",
        "f": "..-.", "g": "--.", "h": "....", "i": "..", "j": ".---",
        "k": "-.-", "l": ".-..", "m": "--", "n": "-.", "o": "---",
        "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
        "u": "..-", "v": "...-", "w": ".--", "x": "-..-", "y": "-.--",
        "z": "--..", "1": ".----", "2": "..---", "3": "...--",
        "4": "....-", "5": ".....", "6": "-....", "7": "--...",
        "8": "---..", "9": "----.", "0": "-----", ",": "--..--",
        ".": ".-.-.-", "?": "..--..", "/": "-..-.", "-": "-....-",
        "(": "-.--.", ")": "-.--.-"
    }
    return " ".join([morse_dict.get(char.lower(), char) for char in code])

# Speech recognition setup
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Talk")
    audio = r.listen(source)
    print("Time over, processing your input.")

try:
    msg = r.recognize_google(audio)
    print(f"Initial text: {msg}")
    morse = convert_morse(msg)
    print(f"Morse code: {morse}")
except Exception as e:
    print("Error processing audio:", e)
