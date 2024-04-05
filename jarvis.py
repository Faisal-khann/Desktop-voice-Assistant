# import time
# import pyautogui
# import pyttsx3
# import datetime
# import speech_recognition as sr
# import wikipedia
# import webbrowser
# import os
# import subprocess
# import requests
# import pywhatkit as kit
# import pyautogui
# import sys
# import instadownloader
# from PyQt5.QtCore import QThread
# from PyQt5 import QtWidgets, QtCore, QtGui
# from PyQt5.QtCore import QTimer, QTime, QDate, Qt
# from PyQt5.QtGui import QMovie
# from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *
# from PyQt5.uic import loadUiType
# from jarvisUi import Ui_jarvisUi # import the complete class of ui file

# class MainThread(QThread):
#     def __init__(self):
#         super(MainThread, self).__init__()

#         # Initialize pyttsx3 engine
#         self.engine = pyttsx3.init("sapi5")
#         self.voices = self.engine.getProperty("voices")
#         # print(voices[1].id)
#         # set id of voices
#         self.engine.setProperty("voice", self.voices[0].id)

#     def run(self):
#         self.TaskExecution()

#     # take command function
#     def takecommand(self):
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("listening...")
#             r.pause_threshold = 1
#             audio = r.listen(source)

#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language="en-in")
#             print(f"user said: {query}")

#         except Exception as e:
#             self.speak("Say that again please....")
#             return "none"
#         return query
    
#     # speak function
#     def speak(self, text):
#        self.engine.say(text)
#        self.engine.runAndWait()

#     # wish me function
#     def wishMe(self):
#         currTime = datetime.datetime.now().strftime("%I:%M:%S %p") # %I for 12-hour format, %p for AM/PM
#         hour = int(datetime.datetime.now().hour)

#         if 0 <= hour < 12:
#             message = f"Good Morning, it's {currTime}"
#         elif 12 <= hour < 18:
#             message = f"Good Afternoon, it's {currTime}"
#         else:
#             message = f"Good Evening, it's {currTime}"

#         print(message)
#         self.speak(message)

#         print("I am Jarvis Sir. Please tell me how may I help you.")
#         self.speak("I am Jarvis Sir. Please tell me how may I help you.")
    
#     # youtube playing function
#     def play_on_youtube(self, video):
#         kit.playonyt(video)
#     # Send Whatsapp message function
#     def send_whatsapp_message(self, number, message):
#         kit.sendwhatmsg_instantly(f"+91{number}", message)

#     def TaskExecution(self):
#         self.wishMe()
#         while True:
#             # if 1:
#             self.query = self.takecommand().lower()  # Converting user query into lower case

#             # Logic for executing tasks based on query.....
#             if "wikipedia" in self.query:
#                 self.speak("Searching Wikipedia...")
#                 self.query = self.query.replace("wikipedia", "")
#                 results = wikipedia.summary(self.query, sentences=3)
#                 self.speak("According to Wikipedia")
#                 print(results)
#                 self.speak(results)

#             elif "open youtube" in self.query:
#                 self.speak("sir, what should I search on YouTube")
#                 video = self.takecommand().lower()
#                 self.play_on_youtube(video)
#                 # webbrowser.open(f"{yt}")
#                 # webbrowser.open("youtube.com")

#             # .........Open Instagram.........#
#             elif "open instagram" in self.query:
#                 webbrowser.open("instagram.com")

#             # ......Check Instagram profile of any account...........#
#             elif "instagram profile" in self.query or "profile on instagram" in self.query:
#                 self.speak("Sir, please enter the username correctly:")
#                 name = input(
#                     "Enter the username:"
#                 )  # Assuming you're running this code in a console
#                 webbrowser.open(f"https://www.instagram.com/{name}")
#                 self.speak(f"Sir, here is the profile of the user {name}")
#                 time.sleep(5)

#                 self.speak("Sir, would you like to download the profile picture of this account?")
#                 condition = self.takecommand().lower()
#                 if "yes" in condition:
#                     mod = instadownloader.InstaDownloader()
#                     mod.download_profile(name, profile_pic_only=True)
#                     self.speak(
#                         "I am done, sir. The profile picture is saved in our main folder. Now I am ready for a new command."
#                     )

