import tkinter.messagebox
from tkinter import *
from turtle import width

#colors------------------------
col0 = "#444466" #black
col1 = "#feffff" #white
col2 = "#004338"
#ui----------------------------
window=Tk()
window.geometry("600x250")
window.configure(bg=col1)
window.resizable(width=False, height=False)
#function for converting values to hexadecimal and showing in the text box
def scale(value):
    r = int(red_scale.get())
    g = int(green_scale.get())
    b = int(blue_scale.get())

    rgb=f'{r},{g},{b}'

    hexadecimal="#%02x%02x%02x" % (r,g,b)
    screen["bg"]=hexadecimal
    color_entry.delete(0,END)
    color_entry.insert(0,hexadecimal)
#function for copying 
def oneclick():
    tkinter.messagebox.showinfo('Color',"Copied Successfully")
    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(color_entry.get())
    clip.destroy()

screen=Label(window,bg=col0,width=40,height=10)
screen.grid(row=0,column=0)

right_frame = Frame(window,bg=col1)
right_frame.grid(row=0,column=1,padx=5)

down_frame = Frame(window,bg=col1)
down_frame.grid(row=1,column=0,columnspan=2,padx=15)
#red---------------------------
red = Label(right_frame,bg=col1,text="Red",width=7,fg="red",anchor=NW,font=("Ivy",12,"bold"))
red.grid(row=0,column=0)

red_scale=Scale(right_frame,command=scale,bg=col1,fg="red",from_=0,to=255,length=150,orient=HORIZONTAL)
red_scale.grid(row=0,column=1)
#green--------------------------
green = Label(right_frame, bg=col1, text="Green", width=7, fg="green", anchor=NW, font=("Ivy", 12, "bold"))
green.grid(row=1,column=0)

green_scale=Scale(right_frame,command=scale,bg=col1,fg="green",from_=0,to=255,length=150,orient=HORIZONTAL)
green_scale.grid(row=1,column=1)
#blue----------------------------
blue = Label(right_frame,bg=col1,text="Blue",width=7,fg="blue",anchor=NW,font=("Ivy",12,"bold"))
blue.grid(row=2,column=0)

blue_scale=Scale(right_frame,command=scale,bg=col1,fg="blue",from_=0,to=255,length=150,orient=HORIZONTAL)
blue_scale.grid(row=2,column=1)
#textbox of hexcode and copy code button
rgb_label= Label(down_frame,bg=col1,text="HEX CODE :",fg="black",anchor=NW,font=("Ivy",10,"bold"))
rgb_label.grid(row=0,column=0,pady=5)

color_entry=Entry(down_frame,width=12,font=("Ivy",10,"bold"),justify=CENTER)
color_entry.grid(row=0,column=1,padx=5)

copy_button= Button(down_frame,text="Copy Color Code",bg=col1,font=("Ivy",10,"bold"),command=oneclick)
copy_button.grid(row=0,column=2,padx=5)

app_name=Label(down_frame,text="Color Picker App",bg=col1,font=("Ivy",20,"bold"))
app_name.grid(row=0,column=3,padx=20)
window.mainloop()
