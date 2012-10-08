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

# Notes for a Python newbie - Me... Eric...
# Interesting links!
# http://stackoverflow.com/questions/443967/how-to-create-python-bytes-object-from-long-hex-string
# http://docs.python.org/py3k/whatsnew/3.0.html#text-vs-data-instead-of-unicode-vs-8-bit
# http://code.activestate.com/recipes/510399-byte-to-hex-and-hex-to-byte-string-conversion/
#
# Interesting conversion info:
# http://python.about.com/od/python30/ss/30_strings.htm
#######################################################################################################################
# http://docs.python.org/py3k/library/stdtypes.html#numeric-types-int-float-complex

# While string objects are sequences of characters (represented by strings of length 1), bytes and bytearray objects
# are sequences of integers (between 0 and 255), representing the ASCII value of single bytes. That means that for a
# bytes or bytearray object b, b[0] will be an integer, while b[0:1] will be a bytes or bytearray object of length
# 1. The representation of bytes objects uses the literal format (b'...') since it is generally more useful than e.g.
# bytes([50, 19, 100]). You can always convert a bytes object into a list of integers using list(b).


#######################################################################################################################
#
# http://code.activestate.com/recipes/578025-decimal-number-to-bytes-and-string-to-bytes-conver/
#
# Note that in Python 3.2 (whether by design or a bug I'm not sure) unhexlify now won't accept a string,
# but only bytes. Pretty silly really, but it means you'd need to use b = unhexlify(bytes(myhexstr, 'utf-8'))
#


# Hey, this is a pyside application!
from PySide import QtCore, QtGui

# This is used in the signal/slot setup.
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

import commander

import sys
# The mainwindow GUI class is one directory level up.
sys.path.append('../')
path = sys.path # A debug ine to examine the path...

# With path set, we can import the module (file) containing the mainwindow class.
import mainwindow

import binascii
from string import hexdigits
import math

from hexmonster import d2b, t2b, d2hexstr, hexstr2d, b2d, hex2hexstr, hexstr2b, hexstr2hexstr

