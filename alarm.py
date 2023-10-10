import time
import subprocess

# Function to set the alarm
def set_alarm(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Time to wake up!")
            play_alarm_sound()
            break
        time.sleep(1)

# Function to play the alarm sound
def play_alarm_sound():
    try:
        # Use AppleScript to play the system alert sound
        subprocess.call(['osascript', '-e', 'display notification "Time to wake up!" with title "Alarm" sound name "default"'])
    except Exception as e:
        print("Error playing alarm sound:", str(e))

# Get the user's input for the alarm time
alarm_time = input("Enter the alarm time (HH:MM:SS): ")

# Start the alarm
set_alarm(alarm_time)
