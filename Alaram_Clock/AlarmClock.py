import tkinter as tk
import datetime
from playsound import playsound


def set_alarm():
    alarm_time = entry.get()
    popUp = tk.Tk()
    popUp.title("Alarm Clock")
    window.minsize(width=200, height=100)
    label = tk.Label(popUp, text="Alarm is finished. ")
    label.pack()

    while True:
        current_time = datetime.datetime.now().strftime("%H:%M")
        if current_time == alarm_time:
            play_alarm_sound()
            break


def play_alarm_sound():
    playsound('./the_rumbling.mp3')


# Create the main window
window = tk.Tk()
window.title("Alarm Clock")
window.minsize(width=200, height=100)

# Create the label and entry for alarm time
label = tk.Label(window, text="Enter alarm time (HH:MM):")
label.pack()

entry = tk.Entry(window)
entry.pack()

# Create the button to set the alarm
button = tk.Button(window, text="Set Alarm", command=set_alarm)
button.pack()

# Start the main event loop
window.mainloop()
