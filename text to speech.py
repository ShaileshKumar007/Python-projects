import pyttsx3
engine=pyttsx3.init()
a=5
while a>0:
    
    text=input("Enter the text:-" )
    engine.say(text)
    engine.runAndWait()