class Command(object):
    def __init__(self, ui, com):
        # Commands to be transmitted:
        self.cmd_tx_test_request                 = 0x01
        self.cmd_tx_reset_request                = 0x03
        self.cmd_tx_settings_request             = 0x04
        self.cmd_tx_set_uart_mode                = 0x05
        self.cmd_tx_sleep_request                = 0x06
        self.cmd_tx_data_request                 = 0x20
        self.cmd_tx_set_address_request          = 0x23
        self.cmd_tx_get_address_request          = 0x24
        self.cmd_tx_set_panid_request            = 0x26
        self.cmd_tx_get_panid_request            = 0x27
        self.cmd_tx_set_channel_request          = 0x29
        self.cmd_tx_get_channel_request          = 0x2a
        self.cmd_tx_set_receiver_state_request   = 0x2c
        self.cmd_tx_get_receiver_state_request   = 0x2d
        self.cmd_tx_set_transmit_power_request   = 0x2f
        self.cmd_tx_get_transmit_power_request   = 0x30
        self.cmd_tx_set_security_key_request     = 0x32
        self.cmd_tx_set_ack_state_request        = 0x35
        self.cmd_tx_get_ack_state_request        = 0x36
        self.cmd_tx_set_led_state_request        = 0x80

        # Commands to be received:
        self.cmd_rx_ack                          = 0x00
        self.cmd_rx_test_response                = 0x02
        self.cmd_rx_wakeup_indication            = 0x07
        self.cmd_rx_data_confirmation            = 0x21
        self.cmd_rx_data_indication              = 0x22
        self.cmd_rx_get_address_response         = 0x25
        self.cmd_rx_get_panid_response           = 0x28
        self.cmd_rx_get_channel_response         = 0x2b
        self.cmd_rx_get_receiver_state_response  = 0x2e
        self.cmd_rx_get_transmit_power_response  = 0x31
        self.cmd_rx_set_ack_state_response       = 0x37

        # The construction of this list is:
        # [0] = number of bytes in the command including command ID byte.
        # [1] = Command name
        # [2] = Command id numeric values
        self.cmd_tx = [
            [1, "cmd_tx_test_request", "0x01"],
            [1, "cmd_tx_reset_request", "0x03"],
            [2, "cmd_tx_settings_request", "0x04"],
            [5, "cmd_tx_set_uart_mode", "0x05"],
            [5, "cmd_tx_sleep_request", "0x06"],
            [5, "cmd_tx_data_request", "0x20"],
            [3, "cmd_tx_set_address_request", "0x23"],
            [1, "cmd_tx_get_address_request", "0x24"],
            [3, "cmd_tx_set_panid_request", "0x26"],
            [1, "cmd_tx_get_panid_request", "0x27"],
            [2, "cmd_tx_set_channel_request", "0x29"],
            [1, "cmd_tx_get_channel_request", "0x2A"],
            [2, "cmd_tx_set_receiver_state_request", "0x2C"],
            [1, "cmd_tx_get_receiver_state_request", "0x2D"],
            [2, "cmd_tx_set_transmit_power_request", "0x2F"],
            [1, "cmd_tx_get_transmit_power_request", "0x30"],
            [17, "cmd_tx_set_security_key_request", "0x32"],
            [2, "cmd_tx_set_ack_state_request", "0x35"],
            [1, "cmd_tx_get_ack_state_request", "0x36"],
            [2, "cmd_tx_set_led_state_request", "0x80"] ]

        self.cmd_rx = [
            [2, "cmd_rx_ack", 0x00],
            [1, "cmd_rx_test_response", 0x02],
            [1, "cmd_rx_wakeup_indication", 0x07],
            [3, "cmd_rx_data_confirmation", 0x21],
            [6, "cmd_rx_data_indication", 0x22],
            [3, "cmd_rx_get_address_response", 0x25],
            [3, "cmd_rx_get_panid_response", 0x28],
            [2, "cmd_rx_get_channel_response", 0x2b],
            [2, "cmd_rx_get_receiver_state_response", 0x2e],
            [2, "cmd_rx_get_transmit_power_response", 0x31],
            [2, "cmd_rx_set_ack_state_response", 0x37] ]

        # UART settings.
        self.dataBits = [ ['5', '0x00'], ['6', '0x01'], ['7', '0x02'], ['8', '0x03'] ]
        self.parity = [ ['None', '0x00'], ['Odd', '0x01'], ['Even', '0x02'], ['Force 1', '0x03'], ['Force 0', '0x04'] ]
        self.stopBits = [ ['1', '0x00'], ['2 (1.5 for 5 data bits', '0x01'] ]
        self.baud = [ ['Reserved (Auto)', '0x00'], ['50', '0x01'], ['75', '0x02'], ['110', '0x03'], ['150', '0x04'],
            ['300', '0x05'], ['1200', '0x06'], ['2400', '0x07'], ['4800', '0x08'], ['9600', '0x09'], ['19200', '0x0A'],
            ['38400', '0x0B'], ['57600', '0x0C'], ['115200', '0x0D'], ['230400', '0x0E'], ['460800', '0x0F'],
            ['2000', '0x10'], ['4000', '0x11'], ['8000', '0x12'], ['10000', '0x13'], ['20000', '0x14'],
            ['30000', '0x15'], ['40000', '0x16'], ['50000', '0x17'], ['60000', '0x18'], ['70000', '0x19'],
            ['80000', '0x1A'], ['90000', '0x1B'], ['100000', '0x1C'], ['200000', '0x1D'], ['300000', '0x1E'],
            ['400000', '0x1F'] ]

        # Data request options.
        self.options = [["None", '0x00'], ["Request ACK", '0x01'], ["Enable Security", '0x02']]

        # Give ourselves global access to this instance inside this class.
        self.local_ui = ui

        # A copy of the "com" instantiation.
        self.local_com = com

        # A class variable for the serial frame
        frame = ''

        # Data request "Handle"...
        self.dataHandle = 0

        # Setup the progress bar. It can be updated on every keystroke in the data request payload...
        # Remember an 802.15.4 frame can only be 128 bytes max, SimpleMesh uses a 9 byte MAC header
        # and the PHY tacks on a SOF (0xA7) automatically and a length byte...
        # So, the total paylaod available is 128 - 11 = 117 bytes.
        #self.payloadCount = 117
        self.payloadCount = 11
        ui.progressBar.setMaximum(128)
        ui.progressBar.setMinimum(0)
        ui.progressBar.setValue(11)

        # Set up some signals and slots...

        # The command constructor may have multiple entry points (signals). We index the main activity on the
        # comboBoxCmd selection.
        ui.comboBoxCmd.setCurrentIndex(-1)
        QtCore.QObject.connect(ui.comboBoxCmd, QtCore.SIGNAL("currentIndexChanged(int)"), self.processcomboBoxCmd)

        # If the command option changes, need to re-run it...
        self.local_ui.comboBoxCmdOption.setCurrentIndex(-1)
        QtCore.QObject.connect(ui.comboBoxCmdOption, QtCore.SIGNAL("activated(int)"), self.processcomboBoxCmdOption)

        # Handle three byte commands.
        QtCore.QObject.connect(ui.lineEditThisAddress, QtCore.SIGNAL("returnPressed()"), self.processThreeByteCmd)

        # Handle the sleep request.
        QtCore.QObject.connect(ui.lineEditSleep, QtCore.SIGNAL("returnPressed()"), self.processFiveByteCommands)

        # Handle the UART.
        QtCore.QObject.connect(ui.comboBoxDataBits, QtCore.SIGNAL("currentIndexChanged(int)"), self.processFiveByteCommands)
        QtCore.QObject.connect(ui.comboBoxParity, QtCore.SIGNAL("currentIndexChanged(int)"), self.processFiveByteCommands)
        QtCore.QObject.connect(ui.comboBoxStopBits, QtCore.SIGNAL("currentIndexChanged(int)"), self.processFiveByteCommands)
        QtCore.QObject.connect(ui.comboBoxBaudRate, QtCore.SIGNAL("currentIndexChanged(int)"), self.processFiveByteCommands)

        # Handle the user typing in a payload on a data request.
        QtCore.QObject.connect(ui.lineEditUserPayload, QtCore.SIGNAL("returnPressed()"), self.processFiveByteCommands)

        # Handle keystrokes for the progress bar.
        QtCore.QObject.connect(ui.lineEditUserPayload, QtCore.SIGNAL("textChanged(const QString&)"), self.processProgressBar)

        # Set up a signal/slot to enable clear button for data request frame construction.
        QtCore.QObject.connect(ui.pushButtonClear, QtCore.SIGNAL("clicked()"), self.clearDataRequest)

        # Set up a slot to fire off the frame when ready...
        QtCore.QObject.connect(ui.pushButtonTxFrame, QtCore.SIGNAL("clicked()"), self.sendData)

        print('command initied... serial_port = ')

    def populateCmdBox (self, ui):
        cmdName = ["cmd_tx_test_request", "cmd_tx_reset_request", "cmd_tx_settings_request",
                   "cmd_tx_set_uart_mode", "cmd_tx_sleep_request", "cmd_tx_data_request",
                   "cmd_tx_set_address_request", "cmd_tx_get_address_request",
                   "cmd_tx_set_panid_request", "cmd_tx_get_panid_request", "cmd_tx_set_channel_request",
                   "cmd_tx_get_channel_request", "cmd_tx_set_receiver_state_request",
                   "cmd_tx_get_receiver_state_request", "cmd_tx_set_transmit_power_request",
                   "cmd_tx_get_transmit_power_request", "cmd_tx_set_security_key_request",
                   "cmd_tx_set_ack_state_request", "cmd_tx_get_ack_state_request", "cmd_tx_set_led_state_request"]

        # Populate the combobox here.
        for each_cmd in cmdName:
            ui.comboBoxCmd.addItem(each_cmd)

    # This method is the heart of catching multi-byte commands processed.
    def processcomboBoxCmd(self, index):
        # Block signals from 2 byte commands.
        self.local_ui.comboBoxCmdOption.blockSignals(True)

        # If this is a single command ID byte, don't show any stacked widget pages other than 0.
        if self.cmd_tx[index][0] == 1:
            # Show the proper stacked widget...
            self.local_ui.stackedWidget.setCurrentIndex(0)
            # Set the length of the payload here. The payload is only the command id.
            self.local_ui.lineEditSizeByte.setText('0x01')
            # Set the command ID.
            self.local_ui.lineEditCmdId.setText(self.cmd_tx[index][2])
            # Don't let the user change it.
            self.local_ui.lineEditPayload.setReadOnly(True)
            # A single byte command will be comprised of 3 bytes:
            # 1. Start byte
            # 2. Size byte
            # 3. Command ID byte
            # Get all the bytes into a single entity.
            serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
                           self.local_ui.lineEditCmdId.text()
            # Get rid of the '0x' characters from the text string
            serial_frame = serial_frame.replace('0x', '')
            print('serial_frame = ', serial_frame)
            # Convert the string representation of hex bytes into real bytes to transmit.
            self.frame = bytearray.fromhex(serial_frame)
            print('frame: ', self.frame)
            # Display the 'semi-raw' byte string for the user to see...
            self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame)

            # Calculate the CRC. Need to turn the CRC into a list of integers
            tmp=[]
            tmp.append(hexstr2d(self.local_ui.lineEditCmdId.text()))
            crc = self.checkCRC(tmp)

            # Post the CRC for for the user and concatenate the CRC bytes.
            self.frame += self.postCRC(crc)

            # Update the window...
            QtGui.QApplication.processEvents()

        # Catch the 3, 4, 5 and more byte commands here first
        elif self.cmd_tx[index][0] == 3:
            # Turn on the correct stacked widget page...
            self.local_ui.stackedWidget.setCurrentIndex(2)
            # Figure out which command...
            if self.cmd_tx[index][1] == "cmd_tx_set_address_request":
                self.local_ui.label3Byte.setText('Set This Node\'s Address: ')
                # Set the command ID.
                self.local_ui.lineEditCmdId.setText(self.cmd_tx[index][2])
            elif self.cmd_tx[index][1] == "cmd_tx_set_panid_request":
                self.local_ui.label3Byte.setText('Set This Node\'s PAN ID: ')
                # Set the command ID.
                self.local_ui.lineEditCmdId.setText(self.cmd_tx[index][2])
            # Clear some possible leftover stuff...
            self.local_ui.lineEditFrameToSend.clear()
            # Set the length of the payload here. The payload is the command id + the two byte address in the payload.
            self.local_ui.lineEditSizeByte.setText('0x03')
            # Update the screen.
            QtGui.QApplication.processEvents()

        elif self.cmd_tx[index][0] == 5:
            # Figure out which command...
            if self.cmd_tx[index][1] == "cmd_tx_sleep_request":
                # Turn on the correct stacked widget page...
                self.local_ui.stackedWidget.setCurrentIndex(3)
                # Set the length of the payload here. The payload is the command id + the two byte address in the payload.
                self.local_ui.lineEditSizeByte.setText('0x05')

            elif self.cmd_tx[index][1] == "cmd_tx_set_uart_mode":
                # Turn on the correct stacked widget page...
                self.local_ui.stackedWidget.setCurrentIndex(4)
                # Set the length of the payload here. The payload is the command id + the two byte address in the payload.
                self.local_ui.lineEditSizeByte.setText('0x05')
                # Populate the combo boxes...
                for i in range(0, len(self.dataBits)):
                    self.local_ui.comboBoxDataBits.addItem(self.dataBits[i][0])
                for i in range(0, len(self.parity)):
                    self.local_ui.comboBoxParity.addItem(self.parity[i][0])
                for i in range(0, len(self.stopBits)):
                    self.local_ui.comboBoxStopBits.addItem(self.stopBits[i][0])
                for i in range(0, len(self.baud)):
                    self.local_ui.comboBoxBaudRate.addItem(self.baud[i][0])

            elif self.cmd_tx[index][1] == "cmd_tx_data_request":
                # Turn on the correct stacked widget page...
                self.local_ui.stackedWidget.setCurrentIndex(5)
                # We don't know how long the data frame will be....
                for i in range(0, len(self.options)):
                    self.local_ui.comboBoxOptions.addItem(self.options[i][0])
                # Display the handle.
                self.local_ui.lineEditHandle.setText(str(self.dataHandle))

            # Set the command ID.
            self.local_ui.lineEditCmdId.setText(self.cmd_tx[index][2])
            # Update the screen.
            QtGui.QApplication.processEvents()

        elif self.cmd_tx[index][0] == 2:
            # Override whatever index is sent in - I used two nearly identical methods (processcomboBoxCmdOption &
            # processcomboBoxCmd) because I couldn't figure out how to separate the signal slots and it was causing
            # infinite recursion...
            index = self.local_ui.comboBoxCmd.currentIndex()
            # Pop the Cmd Id text into the line edit control...
            self.local_ui.lineEditCmdId.setText(self.cmd_tx[index][2])
            # Update the screen.
            QtGui.QApplication.processEvents()
            # A variable to hold command option bytes...
            cmdOpt = ''
            # Clear some possible leftover stuff...
            self.local_ui.lineEditFrameToSend.clear()
            # Each command will have different options.
            # Clear the combo box first!
            self.local_ui.label_x.clear()
            self.local_ui.comboBoxCmdOption.clear()
            QtGui.QApplication.processEvents()
            # Turn on the correct stacked widget page...
            self.local_ui.stackedWidget.setCurrentIndex(1)
            # Set the length of the payload here. The payload is the command id + single byte payload.
            self.local_ui.lineEditSizeByte.setText('0x02')
            # Populate the 2 byte commands.
            for each_option in self.cmd_tx:
                if self.cmd_tx[0] == 2:
                    self.local_ui.comboBoxCmdOption.addItem(each_option)

            # Figure out which option next...
            if self.local_ui.comboBoxCmd.currentText() == "cmd_tx_settings_request":
                self.local_ui.label_x.setText('Settings:')
                cmdList = ['Save current settings', 'Restore default settings']
                self.local_ui.comboBoxCmdOption.addItems(cmdList)
                # Set default.
                cmdOpt = '0x10'

            elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_channel_request":
                self.local_ui.label_x.setText('Channels:')
                cmdList = ['11', '12', '13', '14', '15', '16', '17', '18', '19',
                           '20', '21', '22', '23', '24', '25']
                self.local_ui.comboBoxCmdOption.addItems(cmdList)
                # Set default.
                cmdOpt = ('0x0B')

            elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_receiver_state_request":
                self.local_ui.label_x.setText('Receiver State:')
                cmdList = ['Off', 'On']
                self.local_ui.comboBoxCmdOption.addItems(cmdList)
                # Set default to on1
                cmdOpt = ('0x01')
                self.local_ui.comboBoxCmdOption.setCurrentIndex(1)

            elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_transmit_power_request":
                self.local_ui.label_x.setText('TX Power:')
                cmdList = ['+3.0 dBm', '+2.8 dBm', '+1.8 dBm', '+1.3 dBm', '+0.7 dBm', '0 dBm',
                           '-1.0 dBm', '-2.0 dBm', '-3.0 dBm', '-4.0 dBm', '-5.0 dBm',
                           '-7.0 dBm', '-9.0 dBm', '-12.0 dBm', '-17.0 dBm']
                self.local_ui.comboBoxCmdOption.addItems(cmdList)
                # Set default.
                cmdOpt = ('0x00')

            elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_ack_state_request":
                self.local_ui.label_x.setText('ACK State:')
                cmdList = ['Disable', 'Enable']
                self.local_ui.comboBoxCmdOption.addItems(cmdList)
                # Set default.
                cmdOpt = ('0x00')
                self.local_ui.comboBoxCmdOption.setCurrentIndex(0)

            elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_led_state_request":
                self.local_ui.label_x.setText('LED State:')
                cmdList = ['Off', 'On', 'Toggle']
                self.local_ui.comboBoxCmdOption.addItems(cmdList)
                # Set default.
                cmdOpt = ('0x00')
                self.local_ui.comboBoxCmdOption.setCurrentIndex(0)

            else: # Nothing selected - just return...
                self.local_ui.comboBoxCmdOption.blockSignals(False)
                return

            # Don't let the user change it.
            self.local_ui.lineEditPayload.setReadOnly(True)

            # A single byte & single byte payload command will be comprised of 4 bytes:
            # 1. Start byte
            # 2. Size byte
            # 3. Command ID byte
            # 4. One payload byte
            # Get all the bytes into a single entity.
            print('cmdOpt = ', str(cmdOpt).zfill(2))
            serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
                           self.local_ui.lineEditCmdId.text() + cmdOpt #str(cmdOpt).zfill(2)
            # Get rid of the '0x' characters from the text string
            serial_frame = serial_frame.replace('0x', '')
            print('serial_frame = ', serial_frame)
            # Convert the string representation of hex bytes into real bytes to transmit.
            self.frame = bytearray.fromhex(serial_frame)
            print('frame: ', self.frame)
            # Display the 'semi-raw' byte string for the user to see...
            self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame)

            # Calculate the CRC. The format of the crc_list is converted to integers before sending to the
            # crc function.
            crc_list = []
            crc_list.append(hexstr2d(self.local_ui.lineEditCmdId.text()))
            crc_list.append(hexstr2d(cmdOpt))
            crc = self.checkCRC(crc_list)

            # Post the CRC for for the user and concatenate the CRC bytes.
            self.frame += self.postCRC(crc)
            # Update the window...
            QtGui.QApplication.processEvents()
            self.local_ui.comboBoxCmdOption.blockSignals(False)

    # Both 'processcomboBoxCmdOption' & 'processcomboBoxCmd' are used to formulate the commands with a single payload
    # byte. These commands are:
    # 1. Settings Request
    # 2. Set Channel Request
    # 3. Set Receiver State Request
    # 4. Set Transmit Power Request
    # 5. Set ACK State Request
    # 6. Set LED State Request
    def processcomboBoxCmdOption(self, index):
        self.local_ui.comboBoxCmd.blockSignals(True)
        # Override whatever index is sent in - I used two nearly identical methods (processcomboBoxCmdOption &
        # processcomboBoxCmd) because I couldn't figure out how to separate the signal slots and it was causing
        # infinite recursion...
        index = self.local_ui.comboBoxCmdOption.currentIndex()
        # A variable to hold command option bytes...
        cmdOpt = ''
        # Clear some possible leftover stuff...
        self.local_ui.lineEditFrameToSend.clear()
        # Each command will have different options.
        # Clear the combo box first!
        self.local_ui.label_x.clear()
        self.local_ui.comboBoxCmdOption.clear()
        QtGui.QApplication.processEvents()
        # Turn on the correct stacked widget page...
        self.local_ui.stackedWidget.setCurrentIndex(1)
        # Set the length of the payload here. The payload is the command id + single byte payload.
        self.local_ui.lineEditSizeByte.setText('0x02')
        # Refresh the screen.
        QtGui.QApplication.processEvents()
        # Figure out which option next...
        if self.local_ui.comboBoxCmd.currentText() == "cmd_tx_settings_request":
            self.local_ui.label_x.setText('Settings:')
            cmdList = ['Save current settings', 'Restore default settings']
            self.local_ui.comboBoxCmdOption.addItems(cmdList)
            # We need to turn the 'index' into a string representation of a hex number.
            if index == 0:
                cmdOpt = '0x10'
            elif index == 1:
                cmdOpt = '0x15'
            else:
                self.local_ui.comboBoxCmd.blockSignals(False)
                return
            self.local_ui.comboBoxCmdOption.setCurrentIndex(index)

        elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_channel_request":
            self.local_ui.label_x.setText('Channels:')
            cmdList = [ '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23','24', '25']
            channel = ['0x0B', '0x0C', '0x0D', '0x0E', '0x0F', '0x10', '0x11', '0x12', '0x13', '0x14', '0x15', '0x16',
                       '0z17', '0x18', '0x19']
            self.local_ui.comboBoxCmdOption.addItems(cmdList)
            # We need to turn the 'index' into a string representation of a hex number.
            cmdOpt = channel[index]
            self.local_ui.comboBoxCmdOption.setCurrentIndex(index)

        elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_receiver_state_request":
            self.local_ui.label_x.setText('Receiver State:')
            cmdList = ['Off', 'On']
            # We need to turn the 'index' into a string representation of a hex number.
            self.local_ui.comboBoxCmdOption.addItems(cmdList)
            cmdOpt = '0x' + str(index).zfill(2)
            self.local_ui.comboBoxCmdOption.setCurrentIndex(index)

        elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_transmit_power_request":
            self.local_ui.label_x.setText('TX Power:')
            cmdList = ['+3.0 dBm', '+2.8 dBm', '+2.3', '+1.8 dBm', '+1.3 dBm', '+0.7 dBm', '0 dBm', '-1.0 dBm',
                       '-2.0 dBm', '-3.0 dBm', '-4.0 dBm', '-5.0 dBm', '-7.0 dBm', '-9.0 dBm', '-12.0 dBm', '-17.0 dBm']
            db = ['0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '0x09', '0x0A', '0x0B',
                  '0x0C', '0x0D', '0x0E', '0x0F']
            # We need to turn the 'index' into a string representation of a hex number.
            cmdOpt = db[index]
            self.local_ui.comboBoxCmdOption.addItems(cmdList)
            self.local_ui.comboBoxCmdOption.setCurrentIndex(index)

        elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_ack_state_request":
            self.local_ui.label_x.setText('ACK State:')
            cmdList = ['Disable', 'Enable']
            # We need to turn the 'index' into a string representation of a hex number.
            self.local_ui.comboBoxCmdOption.addItems(cmdList)
            cmdOpt = '0x' + str(index).zfill(2)
            self.local_ui.comboBoxCmdOption.setCurrentIndex(index)

        elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_led_state_request":
            self.local_ui.label_x.setText('LED State:')
            cmdList = ['Off', 'On', 'Toggle']
            # We need to turn the 'index' into a string representation of a hex number.
            self.local_ui.comboBoxCmdOption.addItems(cmdList)
            cmdOpt = '0x' + str(index).zfill(2)
            self.local_ui.comboBoxCmdOption.setCurrentIndex(index)

        else: # Nothing selected - just return...
            self.local_ui.comboBoxCmd.blockSignals(False)
            return

        # Don't let the user change it.
        self.local_ui.lineEditPayload.setReadOnly(True)
        # A single byte & single byte payload command will be comprised of 4 bytes:
        # 1. Start byte
        # 2. Size byte
        # 3. Command ID byte
        # 4. One payload byte
        # Get all the bytes into a single entity.
        print('cmdOpt = ', str(cmdOpt).zfill(2))
        serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
                       self.local_ui.lineEditCmdId.text() + str(cmdOpt).zfill(2)
        # Get rid of the '0x' characters from the text string
        serial_frame = serial_frame.replace('0x', '')
        print('serial_frame = ', serial_frame)
        # Convert the string representation of hex bytes into real bytes to transmit.
        self.frame = bytearray.fromhex(serial_frame)
        print('frame: ', self.frame)
        # Display the 'semi-raw' byte string for the user to see...
        self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame)

        # Calculate the CRC.
        crc_list = []
        crc_list.append(hexstr2d(self.local_ui.lineEditCmdId.text()))
        crc_list.append(hexstr2d(cmdOpt))
        crc = self.checkCRC(crc_list)

        # Post the CRC for for the user and concatenate the CRC bytes.
        self.frame += self.postCRC(crc)
        # Update the window...
        QtGui.QApplication.processEvents()
        self.local_ui.comboBoxCmd.blockSignals(False)

    # This function will process these commands:
    # 1. Set Address Request.
    # 2. Set PANID request.
    def processThreeByteCmd(self):
        # Turn on the correct stacked widget page...
        self.local_ui.stackedWidget.setCurrentIndex(2)
        # Maybe unnecessary, but it helps in debug...
        # A temporary variable, use it to make a hex string of characters where each byte is preceded by '0x'.
        # Before adding the '0x' portion capitalize the hex alpha numbes (a - f).
        addr = self.str2hex(self.local_ui.lineEditThisAddress.text().upper())
        # Build the whole command string.
        serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
                       self.local_ui.lineEditCmdId.text() + addr
        # Get rid of the '0x' characters from the text string
        serial_frame = serial_frame.replace('0x', '')
        # This takes the hex string and gives back a hex byte string, something tha can actually be used by the
        # RadioLego.
        self.frame = bytearray.fromhex(serial_frame)
        # Display the 'semi-raw' byte string for the user to see...
        self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame)

        # Calculate the CRC. In this method the address are entered in the form '1234' or 'abcd' they are assumed
        # to be entered in 'hex' without the 0x or \x...
        crc_list = []                                                   # Clear this variable.
        crc_list.append(hexstr2d(self.local_ui.lineEditCmdId.text()))   # Pop in the CMD id
        crc_list.append(hexstr2d(addr[:4]))                             # The number is in the form 0xAB0x34, grab the 0xAB
        crc_list.append(hexstr2d(addr[4:]))                             # Now grab the 0x34
        crc = self.checkCRC(crc_list)                                   # Get the CRCs

        # Post the CRC for for the user and concatenate the CRC bytes.
        self.frame += self.postCRC(crc)
        # Update the window...
        QtGui.QApplication.processEvents()
        # DEBUG
        print('frame: ', self.frame)


    def processFiveByteCommands(self):
        self.local_ui.comboBoxCmd.blockSignals(True)
        # For CRC calculation
        crc_list = []

        if self.local_ui.comboBoxCmd.currentText() == "cmd_tx_sleep_request":
            # Turn on the correct stacked widget page...
            self.local_ui.stackedWidget.setCurrentIndex(3)
            # Set the length of the payload here. The payload is the command id + the two byte address in the payload.
            self.local_ui.lineEditSizeByte.setText('0x05')
            # If anything is in the sleep line edit box, clear it.
            #self.local_ui.lineEditSleep.clear()
            # Maybe unnecessary, but it helps in debug...
            # A temporary variable, use it to make a hex string of characters where each byte is preceeded by '0x'.
            milliseconds = self.local_ui.lineEditSleep.text()
            tmp = self.str2hex(self.local_ui.lineEditSleep.text().zfill(6))
            # Get the user input, transform it into hex and be done here.
            # Build the whole command string.
            serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
            self.local_ui.lineEditCmdId.text() + tmp
            # Get rid of the '0x' characters from the text string
            serial_frame = serial_frame.replace('0x', '')
            # This takes the hex string and gives back a hex byte string, something tha can acutally be used by the
            # RadioLego.
            self.frame = bytearray.fromhex(serial_frame)
            # Display the 'semi-raw' byte string for the user to see...
            self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame)

            # Take care of some crc housekeeping.
            crc_list.append(hexstr2d(self.local_ui.lineEditCmdId.text()))
            # The number of milliseconds is a 32 bit integer (i.e. 4 bytes) using built in functions
            milliseconds = int(milliseconds).to_bytes(2, byteorder='big')
            # Now append the bytes as integers...
            for uint in list(milliseconds):
                crc_list.append(uint)
            # DEBUG
            print('frame: ', self.frame)

        elif self.local_ui.comboBoxCmd.currentText() == "cmd_tx_set_uart_mode":
            # Turn on the correct stacked widget page...c
            self.local_ui.stackedWidget.setCurrentIndex(4)
            # Set the length of the payload here. The payload is the command id + the two byte address in the payload.
            self.local_ui.lineEditSizeByte.setText('0x05')

            # The combo boxes are filled in in the initial call (signal slot connection) in the
            # processcomboBoxCmd method.

            # Build the whole command string.
            serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
                           self.local_ui.lineEditCmdId.text() +\
                           self.dataBits[self.local_ui.comboBoxDataBits.currentIndex()][1] +\
                           self.parity[self.local_ui.comboBoxParity.currentIndex()][1] +\
                           self.stopBits[self.local_ui.comboBoxStopBits.currentIndex()][1] +\
                           self.baud[self.local_ui.comboBoxBaudRate.currentIndex()][1]
            # Get rid of the '0x' characters from the text string
            serial_frame = serial_frame.replace('0x', '')
            # This takes the hex string and gives back a hex byte string, something tha can acutally be used by the
            # RadioLego.
            self.frame = bytearray.fromhex(serial_frame)
            # Display the 'semi-raw' byte string for the user to see...
            self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame)

            # Take care of some crc housekeeping.
            crc_list.append(hexstr2d(self.local_ui.lineEditCmdId.text()))
            # Change all the other hex strings to decimals...
            crc_list.append(hexstr2d(self.dataBits[self.local_ui.comboBoxDataBits.currentIndex()][1]))
            crc_list.append(hexstr2d(self.parity[self.local_ui.comboBoxParity.currentIndex()][1]))
            crc_list.append(hexstr2d(self.stopBits[self.local_ui.comboBoxStopBits.currentIndex()][1]))
            crc_list.append(hexstr2d(self.baud[self.local_ui.comboBoxBaudRate.currentIndex()][1]))

            # DEBUG
            print('frame: ', self.frame)


        elif self.local_ui.comboBoxCmd.currentText() ==  "cmd_tx_data_request":
            # Turn on the correct stacked widget page...
            self.local_ui.stackedWidget.setCurrentIndex(5)
            # We don't know how long the data frame will be....

            # Maybe unnecessary, but it helps in debug...
            # A temporary variable, use it to make a hex string of characters where each byte is preceeded by '0x'.
            dest_addr = self.local_ui.lineEditDestAddr.text()
            # Check for a valid address 0 to 65,535
            if int(dest_addr, 16) > 65535:
                self.local_ui.comboBoxCmd.blockSignals(False)
                return
            dest = self.str2hex(self.local_ui.lineEditDestAddr.text().zfill(4))
            # Use the Class handle.
            self.local_ui.lineEditHandle.setText(str(self.dataHandle))
            if self.dataHandle < 10:
                handle = self.str2hex(self.local_ui.lineEditHandle.text().zfill(2))
            elif self.dataHandle < 100:
                handle = self.str2hex(self.local_ui.lineEditHandle.text().zfill(1))
            else:
                handle = self.str2hex(self.local_ui.lineEditHandle.text())
            self.dataHandle += 1

            payload =  self.local_ui.lineEditUserPayload.text()
            # The payload is equal to the 127 minus the IEEE 802.15.4 MAC header, Since the MAC header is 9 bytes:
            # FCF
            # Sequence Number
            # Short Dest Address
            # Intra-PANID
            # Short Node Address
            if len(payload) > 118:
                self.local_ui.lineEditUserPayload.clear()
                self.local_ui.lineEditUserPayload.setText("Payload too long!")
                self.local_ui.comboBoxCmd.blockSignals(False)
                return
            # Figure out the options.
            opt = (self.options[self.local_ui.comboBoxOptions.currentIndex()][1])
            # Make sure the string is divisible by 2, left fill with a zero if necessary...
            payload_len = len(self.local_ui.lineEditUserPayload.text())
            if payload_len % 2 != 0:
                payload = self.str2hex(self.local_ui.lineEditUserPayload.text().zfill(payload_len + 1))
            else:
                payload = self.str2hex(self.local_ui.lineEditUserPayload.text())

            # If the payload is PURE ASCII, it can be converted with this:
            # string = binascii.b2a_hex(bytes(self.local_ui.lineEditUserPayload.text(), 'utf-8'))
            # If the payload is PURE HEX, it can be converted with this:
            # string = binascii.unhexlify(bytes(self.local_ui.lineEditUserPayload.text(), 'utf-8'))

            # LET'S PRESUME THE PAYLOAD IS ALL ASCII!!!!
            payload = self.local_ui.lineEditUserPayload.text()

            # Convert the ASCII payload to a bytearray.
            hex_payload = []
            for item in self.local_ui.lineEditUserPayload.text():
                 hex_payload.append(ord(item))

            # Get the length of the PAYLOAD. This could be made might tighter of course but I wanted to
            # see some of the internal steps in debug...
            self.local_ui.lineEditSizeByte.clear()
            int_length = len(payload)   # Get the actual size of the payload in an integer variable
            int_length += 5                 # Add in the 5 static bytes: CMD id, address, option, handle.
            s_len = chr(int_length)         # This puts, say an length of integer 10 into hex form \x0a
            h_len = binascii.b2a_hex(bytes(s_len))          # This converts the \x0a into b'0a'
            p = str(h_len)                                  # This turns the b'0a' into "b'0a'"
            s_len = len(str(int_length))                    # Get the length of the integer variable.

            if s_len % 2 != 0:
                length = self.str2hex(p.zfill(s_len + 1))
            else:
                length = self.str2hex(p)

            # Put the length in the GUI...
            self.local_ui.lineEditSizeByte.setText(length)
            # Build the whole command string. Don't add ascii payload here.
            serial_frame = self.local_ui.lineEditStartByte.text() + self.local_ui.lineEditSizeByte.text() +\
                           self.local_ui.lineEditCmdId.text() + dest + opt + handle
            # Get rid of the '0x' characters from the text string
            serial_frame = serial_frame.replace('0x', '')
            # Convert the string representation of hex bytes into real bytes to transmit.
            self.frame = binascii.unhexlify(bytes(serial_frame)) # Same
            # Now concatenate the payload bytes.
            for item in self.local_ui.lineEditUserPayload.text():
                self.frame += bytes(item)
            # Display the 'semi-raw' byte string for the user to see...
            self.local_ui.lineEditFrameToSend.setText('0x' + serial_frame + self.local_ui.lineEditUserPayload.text())

            # Take care of some crc housekeeping. CMD id + Dest addr + Options + Handle + Payload
            crc_list.append(hex2hexstr(self.local_ui.lineEditCmdId.text()))
            # Dest addr + Options + Handle + Payload (need to detect hex a - f values).
            if self.is_number(self.local_ui.lineEditDestAddr.text()):
                #dest_addr = int(dest_addr).to_bytes(2, byteorder='big')
                # Now append the bytes as integers...
                crc_list.append(hex2hexstr(dest[:4]))     # The address is in the form \x12\x34, grab the \x12
                crc_list.append(hex2hexstr(dest[4:]))     # Now grab the \x34
            else: # They must be hex values a - f... The address is in the form 'abcd', '123e'...
                crc_list.append(hexstr2b(dest_addr[:2].upper()))     # The address is in the form 'abcd', grab the ab
                crc_list.append(hexstr2b(dest_addr[2:].upper()))     # Now grab the cd

            # Options + Handle + Payload
            crc_list.append(hex2hexstr(opt))
            # Handle + Payload
            crc_list.append(hex2hexstr(handle))
            # Payload
            for i in self.local_ui.lineEditUserPayload.text():
                crc_list.append(i)

            # DEBUG
            print('frame: ', self.frame)

        # We handle crc calculation for the data request a little differently.
        if self.local_ui.comboBoxCmd.currentText() ==  "cmd_tx_data_request":
            crc = self.checkDataCRC(crc_list) # Calculate the CRC for the DATA REQUEST only
        else:
            crc = self.checkCRC(crc_list)

        # Post the CRC for for the user and concatenate the CRC bytes.
        self.frame += self.postCRC(crc)
        # Update the screen.
        QtGui.QApplication.processEvents()
        self.local_ui.comboBoxCmd.blockSignals(False)

    def postCRC(self, crc):
        # Post the CRC for for the user.        
        #tmp = bytes(chr(crc))
        msb = ((crc >> 8) & 0xFF)
        lsb = (crc & 0xFF)

        # Python3.x msb_str = "%2x"%msb
        # Python3.x lsb_str = "%2x"%lsb
        msb_str = hex(msb).upper()[2:]
        lsb_str = hex(lsb).upper()[2:]
        
        # The LPC1114 has the CRC unit16_t byte swapped, so let's fix that here.
        # Python3.x msblsb = str(msb) + str(lsb) # Un-swapped case.
        # msblsb =  lsb_str + msb_str # The LPC1114 needs the CRC byte swapped.

        # Python3.x msblsb = msblsb.replace('b\'\\x', '')
        # Python3.x msblsb = msblsb.replace('\'', '')
        # Python3.x msblsb = '0x' + msblsb
        msblsb = '0x' + msb_str + lsb_str
        self.local_ui.lineEditCRC.setText(msblsb)

        #Use this format as it's easier to change msb/lsb order around if required
        return bytearray([lsb, msb])

    def processProgressBar(self, s):
        self.payloadCount += 1
        # Calculate the percentage payload left.
        dbg = self.payloadCount/self.local_ui.progressBar.maximum()
        #dbg = (self.local_ui.progressBar.value() - self.local_ui.progressBar.minimum())/(self.local_ui.progressBar.maximum() - self.local_ui.progressBar.minimum())
        prog = round(100*dbg)
        self.local_ui.progressBar.setValue(prog)

        # Update the screen.
        QtGui.QApplication.processEvents()

    # Turn a string of "hexidecimal' characters into a real hex string.
    # ex: s = '12abcd'
    #     h = 0x120x340xab0xcd
    # Note that the string must be an even number of digits and proper hex characters 0 - 9, a - f or A - F.
    def str2hex(self, s):
        if len(s) % 2 != 0:
            return 0

        h = ''
        i = 0
        while i < len(s):
            h = h + '0x' + s[i:i+2]
            i += 2

        return h

    def getOpenComPort(self):
        # Set up the serial port.
        self.local_serial = self.local_com.getSerialPort()
        print('getOpenComPort has this COM port: ', self.local_serial)

        return self.local_serial

    def sendData(self):
        local_serial = self.getOpenComPort()

        # Flush any crap before sending!
        local_serial.flush()

        print self.frame
        for ch in self.frame:
            self.local_ui.textEditTx.insertPlainText(d2hexstr(ch))
            self.local_ui.textEditTx.insertPlainText(" ")
        self.local_ui.textEditTx.insertPlainText("\n")

        # This transmits the data in the serial frame!
        local_serial.write(self.frame)



    # When the clear pushbutton is pressed on the Data page of the stackedwidget, clear all
    # stuff out...
    def clearDataRequest(self):
        self.local_ui.lineEditDestAddr.clear()
        self.local_ui.lineEditHandle.clear()
        self.local_ui.lineEditUserPayload.clear()
        self.local_ui.lineEditPayload.clear()
        self.local_ui.comboBoxOptions.setCurrentIndex(0)
        self.local_ui.progressBar.setValue(11)

    # Try this for calculating the CRC for the serial interface.
    # buf is a list of integers!!
    def checkCRC(self, buf):
        crc = 0x1234
        for i in range(len(buf)):
            data = buf[i]
            data ^= crc & 0xff
            data ^= (data << 4) & 0xff
            crc = (((data << 8) & 0xffff) | ((crc >> 8) & 0xff)) ^ ((data >> 4) & 0xff) ^ ((data << 3) & 0xffff)

        return crc

    # Since the payload of the data request is a bunch of ASCII bytes we need to convert it differently.
    # buf is a list of bytes or a bytearray.
    def checkDataCRC(self, buf):
        crc = 0x1234
        for i in buf:
            data = ord(i)

            data ^= crc & 0xff
            data ^= (data << 4) & 0xff
            crc = (((data << 8) & 0xffff) | ((crc >> 8) & 0xff)) ^ ((data >> 4) & 0xff) ^ ((data << 3) & 0xffff)

        return crc

    # Sheesh, figure out if a number is a number...
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False
