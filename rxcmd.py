#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2016 F Dou<programmingrobotsstudygroup@gmail.com>
# See LICENSE for details.

import bluetooth
import sys

import curses
import logging
from rxbtcomm import RxBtComm

class RxCmd(object):
    """rxcmd accepts commands from user:

    Attributes:
        addy: A string representing the device address.
        name: A string representing the device name.
    """
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        """Return a RxCmd object
        """
        self.cmd = ''
        self.kill = False

    """connect:
       Connect to BT addr
    """
    def initScreen(self, stdscr, addr):
        stdscr.addstr(0,0,"Talking to: "+addr+". Hit enter to send, 'esc' to quit")
        stdscr.addstr(1,0,"")
        stdscr.refresh()

    def curses_main(self, args, addr):
        stdscr = curses.initscr()
        self.initScreen(stdscr, addr)
        self.getLine(stdscr)


    def getLine(self, stdscr):
        # Get a line to send
        key = ''
        # TODO Replace # w/ curses curses.KEY_XXX equivalent
        self.cmd = ''
        while (key != 27) and (key != 10):
            key = stdscr.getch()
            stdscr.refresh()
            if (key != curses.KEY_UP) and (key != curses.KEY_DOWN): 
                self.cmd = self.cmd + chr(key)
                stdscr.addstr(1,0,self.cmd)
        if (key == 27):
            self.kill = True
        #
        self.cmd = self.cmd.strip()

##########################################################
#


# Turn on logging
logging.basicConfig(level=logging.DEBUG)

# BT 
bd_addr = None
port = 1
cmd=""

# Check command line params
if len(sys.argv) > 1:
    bd_addr = sys.argv[1]
else:
    print "usage: rxcmd xx:xx:xx:xx:xx:xx"
    sys.exit(0)

## Attempt to connect
try:
    comm = RxBtComm(bd_addr,'unknown')
    deviceName = comm.connect()
except Exception as e:
    logging.exception(e)

# Instance of UI object
ui = RxCmd()
##
while (not ui.kill):
    curses.wrapper(ui.curses_main, deviceName)
    if ui.kill: break
    # Send a line
    try:
        comm.send(ui.cmd)
    except Exception as e:
        logging.exception(e)
        ui.kill = True

comm.disconnect()

