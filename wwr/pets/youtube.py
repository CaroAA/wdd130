from time import time
from tkinter import HORIZONTAL, Y, Label, Tk
Import time

window= Tk{}
window.config(bg="gray")
window.geometry("500x200")
window.wm_attributes('=Transpatentcolor','grey')
window.overrideredirect(1)

def out(*args):
    window.destroy()
    window.quit()

def get_time():
    hour = time.strftime('%H:%M:%S')
    zone = time.strftime('%Z')
    date_12 =time.strftime('%A ' ' '%d' ' '%B'' ' ' %Y')

    text_hour  'text' = hour
    text_date12 'text' = date_12
    time_zone.after(1000, get_time)

def start(event):
    global x, y 
    x=event.x
    y= event.y

def stop(event):
    global x,y 
    x= None
    x= None
