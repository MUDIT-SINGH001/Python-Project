import PyAudio
import pyttsx3
import pyttsx
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import psutil
import pyautogui
import os
import wmi
import sys
import time
import ctypes
import getpass

INFO = '''
        *=======================================*
        |   ....ARTIFICIAL INTELLIGENCE.....    |
        +---------------------------------------+
        |#Name: NOT DECIDED        		|
        |#Owner: ANIMESH SINHA                  |
        |#Date: -/-/-(UNDER TESTING)            |
        *=======================================*
        '''
print(INFO)


engine = pyttsx.init('sapi5')

client = wolframalpha.Client('V9A93E-GP32YA8GJL')

voices = engine.getProperty('voices')
engine.setProperty('rate', 150)
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Computer: ' + audio)
    engine.say(audio)
    engine.runAndWait()

    
def Greetme():
      time=int(datetime.datetime.now().hour)
      if time>=0 and time<12:
       speak('Good Morning '+username)
      if time>=12 and time<18:
       speak('Good Afternoon '+username)
      if time>=18 and time!=0:
       speak('Good Evening '+username)


def brightness(query):
	if 'decrease ' in query:
		print ('ok listen.......')
		dec = wmi.WMI(namespace='wmi')
		methods = dec.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(30, 0)
	elif 'increase ' in query:
		print ('ok listen.......')
		ins = wmi.WMI(namespace='wmi')
		methods = ins.WmiMonitorBrightnessMethods()[0]
		methods.WmiSetBrightness(100, 0)
                    

def secs2hours(secs):
    mm, ss = divmod(secs, 60)
    hh, mm = divmod(mm, 60)
    return "%d hour, %02d minute, %02s seconds" % (hh, mm, ss)


def mycommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the command!')
        query = str(input('Command: '))

    return query


def username():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = str(input('Username: '))
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the Username!')
        query = str(input('Username: '))

    return query


def password():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        query = str(input('Password: '))
        query = getpass.getpass()
        
    except sr.UnknownValueError:
        speak('Sorry sir! I didn\'t get that! Try typing the Password!')
        query = str(input('Password: '))
        query = getpass.getpass()
        

    return query
       
speak('Welcome Sir or Mam')
speak('enter your username to connect to your database')




#when file is there this will run
username=username()
try:
    f=open("username.txt" , "r")
    val_name=f.read()
    if username in val_name:
        speak('welcome ' + username)
        speak('please speak password for accessing your database')
        password=password()
        f=open("password.txt" , "r")
        val_pass=f.read()
        if password in val_pass:
            speak("logged in successfully")
            speak('setting up your environment , setting up , installing some requirnments')
            speak('Hello Sir!')
            Greetme()
            f.close()
        else:
            speak("password doesn\'t match")
            speak("try again , this is last try")
            speak('re-try: ')
            pwd='0'
            while(pwd!='1'):
                password=password()
                val_pass=f.read()
                if password in val_pass:
                    speak("logged in successfully")
                    speak('setting up your environment , setting up , installing some requirnments')
                    speak('Hello Sir!')
                    Greetme()
                    f.close()
                    pwd='1'
                else:
                    speak("want to try again yes or no")
                    query=mycommand()
                    if 'yes' in query:
                        pwd='0'
                    else:
                        pwd='1'
    else:
        speak("didn\'t get you in my database")
        speak("want to create your profile yes or no")
        query=mycommand()
        if 'yes' in query:
          ans='yes'
          while(ans!='no'):
              f=open("username.txt","w+")
              speak('enter your username: ')
              username=username()
              f.write(username)
              speak("username saved")
              speak("want to change it? yes or no")
              query=mycommand()
          f.close()

          query='yes'
          while(query!='no'):
            f=open("password.txt","w+")
            speak('enter your password: ')
            password=password()
            f.write(password)
            speak("password saved")
            speak("want to change it? yes or no")
            query=mycommand()
          speak("password updated")
          f.close()
        
#when file is not there this will run

        
except FileNotFoundError:


#username change and update
  speak("didn\'t get you in my database")
  speak("want to create your profile yes or no")
  query=mycommand()
  if 'yes' in query:
    while(query!='no'):
      f=open("username.txt","w+")
      speak('enter your username')
      username=username()
      f.write(username)
      speak("username saved")
      speak("want to change it? yes or no")
      query=mycommand()
    f.close()
#password change and update
    query='yes'
    while(query!='no'):
        f=open("password.txt","w+")
        speak('enter your password: ')
        password=password()
        f.write(password)
        speak("password saved")
        speak("want to change it? yes or no")
        query=mycommand()
    speak("password updated")
    f.close()
    

