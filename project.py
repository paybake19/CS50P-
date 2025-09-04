#import modules
import json
import datetime, time
import os
from pyfiglet import figlet_format



#def main funciton: show menu, start timer, view stat, and exit.
def main():
    print("Welcome, time to study")
    while True:
        print("\nMenu")
        print("1. Start 25min Timer")
        print("2. View session history")
        print("3. Exit program")
        option = input("Option: ")

 #configure selections
        if option == "1":
            try:
                time_len = int(input("How long do you want to study(min)? "))
                duration = time_len #*60 #leaving the conversion to minutes out for submission and video
                start_timer(duration)
            except ValueError:
                print("Please provide a valid number")
            if duration == 0:
                break
        elif option == "2":
            stats = session_statistics()
            print(f"Sessions Completed: {stats}")
        elif option == "3":
            break
        else:
            print("Invalid Answer, try again")

#Start timer, provide notificaiton, log session
def start_timer(duration: int):
    print("25min timer started!")
    original_duration = duration
    while duration:
        min, sec = divmod(duration, 60)
        time_string = f"{min}:{sec}"
        print(f"\r Time Remaining:{time_string}, end=""")
        time.sleep(1)
        duration -= 1
    print("Time is up, take a walk", "\a")
    alarm_display()
    log_session(original_duration)



#def log timer sessions, enable a saved file to capture sessions
def log_session(duration: int):
    session_entry = {
        "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "duration": duration
        }
#Create an empty list to store sessions if no sessions exist.
    data = []
    if os.path.exists("sessions.json"):
        try:
            with open ("sessions.json", "r") as file:
                data = json.load(file)
        except(FileNotFoundError):
            print("Could not find session entry file")

#add session to new list created above
    data.append(session_entry)
    with open("sessions.json", "w") as file:
        json.dump(data, file, indent= 2)
    print("Logging Session: ", session_entry)



#view session stats, read and view session_data
#verify file path
def session_statistics():
    if not os.path.exists("sessions.json"):
        return {"Total Sessions", len(data)}

#if sessions exists,open and read file, get length of data and return to dict.
    with open("sessions.json", "r") as file:
        data = json.load(file)
    return{"total_sessions": len(data)}



#configure alarm visual at the end of the countdown.
def alarm_display():
    try:
        os.system("cls" if os.name == "nt" else "clear")
        terminal_txt = figlet_format("time is up", font="standard")
        print("\n" + "=" * 60)
        print(terminal_txt)
        time.sleep(5)
    except Exception as e:
        print("try again later", e)


# entry into program
if __name__ == "__main__":
    main()
