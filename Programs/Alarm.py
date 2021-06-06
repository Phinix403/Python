import datetime
from pydub import AudioSegment
from pydub.playback import play

audio = AudioSegment.from_wav("alarm.wav")

cur_time = datetime.datetime.now().strftime("%I:%M:%S")
print(f"\n{cur_time}\n")

print("Enter the alarm time to be set - HH:MM::SS\n")

hour = input("Hour: ")
minute = input("Minute: ")
Second = input("Seconds: ")

print(f"Alarm is Starting from {cur_time}\n")

while True:

    time = datetime.datetime.now()

    cur_hour = time.strftime("%I")
    cur_min = time.strftime("%M")
    cur_sec = time.strftime("%S")
    cur_period = time.strftime("%p")

    if cur_period:
        if hour == cur_hour:
            if minute == cur_min:
                if Second == cur_sec:
                    print("\nTime is Now!\n")
                    play(audio)
                    break