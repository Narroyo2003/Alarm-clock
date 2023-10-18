from datetime import datetime, time
from playsound import playsound
import threading
import time

"""
TODO Add a GUI class
TODO Add song to alarm
"""

def alarm_clock(alarm_time, sound_file):
    while True:
        current_time = datetime.now().time()
        if current_time >= alarm_time:
            print("Time to wake up!")
            if sound_file:
                playsound(sound_file)
            break
        time.sleep(1)

def set_alarm():
    while True:
        alarm_time_str = input("Enter alarm time (24 hour format (HH:MM)): ")
        try:
            alarm_time = datetime.strptime(alarm_time_str, "%H:%M").time()
        except ValueError:
            print("Invalid format. Valid format is (HH:MM)")
            continue
        break
    sound_file = input("Enter the path of the sound file you would like to play. Ex. Home/Sounds/SoundFile.mp3 ")
    if not sound_file:
        print("Sound file not provided, there will be no sound for the alarm.")
    threading.Thread(target=alarm_clock, args=(alarm_time, sound_file)).start()

if __name__ == "__main__":
    try:
        set_alarm()
    except KeyboardInterrupt as e:
        print("\nAlarm clock terminated")
