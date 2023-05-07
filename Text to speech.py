from tkinter import *             # Tkinter-Python package
from gtts import gTTS             # gTTS(Google Text-to-Speech)Customizable speech-specific sentence tokenizer
from playsound import playsound   # for playing sound
root = Tk()                       # display the root window
#geometry root.("350x300") 
root.configure(bg='ghost white')  #background colour
root.title("TEXT TO SPEECH")      # window title
# texts on the window
Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg='yellow').pack() 
Label(text ="Created by: Ananya:)", font = 'arial 15 bold', bg ='Blue' , width = '20').pack(side = 'bottom')
Msg = StringVar()                 # variable holding string data
Label(root,text ="Enter Text", font = 'arial 15 bold', bg ='white smoke').place(x=20,y=60)
# creating entry field
entry_field = Entry(root, textvariable = Msg ,width ='50')
entry_field.place(x=20,y=100)
# functions
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('DataFlair.mp3')
    playsound('DataFlair.mp3')
def Exit():
    root.destroy()
def Reset():
    Msg.set("")
#creating buttons
Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_speech ,width = '4').place(x=25,y=140)
Button(root, font = 'arial 15 bold',text = 'EXIT', width = '4' , command = Exit, bg = 'OrangeRed1').place(x=100 , y = 140)
Button(root, font = 'arial 15 bold',text = 'RESET', width = '6' , command = Reset, bg = 'Sea green').place(x=175 , y = 140)
root.mainloop() # executes untill exit
