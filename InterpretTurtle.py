import Tkinter as tk
import tkMessageBox
from turtle import *

def translate(commands):
    print "Translating: " + commands
    script = commands.split("\n")
    count = 0
    for line in script:
        print "Translating Line: " + str(count)
        if len(line) > 0:
            instruction = line.split("(")
            if len(instruction) < 2:
                tkMessageBox.showerror("Command Not Found", line + "does not exits")
                return
                
            if instruction[1][0] == "\"" or instruction[1][0] == "\'":
                value = instruction[1][1:len(instruction[1]) - 2]
            else:
                value = int(instruction[1][:len(instruction[1]) - 1])
                            
            print value
            if instruction[0] == "forward":
                forward(value)
            elif instruction[0] == "right":
                right(value)
            elif instruction[0] == "left":
                left(value)
            elif instruction[0] == "up":
                up()
            elif instruction[0] == "down":
                down()
            elif instruction[0] == "color":
                tkMessageBox.showinfo("Under Construction", "Color not available")
                #color(value)
            elif instruction[0] == "shape":
                shape(value)
            elif instruction[0] == "seth":
                seth(value)
            elif instruction[0] == "speed":
                speed(value)
            elif instruction[0] == "seth":
                seth(value)
            else:
                tkMessageBox.showerror("Command Not Found", line + "does not exits")
                return
            
        count += 1
    print "Translation Complete"
        
