import Tkinter as tk
import tkMessageBox
from turtle import *

def translate(commands):
    for line in script:
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
            elif instruction[0] == "shape":
                shape(value)
            elif instruction[0] == "seth":
                seth(value)
            elif instruction[0] == "speed":
                speed(value)
            elif instruction[0] == "seth":
                seth(value)
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
                elif value == "DeepPink":
                    color('DeepPink')
                elif value == "DeepPink1":
                    color('DeepPink1')
                elif value == "DeepPink2":
                    color('DeepPink2')
                elif value == "DeepPink3":
                    color('DeepPink3')
                elif value == "DeepPink4":
                    color('DeepPink4')
                elif value == "DeepSkyBlue":
                    color('DeepSkyBlue')
                elif value == "DeepSkyBlue1":
                    color('DeepSkyBlue1')
                elif value == "DeepSkyBlue2":
                    color('DeepSkyBlue2')
                elif value == "DeepSkyBlue3":
                    color('DeepSkyBlue3')
                elif value == "DeepSkyBlue4":
                    color('DeepSkyBlue4')
                elif value == "dim gray":
                    color('dim gray')
                elif value == "dim grey":
                    color('dim grey')
                elif value == "DimGray":
                    color('DimGray')
                elif value == "DimGrey":
                    color('DimGrey')
                elif value == "dodger blue":
                    color('dodger blue')
                elif value == "DodgerBlue":
                    color('DodgerBlue')
                elif value == "DodgerBlue1":
                    color('DodgerBlue1')
                elif value == "DodgerBlue2":
                    color('DodgerBlue2')
                elif value == "DodgerBlue3":
                    color('DodgerBlue3')
                elif value == "DodgerBlue4":
                    color('DodgerBlue4')
                elif value == "firebrick":
                    color('firebrick')
                elif value == "firebrick1":
                    color('firebrick1')
                elif value == "firebrick2":
                    color('firebrick2')
                elif value == "firebrick3":
                    color('firebrick3')
                elif value == "firebrick4":
                    color('firebrick4')
                elif value == "floral white":
                    color('floral white')
                elif value == "FloralWhite":
                    color('FloralWhite')
                elif value == "forest green":
                    color('forest green')
                elif value == "ForestGreen":
                    color('ForestGreen')
                elif value == "gainsboro":
                    color('gainsboro')
                elif value == "ghost white":
                    color('ghost white')
                elif value == "GhostWhite":
                    color('GhostWhite')
                elif value == "gold":
                    color('gold')
                elif value == "gold1":
                    color('gold1')
                elif value == "gold2":
                    color('gold2')
                elif value == "gold3":
                    color('gold3')
                elif value == "gold4":
                    color('gold4')
                elif value == "goldenrod":
                    color('goldenrod')
                elif value == "goldenrod1":
                    color('goldenrod1')
                elif value == "goldenrod2":
                    color('goldenrod2')
                elif value == "goldenrod3":
                    color('goldenrod3')
                elif value == "goldenrod4":
                    color('goldenrod4')
                elif value == "gray":
                    color('gray')
                elif value == "gray0":
                    color('gray0')
                elif value == "gray1":
                    color('gray1')
                elif value == "gray2":
                    color('gray2')
                elif value == "gray3":
                    color('gray3')
                elif value == "gray4":
                    color('gray4')
                elif value == "gray5":
                    color('gray5')
                elif value == "gray6":
                    color('gray6')
                elif value == "gray7":
                    color('gray7')
                elif value == "gray8":
                    color('gray8')
                elif value == "gray9":
                    color('gray9')
                elif value == "gray10":
                    color('gray10')
                elif value == "gray11":
                    color('gray11')
                elif value == "gray12":
                    color('gray12')
                elif value == "gray13":
                    color('gray13')
                elif value == "gray14":
                    color('gray14')
                elif value == "gray15":
                    color('gray15')
                elif value == "gray16":
                    color('gray16')
                elif value == "gray17":
                    color('gray17')
                elif value == "gray18":
                    color('gray18')
                elif value == "gray19":
                    color('gray19')
                elif value == "gray20":
                    color('gray20')
                elif value == "gray21":
                    color('gray21')
                elif value == "gray22":
                    color('gray22')
                elif value == "gray23":
                    color('gray23')
                elif value == "gray24":
                    color('gray24')
                elif value == "gray25":
                    color('gray25')
                elif value == "gray26":
                    color('gray26')
                elif value == "gray27":
                    color('gray27')
                elif value == "gray28":
                    color('gray28')
                elif value == "gray29":
                    color('gray29')
                elif value == "gray30":
                    color('gray30')
                elif value == "gray31":
                    color('gray31')
                elif value == "gray32":
                    color('gray32')
                elif value == "gray33":
                    color('gray33')
                elif value == "gray34":
                    color('gray34')
                elif value == "gray35":
                    color('gray35')
                elif value == "gray36":
                    color('gray36')
                elif value == "gray37":
                    color('gray37')
                elif value == "gray38":
                    color('gray38')
                elif value == "gray39":
                    color('gray39')
                elif value == "gray40":
                    color('gray40')
                elif value == "gray41":
                    color('gray41')
                elif value == "gray42":
                    color('gray42')
                elif value == "gray43":
                    color('gray43')
                elif value == "gray44":
                    color('gray44')
                elif value == "gray45":
                    color('gray45')
                elif value == "gray46":
                    color('gray46')
                elif value == "gray47":
                    color('gray47')
                elif value == "gray48":
                    color('gray48')
                elif value == "gray49":
                    color('gray49')
                elif value == "gray50":
                    color('gray50')
                elif value == "gray51":
                    color('gray51')
                elif value == "gray52":
                    color('gray52')
                elif value == "gray53":
                    color('gray53')
                elif value == "gray54":
                    color('gray54')
                elif value == "gray55":
                    color('gray55')
                elif value == "gray56":
                    color('gray56')
                elif value == "gray57":
                    color('gray57')
                elif value == "gray58":
                    color('gray58')
                elif value == "gray59":
                    color('gray59')
                elif value == "gray60":
                    color('gray60')
                elif value == "gray61":
                    color('gray61')
                elif value == "gray62":
                    color('gray62')
                elif value == "gray63":
                    color('gray63')
                elif value == "gray64":
                    color('gray64')
                elif value == "gray65":
                    color('gray65')
                elif value == "gray66":
                    color('gray66')
                elif value == "gray67":
                    color('gray67')
                elif value == "gray68":
                    color('gray68')
                elif value == "gray69":
                    color('gray69')
                elif value == "gray70":
                    color('gray70')
                elif value == "gray71":
                    color('gray71')
                elif value == "gray72":
                    color('gray72')
                elif value == "gray73":
                    color('gray73')
                elif value == "gray74":
                    color('gray74')
                elif value == "gray75":
                    color('gray75')
                elif value == "gray76":
                    color('gray76')
                elif value == "gray77":
                    color('gray77')
                elif value == "gray78":
                    color('gray78')
                elif value == "gray79":
                    color('gray79')
                elif value == "gray80":
                    color('gray80')
                elif value == "gray81":
                    color('gray81')
                elif value == "gray82":
                    color('gray82')
                elif value == "gray83":
                    color('gray83')
                elif value == "gray84":
                    color('gray84')
                elif value == "gray85":
                    color('gray85')
                elif value == "gray86":
                    color('gray86')
                elif value == "gray87":
                    color('gray87')
                elif value == "gray88":
                    color('gray88')
                elif value == "gray89":
                    color('gray89')
                elif value == "gray90":
                    color('gray90')
                elif value == "gray91":
                    color('gray91')
                elif value == "gray92":
                    color('gray92')
                elif value == "gray93":
                    color('gray93')
                elif value == "gray94":
                    color('gray94')
                elif value == "gray95":
                    color('gray95')
                elif value == "gray96":
                    color('gray96')
                elif value == "gray97":
                    color('gray97')
                elif value == "gray98":
                    color('gray98')
                elif value == "gray99":
                    color('gray99')
                elif value == "gray100":
                    color('gray100')
                elif value == "green":
                    color('green')
                elif value == "green yellow":
                    color('green yellow')
                elif value == "green1":
                    color('green1')
                elif value == "green2":
                    color('green2')
                elif value == "green3":
                    color('green3')
                elif value == "green4":
                    color('green4')
                elif value == "GreenYellow":
                    color('GreenYellow')
                elif value == "grey":
                    color('grey')
                elif value == "grey0":
                    color('grey0')
                elif value == "grey1":
                    color('grey1')
                elif value == "grey2":
                    color('grey2')
                elif value == "grey3":
                    color('grey3')
                elif value == "grey4":
                    color('grey4')
                elif value == "grey5":
                    color('grey5')
                elif value == "grey6":
                    color('grey6')
                elif value == "grey7":
                    color('grey7')
                elif value == "grey8":
                    color('grey8')
                elif value == "grey9":
                    color('grey9')
                elif value == "grey10":
                    color('grey10')
                elif value == "grey11":
                    color('grey11')
                elif value == "grey12":
                    color('grey12')
                elif value == "grey13":
                    color('grey13')
                elif value == "grey14":
                    color('grey14')
                elif value == "grey15":
                    color('grey15')
                elif value == "grey16":
                    color('grey16')
                elif value == "grey17":
                    color('grey17')
                elif value == "grey18":
                    color('grey18')
                elif value == "grey19":
                    color('grey19')
                elif value == "grey20":
                    color('grey20')
                elif value == "grey21":
                    color('grey21')
                elif value == "grey22":
                    color('grey22')
                elif value == "grey23":
                    color('grey23')
                elif value == "grey24":
                    color('grey24')
                elif value == "grey25":
                    color('grey25')
                elif value == "grey26":
                    color('grey26')
                elif value == "grey27":
                    color('grey27')
                elif value == "grey28":
                    color('grey28')
                elif value == "grey29":
                    color('grey29')
                elif value == "grey30":
                    color('grey30')
                elif value == "grey31":
                    color('grey31')
                elif value == "grey32":
                    color('grey32')
                elif value == "grey33":
                    color('grey33')
                elif value == "grey34":
                    color('grey34')
                elif value == "grey35":
                    color('grey35')
                elif value == "grey36":
                    color('grey36')
                elif value == "grey37":
                    color('grey37')
                elif value == "grey38":
                    color('grey38')
                elif value == "grey39":
                    color('grey39')
                elif value == "grey40":
                    color('grey40')
                elif value == "grey41":
                    color('grey41')
                elif value == "grey42":
                    color('grey42')
                elif value == "grey43":
                    color('grey43')
                elif value == "grey44":
                    color('grey44')
                elif value == "grey45":
                    color('grey45')
                elif value == "grey46":
                    color('grey46')
                elif value == "grey47":
                    color('grey47')
                elif value == "grey48":
                    color('grey48')
                elif value == "grey49":
                    color('grey49')
                elif value == "grey50":
                    color('grey50')
                elif value == "grey51":
                    color('grey51')
                elif value == "grey52":
                    color('grey52')
                elif value == "grey53":
                    color('grey53')
                elif value == "grey54":
                    color('grey54')
                elif value == "grey55":
                    color('grey55')
                elif value == "grey56":
                    color('grey56')
                elif value == "grey57":
                    color('grey57')
                elif value == "grey58":
                    color('grey58')
                elif value == "grey59":
                    color('grey59')
                elif value == "grey60":
                    color('grey60')
                elif value == "grey61":
                    color('grey61')
                elif value == "grey62":
                    color('grey62')
                elif value == "grey63":
                    color('grey63')
                elif value == "grey64":
                    color('grey64')
                elif value == "grey65":
                    color('grey65')
                elif value == "grey66":
                    color('grey66')
                elif value == "grey67":
                    color('grey67')
                elif value == "grey68":
                    color('grey68')
                elif value == "grey69":
                    color('grey69')
                elif value == "grey70":
                    color('grey70')
                elif value == "grey71":
                    color('grey71')
                elif value == "grey72":
                    color('grey72')
                elif value == "grey73":
                    color('grey73')
                elif value == "grey74":
                    color('grey74')
                elif value == "grey75":
                    color('grey75')
                elif value == "grey76":
                    color('grey76')
                elif value == "grey77":
                    color('grey77')
                elif value == "grey78":
                    color('grey78')
                elif value == "grey79":
                    color('grey79')
                elif value == "grey80":
                    color('grey80')
                elif value == "grey81":
                    color('grey81')
                elif value == "grey82":
                    color('grey82')
                elif value == "grey83":
                    color('grey83')
                elif value == "grey84":
                    color('grey84')
                elif value == "grey85":
                    color('grey85')
                elif value == "grey86":
                    color('grey86')
                elif value == "grey87":
                    color('grey87')
                elif value == "grey88":
                    color('grey88')
                elif value == "grey89":
                    color('grey89')
                elif value == "grey90":
                    color('grey90')
                elif value == "grey91":
                    color('grey91')
                elif value == "grey92":
                    color('grey92')
                elif value == "grey93":
                    color('grey93')
                elif value == "grey94":
                    color('grey94')
                elif value == "grey95":
                    color('grey95')
                elif value == "grey96":
                    color('grey96')
                elif value == "grey97":
                    color('grey97')
                elif value == "grey98":
                    color('grey98')
                elif value == "grey99":
                    color('grey99')
                elif value == "grey100":
                    color('grey100')
                elif value == "honeydew":
                    color('honeydew')
                elif value == "honeydew1":
                    color('honeydew1')
                elif value == "honeydew2":
                    color('honeydew2')
                elif value == "honeydew3":
                    color('honeydew3')
                elif value == "honeydew4":
                    color('honeydew4')
                elif value == "hot pink":
                    color('hot pink')
                elif value == "HotPink":
                    color('HotPink')
                elif value == "HotPink1":
                    color('HotPink1')
                elif value == "HotPink2":
                    color('HotPink2')
                elif value == "HotPink3":
                    color('HotPink3')
                elif value == "HotPink4":
                    color('HotPink4')
                elif value == "indian red":
                    color('indian red')
                elif value == "IndianRed":
                    color('IndianRed')
                elif value == "IndianRed1":
                    color('IndianRed1')
                elif value == "IndianRed2":
                    color('IndianRed2')
                elif value == "IndianRed3":
                    color('IndianRed3')
                elif value == "IndianRed4":
                    color('IndianRed4')
                elif value == "ivory":
                    color('ivory')
                elif value == "ivory1":
                    color('ivory1')
                elif value == "ivory2":
                    color('ivory2')
                elif value == "ivory3":
                    color('ivory3')
                elif value == "ivory4":
                    color('ivory4')
                elif value == "khaki":
                    color('khaki')
                elif value == "khaki1":
                    color('khaki1')
                elif value == "khaki2":
                    color('khaki2')
                elif value == "khaki3":
                    color('khaki3')
                elif value == "khaki4":
                    color('khaki4')
                elif value == "lavender":
                    color('lavender')
                elif value == "lavender blush":
                    color('lavender blush')
                elif value == "LavenderBlush":
                    color('LavenderBlush')
                elif value == "LavenderBlush1":
                    color('LavenderBlush1')
                elif value == "LavenderBlush2":
                    color('LavenderBlush2')
                elif value == "LavenderBlush3":
                    color('LavenderBlush3')
                elif value == "LavenderBlush4":
                    color('LavenderBlush4')
                elif value == "lawn green":
                    color('lawn green')
                elif value == "LawnGreen":
                    color('LawnGreen')
                elif value == "lemon chiffon":
                    color('lemon chiffon')
                elif value == "LemonChiffon":
                    color('LemonChiffon')
                elif value == "LemonChiffon1":
                    color('LemonChiffon1')
                elif value == "LemonChiffon2":
                    color('LemonChiffon2')
                elif value == "LemonChiffon3":
                    color('LemonChiffon3')
                elif value == "LemonChiffon4":
                    color('LemonChiffon4')
                elif value == "light blue":
                    color('light blue')
                elif value == "light coral":
                    color('light coral')
                elif value == "light cyan":
                    color('light cyan')
                elif value == "light goldenrod":
                    color('light goldenrod')
                elif value == "light goldenrod yellow":
                    color('light goldenrod yellow')
                elif value == "light gray":
                    color('light gray')
                elif value == "light green":
                    color('light green')
                elif value == "light grey":
                    color('light grey')
                elif value == "light pink":
                    color('light pink')
                elif value == "light salmon":
                    color('light salmon')
                elif value == "light sea green":
                    color('light sea green')
                elif value == "light sky blue":
                    color('light sky blue')
                elif value == "light slate blue":
                    color('light slate blue')
                elif value == "light slate gray":
                    color('light slate gray')
                elif value == "light slate grey":
                    color('light slate grey')
                elif value == "light steel blue":
                    color('light steel blue')
                elif value == "light yellow":
                    color('light yellow')
                elif value == "LightBlue":
                    color('LightBlue')
                elif value == "LightBlue1":
                    color('LightBlue1')
                elif value == "LightBlue2":
                    color('LightBlue2')
                elif value == "LightBlue3":
                    color('LightBlue3')
                elif value == "LightBlue4":
                    color('LightBlue4')
                elif value == "LightCoral":
                    color('LightCoral')
                elif value == "LightCyan":
                    color('LightCyan')
                elif value == "LightCyan1":
                    color('LightCyan1')
                elif value == "LightCyan2":
                    color('LightCyan2')
                elif value == "LightCyan3":
                    color('LightCyan3')
                elif value == "LightCyan4":
                    color('LightCyan4')
                elif value == "LightGoldenrod":
                    color('LightGoldenrod')
                elif value == "LightGoldenrod1":
                    color('LightGoldenrod1')
                elif value == "LightGoldenrod2":
                    color('LightGoldenrod2')
                elif value == "LightGoldenrod3":
                    color('LightGoldenrod3')
                elif value == "LightGoldenrod4":
                    color('LightGoldenrod4')
                elif value == "LightGoldenrodYellow":
                    color('LightGoldenrodYellow')
                elif value == "LightGray":
                    color('LightGray')
                elif value == "LightGreen":
                    color('LightGreen')
                elif value == "LightGrey":
                    color('LightGrey')
                elif value == "LightPink":
                    color('LightPink')
                elif value == "LightPink1":
                    color('LightPink1')
                elif value == "LightPink2":
                    color('LightPink2')
                elif value == "LightPink3":
                    color('LightPink3')
                elif value == "LightPink4":
                    color('LightPink4')
                elif value == "LightSalmon":
                    color('LightSalmon')
                elif value == "LightSalmon1":
                    color('LightSalmon1')
                elif value == "LightSalmon2":
                    color('LightSalmon2')
                elif value == "LightSalmon3":
                    color('LightSalmon3')
                elif value == "LightSalmon4":
                    color('LightSalmon4')
                elif value == "LightSeaGreen":
                    color('LightSeaGreen')
                elif value == "LightSkyBlue":
                    color('LightSkyBlue')
                elif value == "LightSkyBlue1":
                    color('LightSkyBlue1')
                elif value == "LightSkyBlue2":
                    color('LightSkyBlue2')
                elif value == "LightSkyBlue3":
                    color('LightSkyBlue3')
                elif value == "LightSkyBlue4":
                    color('LightSkyBlue4')
                elif value == "LightSlateBlue":
                    color('LightSlateBlue')
                elif value == "LightSlateGray":
                    color('LightSlateGray')
                elif value == "LightSlateGrey":
                    color('LightSlateGrey')
                elif value == "LightSteelBlue":
                    color('LightSteelBlue')
                elif value == "LightSteelBlue1":
                    color('LightSteelBlue1')
                elif value == "LightSteelBlue2":
                    color('LightSteelBlue2')
                elif value == "LightSteelBlue3":
                    color('LightSteelBlue3')
                elif value == "LightSteelBlue4":
                    color('LightSteelBlue4')
                elif value == "LightYellow":
                    color('LightYellow')
                elif value == "LightYellow1":
                    color('LightYellow1')
                elif value == "LightYellow2":
                    color('LightYellow2')
                elif value == "LightYellow3":
                    color('LightYellow3')
                elif value == "LightYellow4":
                    color('LightYellow4')
                elif value == "lime green":
                    color('lime green')
                elif value == "LimeGreen":
                    color('LimeGreen')
                elif value == "linen":
                    color('linen')
                elif value == "magenta":
                    color('magenta')
                elif value == "magenta1":
                    color('magenta1')
                elif value == "magenta2":
                    color('magenta2')
                elif value == "magenta3":
                    color('magenta3')
                elif value == "magenta4":
                    color('magenta4')
                elif value == "maroon":
                    color('maroon')
                elif value == "maroon1":
                    color('maroon1')
                elif value == "maroon2":
                    color('maroon2')
                elif value == "maroon3":
                    color('maroon3')
                elif value == "maroon4":
                    color('maroon4')
                elif value == "medium aquamarine":
                    color('medium aquamarine')
                elif value == "medium blue":
                    color('medium blue')
                elif value == "medium orchid":
                    color('medium orchid')
                elif value == "medium purple":
                    color('medium purple')
                elif value == "medium sea green":
                    color('medium sea green')
                elif value == "medium slate blue":
                    color('medium slate blue')
                elif value == "medium spring green":
                    color('medium spring green')
                elif value == "medium turquoise":
                    color('medium turquoise')
                elif value == "medium violet red":
                    color('medium violet red')
                elif value == "MediumAquamarine":
                    color('MediumAquamarine')
                elif value == "MediumBlue":
                    color('MediumBlue')
                elif value == "MediumOrchid":
                    color('MediumOrchid')
                elif value == "MediumOrchid1":
                    color('MediumOrchid1')
                elif value == "MediumOrchid2":
                    color('MediumOrchid2')
                elif value == "MediumOrchid3":
                    color('MediumOrchid3')
                elif value == "MediumOrchid4":
                    color('MediumOrchid4')
                elif value == "MediumPurple":
                    color('MediumPurple')
                elif value == "MediumPurple1":
                    color('MediumPurple1')
                elif value == "MediumPurple2":
                    color('MediumPurple2')
                elif value == "MediumPurple3":
                    color('MediumPurple3')
                elif value == "MediumPurple4":
                    color('MediumPurple4')
                elif value == "MediumSeaGreen":
                    color('MediumSeaGreen')
                elif value == "MediumSlateBlue":
                    color('MediumSlateBlue')
                elif value == "MediumSpringGreen":
                    color('MediumSpringGreen')
                elif value == "MediumTurquoise":
                    color('MediumTurquoise')
                elif value == "MediumVioletRed":
                    color('MediumVioletRed')
                elif value == "midnight blue":
                    color('midnight blue')
                elif value == "MidnightBlue":
                    color('MidnightBlue')
                elif value == "mint cream":
                    color('mint cream')
                elif value == "MintCream":
                    color('MintCream')
                elif value == "misty rose":
                    color('misty rose')
                elif value == "MistyRose":
                    color('MistyRose')
                elif value == "MistyRose1":
                    color('MistyRose1')
                elif value == "MistyRose2":
                    color('MistyRose2')
                elif value == "MistyRose3":
                    color('MistyRose3')
                elif value == "MistyRose4":
                    color('MistyRose4')
                elif value == "moccasin":
                    color('moccasin')
                elif value == "navajo white":
                    color('navajo white')
                elif value == "NavajoWhite":
                    color('NavajoWhite')
                elif value == "NavajoWhite1":
                    color('NavajoWhite1')
                elif value == "NavajoWhite2":
                    color('NavajoWhite2')
                elif value == "NavajoWhite3":
                    color('NavajoWhite3')
                elif value == "NavajoWhite4":
                    color('NavajoWhite4')
                elif value == "navy":
                    color('navy')
                elif value == "navy blue":
                    color('navy blue')
                elif value == "NavyBlue":
                    color('NavyBlue')
                elif value == "old lace":
                    color('old lace')
                elif value == "OldLace":
                    color('OldLace')
                elif value == "olive drab":
                    color('olive drab')
                elif value == "OliveDrab":
                    color('OliveDrab')
                elif value == "OliveDrab1":
                    color('OliveDrab1')
                elif value == "OliveDrab2":
                    color('OliveDrab2')
                elif value == "OliveDrab3":
                    color('OliveDrab3')
                elif value == "OliveDrab4":
                    color('OliveDrab4')
                elif value == "orange":
                    color('orange')
                elif value == "orange red":
                    color('orange red')
                elif value == "orange1":
                    color('orange1')
                elif value == "orange2":
                    color('orange2')
                elif value == "orange3":
                    color('orange3')
                elif value == "orange4":
                    color('orange4')
                elif value == "OrangeRed":
                    color('OrangeRed')
                elif value == "OrangeRed1":
                    color('OrangeRed1')
                elif value == "OrangeRed2":
                    color('OrangeRed2')
                elif value == "OrangeRed3":
                    color('OrangeRed3')
                elif value == "OrangeRed4":
                    color('OrangeRed4')
                elif value == "orchid":
                    color('orchid')
                elif value == "orchid1":
                    color('orchid1')
                elif value == "orchid2":
                    color('orchid2')
                elif value == "orchid3":
                    color('orchid3')
                elif value == "orchid4":
                    color('orchid4')
                elif value == "pale goldenrod":
                    color('pale goldenrod')
                elif value == "pale green":
                    color('pale green')
                elif value == "pale turquoise":
                    color('pale turquoise')
                elif value == "pale violet red":
                    color('pale violet red')
                elif value == "PaleGoldenrod":
                    color('PaleGoldenrod')
                elif value == "PaleGreen":
                    color('PaleGreen')
                elif value == "PaleGreen1":
                    color('PaleGreen1')
                elif value == "PaleGreen2":
                    color('PaleGreen2')
                elif value == "PaleGreen3":
                    color('PaleGreen3')
                elif value == "PaleGreen4":
                    color('PaleGreen4')
                elif value == "PaleTurquoise":
                    color('PaleTurquoise')
                elif value == "PaleTurquoise1":
                    color('PaleTurquoise1')
                elif value == "PaleTurquoise2":
                    color('PaleTurquoise2')
                elif value == "PaleTurquoise3":
                    color('PaleTurquoise3')
                elif value == "PaleTurquoise4":
                    color('PaleTurquoise4')
                elif value == "PaleVioletRed":
                    color('PaleVioletRed')
                elif value == "PaleVioletRed1":
                    color('PaleVioletRed1')
                elif value == "PaleVioletRed2":
                    color('PaleVioletRed2')
                elif value == "PaleVioletRed3":
                    color('PaleVioletRed3')
                elif value == "PaleVioletRed4":
                    color('PaleVioletRed4')
                elif value == "papaya whip":
                    color('papaya whip')
                elif value == "PapayaWhip":
                    color('PapayaWhip')
                elif value == "peach puff":
                    color('peach puff')
                elif value == "PeachPuff":
                    color('PeachPuff')
                elif value == "PeachPuff1":
                    color('PeachPuff1')
                elif value == "PeachPuff2":
                    color('PeachPuff2')
                elif value == "PeachPuff3":
                    color('PeachPuff3')
                elif value == "PeachPuff4":
                    color('PeachPuff4')
                elif value == "peru":
                    color('peru')
                elif value == "pink":
                    color('pink')
                elif value == "pink1":
                    color('pink1')
                elif value == "pink2":
                    color('pink2')
                elif value == "pink3":
                    color('pink3')
                elif value == "pink4":
                    color('pink4')
                elif value == "plum":
                    color('plum')
                elif value == "plum1":
                    color('plum1')
                elif value == "plum2":
                    color('plum2')
                elif value == "plum3":
                    color('plum3')
                elif value == "plum4":
                    color('plum4')
                elif value == "powder blue":
                    color('powder blue')
                elif value == "PowderBlue":
                    color('PowderBlue')
                elif value == "purple":
                    color('purple')
                elif value == "purple1":
                    color('purple1')
                elif value == "purple2":
                    color('purple2')
                elif value == "purple3":
                    color('purple3')
                elif value == "purple4":
                    color('purple4')
                elif value == "red":
                    color('red')
                elif value == "red1":
                    color('red1')
                elif value == "red2":
                    color('red2')
                elif value == "red3":
                    color('red3')
                elif value == "red4":
                    color('red4')
                elif value == "rosy brown":
                    color('rosy brown')
                elif value == "RosyBrown":
                    color('RosyBrown')
                elif value == "RosyBrown1":
                    color('RosyBrown1')
                elif value == "RosyBrown2":
                    color('RosyBrown2')
                elif value == "RosyBrown3":
                    color('RosyBrown3')
                elif value == "RosyBrown4":
                    color('RosyBrown4')
                elif value == "royal blue":
                    color('royal blue')
                elif value == "RoyalBlue":
                    color('RoyalBlue')
                elif value == "RoyalBlue1":
                    color('RoyalBlue1')
                elif value == "RoyalBlue2":
                    color('RoyalBlue2')
                elif value == "RoyalBlue3":
                    color('RoyalBlue3')
                elif value == "RoyalBlue4":
                    color('RoyalBlue4')
                elif value == "saddle brown":
                    color('saddle brown')
                elif value == "SaddleBrown":
                    color('SaddleBrown')
                elif value == "salmon":
                    color('salmon')
                elif value == "salmon1":
                    color('salmon1')
                elif value == "salmon2":
                    color('salmon2')
                elif value == "salmon3":
                    color('salmon3')
                elif value == "salmon4":
                    color('salmon4')
                elif value == "sandy brown":
                    color('sandy brown')
                elif value == "SandyBrown":
                    color('SandyBrown')
                elif value == "sea green":
                    color('sea green')
                elif value == "SeaGreen":
                    color('SeaGreen')
                elif value == "SeaGreen1":
                    color('SeaGreen1')
                elif value == "SeaGreen2":
                    color('SeaGreen2')
                elif value == "SeaGreen3":
                    color('SeaGreen3')
                elif value == "SeaGreen4":
                    color('SeaGreen4')
                elif value == "seashell":
                    color('seashell')
                elif value == "seashell1":
                    color('seashell1')
                elif value == "seashell2":
                    color('seashell2')
                elif value == "seashell3":
                    color('seashell3')
                elif value == "seashell4":
                    color('seashell4')
                elif value == "sienna":
                    color('sienna')
                elif value == "sienna1":
                    color('sienna1')
                elif value == "sienna2":
                    color('sienna2')
                elif value == "sienna3":
                    color('sienna3')
                elif value == "sienna4":
                    color('sienna4')
                elif value == "sky blue":
                    color('sky blue')
                elif value == "SkyBlue":
                    color('SkyBlue')
                elif value == "SkyBlue1":
                    color('SkyBlue1')
                elif value == "SkyBlue2":
                    color('SkyBlue2')
                elif value == "SkyBlue3":
                    color('SkyBlue3')
                elif value == "SkyBlue4":
                    color('SkyBlue4')
                elif value == "slate blue":
                    color('slate blue')
                elif value == "slate gray":
                    color('slate gray')
                elif value == "slate grey":
                    color('slate grey')
                elif value == "SlateBlue":
                    color('SlateBlue')
                elif value == "SlateBlue1":
                    color('SlateBlue1')
                elif value == "SlateBlue2":
                    color('SlateBlue2')
                elif value == "SlateBlue3":
                    color('SlateBlue3')
                elif value == "SlateBlue4":
                    color('SlateBlue4')
                elif value == "SlateGray":
                    color('SlateGray')
                elif value == "SlateGray1":
                    color('SlateGray1')
                elif value == "SlateGray2":
                    color('SlateGray2')
                elif value == "SlateGray3":
                    color('SlateGray3')
                elif value == "SlateGray4":
                    color('SlateGray4')
                elif value == "SlateGrey":
                    color('SlateGrey')
                elif value == "snow":
                    color('snow')
                elif value == "snow1":
                    color('snow1')
                elif value == "snow2":
                    color('snow2')
                elif value == "snow3":
                    color('snow3')
                elif value == "snow4":
                    color('snow4')
                elif value == "spring green":
                    color('spring green')
                elif value == "SpringGreen":
                    color('SpringGreen')
                elif value == "SpringGreen1":
                    color('SpringGreen1')
                elif value == "SpringGreen2":
                    color('SpringGreen2')
                elif value == "SpringGreen3":
                    color('SpringGreen3')
                elif value == "SpringGreen4":
                    color('SpringGreen4')
                elif value == "steel blue":
                    color('steel blue')
                elif value == "SteelBlue":
                    color('SteelBlue')
                elif value == "SteelBlue1":
                    color('SteelBlue1')
                elif value == "SteelBlue2":
                    color('SteelBlue2')
                elif value == "SteelBlue3":
                    color('SteelBlue3')
                elif value == "SteelBlue4":
                    color('SteelBlue4')
                elif value == "tan":
                    color('tan')
                elif value == "tan1":
                    color('tan1')
                elif value == "tan2":
                    color('tan2')
                elif value == "tan3":
                    color('tan3')
                elif value == "tan4":
                    color('tan4')
                elif value == "thistle":
                    color('thistle')
                elif value == "thistle1":
                    color('thistle1')
                elif value == "thistle2":
                    color('thistle2')
                elif value == "thistle3":
                    color('thistle3')
                elif value == "thistle4":
                    color('thistle4')
                elif value == "tomato":
                    color('tomato')
                elif value == "tomato1":
                    color('tomato1')
                elif value == "tomato2":
                    color('tomato2')
                elif value == "tomato3":
                    color('tomato3')
                elif value == "tomato4":
                    color('tomato4')
                elif value == "turquoise":
                    color('turquoise')
                elif value == "turquoise1":
                    color('turquoise1')
                elif value == "turquoise2":
                    color('turquoise2')
                elif value == "turquoise3":
                    color('turquoise3')
                elif value == "turquoise4":
                    color('turquoise4')
                elif value == "violet":
                    color('violet')
                elif value == "violet red":
                    color('violet red')
                elif value == "VioletRed":
                    color('VioletRed')
                elif value == "VioletRed1":
                    color('VioletRed1')
                elif value == "VioletRed2":
                    color('VioletRed2')
                elif value == "VioletRed3":
                    color('VioletRed3')
                elif value == "VioletRed4":
                    color('VioletRed4')
                elif value == "wheat":
                    color('wheat')
                elif value == "wheat1":
                    color('wheat1')
                elif value == "wheat2":
                    color('wheat2')
                elif value == "wheat3":
                    color('wheat3')
                elif value == "wheat4":
                    color('wheat4')
                elif value == "white":
                    color('white')
                elif value == "white smoke":
                    color('white smoke')
                elif value == "WhiteSmoke":
                    color('WhiteSmoke')
                elif value == "yellow":
                    color('yellow')
                elif value == "yellow green":
                    color('yellow green')
                elif value == "yellow1":
                    color('yellow1')
                elif value == "yellow2":
                    color('yellow2')
                elif value == "yellow3":
                    color('yellow3')
                elif value == "yellow4":
                    color('yellow4')
                elif value == "YellowGreen":
                    color('YellowGreen')
                else:
                    tkMessageBox.showerror("Error", "Color, " + value + ", not available")
                print value
            else:
                tkMessageBox.showerror("Command Not Found", line + "does not exits")
                return
        
