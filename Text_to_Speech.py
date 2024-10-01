import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")

names = ["Kiran", "Kunal", "Aditya", "Mithil"]

for name in names:
    s = (f"Shoutout to {name}")
    speaker.speak(s)


