# Desktop-voice-Assistant (JARVIS)

<em>JARVIS is built to understand and respond to natural voice commands, enabling hands-free interaction with desktop applications and services. It combines speech recognition, text-to-speech, and automation to deliver a smart, responsive, and AI-powered experience — bringing productivity and convenience right to your desktop!</em>

---

## Table of Contents

- [Project Description](#project-description)
- [Core Features](#core-features)
- [GUI Section](#gui-section)
- [Features](#features)
- [Project Structure](#project-structure)
- [Contributions](#contributions)
- [License](#license)

---

## Project Description

JARVIS is an AI-powered desktop voice assistant designed to interpret and respond to natural language voice commands, enabling seamless hands-free interaction with desktop applications and services. It integrates **speech recognition**, **text-to-speech**, and **automation capabilities** to deliver an intelligent, responsive, and efficient user experience.  

Built in **Python 3** with a **GUI designed using Qt Designer**, this application allows users to perform system operations using voice commands. JARVIS leverages advanced speech recognition technology to accurately understand and execute user instructions.

---

## Core Features

| Feature | Description |
|---------|-------------|
| Voice Command Processing | Recognizes and processes real-time user voice input using natural language. |
| Task Automation | Executes tasks such as launching applications, retrieving information, setting reminders, and more. |
| Interactive GUI | Developed using Qt Designer, providing an intuitive and user-friendly interface. |
| System Control | Capable of performing system-level operations like opening files, folders, or managing utilities. |
| Information Retrieval | Answers general queries using integrated APIs and logic-driven modules. |

---

## GUI Section

https://github.com/user-attachments/assets/a9c6fa45-8772-4e1f-a240-1c80a9a4a730

---

## Features

| Feature | Description |
|---------|-------------|
| Greet User | Welcomes the user when activated. |
| Time & Date | Tells the current time and date. |
| Launch Applications | Opens software or applications on the system. |
| IP Address | Retrieves the device's IP address. |
| Location Finder | Finds the user's current location. |
| Open Website | Opens any website as requested. |
| YouTube Search | Opens YouTube and searches according to user input. |
| WhatsApp Messages | Sends WhatsApp messages to anyone. |
| Music Control | Plays, pauses, or manages the music system. |
| Battery Info | Displays device battery information. |
| Wikipedia Info | Provides information about any person or topic via Wikipedia. |
| Window Control | Switches between windows and returns to the main window. |
| Notes | Takes important notes in Notepad. |

---

## Project Structure

    ├── driver
    ├── Jarvis # Main folder for features
    │ ├── config # Contains all secret API Keys
    │ ├── features # All functionalities of JARVIS
    │ └── utils # GUI images
    ├── init.py # Definition of feature's functions
    ├── gui.ui # GUI file (in .ui format)
    ├── main.py # Main driver program of JARVIS
    ├── requirements.txt # All dependencies of the program


**Adding New Features:**  
- Create a new file in the `features` folder and write the feature function.  
- Add the function's definition to `__init__.py`.  
- Define the voice commands that will invoke the function.  

---

## Contributions

Contributions are welcome! Feel free to fork this repository, make improvements, and submit pull requests. Together, we can make this voice assistant even more powerful and versatile.

---

## License

This project is licensed under the [MIT License](https://github.com/Faisal-khann/Desktop-voice-Assistant?tab=MIT-1-ov-file).  

2024 Faisal Khan  

<p>If you like this project, don’t forget to 🌟 the repository and clone it to start using JARVIS! 😎</p>


