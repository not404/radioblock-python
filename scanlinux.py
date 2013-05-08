#! /usr/bin/env python
"""\
Scan for serial ports. Linux specific variant that also includes USB/Serial
adapters.

Part of pySerial (http://pyserial.sf.net)
(C) 2009 <cliechti@gmx.net>
"""

import serial
import glob

def scan():
    """scan for available ports. return a list of device names."""
    # ports = glob.glob('/dev/ttys*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob('/dev/tty.SLAB*')
    # Just use some ports...
    ports = glob.glob('/dev/tty.SLAB*') + glob.glob('/dev/ttyUSB*') + glob.glob('/dev/ttyACM*') + glob.glob('/dev/ttyAMA*')
    return ports

def print_scan():
    com_ports = scan()
    print ("Found ports:")
    for name in com_ports:
        print (name)
    return com_ports
