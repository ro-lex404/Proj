import tkinter as tk
import turtle
wn=turtle.Screen()
wn.bgcolor("black")
turtle.color("yellow")
turtle.setpos(0,0)
turtle.setheading(90)
app=tk.Tk()
app.geometry("400x200")
app.title("TkinterXTurtle")
def tk_button_melillottu():
    turtle.setheading(90)
    turtle.forward(10)
def tk_button_thazhottu():
    turtle.setheading(270)
    turtle.forward(10)
def tk_button_leftaddi():
    turtle.setheading(180)
    turtle.forward(10)
def tk_button_rightaddi():
    turtle.setheading(0)
    turtle.forward(10)
def tk_button_penup():
    turtle.penup()
def tk_button_pendown():
    turtle.pendown()
button1=tk.Button(app,text="Up",command=tk_button_melillottu)
button2=tk.Button(app,text="Down",command=tk_button_thazhottu)
button3=tk.Button(app,text="Right",command=tk_button_rightaddi)
button4=tk.Button(app,text="Left",command=tk_button_leftaddi)
button5=tk.Button(app,text="PnUp",command=tk_button_penup)
button6=tk.Button(app,text="PnDn",command=tk_button_pendown)
button1.grid(row=0, column=1)
button2.grid(row=1, column=1)
button3.grid(row=1, column=2)
button4.grid(row=1, column=0)
button5.grid(row=0,column=4)
button6.grid(row=1,column=4)
app.mainloop()


