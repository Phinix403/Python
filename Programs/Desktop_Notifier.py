# Install Notification Module - pip install notify2

import notify2
import time
import os

notify2.init('Notification')

icon_path = os.getcwd() + "/icon.ico"

def notiFunc():
    noti = notify2.Notification("Welcome to Techix", "Techix is an Tech Dependent Youtube Channel, Please Subscribe to get more Videos Frequently.", icon=icon_path)
    noti.set_urgency(notify2.URGENCY_NORMAL)
    noti.show()
    noti.set_timeout(15000)
    time.sleep(120)

if __name__ == "__main__":
    notiFunc()