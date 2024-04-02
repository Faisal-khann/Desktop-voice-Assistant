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
import pyautogui
import sys
import instadownloader

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
# print(voices[1].id)
# set id of voices
engine.setProperty("voices", voices[0].id)


# speak function
def speak(text):
    engine.say(text)
    engine.runAndWait()


# wish me function
def wishMe():
    currTime = datetime.datetime.now().strftime(
        "%I:%M:%S %p"
    )  # %I for 12-hour format, %p for AM/PM
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        message = f"Good Morning, it's {currTime}"
    elif hour >= 12 and hour < 18:
        message = f"Good Afternoon, it's {currTime}"
    else:
        message = f"Good Evening, it's {currTime}"

    print(message)  # Print the message
    speak(
        message
    )  # Assuming there's a function called `speak()` elsewhere in your code

    print("I am Jarvis Sir. Please tell me how may I help you.")
    speak("I am Jarvis Sir. Please tell me how may I help you.")


# take command function
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f"user said: {query}")

    except Exception as e:
        speak("Say that again please....")
        return "none"
    return query


# send email
# def sendEmail(to, content):
#     server = smtplib.SMTP('smtp.gmail.com', 587)
#     server.ehlo()
#     server.starttls()
#     server.login('faisalkhanfaisal919@gmail.com', 'faisal2301khan')
#     server.sendmail('faisalkhanfaisal919@gmail.com', to, content)
#     server.close()


# youtube playing function
def play_on_youtube(video):
    kit.playonyt(video)


# Send Whatsapp message function
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)


if __name__ == "__main__":
    wishMe()


while True:
    # if 1:
    query = takecommand().lower()  # Converting user query into lower case

    # Logic for executing tasks based on query.....
    if "wikipedia" in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif "open youtube" in query:
        speak("sir, what should I search on YouTube")
        video = takecommand().lower()
        play_on_youtube(video)
        # webbrowser.open(f"{yt}")
        # webbrowser.open("youtube.com")

    elif "send whatsapp message" in query:
        speak(
            "On what number should I send the message sir? Please enter in the console: "
        )
        number = input("Enter the number: ")
        speak("What is the message sir?")
        message = takecommand().lower()
        send_whatsapp_message(number, message)
        speak("I've sent the message sir.")

    # elif "ip address" in query:
    #     ip = requests.get("https://api.ipify.org").text
    #     speak(f"your Ip address is {ip}")
    #     print("Your Ip Address is ", ip)

    elif "open google" in query:
        speak("sir, what should i search on google")
        cm = takecommand().lower()
        webbrowser.open(f"{cm}")
        # webbrowser.open("google.com")

    # .........Open Instagram.........#
    elif "open instagram" in query:
        webbrowser.open("instagram.com")

    # ......Check Instagram profile of any account...........#
    elif "instagram profile" in query or "profile on instagram" in query:
        speak("Sir, please enter the username correctly:")
        name = input(
            "Enter the username:"
        )  # Assuming you're running this code in a console
        webbrowser.open(f"https://www.instagram.com/{name}")
        speak(f"Sir, here is the profile of the user {name}")
        time.sleep(5)

        speak("Sir, would you like to download the profile picture of this account?")
        condition = takecommand().lower()
        if "yes" in condition:
            mod = instadownloader.InstaDownloader()
            mod.download_profile(name, profile_pic_only=True)
            speak(
                "I am done, sir. The profile picture is saved in our main folder. Now I am ready for a new command."
            )

    elif "open camera" in query:
        subprocess.run("start microsoft.windows.camera:", shell=True)

    elif "close camera" in query:
        speak("Okay sir, closing camera")
        os.system("taskkill /f /im WindowsCamera.exe")

    elif "the time" in query:
        strTime = datetime.datetime.now().strftime("%I:%M:%S %p")
        print(f"Sir, the time is {strTime}")
        speak(f"Sir, the time is {strTime}")

    elif "open vs code" in query:
        codePath = (
            "C:\\Users\\faisa\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        )
        os.startfile(codePath)

    elif "close vs code" in query:
        speak("Okay sir, closing vs code")
        os.system("taskkill /f /im Code.exe")

    elif "open notepad" in query:
        os.startfile("C:\\Users\\faisa\\Desktop\\Notepad.lnk")

    elif "close notepad" in query:
        speak("Okay sir, closing notepad")
        os.system("taskkill /f /im notepad.exe")

    elif "open command prompt" in query:
        os.system("start cmd")

    elif "play music" in query:
        music_dir = "C:\\Users\\faisa\\Music"
        song = os.listdir(music_dir)
        # rd = random.choice(songs)
        os.startfile(os.path.join(music_dir, song[2]))

    elif "switch the window" in query:
        pyautogui.keyDown("alt")
        pyautogui.press("tab")
        time.sleep(1)
        pyautogui.keyUp("alt")

    # elif "email to faisal" in query:
    #     try:
    #         speak("What should I say")
    #         content = takecommand().lower()
    #         to = "faisalkhanfaisal496@gmail.com"
    #         sendEmail(to, content)
    #         speak("Email has been Send to faisal")
    #
    #     except Exception as e:
    #         print(e)
    #         speak("Sorry sir I am not able to send this email") # import smtplib for email

    elif "thanks buddy" in query:
        speak("you're most welcome sir, i am ready for new command")

    elif "you can sleep now" in query:
        speak("Thanks for using me sir, have a good day ")
        sys.exit()


    # ......To set the alarm.....#
    elif "set alarm" in query:
        al = int(datetime.datetime.now().hour)
        if al == 22:  # check time for alarm
            music_dir = "C:\\Users\\fais a\\Music"
            song = os.listdir(music_dir)
            os.startfile(os.path.join(music_dir, song[1]))

    # ......To find my Ip Address........#
    elif "ip address" in query:
        try:
            speak("Wait sir, let me check.")
            ip = requests.get("https://api.ipify.org").text
            speak(f"Your IP address is {ip}")
            print("Your IP Address is ", ip)
        except requests.RequestException as e:
            speak("Sorry, I couldn't retrieve your IP address at the moment.")
            print("Error:", e)

    # ......To find my location using IP Address..........#
    elif "where i am" in query or "Where we are" in query:
        try:
            speak("Wait sir, let me check.")

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

            speak(
                f"Sir, I am not sure, but I think we are in {city} city, {district} district of {country} country."
            )
            print(
                f"Sir, I am not sure, but I think we are in {city} city, {district} district of {country} country."
            )

            if village != "unknown":
                speak(f"We are in {village} village.")
                print(f"We are in {village} village.")
            else:
                speak("Sorry, I couldn't retrieve village information.")
                print("Sorry, I couldn't retrieve village information.")

        except (requests.RequestException, KeyError) as e:
            speak("Sorry, I couldn't retrieve the location information at the moment.")
            # Handle the error gracefully without printing
