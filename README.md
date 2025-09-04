# Title: Timer and Productivity Log

### Video Demo:[https://youtu.be/1MmrvKvaBMQ]

## Description:
This is a customizable timer for study or work sessions. Additionally, it will log your sessions completed in a .json file for future reference. Once the program is complete, you will see a visual alarm in the terminal and an audible alert.The menu will display again so the user can choose to begin another study/work session or exit the program.

**For the CS50 Submission and video, the timer will be executed in seconds. In order to convert the time in minutes, the "#" must be removed from line 23 to enable the * 60 conversion to minutes. This will also effect test_project.py. If a user alters the timer. It may fail the tests established in test_project.py**

## Features ##
- Customizable Timer
- Sessions Log via. JSON output
- Terminal Based alarm visual and audible using "\a"

## Project Design ##
This project was deisgned to use minimal dependencies, but still function as a way to mananage work and study sessions. Because this project is hosted on codespaces, it needed to be a lightweight terminal based interface. This restriction was the primary reason for not utilizing a GUI interface for an alarm display and sound utlizing pygame.

The project is split into several code blocks to ensure troubleshooting was manageable and to keep the code as readable as possible. Additionally, because the code is broken up into several blocks, it should be realitely easy to expand upon in the future. For example, if a user decides to execute it out of codespaces, they may choose a more robust display and audio alert through other packages i.e. pygame.

## Requirements ##
Imported Modules:
- Python
- pyfiglet, figlet_format
- json
- datetime, time
- os
- pytest (for testing program in test_project.py)


## Files ##
- README.md
- Requirements.txt
- project.py
- test_project.py
- sessions.json

## Installation ##
- pyfiglet==1.0.3

- bash "pip install -r requirements.txt"
