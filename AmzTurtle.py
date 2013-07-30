#!/usr/bin/env python

import Tkinter as tk
import InterpretTurtle as Interpretor
import sys
from turtle import *

class AmazeTurtle(tk.Frame):
    def __init__(self, master = None, maze = None):
        self.__currentMaze = maze
        tk.Frame.__init__(self, master)
        self.grid()
        self.createLayout()
    
    def createLayout(self):
        self.quitButton = tk.Button(self, text = "Close", command = self.quit)
        self.quitButton.grid(row = 0, column = 0)
        self.drawButton = tk.Button(self, text = "Draw", command = self.drawTurtle)
        self.drawButton.grid(row = 0, column = 3)
        self.mapLabel = tk.Label(self, text = "Maze:")
        self.mapLabel.grid(row = 1, column = 0, sticky = tk.NE)
        self.codeLabel = tk.Label(self, text = "Commands:")
        self.codeLabel.grid(row = 2, column = 0, sticky = tk.NE)
        self.mapName = tk.StringVar()
        self.mapName.set("none")
        self.mapEnter = tk.Entry(self, textvariable = self.mapName, width = 79)
        self.mapEnter.grid(row = 1, column = 2)
        self.commands = tk.StringVar()
        self.commands.set("")
        self.codeScroll = tk.Scrollbar(self, orient = tk.VERTICAL, command = self.__scroll)
        self.codeScroll.grid(row = 2, column = 3, rowspan = 12, sticky = tk.NW +tk.SW)
        self.codeEnter = tk.Text(self, width = 79)
        self.codeEnter.grid(row = 2, column = 2, sticky = tk.NW + tk.SE)
        self.codeEnter['yscrollcommand'] = self.codeScroll.set
#        self.turtleField = ScrolledCanvas(self)
#        self.turtleField.grid(row = 14, column = 0, columnspan = 4, sticky = tk.NW + tk.SE)
                
    def drawTurtle(self):
        reset()
        shape()
        
        self.__currentMaze = self.mapEnter.get()
        try:
            exec("import {}".format(self.__currentMaze))
            sys.modules[self.__currentMaze].drawMaze()
        except ImportError:
            print "Maze not found"
        
        Interpretor.translate(self.codeEnter.get(1.0, tk.END))
            
    def __scroll(self, *L):
        op, howMany = L[0], L[1]

        if op == 'scroll':
            units = L[2]
            self.codeEnter.yview_scroll(howMany, units)
        elif op == 'moveto':
            self.codeEnter.yview_moveto(howMany)

        
        
app = AmazeTurtle()
app.master.title("Amazing Turtle")
app.mainloop()
