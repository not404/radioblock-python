# Copyright (c) 2011 - 2012, SimpleMesh AUTHORS
# Eric Gnoske,
# Colin O'Flynn,
# Blake Leverett,
# Rob Fries,
# Colorado Micro Devices Inc..
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   1) Redistributions of source code must retain the above copyright notice,
#      this list of conditions and the following disclaimer.
#
#   2) Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#
#   3) Neither the name of the SimpleMesh AUTHORS nor the names of its contributors
#       may be used to endorse or promote products derived from this software
#       without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
#  ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE
#  LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
#  CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
#  SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
#  INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
#  CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
#  ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
#  POSSIBILITY OF SUCH DAMAGE.

__author__ = 'egnoske'

# Hey, this is a pyside application!
from PySide import QtCore, QtGui

from PySide.QtGui import QColor

# Needed for string handling (I think)...
try:
    from PySide.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = type("")

# This is used in the signal/slot setup in the Com_Port class.
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

# Need sys to play with paths.
import sys

# The mainwindow GUI class is one directory level up.
sys.path.append('../')
path = sys.path # A debug ine to examine the path...

# With path set, we can import the module (file) containing the mainwindow class.
import mainwindow

# This enables the serial port.
import serial
import scanlinux
import scan

# When we scan we need to know which OS we're operating on.
import os
import platform

# Stuff to mangle strings and hex...
from binascii import unhexlify, hexlify, b2a_hex, a2b_hex
from hexmonster import d2b, t2b, d2hexstr, hexstr2d, b2d, hex2hexstr, hexstr2b

# Create a QTimer, 'f()' will be implemented near the end of this module but we
# need to kick the timer off inside the openComPort method so it needs to be
# created here.
from PySide.QtCore import QTimer

###############################################################################

