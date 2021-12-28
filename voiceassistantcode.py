import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()

init_command = 'zaid'
# list of actions
actions = ['play', 'time', 'whois', 'information', 'country', 'joke']


def talk(text):
    '''This function is for instructing the machine to talk'''
    engine.say(text)
    engine.runAndWait()


def play(song: str):
    talk('playing' + song)
    pywhatkit.playonyt(song)


def time():
    time = datetime.datetime.now().strftime('%H:%M %p')
    talk('The time right now is ' + time)


def whois(person):
    info = wikipedia.summary(person, 2)
    print(info)
    talk('This is what I found on the internet. ' + info)


def information(person):
    info = wikipedia.summary(person, 2)
    print(info)
    talk(info)


def country():
    talk('I am not from a country, I was made in Python')


def joke():
    talk(pyjokes.get_joke())


def get_command():
    """
    Initiate the voice commander
    """
    try:
        with sr.Microphone() as source:
            print('listening now...')
        voice = listener.listen(source)
        if voice:
            command = listener.recognize_google(voice)
            if command:
                command = command.lower()
    except sr.UnknownValueError:
        print("Audio Unintelligible")
    return command


def extract_commands(command: str):
    command_list = command.split(" ")  # ['zaid', 'play', 'song']
    if command_list:
        if command_list[0] != init_command:()
    return "Please say zaid!"

    action = command_list[1]
    if action not in actions:()


    return 'Sorry, none of the commands match what you said'

eval(action + "()")
else:
talk('I did not understand what you said, can you please repeat?')

while True:
    run_zaid()
