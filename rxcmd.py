#!/usr/bin/python

import bluetooth
import sys

bd_addr = None
cmd="date"
port = 1

if len(sys.argv) > 1:
    bd_addr = sys.argv[1]
else:
    print "usage: rxcmd xx:xx:xx:xx:xx:xx"
    sys.exit(0)

print bd_addr
sock=bluetooth.BluetoothSocket( bluetooth.RFCOMM )
sock.connect((bd_addr, port))

sock.send(cmd)

sock.close()
