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
                if value == "alice blue":
                    color('alice blue')
                elif value == "AliceBlue":
                    color('AliceBlue')
                elif value == "antique white":
                    color('antique white')
                elif value == "AntiqueWhite":
                    color('AntiqueWhite')
                elif value == "AntiqueWhite1":
                    color('AntiqueWhite1')
                elif value == "AntiqueWhite2":
                    color('AntiqueWhite2')
                elif value == "AntiqueWhite3":
                    color('AntiqueWhite3')
                elif value == "AntiqueWhite4":
                    color('AntiqueWhite4')
                elif value == "aquamarine":
                    color('aquamarine')
                elif value == "aquamarine1":
                    color('aquamarine1')
                elif value == "aquamarine2":
                    color('aquamarine2')
                elif value == "aquamarine3":
                    color('aquamarine3')
                elif value == "aquamarine4":
                    color('aquamarine4')
                elif value == "azure":
                    color('azure')
                elif value == "azure1":
                    color('azure1')
                elif value == "azure2":
                    color('azure2')
                elif value == "azure3":
                    color('azure3')
                elif value == "azure4":
                    color('azure4')
                elif value == "beige":
                    color('beige')
                elif value == "bisque":
                    color('bisque')
                elif value == "bisque1":
                    color('bisque1')
                elif value == "bisque2":
                    color('bisque2')
                elif value == "bisque3":
                    color('bisque3')
                elif value == "bisque4":
                    color('bisque4')
                elif value == "black":
                    color('black')
                elif value == "blanched almond":
                    color('blanched almond')
                elif value == "BlanchedAlmond":
                    color('BlanchedAlmond')
                elif value == "blue":
                    color('blue')
                elif value == "blue1":
                    color('blue1')
                elif value == "blue violet":
                    color('blue violet')
                elif value == "blue2":
                    color('blue2')
                elif value == "blue3":
                    color('blue3')
                elif value == "blue4":
                    color('blue4')
                elif value == "BlueViolet":
                    color('BlueViolet')
                elif value == "brown":
                    color('brown')
                elif value == "brown1":
                    color('brown1')
                elif value == "brown2":
                    color('brown2')
                elif value == "brown3":
                    color('brown3')
                elif value == "brown4":
                    color('brown4')
                elif value == "burlywood":
                    color('burlywood')
                elif value == "burlywood1":
                    color('burlywood1')
                elif value == "burlywood2":
                    color('burlywood2')
                elif value == "burlywood3":
                    color('burlywood3')
                elif value == "burlywood4":
                    color('burlywood4')
                elif value == "cadet blue":
                    color('cadet blue')
                elif value == "CadetBlue":
                    color('CadetBlue')
                elif value == "CadetBlue1":
                    color('CadetBlue1')
                elif value == "CadetBlue2":
                    color('CadetBlue2')
                elif value == "CadetBlue3":
                    color('CadetBlue3')
                elif value == "CadetBlue4":
                    color('CadetBlue4')
                elif value == "chartreuse":
                    color('chartreuse')
                elif value == "chartreuse1":
                    color('chartreuse1')
                elif value == "chartreuse2":
                    color('chartreuse2')
                elif value == "chartreuse3":
                    color('chartreuse3')
                elif value == "chartreuse4":
                    color('chartreuse4')
                elif value == "chocolate":
                    color('chocolate')
                elif value == "chocolate1":
                    color('chocolate1')
                elif value == "chocolate2":
                    color('chocolate2')
                elif value == "chocolate3":
                    color('chocolate3')
                elif value == "chocolate4":
                    color('chocolate4')
                elif value == "coral":
                    color('coral')
                elif value == "coral1":
                    color('coral1')
                elif value == "coral2":
                    color('coral2')
                elif value == "coral3":
                    color('coral3')
                elif value == "coral4":
                    color('coral4')
                elif value == "cornflower blue":
                    color('cornflower blue')
                elif value == "CornflowerBlue":
                    color('CornflowerBlue')
                elif value == "cornsilk":
                    color('cornsilk')
                elif value == "cornsilk1":
                    color('cornsilk1')
                elif value == "cornsilk2":
                    color('cornsilk2')
                elif value == "cornsilk3":
                    color('cornsilk3')
                elif value == "cornsilk4":
                    color('cornsilk4')
                elif value == "cyan":
                    color('cyan')
                elif value == "cyan1":
                    color('cyan1')
                elif value == "cyan2":
                    color('cyan2')
                elif value == "cyan3":
                    color('cyan3')
                elif value == "cyan4":
                    color('cyan4')
                elif value == "dark blue":
                    color('dark blue')
                elif value == "dark cyan":
                    color('dark cyan')
                elif value == "dark goldenrod":
                    color('dark goldenrod')
                elif value == "dark gray":
                    color('dark gray')
                elif value == "dark green":
                    color('dark green')
                elif value == "dark grey":
                    color('dark grey')
                elif value == "dark khaki":
                    color('dark khaki')
                elif value == "dark magenta":
                    color('dark magenta')
                elif value == "dark olive green":
                    color('dark olive green')
                elif value == "dark orange":
                    color('dark orange')
                elif value == "dark orchid":
                    color('dark orchid')
                elif value == "dark red":
                    color('dark red')
                elif value == "dark salmon":
                    color('dark salmon')
                elif value == "dark sea green":
                    color('dark sea green')
                elif value == "dark slate blue":
                    color('dark slate blue')
                elif value == "dark slate gray":
                    color('dark slate gray')
                elif value == "dark slate grey":
                    color('dark slate grey')
                elif value == "dark turquoise":
                    color('dark turquoise')
                elif value == "dark violet":
                    color('dark violet')
                elif value == "DarkBlue":
                    color('DarkBlue')
                elif value == "DarkCyan":
                    color('DarkCyan')
                elif value == "DarkGoldenrod":
                    color('DarkGoldenrod')
                elif value == "DarkGoldenrod1":
                    color('DarkGoldenrod1')
                elif value == "DarkGoldenrod2":
                    color('DarkGoldenrod2')
                elif value == "DarkGoldenrod3":
                    color('DarkGoldenrod3')
                elif value == "DarkGoldenrod4":
                    color('DarkGoldenrod4')
                elif value == "DarkGray":
                    color('DarkGray')
                elif value == "DarkGreen":
                    color('DarkGreen')
                elif value == "DarkGrey":
                    color('DarkGrey')
                elif value == "DarkKhaki":
                    color('DarkKhaki')
                elif value == "DarkMagenta":
                    color('DarkMagenta')
                elif value == "DarkOliveGreen":
                    color('DarkOliveGreen')
                elif value == "DarkOliveGreen1":
                    color('DarkOliveGreen1')
                elif value == "DarkOliveGreen2":
                    color('DarkOliveGreen2')
                elif value == "DarkOliveGreen3":
                    color('DarkOliveGreen3')
                elif value == "DarkOliveGreen4":
                    color('DarkOliveGreen4')
                elif value == "DarkOrange":
                    color('DarkOrange')
                elif value == "DarkOrange1":
                    color('DarkOrange1')
                elif value == "DarkOrange2":
                    color('DarkOrange2')
                elif value == "DarkOrange3":
                    color('DarkOrange3')
                elif value == "DarkOrange4":
                    color('DarkOrange4')
                elif value == "DarkOrchid":
                    color('DarkOrchid')
                elif value == "DarkOrchid1":
                    color('DarkOrchid1')
                elif value == "DarkOrchid2":
                    color('DarkOrchid2')
                elif value == "DarkOrchid3":
                    color('DarkOrchid3')
                elif value == "DarkOrchid4":
                    color('DarkOrchid4')
                elif value == "DarkRed":
                    color('DarkRed')
                elif value == "DarkSalmon":
                    color('DarkSalmon')
                elif value == "DarkSeaGreen":
                    color('DarkSeaGreen')
                elif value == "DarkSeaGreen1":
                    color('DarkSeaGreen1')
                elif value == "DarkSeaGreen2":
                    color('DarkSeaGreen2')
                elif value == "DarkSeaGreen3":
                    color('DarkSeaGreen3')
                elif value == "DarkSeaGreen4":
                    color('DarkSeaGreen4')
                elif value == "DarkSlateBlue":
                    color('DarkSlateBlue')
                elif value == "DarkSlateGray":
                    color('DarkSlateGray')
                elif value == "DarkSlateGray1":
                    color('DarkSlateGray1')
                elif value == "DarkSlateGray2":
                    color('DarkSlateGray2')
                elif value == "DarkSlateGray3":
                    color('DarkSlateGray3')
                elif value == "DarkSlateGray4":
                    color('DarkSlateGray4')
                elif value == "DarkSlateGrey":
                    color('DarkSlateGrey')
                elif value == "DarkTurquoise":
                    color('DarkTurquoise')
                elif value == "DarkViolet":
                    color('DarkViolet')
                elif value == "deep pink":
                    color('deep pink')
                elif value == "deep sky blue":
                    color('deep sky blue')
                else:
                    tkMessageBox.showerror("Error", "Color, " + value + ", not available")
                print value
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
        