class Com_Port(object):

    com_port_opened = ''
    serial_frame = ''
    #-------------------------------------------------------------------------#

    def __init__(self, name):
        self.name = name
    #-------------------------------------------------------------------------#

    def printme(self):
        print(self.name)
    #-------------------------------------------------------------------------#

    def findComPorts(self, ui, serial_port):
        # This function just prints them to the terminal/console.
        if platform.system() == 'Windows':
            ports = []
            port_index = 0
            win_ports = scan.scan()
            # For Windows, we need to get just the name not the tuple...
            for each_tuple in win_ports:
                #ports = ports + each_tuple[1] + ', '
                ports.append(each_tuple[1])
                #port_index =port_index + 1

        elif platform.system() == 'Linux':
            ports = scanlinux.scan()
        else: # We're a Mac
            ports = scanlinux.scan()

        # Populate the drop down list box for the COM ports
        for item in ports:
            ui.comboBoxCOMPort.addItem(item)

        # Create a list of typical BAUD rates and populate the Combo Box with those.
        baud = ['9600','14400','19200','28800','38400','57600','115200','230400','256000']
        for item in baud:
            ui.comboBoxBAUDRate.addItem(item)

        # Setup a signal slot to test that when a user selects a BAUD rate we can 'use' that BAUD rate in
        # another method/function...
        QtCore.QObject.connect(ui.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openComPort)

        # Setup the signal/slot for the quit button too.
        QtCore.QObject.connect(ui.pushButton_4, QtCore.SIGNAL(_fromUtf8("clicked()")), self.quitTheApp)

        # Setup the signal/slot for the close COM Port button too.
        QtCore.QObject.connect(ui.pushButton_2, QtCore.SIGNAL(_fromUtf8("clicked()")), self.closeComPort)

        # Override the built in keyPressEvent to handle it with our logic.
        ui.textEditTx.keyPressEvent = self.keyPressEvent
    #-------------------------------------------------------------------------#

    def openComPort(self):
        # This gets the text of the user selected item
        baud = QString(ui.comboBoxBAUDRate.currentText())
        baudnum = int(baud, 10) # The '10' indicates decimal.

        # Get the serial port to connect to.
        comport = QString(ui.comboBoxCOMPort.currentText())

        # Using pyserial and the user entered GUI stuff, open the damn serial port
        serial_port = serial.Serial(comport, baudnum,  timeout=5)

        if serial_port.isOpen():
            ui.textEditRx.setTextColor(QColor("green"))
            ui.textEditRx.setText("COM port is open!")
        else:
            ui.textEditRx.setTextColor(QColor("red"))
            ui.textEditRx.setText("COM port is closed!")
        # Revert back to black text.
        ui.textEditRx.setTextColor(QColor("black"))

        # This fires the timer that get's us into this application's while(1) loop!
        QtCore.QTimer.singleShot(1000, com.radioLegoApp(serial_port))

        return serial_port
    #-------------------------------------------------------------------------#

    def closeComPort(self):
        serial_port.close()
        ui.textEditRx.setTextColor(QColor("red"))
        ui.textEditRx.setText("COM port is closed!")
        ui.textEditRx.setTextColor(QColor("black"))
    #-------------------------------------------------------------------------#

    def quitTheApp(self):
        sys.exit(app.exec_())
        # This works but I get a 'Process finished with exit code 255' message?
        # Something about 'QCoreApplication::exec: The event loop is already running'...
    #-------------------------------------------------------------------------#

    def readComPort(self, serial_port, num_bytes):
        # Create some states to help parse the returned frame.
        RESETSTATE =        255
        STARTSTATE =        0
        LENGTHSTATE =       1
        COMMANDIDSTATE =    2
        PAYLOADSTATE =      3
        current_state =     STARTSTATE
        command_id = 0
        frame_length = 0
        payload = []

        # Get the data and post it to the box.
        rxdata = serial_port.read(num_bytes)
        print('rx data received = ', rxdata)

        for ch in rxdata:

            ch = ord(ch)    # Python3.x The data is in the form '\xab'

            ui.textEditRx.insertPlainText(d2hexstr(ch))
            ui.textEditRx.insertPlainText(' ')

            # Put it into the command frame constructor area too...
            ui.textEditRfResponse.insertPlainText(d2hexstr(ch))
            ui.textEditRfResponse.insertPlainText(' ')

            # We can pick off the start of frame, command id and payload here to parse it...
            if current_state == STARTSTATE:
                if ch == ord(b'\xAB'):
                    current_state = LENGTHSTATE
                    print 'Parsing started, ch = ', hex(ch)
            elif current_state == LENGTHSTATE:
                frame_length = ch
                print 'Grabbing frame length, ch = ', hex(ch)
                current_state = COMMANDIDSTATE
            elif current_state == COMMANDIDSTATE:
                command_id = ch
                print 'Getting the command id, ch = ', hex(ch)
                current_state = PAYLOADSTATE
            elif current_state == PAYLOADSTATE:
                print 'Parsing the payload, ch = ', hex(ch)
                if frame_length == 0:
                    current_state = STARTSTATE
                    # Add a carriage return...
                    ui.textEditRx.insertPlainText('\n')
                    ui.textEditRfResponse.insertPlainText('\n')
                else:
                    frame_length -= 1

                if frame_length >= 1: # Don't grab any CRC bytes.
                    payload.append(hex(ch))

    #-------------------------------------------------------------------------#

    # This is our custom event - we have usurped the built in one.
    # I didn't do anything fancy like sub-classing or filter lists.
    # This handles all the characters necessary...

    # For user interface, it might be nice to setup a backspace...
    def keyPressEvent(self, event):
        if event.key() in ( QtCore.Qt.Key_Return, QtCore.Qt.Key_Enter):
            ui.textEditTx.insertPlainText(str('\n')) # Put a new line in.
            # OK, the user has hit return or enter - Time to fire the serial_frame
            # over the UART...
            self.com_port_opened.write(bytes(self.serial_frame, "utf-8"))

            # Clear the serial_frame
            self.serial_frame = ''

        # If it is a capital letter
        if event.modifiers() & QtCore.Qt.ShiftModifier:
            ui.textEditTx.insertPlainText(str(chr(event.key())))
            # Add a the character to the serial_frame.
            self.serial_frame = self.serial_frame + str(chr(event.key()))

        else: # A lower case letter
            if (event.key() > 0x40) & (event.key() < 0x5B): # Only work on A - Z
                letter = event.key() + 0x20
                ui.textEditTx.insertPlainText(str(chr(letter)))
                # Add a the character to the serial_frame.
                self.serial_frame = self.serial_frame + str(chr(letter))
            else: # Some other non alpha character
                letter = event.key()
                ui.textEditTx.insertPlainText(str(chr(letter)))
                # Add a the character to the serial_frame.
                self.serial_frame = self.serial_frame + str(chr(letter))

        # We process all the keypresses....
        event.accept()
    #-------------------------------------------------------------------------#

    def getSerialPort(self):
        return self.com_port_opened

    #-------------------------------------------------------------------------#

    def sendData(self, dat):
        print('In sendData...')


###############################################################################

    def radioLegoApp(self, serial_port):
        while True:
            # Yield control back to the main application loop to process its stuff.
            QtGui.QApplication.processEvents()

            if serial_port._isOpen:
                # Set the class variable.
                com.com_port_opened = serial_port

                # How many bytes are in the receive queue?
                num_bytes = serial_port.inWaiting()
                if num_bytes > 0:
                    # Go check to see if we've received characters.
                    self.readComPort(serial_port, num_bytes)
###############################################################################

if __name__ == '__main__':
    # More or less a test to call a function to display the mainwindow GUI...
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)

    # Show the window
    mainwindow.show_mainwindow(app, MainWindow)

    # Use PySerial to setup the COM ports and the GUI.
    serial_port = serial.Serial()
    com = Com_Port('printing: com = commander.Com_Port')
    com.printme()
    com.findComPorts(ui, serial_port)

    # Work out the command stuff...
    import serialcommand
    cmd = serialcommand.Command(ui, com)
    cmd.populateCmdBox(ui)

    # A call to the application code is in the 'openComPort' method - that's the only time we have valid
    # COM port data...

    # Start the application loop...
    sys.exit(app.exec_())






