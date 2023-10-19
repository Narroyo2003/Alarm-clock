"""
TODO Add a GUI class
This is the program using pygame to play the sound instead of the playsound module
"""

from datetime import datetime, time
#from playsound import playsound
import pygame
import threading
import time

pygame.init()
pygame.mixer.init() 

stop_alarm = threading.Event()

def alarm_clock(alarm_time, sound_file):
    while True:
        current_time = datetime.now().time()
        if current_time >= alarm_time:
            print("Time to wake up!")
            if sound_file:
                alarm_sound = pygame.mixer.Sound(sound_file)
                alarm_sound.play()
                delay_ms = int(alarm_sound.get_length() * 1000)
                pygame.time.delay(delay_ms)
                pygame.quit()
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
    alarm_thread = threading.Thread(target=alarm_clock, args=(alarm_time, sound_file))
    alarm_thread.start()
    global stop_alarm
    try:
        while not stop_alarm.is_set():
            pass
    except KeyboardInterrupt:
        print("\nAlarm clock terminated")
        stop_alarm.set()


if __name__ == "__main__":
    try:
        set_alarm()
    except KeyboardInterrupt as e:
        print("\nAlarm clock terminated")
        stop_alarm.set()
