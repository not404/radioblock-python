# Copyright (c) 2011 - 2013, SimpleMesh AUTHORS
# Eric Gnoske,
# Colin O'Flynn,
# Blake Leverett,
# Rob Fries,
# Clara Ferrando,
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

from threading import Thread, Timer
import serial
import platform
import scanlinux
import scan
from support import *

DEBUG = 0

class comHandler (Thread):
    # Com port related defines
    PARITY_NAMES = {
        'none' :serial.PARITY_NONE,
        'even' :serial.PARITY_EVEN,
        'odd'  :serial.PARITY_ODD,
        'mark' :serial.PARITY_MARK,
        'space':serial.PARITY_SPACE,
    }

    def __init__(self,ctrlQueue,respQueue):

        # Init serial object and find available com ports
        self.serial_port = serial.Serial()
        self.ports = self.findComPorts(self.serial_port)

        # set queue
        #  objects
        self.ctrlQ = ctrlQueue
        self.respQ = respQueue

        #set RX parser objects
        [self.START,self.LENGTH,self.CODE,self.PAYLOAD,self.CRC_LO]= [0,1,2,3,4]
        self.state = self.START
        self.frame = []
        self.length = 0
        self.cmdid = 0
        self.crc = [0x00,0x00]

        self.respQ.put({'ports': self.ports})
        self.go = True

        self.dict = {'open':self.openComPort,
                     'close':self.closeComPort,
                     'quit':self.quit,
                     'send':self.txCommand
                     }

        self._baudrate = None
        self._bytesize = None
        self._parity   = None
        self._stopbits = None
        self.timeout = None
        Thread.__init__(self)

    def run (self):
        while self.go:
            # -------------------------------------------
            # Check TX queue and send commands
            # -------------------------------------------
            if not(self.ctrlQ.empty()):
                cmd = self.ctrlQ.get()
                fname = cmd[0]
                argvect = cmd[1]
                self.dict[fname](*argvect)
            # -------------------------------------------
            # Check RX data and process it
            # -------------------------------------------
            elif self.serial_port.isOpen():
                 rxbyte = self.serial_port.read()
                 if len(rxbyte):
                     self.parseRxData (rxbyte)


    def findComPorts(self, serial_port):
        # This function just prints them to the terminal/console.
        if platform.system() == 'Windows':
            ports = []
            port_index = 0
            win_ports = scan.scan()
            # For Windows, we need to get just the name not the tuple...
            for each_tuple in win_ports:
                ports.append(each_tuple[1])

        elif platform.system() == 'Linux':
            ports = scanlinux.scan()
        else: # We're a Mac
            ports = scanlinux.scan()
        #print ports
        return ports

    def setComDefaults(self):
        self._bytesize = 8
        self._parity = 'N'
        self._stopbits = 1
        self._baudrate = 115200

    def openComPort(self, comport, baudrate = 115200, databits=8, parity='N',stopbits = 1):
        if self.serial_port.isOpen():
            return

        self.setComDefaults()

        if databits in self.serial_port.BYTESIZES:
            self._bytesize = databits

        if parity in self.PARITY_NAMES.keys():
            self._parity = parity

        if stopbits in self.serial_port.STOPBITS:
            self._stopbits = stopbits

        if baudrate in self.serial_port.BAUDRATES:
            self._baudrate = baudrate

        self.serial_port = serial.Serial(comport, self._baudrate, self._bytesize,  self._parity, self._stopbits, \
                                         timeout=5)

        if self.serial_port.isOpen():
            print 'port open'
        else:
            print "\tCOM port open operation failed",
        return self.serial_port

    def closeComPort(self):
        if self.serial_port.isOpen():
            self.serial_port.close()

    def reconfigureCom (baudrate = 115200, databits=8, parity='N',stopbits = 1):
        self.setBaudrate(baudrate)
        self.setByteSize(databits)
        self.setParity(parity)
        self.setStopbits(stopbits)

    def buildCommand (self,name,pars):
        frame = []
        if name in TX_SB_COMMANDS.keys():
            frame = list(TX_SB_COMMANDS[name])
            frame = appendCRC(frame)
        elif name in TX_1PAR_COMMANDS.keys():
            if DEBUG:
                print "TX_1PAR_COMMANDS case", name
            fname = getattr(self,name)
            frame = fname(pars)
        elif name in TX_MUL_PAR_COMMANDS.keys():
            if DEBUG:
                print "TX_MUL_PAR_COMMANDS case", name
            fname = getattr(self,name)
            frame = fname(pars)
        return frame


    def txCommand (self, frame):
        for el in frame:
            self.serial_port.write(chr(el))

    def sendFrame (self,frame):
        self.timeout = Timer(2.0, self.ackTimeout)
        self.timeout.start()
        if DEBUG:
            print "Timeout launched"
        self.txCommand(frame)

    def sendCommand (self,name,pars):
        frame = self.buildCommand(name,pars)

        self.timeout = Timer(5.0, self.ackTimeout)
        self.timeout.start()
        if DEBUG:
            print "Timeout launched"
        self.txCommand(frame)

    def ackTimeout (self):
        print "Timeout occurred"
        self.respQ.put({"rxframedesc":"Timeout. No response received from module."})

    def settings_request (self, par):
        frame = []
        if par in settingsdict.keys():
            frame = list(TX_1PAR_COMMANDS["settings_request"])
            frame.append(settingsdict[par])
            frame = appendCRC(frame)
        else:
            raise Exception('invalid argument')
        return frame

    def set_channel_request(self, par):
        frame = []
        channelpar = int(par)
        if channelpar > 10 and channelpar < 26:
            frame = list(TX_1PAR_COMMANDS["set_channel_request"])
            frame.append(channelpar)
            frame = appendCRC(frame)
        else:
            raise Exception('invalid argument')
        return frame

    def set_receiver_state_request(self, par):
        frame = list(TX_1PAR_COMMANDS["set_receiver_state_request"])
        if par.lower() == 'on':
            frame.append(1)
        elif par.lower() == 'off':
            frame.append(0)
        else:
            raise Exception('invalid argument')
        frame = appendCRC(frame)
        return frame

    def set_transmit_power_request (self,power):
        frame = list(TX_1PAR_COMMANDS["set_transmit_power_request"])
        powerpar = int(power)
        if powerpar >= 0 and powerpar < 16:
            frame.append(powerpar)
        else:
            raise Exception('invalid argument')
        frame = appendCRC(frame)
        return frame

    def set_ack_state_request (self,state):
        frame = list(TX_1PAR_COMMANDS["set_ack_state_request"])
        if state.lower().startswith('ena'):
            frame.append(1)
        elif state.lower().startswith('dis'):
            frame.append(0)
        else:
            raise Exception('invalid argument')
        frame = appendCRC(frame)
        return frame

    def  set_led_state_request(self,state):
        frame = list(TX_1PAR_COMMANDS["set_led_state_request"])
        if state.lower() == 'off':
            frame.append(0)
        elif state.lower() == 'on':
            frame.append(1)
        elif state.lower() == 'toggle':
            frame.append(2)
        else:
            raise Exception('invalid argument')
        frame = appendCRC(frame)
        return frame

    def  set_address_request(self,address):
        frame = list(TX_1PAR_COMMANDS["set_address_request"])
        if address.startswith('0x'):
            addresspar = int(address[2:],16)
        else:
            addresspar = int(address)

        add_hi = (addresspar & 0xFF00) >> 8
        add_lo = addresspar & 0x00FF
        frame.append(add_lo)
        frame.append(add_hi)

        frame = appendCRC(frame)
        return frame

    def set_panid_request (self,address):
        frame = list(TX_1PAR_COMMANDS["set_panid_request"])
        if address.startswith('0x'):
            addresspar = int(address[2:],16)
        else:
            addresspar = int(address)

        add_hi = (addresspar & 0xFF00) >> 8
        add_lo = addresspar & 0x00FF

        frame.append(add_lo)
        frame.append(add_hi)
        frame = appendCRC(frame)
        return frame

    def sleep_request (self,timems):
        frame = list(TX_1PAR_COMMANDS["sleep_request"])
        if timems.startswith('0x'):
            timepar = int(timems[2:],16)
        else:
            timepar = int(timems)

        time_3 = int((timepar & 0xFF000000) >> 24)
        time_2 = int((timepar & 0x00FF0000) >> 16)
        time_1 = int((timepar & 0x0000FF00) >> 8)
        time_0 = int(timepar & 0x00FF)
        frame.append(time_0)
        frame.append(time_1)
        frame.append(time_2)
        frame.append(time_3)

        frame = appendCRC(frame)
        return frame

    def set_security_key_request (self,seckey):
        frame = list(TX_1PAR_COMMANDS["set_security_key_request"])
        seckey = seckey.replace(' ','')
        if len(seckey)== SEC_KEY_LEN:
            for i in range(0,SEC_KEY_LEN/2):
                byte = int(seckey[2*i:(2*i)+2], 16)
                frame.append(byte)

        frame = appendCRC(frame)
        return frame

    def set_uart_mode_request (self,uartpars):
        frame = []
        [databits,parity,stopbits, baudrate] = uartpars
        if int(databits) in range(5,9) and \
            parity in paritydict.keys() and \
            int(stopbits) in range(1,3) and \
            int(baudrate) in baudratedict.keys():
            frame = list(TX_MUL_PAR_COMMANDS["set_uart_mode_request"])
            frame.append(int(databits) - 5)
            frame.append(paritydict[parity])
            frame.append(int(stopbits) - 1)
            frame.append(baudratedict[int(baudrate)])
            frame = appendCRC(frame)
            return frame
        return frame

    def send_data_request (self,datapars):
        frame = []
        print "send_data_request",datapars
        [destination,options,handle, payload] = datapars
        if destination.startswith('0x'):
            destinationpar = int(destination[2:],16)
        else:
            destinationpar = int(destination)

        payloadLenValid = False
        if (payload.startswith("0x") and len(payload)<=(PAYLOAD_MAX_LEN + 2) and len(payload) % 2 == 0):
            payloadLenValid = True

        if not(payload.startswith("0x")) and len(payload)<=PAYLOAD_MAX_LEN/2:
            payloadLenValid = True

        print "payloadLenValid", payloadLenValid
        if options in optionsdict.keys() and payloadLenValid:

            frame = list(TX_MUL_PAR_COMMANDS["send_data_request"])
            dest_hi = (destinationpar & 0xff00) >> 8
            dest_lo = (destinationpar & 0x00ff)

            frame.append(dest_lo)
            frame.append(dest_hi)

            frame.append(optionsdict[options])
            frame.append(int(handle))

            #check if payload is a hex string or ascii string
            #HEX STRING CASE
            if payload.startswith('0x'):
                print "HEX STRING"
                payload = payload[2:]
                for i in range(0,len(payload)/2):
                    byte = int(payload[2*i:(2*i)+2], 16)
                    frame.append(byte)
                    frame[LENGTH_INDEX] = 5 + len(payload)/2

            #ASCII STRING
            else:
                print "ASCII STRING"
                print payload
                for i in range(0,len(payload)):
                    frame.append(ord(payload[i]))
                frame[LENGTH_INDEX] = 5 + len(payload)
            frame = appendCRC(frame)
            print frame
            return frame
        return frame


    def parseRxData (self,rxbyte):
        if self.state == self.START:
            if rxbyte == '\xab':
                self.state += 1
                self.frame = [0xab]
            return

        elif self.state == self.LENGTH:
            self.length = int(ord(rxbyte))
            if self.length > 0:
                self.frame.append(ord(rxbyte))
                self.state += 1
            else:
                self.state = self.START
                print "Invalid frame"
            return

        elif self.state == self.CODE:
            self.cmdid = ord(rxbyte)
            if self.cmdid in RX_TABLE.keys():
                self.state += 1
                self.length -= 1
                self.frame.append(ord(rxbyte))
            else:
                self.state = self.START
                print "Invalid frame"
            return

        elif self.state == self.PAYLOAD:
            if self.length > 0:
                self.frame.append(ord(rxbyte))
                self.length -= 1
            else:
                #get CRC High here
                self.crc[0]= ord(rxbyte)
                self.state += 1
            return

        elif self.state == self.CRC_LO :
            self.crc[1]= ord(rxbyte)

            self.state = self.START

            if checkFrame(self.frame, self.crc) == 1:
                #print "Frame decoded correctly!"
                self.processFrame(self.frame + self.crc)

            else:
                print "Invalid frame"
            return

    def processFrame (self, msg):
        print self.getFrameDescription(msg)
        #self.respQ.put({"rxframe":msg})
        #self.respQ.put({"rxframedesc":self.getFrameDescription(msg)})
        print msg


    def getFrameDescription (self,frame):
        '''This function parses the received frame and returns user friendly information on received frame'''
        code = frame[CODE_INDEX]

        if DEBUG:
            print "Command Code:", code

        #call description function
        if code == 0x00:   #is this an Ack?
            self.timeout.cancel()

        outstr = desc_functions[code](frame)
        return outstr

    def quit(self):
        if self.serial_port.isOpen():
            self.serial_port.close()

        self.go = False

