#!/bin/bash

yum install -y git
yum install -y tkinter
mkdir code
cd code
git clone git://github.com/Zanarama/AmazingTurtle
cp /home/olpc/code/AmazingTurtle/maze.py /home/olpc/Activities/Pippy.activity/data/python/
cp /home/olpc/code/AmazingTurtle/solution.py /home/olpc/Activities/Pippy.activity/data/python/
su -c 'cp /home/olpc/code/AmazingTurtle/maze.py /usr/lib/python2.7'