#             elif "open vs code" in self.query:
#                 codePath = (
#                     "C:\\Users\\faisa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
#                 )
#                 os.startfile(codePath)

#             elif "close vs code" in self.query:
#                 self.speak("Okay sir, closing vs code")
#                 os.system("taskkill /f /im Code.exe")


#             # ......To set the alarm.....#
#             elif "set alarm" in self.query:
#                 al = int(datetime.datetime.now().hour)
#                 if al == 22:  # check time for alarm
#                     music_dir = "C:\\Users\\fais a\\Music"
#                     song = os.listdir(music_dir)
#                     os.startfile(os.path.join(music_dir, song[1]))
import time
import pyautogui
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import subprocess
import requests
import pywhatkit as kit
import sys
import instadownloader
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtCore import QThread
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisUi import Ui_jarvisUi  # import the complete class of ui file

class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()

        # Initialize pyttsx3 engine
        self.engine = pyttsx3.init("sapi5")
        self.voices = self.engine.getProperty("voices")
        self.engine.setProperty("voice", self.voices[0].id)

    def run(self):
        self.TaskExecution()

    # take command function
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"user said: {query}")
            return query.lower()  # Convert query to lowercase
        except Exception as e:
            self.speak("Sorry, I couldn't understand. Can you repeat that?")
            return "none"

    # speak function
    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()

    # wish me function
    def wishMe(self):
        currTime = datetime.datetime.now().strftime("%I:%M:%S %p") # %I for 12-hour format, %p for AM/PM
        hour = int(datetime.datetime.now().hour)

        if 0 <= hour < 12:
            message = f"Good Morning, it's {currTime}"
        elif 12 <= hour < 18:
            message = f"Good Afternoon, it's {currTime}"
        else:
            message = f"Good Evening, it's {currTime}"

        print(message)
        self.speak(message)

        print("I am Jarvis Sir. Please tell me how may I help you.")
        self.speak("I am Jarvis Sir. Please tell me how may I help you.")
    
    # youtube playing function
    def play_on_youtube(self, video):
        kit.playonyt(video)

    # Send Whatsapp message function
    def send_whatsapp_message(self, number, message):
        kit.sendwhatmsg_instantly(f"+91{number}", message)

    def TaskExecution(self):
        self.wishMe()
        while True:
            self.query = self.takecommand()  # Converting user query into lower case

            # Logic for executing tasks based on query.....
            if "wikipedia" in self.query:
                self.speak("Searching Wikipedia...")
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=3)
                self.speak("According to Wikipedia")
                print(results)
                self.speak(results)

            elif "open youtube" in self.query:
                self.speak("What should I search on YouTube?")
                video = self.takecommand()
                self.play_on_youtube(video)

            elif "send whatsapp message" in self.query:
                self.speak("On what number should I send the message sir?")
                number = input("Enter the number: ")
                self.speak("What is the message sir?")
                message = self.takecommand()
                self.send_whatsapp_message(number, message)
                self.speak("I've sent the message sir.")

            elif "open google" in self.query:
                self.speak("sir, what should i search on google")
                cm = self.takecommand().lower()
                webbrowser.open(f"{cm}")
            
            elif "open camera" in self.query:
                subprocess.run("start microsoft.windows.camera:", shell=True)

            elif "close camera" in self.query:
                self.speak("Okay sir, closing camera")
                os.system("taskkill /f /im WindowsCamera.exe")

            elif "open notepad" in self.query:
                os.startfile("C:\\Users\\faisa\\Desktop\\Notepad.lnk")

            elif "close notepad" in self.query:
                self.speak("Okay sir, closing notepad")
                os.system("taskkill /f /im notepad.exe")

            elif "open command prompt" in self.query:
                os.system("start cmd")

            elif "the current time" in self.query:
                strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
                print(f"Sir, the time is {strTime}")
                self.speak(f"Sir, the time is {strTime}")

            # ......Switch the window section..........#
            elif "switch the window" in self.query:
                try:
                    pyautogui.keyDown("alt")
                    pyautogui.press("tab")
                    time.sleep(1)
                except Exception as e:
                    self.speak("Sorry, I encountered an error while switching windows.")
                    print("Error occurred while switching the window:", e)
                finally:
                    pyautogui.keyUp("alt")

            elif "switch back" in self.query:
                try:
                    pyautogui.keyDown("alt")
                    pyautogui.keyDown("shift")
                    pyautogui.press("tab")
                    time.sleep(1)
                except Exception as e:
                    self.speak(
                        "Sorry, I encountered an error while switching back to the previous window."
                    )
                    print("Error occurred while switching back to the previous window:", e)
                finally:
                    pyautogui.keyUp("alt")
                    pyautogui.keyUp("shift")
            
            # Play the music
            elif "play music" in self.query:
                music_dir = "C:\\Users\\faisa\\Music"
                songs = os.listdir(music_dir)
                os.startfile(
                    os.path.join(music_dir, songs[2])
                )  # Assuming you're playing the third song

            elif "stop music" in self.query:
                pyautogui.press("stop")  # Simulate pressing the spacebar to pause music

            elif "shutdown the music" in self.query:
                pyautogui.hotkey("alt", "F4")  # Simulate pressing Alt + F4 to close the current

             # ......To find my Ip Address........#
            elif "ip address" in self.query:
                try:
                    self.speak("Wait sir, let me check.")
                    ip = requests.get("https://api.ipify.org").text
                    self.speak(f"Your IP address is {ip}")
                    print("Your IP Address is ", ip)
                except requests.RequestException as e:
                    self.speak("Sorry, I couldn't retrieve your IP address at the moment.")
                    print("Error:", e)

             # ......To find my location using IP Address..........#
            elif "where i am" in self.query or "Where we are" in self.query:
                try:
                    self.speak("Wait sir, let me check.")

                    # Use the request module to get the public IP address of the machine using the ipify API
                    ip_address = requests.get("https://api.ipify.org").text

                    # Construct the URL for obtaining geographical information based on the IP address using the geojs.io API
                    url = "https://get.geojs.io/v1/ip/geo/" + ip_address + ".json"

                    # use 'requests' to send a GET request to the geojs.io API and get the geographic information in JSON format
                    geo_response = requests.get(url)
                    geo_response.raise_for_status()  # Raise an exception for HTTP errors

                    geo_data = geo_response.json()
                    # Extract relevant information from the JSON response
                    # state = geo_data["state"]
                    city = geo_data["city"]
                    country = geo_data["country"]
                    district = geo_data.get("region", "unknown")
                    village = geo_data.get("district", "unknown")

                    self.speak(
                        f"Sir, I am not sure, but I think we are in {city} city, {district} district of {country} country."
                    )
                    print(
                        f"Sir, I am not sure, but I think we are in {city} city, {district} district of {country} country."
                    )

                    if village != "unknown":
                        self.speak(f"We are in {village} village.")
                        print(f"We are in {village} village.")
                    else:
                        self.speak("Sorry, I couldn't retrieve village information.")
                        print("Sorry, I couldn't retrieve village information.")

                except (requests.RequestException, KeyError) as e:
                    self.speak("Sorry, I couldn't retrieve the location information at the moment.")
                    # Handle the error gracefully without printing

            elif "how are you" in self.query:
                self.speak("I'm fine sir, what about you!")
            
            elif "i'm good" in self.query:
                self.speak("That's great sir, Now i'm ready for new command")

            elif any(greeting in self.query for greeting in ["hello", "hi", "hey"]):
                self.speak("Hello! How can I assist you today?")

            elif "you can sleep now" in self.query:
                self.speak("Thanks for using me sir, have a good day.")
                sys.exit()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_jarvisUi()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
        self.thread = MainThread()  # Create an instance of MainThread

    def startTask(self):
        self.ui.movie1 = QMovie("../imgg/iron.gif.gif")
        self.ui.label.setMovie(self.ui.movie1)
        self.ui.movie1.start()

        self.ui.movie2 = QMovie("../imgg/initial.gif.gif")
        self.ui.label_2.setMovie(self.ui.movie2)
        self.ui.movie2.start()

        self.ui.movie3 = QMovie("../imgg/motion.gif")
        self.ui.label_3.setMovie(self.ui.movie3)
        self.ui.movie3.start()

        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)

        # Start the MainThread when the button is clicked
        self.thread.start()

    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm AP')  # Format for time in 12-hour clock with AM/PM indicator
        # label_date = current_date.toString(Qt.ISODate)   # Format date as ISO 8601

        # self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)

app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())
