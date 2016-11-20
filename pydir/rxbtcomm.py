#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2016 F Dou<programmingrobotsstudygroup@gmail.com>
# See LICENSE for details.


import bluetooth
import logging

class RxBtComm(object):
    """BT communication wrapper:

    Attributes:
        addy: A string representing the device address.
        name: A string representing the device name.
    """
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self, addr, name=None):
        """Return a RxBtComm object
           param *addr* device address
           param *name* device name
        """
        self.addr = addr
        self.name = name
        self.sock = None

    """connect:
       Connect to BT addr
    """
    def connect(self):
        try:
            port = 1
            self.sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            self.sock.connect((self.addr, port))
            return bluetooth.lookup_name(self.addr)
        except Exception as e:
            logging.exception(e)
            return ''

    """disconnect:
       Disconnect from BT addr
    """
    def disconnect(self):
        try:
            self.sock.close()
        except Exception as e:
            logging.exception(e)
        self.sock = None

    """send:
       Send a command to host
    """
    def send(self, cmd):
        self.sock.send(cmd)

    """recieve:
       Recieve a response from host
    """
    def recieve(self):
        self.sock.recieve(cmd)

### Replace xx:xx:xx:xx:xx:xx with your test device address
#test = RXComm('xx:xx:xx:xx:xx:xx', 'Test Device')
#test.connect()
#test.send('date')
#test.disconnect()