speak('how may i help you ' + username)
if __name__ == "__main__":
 while True:

    query = mycommand();
    query = query.lower()

    if 'hi' in query or 'hey' in query or 'hii' in query or 'hello' in query:
          myList=["hi!" , "hey!" , "hello!" , "hey there"]
          speak(random.choice(myList))

    elif 'who is your creator' in query or 'who invented you?' in query or 'who invented you' in query or 'who is your creator?' in query:
          CList=["Animmesh Sinha" , "I am invented by Animesh Sinha" , "my creator is Animesh Sinha"]
          speak(random.choice(CList))

    elif 'open cmd' in query or 'cmd' in query:
          speak('opening CMD(Command Promt)...')
          command=input('enter your command: ')
          os.system('cmd.exe')
    elif 'open firefox' in query or 'firefox' in query:
          speak('opening firefox...')
          os.startfile('firefox.exe')

    elif 'open google chrome' in query or 'open chrome' in query or 'chrome' in query:
          speak('opening Google Chrome...')
          os.startfile('chrome.exe')

    elif 'i want to code something any application for it' in query or 'application for coding' in query or 'application for programming ' in query or 'notepad\'++' in query:
          speak('opening Notepad++...')
          os.startfile('notepad++.exe')

    elif 'open notepad' in query or 'notepad' in query or 'i want to write something' in query or 'i want to note something' in query:
          speak('opening notepad...')
          os.startfile('notepad.exe')

#open default webbrowser and search whatever you search

          
    elif 'i want  to search something' in query or 'search on google' in query or 'search' in query:
        a='yes'
        while(a!='no'):
          url="http://google.com/?#q="
          search=input('enter your search query: ')
          speak('opening your browser and searching your input...')
          webbrowser.open(url+search)
          speak("search completed!!!")
          a=input('want to search more yes/no: ')

    elif 'email' in query:
         speak('Who is the recipient? ')
         recipient = myCommand()

         if 'me' in recipient:
            try:
             speak('What should I say? ')
             content = myCommand()
        
             server = smtplib.SMTP('smtp.gmail.com', 587)
             server.ehlo()
             server.starttls()
             server.login("Your_Username", 'Your_Password')
             server.sendmail('Your_Username', "Recipient_Username", content)
             server.close()
             speak('Email sent!')

            except:
             speak('Sorry Sir! I am unable to send your message at this moment!')

    elif 'nothing' in query or 'abort' in query or 'stop' in query or 'exit' in query:
        
             speak('okay')
             speak('Bye Sir, have a good day.')
             sys.exit()

    elif 'translate' in query:
         speak('in which language you want to translate')
         query = str(input('language: '))
         if english in query:
            translator= Translator(to_lang="en")
            translation = translator.translate(query)
    
         elif chinese in query:
            translator= Translator(to_lang="zh")
            translation = translator.translate(query)
            

    elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('Okay, here is your music! Enjoy!')

    elif 'open website' in query:
        reg_ex = re.search('open website (.+)', command)
        if reg_ex:
            domain = reg_ex.group(1)
            url = 'https://www.' + domain
            webbrowser.open(url)
            print('Done!')
        else:
            pass


    elif 'lock' in query:
            speak('ok, sir')
            ctypes.windll.user32.LockWorkStation()


    elif 'screenshot' in query or 'screen shot' in query or 'snapshot' in query:
            speak('ok, sir let me take a snapshot ')
            speak('ok done')
            speak('check your desktop, i saved there')
            pic = pyautogui.screenshot()
            pic.save('C:/Users/Animesh/Desktop/Screenshot.png')


    elif 'who are you' in query:
            speak('i am not really a person, i am  a i robot')
            speak('i had prefer to think of myself as your friend')


    elif 'brightness' in query:
            brightness(query)
            speak('okay sir! customising your brightness setting accessin to your setting okay sir now tell me what to do increase or decrease?')


    elif 'time' in query:
            current_time = time.strftime("%d:%B:%Y:%A:%H:%M:%S")
            print (current_time)
            speak('sir, today date is ' + time.strftime("%d:%B:%Y"))
            speak (time.strftime("%A"))
            speak('and time is ' + time.strftime("%H:%M:%S"))


    elif 'charge' in query or 'what\'s the battery status' in query or 'what is the battery status' in query or 'what is your enery status' in query:
            battery = psutil.sensors_battery()
            plugged = battery.power_plugged
            percent = int(battery.percent)
            time_left = secs2hours(battery.secsleft)
            print (percent)
            if percent < 40 and plugged == False:
                static_speech('sir, please connect charger because i can survive only ' + time_left)
            if percent < 40 and plugged == True:
                speak("don't worry, sir charger is connected")
            else:
                speak('sir, no need to connect the charger because i can survive ' + time_left)
                   
                   

    else:
            query = query
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('Got it.')
                    speak(results)
                    
                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('searching...')
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)
        
            except:
                a='yes'
                while(a!='no'):
                    url="http://google.com/?#q="
                    speak('opening your browser and searching your input...')
                    webbrowser.open(url+query)
                    speak("search completed!!!")
                    speak('want to search more yes/no: ')
                    a=mycommand()
                    webbrowser.open('www.google.com')


 speak('Next Command! Sir!') 
