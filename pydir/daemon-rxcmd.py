#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright (c) 2016 F Dou<programmingrobotsstudygroup@gmail.com>
# See LICENSE for details.

import bluetooth
import os
import logging
import time
from daemon import runner

class RxCmdDaemon():
    def __init__(self):
        self.stdin_path   = '/dev/null'
#        self.stdout_path  = '/dev/tty'
        self.stdout_path = '/tmp/RxCmdDaemon.log'
        self.stderr_path = self.stdout_path
#        self.stderr_path = '/home/robot/pydir/daemon.log'
#        self.stderr_path  = '/dev/tty'
        self.pidfile_path = '/tmp/RxCmdDaemon.pid'
        self.pidfile_timeout = 5

    def run(self):
        while True:
            server_sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
            port = 1
            server_sock.bind(("",port))
            server_sock.listen(1)
            client_sock,address = server_sock.accept()
            print "Accepted connection from ",address
            try:
                while True:
                    data = client_sock.recv(1024)
                    print "received [%s]" % data
                    os.system(data)
            except Exception as e:
                logging.exception(e)

rxCmdDaemon = RxCmdDaemon()
daemon_runner = runner.DaemonRunner(rxCmdDaemon)
daemon_runner.do_action()

