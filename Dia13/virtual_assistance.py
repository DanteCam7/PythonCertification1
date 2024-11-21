import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# listen microphone and return audio as text
def transform_audio_into_text():
    # keep recognizer in variable
    r = sr.Recognizer()

    # configure microphone
    with sr.Microphone() as origin:
        r.pause_threshold = 0.8

        # notify recording started
        print('You can talk now')

        # save the audio
        audio = r.listen(origin)

    try:
        # search in google
        request = r.recognize_google(audio, language="en")

        # test if it was possible
        print("You said: " + request)

        # return request
        return request
    # incomprehensible audio error
    except sr.UnknownValueError:
        # test incomprehensible audio
        print("ERROR, COULDN'T UNDERSTAND")

        # return error
        return "Keep waiting"

    # couldn't solved request
    except sr.RequestError:

        # test to solve audio
        print("Couldn't solved it")

        # return error
        return "Keep waiting"

    # unexpected error
    except:

        # test of error
        print("Failed")

        # return error
        return "ERROR"


# voice options
id1 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0'
id2 = 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0'


# method for assistant can be heard
def speak(message):
    # turn on pyssx3 motor
    engine = pyttsx3.init()
    engine.setProperty('voice', id1)

    # pronounce messsage
    engine.say(message)
    engine.runAndWait()


# give the day
def ask_day():
    # create today variable
    day = datetime.date.today()
    print(day)

    # create variable for the week day
    week_day = day.weekday()
    print(week_day)

    # dictionary of days with names
    calendary = {0: 'Monday',
                 1: 'Tuesday',
                 2: 'Wednesday',
                 3: 'Thursday',
                 4: 'Saturday',
                 5: 'Friday',
                 6: 'Sunday'}

    # say day of the week
    speak(f'Today is {calendary[week_day]}')


# give the hour
def ask_hour():
    # create variable with hour
    hour1 = datetime.datetime.now()
    hour = f'''It's {hour1.hour} with {hour1.minute} minutes and {hour1.second} seconds'''
    print(hour)

    # say hour
    speak(hour)


# greetings
def greetings():
    # create variable with hour
    hour1 = datetime.datetime.now()
    if hour1.hour < 6 or hour1.hour > 20:
        moment = 'Good night'
    elif 6 <= hour1.hour < 13:
        moment = 'Good morning'
    else:
        moment = 'Good Evening'

    # say the greetings
    speak(f'''Hi {moment}, i'm Zyra, your personal Assistant''')


# central function of the assistant
def ask_stuff():
    # active greetings
    greetings()

    # variable to cort
    start = True

    # central loop
    while start:
        # active the microphone and save it in a string
        request = transform_audio_into_text().lower()

        if 'open youtube' in request:
            speak('Sure, im opening YouTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'open browser' in request:
            speak('Sure, ill open it')
            webbrowser.open('https://www.google.com')
            continue
        elif 'open the sea' in request:
            speak('Sure, ill open the Integral Information System')
            webbrowser.open('https://sii.itcelaya.edu.mx/sii/index.php?r=cruge/ui/login')
            continue
        elif 'what day is it' in request:
            ask_day()
            continue
        elif 'what time is it' in request:
            ask_hour()
            continue
        elif 'tell me the day and the hour' in request:
            ask_day()
            ask_hour()
            continue
        elif 'search in wikipedia' in request:
            speak('Searching in wikipedia')
            request = request.replace('wikipedia', '')
            wikipedia.set_lang('en')
            result = wikipedia.summary(request, sentences=1)
            speak('Wikipedia says the next:')
            speak(result)
        elif 'search for' in request:
            speak('Im searching for it')
            request = request.replace(f'search for', '')
            pywhatkit.search(request)
            speak('This is what i found')
            continue
        elif 'reproduce' in request:
            speak('Ill reproduce it')
            pywhatkit.playonyt(request)
            continue
        elif 'joke' in request:
            speak(f'Great idea{pyjokes.get_joke('en')}')
            continue
        elif 'actions prices' in request:
            action = request.split('of')[-1].strip()
            wallet = {'apple': 'APPL',
                      'amazon': 'AMZN',
                      'goole': 'GOOGL'}
            try:
                action_searched = wallet[action]
                action_searched = yf.Ticker(action)
                price = action_searched.info['regularMarketPrice']
                speak(f'I found it, the price of {action} is {price}')
                continue
            except:
                speak('Sorry, o couldnt find it')
                continue
        elif 'see you later zaira' in request:
            speak('Ok, have a nice day')
            start = False
            continue


ask_stuff()
