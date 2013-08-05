#!/usr/bin/env python

# Amazing Turtle is Licensed under
#
# Authors:
#     Ian Furry <Thengrad@gmail.com>


import Tkinter as tk
import InterpretTurtle as Interpretor
import sys
from turtle import *


class AmzTurtle(tk.Frame):

    def __init__(self, master=None, maze=None):
        self.__currentMaze = maze
        tk.Frame.__init__(self, master)
        self.grid()
        self.createLayout()

    def createLayout(self):
        """
        Creates the GUI interpretor environment
        """

        # Creates a button to close the GUI
        self.quitButton = tk.Button(self, text="Close", command=self.quit)
        self.quitButton.grid(row=0, column=0)

        # Creates a button that draws the turtle when clicked
        self.drawButton = tk.Button(self, text="Draw", command=self.drawTurtle)
        self.drawButton.grid(row=0, column=3)

        # Label for entry field of which maze to draw
        self.mapLabel = tk.Label(self, text="Maze:")
        self.mapLabel.grid(row=1, column=0, sticky=tk.NE)

        # Label for the entry field of instructions for the turtle
        self.codeLabel = tk.Label(self, text="Commands:")
        self.codeLabel.grid(row=2, column=0, sticky=tk.NE)

        # Entry value of which maze to draw.
        self.mapName = tk.StringVar()
        self.mapName.set("none")

        # Entry field for selecting a maze
        self.mapEnter = tk.Entry(self, textvariable=self.mapName, width=79)
        self.mapEnter.grid(row=1, column=2)

        # Scroll bar for Code entry field
        self.codeScroll = tk.Scrollbar(self, orient=tk.VERTICAL,
                                       command=self.__scroll)
        self.codeScroll.grid(row=2, column=3, rowspan=12,
                             sticky=(tk.NW + tk.SW))

        # Entry Field for enterting turtle code
        self.codeEnter = tk.Text(self, width=79)
        self.codeEnter.grid(row=2, column=2, rowspan=12,
                            sticky=(tk.NW + tk.SE))
        self.codeEnter['yscrollcommand'] = self.codeScroll.set

    def drawTurtle(self):
        """
        Draws the maze and turtle on to the field
        """

        # Resets the turtle canvas to the way it starts.
        reset()
        shape()

        # Checks if the maze can be found and imported.
        # If maze is found the maze is drawn.
        # If maze can't be found turtle starts on a blank canvas
        self.__currentMaze = self.mapEnter.get()
        try:
            speed(11)
            exec("import {}".format(self.__currentMaze))
            sys.modules[self.__currentMaze].drawMaze()
        except ImportError:
            print "Maze not found"

        # Sends turtle code through interpretor to be drawn.
        speed(1)
        Interpretor.translate(self.codeEnter.get(1.0, tk.END))

    def __scroll(self, *L):
        """
        Scrolls the code entry field when there are more than
        12 lines of code.

        :type L: optional parameters
        :param L: commands on the scroll bar
        """

        op, howMany = L[0], L[1]

        # checks if the scroll bar was scrolled or
        # if move to a certain position.
        if op == 'scroll':
            units = L[2]
            self.codeEnter.yview_scroll(howMany, units)
        elif op == 'moveto':
            self.codeEnter.yview_moveto(howMany)

# runs the main loop of Amazing Turtle
app = AmzTurtle()
app.master.title("Amazing Turtle")
app.mainloop()
