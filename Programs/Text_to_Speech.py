from gtts import gTTS # pip install gtts
from playsound import playsound

text = "Subscribe to Techix, to Get More Videos Frequently"

obj = gTTS(lang='en', text=text, slow=False)

obj.save("file.mp3")

playsound("file.mp3")