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

import datetime

DEBUG = 0

TX_START_BYTE = 0xAB
# Defines of indexes for frame buffer according to protocol
START_INDEX = 0
LENGTH_INDEX = 1
CODE_INDEX = 2
PAYLOAD_INDEX = 3
STATUS = 3
HANDLE = 4
PANID = ADDRESS = CHANNEL = STATE = TXPOWER = 3
PANID_LEN = ADDRESS_LEN = 2
SEC_KEY_LEN = 32
PAYLOAD_MAX_LEN = 118*2
OPEN = 1
CLOSED = 0

statedict = {1: "ON",
            0: "OFF"}

enadict =    {0: "DISABLED",
             1: "ENABLED"}

settingsdict = {'save'   : 0x10,
                'restore': 0x15}

paritydict = {"none"    : 0,
              "odd"     : 1,
              "even"    : 2,
              "force_1" : 3,
              "force_0" : 4,
             }
paritydict2 ={0:'N',
              1:'E', 
              2:'O', 
              3:'M', 
              4:'S'
              }


baudratedict = { 0              :  0x00,
                 50             :  0x01,
                 75             :  0x02,
                 110            :  0x03,
                 150            :  0x04,
                 300            :  0x05,
                 1200           :  0x06,
                 2400           :  0x07,
                 4800           :  0x08,
                 9600           :  0x09,
                 19200          :  0x0a,
                 38400          :  0x0b,
                 57600          :  0x0c,
                 115200         :  0x0d,
                 230400         :  0x0e,
                 460800         :  0x0f,
                 2000           :  0x10,
                 4000           :  0x11,
                 8000           :  0x12,
                 10000          :  0x13,
                 20000          :  0x14,
                 30000          :  0x15,
                 40000          :  0x16,
                 50000          :  0x17,
                 60000          :  0x18,
                 70000          :  0x19,
                 80000          :  0x1a,
                 90000          :  0x1b,
                 100000         :  0x1c,
                 200000         :  0x1d,
                 300000         :  0x1e,
                 400000         :  0x1f,
                }

optionsdict = { 'none'      : 0,
                'ack'       : 1,
                'security'  : 2}

RX_STRING = "Rx frame: "


TX_SB_COMMANDS={
        	 'test_request'              : (TX_START_BYTE , 0x01, 0x01),
        	 'reset_request'             : (TX_START_BYTE , 0x01, 0x03),
        	 'get_address_request'       : (TX_START_BYTE , 0x01, 0x24),
             'get_panid_request'         : (TX_START_BYTE , 0x01, 0x27),         
             'get_channel_request'       : (TX_START_BYTE , 0x01, 0x2A),       
             'get_receiver_state_request': (TX_START_BYTE , 0x01, 0x2D),
             'get_transmit_power_request': (TX_START_BYTE , 0x01, 0x30),
             'get_ack_state_request'     : (TX_START_BYTE , 0x01, 0x36)
        	 }
	 
	
TX_1PAR_COMMANDS={
             'settings_request'          :  (TX_START_BYTE , 0x02, 0x04),
             'set_channel_request'       :  (TX_START_BYTE , 0x02, 0x29),
             'set_receiver_state_request':  (TX_START_BYTE , 0x02, 0x2C),
             'set_transmit_power_request':  (TX_START_BYTE , 0x02, 0x2F),         
             'set_ack_state_request'     :  (TX_START_BYTE , 0x02, 0x35),       
             'set_led_state_request'     :  (TX_START_BYTE , 0x02, 0x80),

             'set_address_request'       :  (TX_START_BYTE , 0x03, 0x23),
             'set_panid_request'         :  (TX_START_BYTE , 0x03, 0x26),

             'sleep_request'             :  (TX_START_BYTE , 0x05, 0x06),
             'set_security_key_request'  :  (TX_START_BYTE , 0x11, 0x32),
             }

TX_MUL_PAR_COMMANDS={
             'set_uart_mode_request'      :  (TX_START_BYTE , 0x05, 0x05),
             'send_data_request'          :  (TX_START_BYTE , 0x00, 0x20),
            }
	

RX_TABLE={   0x00:'ACK'                         ,
             0x02:'TEST_RESPONSE'               ,
             0x07:'WAKEUP_INDICATION'           ,
             0x21:'DATA_CONFIRMATION'           ,
             0x22:'DATA_INDICATION'             ,
             0x25:'GET_ADDRESS_RESPONSE'        ,
             0x28:'GET_PANID_RESPONSE'          ,
             0x2B:'GET_CHANNEL_RESPONSE'        ,
             0x2E:'GET_RECEIVER_STATE_RESPONSE' ,
             0x31:'GET_TRANSMIT_POWER_RESPONSE' ,
             0x37:'SET_ACK_STATE_RESPONSE'     
             }


ACK_CODES={  0x00: 'Success',
             0x01: 'Unknown error',
             0x02: 'Out Of Memory',
             0x11: 'No Acknowledgment Was Received',
             0x40: 'Channel Access Failure',
             0x41: 'No Physical Acknowledgment Was Received',
             0x80: 'Invalid Command Size',
             0x81: 'Invalid CRC',
             0x82: 'Timeout',
             0x83: 'Unknown Command',
             0x84: 'Malformed Command',
             0x85: 'Internal Flash Error',
             0x86: 'Invalid Data Request payload size'
             }


DATA_CONFIRMATION_CODES = [0x00,0x01,0x02,0x11,0x40,0x41]                     


TX_LEVELS = {0x00:'+3.0 dBm',
             0x01:'+2.8 dBm',
             0x02:'+2.3 dBm',
             0x03:'+1.8 dBm',
             0x04:'+1.3 dBm',
             0x05:'+0.7 dBm',
             0x06:'0 dBm',
             0x07:'-1.0 dBm',
             0x08:'-2.0 dBm',
             0x09:'-3.0 dBm',
             0x0a:'-4.0 dBm',
             0x0b:'-5.0 dBm',
             0x0c:'-7.0 dBm',
             0x0d:'-9.0 dBm',
             0x0e:'-12.0 dBm',
             0x0f:'-17.0 dBm'
             }


def checkCRC( buf):
      ''' Try this for calculating the CRC for the serial interface.
      buf is a list of integers!! '''
      crc = 0x1234
      for i in range(len(buf)):
            data = buf[i]
            data ^= crc & 0xff
            data ^= (data << 4) & 0xff
            crc = (((data << 8) & 0xffff) | ((crc >> 8) & 0xff)) ^ ((data >> 4) & 0xff) ^ ((data << 3) & 0xffff)
      return crc


def appendCRC( buf):
      ''' This function takes a list of 1-byte integers and appends 2 more elements to the list corresponding 
      to the 2-byte CRC. Initial value of CRC is 0x1234. The CRC is applied from the element 2 of the list on'''
      crc = 0x1234
      for i in range(2,len(buf)):
            data = buf[i]
            data ^= crc & 0xff
            data ^= (data << 4) & 0xff
            crc = (((data << 8) & 0xffff) | ((crc >> 8) & 0xff)) ^ ((data >> 4) & 0xff) ^ ((data << 3) & 0xffff)

      crc_hi = (crc & 0xFF00) >> 8
      crc_lo = (crc & 0x00FF)

      bufcrc= buf
      # Hi and Lo are swapped ? 
      bufcrc.append(crc_lo)
      bufcrc.append(crc_hi)
      return bufcrc


def getCRC( buf):
      ''' This function takes a list of 1-byte integers and appends 2 more elements to the list corresponding 
      to the 2-byte CRC. Initial value of CRC is 0x1234. The CRC is applied from the element 2 of the list on'''
      crc = 0x1234
      for i in range(2,len(buf)):
            data = buf[i]
            data ^= crc & 0xff
            data ^= (data << 4) & 0xff
            crc = (((data << 8) & 0xffff) | ((crc >> 8) & 0xff)) ^ ((data >> 4) & 0xff) ^ ((data << 3) & 0xffff)

      crc_hi = (crc & 0xFF00) >> 8
      crc_lo = (crc & 0x00FF)
      return ([crc_lo,crc_hi])


def checkFrame(frame, crc):
    '''This function checks if the received CRC is correct. 
    frame is a list of integer and crc is a 2 element list '''
    framecrc = getCRC(frame)
    if DEBUG:
        print getHexString (framecrc)
    if framecrc == crc:
        return 1
    return 0


def getHexString (buffer):
    '''This function takes as input a list of integers (0..255) and returns an array of text in hexadecimal 
    for printing'''
    out = []
    for el in buffer:
        hexbyte = hex(el)[2:].upper()
        if len(hexbyte)== 1: hexbyte = '0' + hexbyte
        out.append(hexbyte)

    return ' '.join(out)

def getTimeStamp ():
    return ("[" + datetime.datetime.now().strftime("%H:%M:%S.%f")[:-3] + "] ")

def ack(frame):
    ackresult = frame[PAYLOAD_INDEX]
    hexframe = " ( " + getHexString(frame) + " )"
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + ' - ' + ACK_CODES[ackresult] + hexframe
    return outstr


def test_response(frame):               
    hexframe = " ( " + getHexString(frame) + " )"
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]]  + hexframe
    return outstr


def wakeup_indication(frame):           
    hexframe = " ( " + getHexString(frame) + " )"
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]]  + hexframe
    return outstr


def data_confirmation(frame):   
    status = frame[STATUS]
    handle = frame[HANDLE]
    ackresult = frame[PAYLOAD_INDEX]

    if status in DATA_CONFIRMATION_CODES:
        hexframe = " ( " + getHexString(frame) + " )"
        handlestring = " - HANDLE: " + hex(handle)
        outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + ' - ' + ACK_CODES[ackresult] + handlestring + hexframe
    else:
        outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + ' - Invalid status code '
    return outstr


def data_indication(frame):             
    address = frame[ADDRESS:ADDRESS + ADDRESS_LEN]
    address.reverse()
    payload = "\nPAYLOAD:" + getHexString(frame[8:-2])
    addressstr = " - SRC ADDRESS: " + getHexString(address)
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + addressstr +  payload
    return outstr


def get_address_response(frame):        
    address = frame[ADDRESS:ADDRESS + ADDRESS_LEN]
    address.reverse()
    hexframe = " ( " + getHexString(frame) + " )"
    addressstr = " - ADDRESS: " + getHexString(address)
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + addressstr +  hexframe
    return outstr


def get_panid_response(frame):          
    address = frame[ADDRESS:ADDRESS + ADDRESS_LEN]
    address.reverse()
    hexframe = " ( " + getHexString(frame) + " )"
    addressstr = " - PANID: " + getHexString(address)
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + addressstr + hexframe
    return outstr


def get_channel_response(frame):        
    address = frame[CHANNEL]
    hexframe = " ( " + getHexString(frame) + " )"
    addressstr = " - CHANNEL: " + str(address)
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + addressstr + hexframe
    return outstr


def get_receiver_state_response(frame): 
    state = statedict[ frame[STATE] ]
    hexframe = " ( " + getHexString(frame) + " )"
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + " - STATE: " + state + hexframe
    return outstr


def get_transmit_power_response(frame): 
    txpower = int(frame[TXPOWER])
    hexframe = " ( " + getHexString(frame) + " )"
    if txpower in TX_LEVELS.keys():
        outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + " - TX LEVEL: " + TX_LEVELS[txpower] + hexframe
    else:
        outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + " - TX LEVEL: invalid value"  + hexframe
    return outstr

def find_key(dic, val):
    """return the key of dictionary dic given the value"""
    return [k for k, v in dic.iteritems() if v == val][0]

def set_ack_state_response(frame):      
    state = enadict[ frame[STATE] ]
    hexframe = " ( " + getHexString(frame) + " )"
    outstr = RX_STRING + RX_TABLE[frame[CODE_INDEX]] + " - STATE: " + state + hexframe
    return outstr

def getIntValue (par):
    if par.startswith('0x'):
        try:
            out = int(par,16)
        except:
            return -1
    else:
        try:
            out=int(par)
        except:
            return -1
    return out

def isHexString (instring):
    if not(instring.startswith("0x")):
        return False
    valid = True
    auxstring = instring.lower()
    for el in auxstring[2:]:
        if not (el in "0123456789abcdef"):
            valid = False
    return valid


desc_functions = {0x00:ack                          ,
                  0x02:test_response                ,
                  0x07:wakeup_indication            ,
                  0x21:data_confirmation            ,
                  0x22:data_indication              ,
                  0x25:get_address_response         ,
                  0x28:get_panid_response           ,
                  0x2B:get_channel_response         ,
                  0x2E:get_receiver_state_response  ,
                  0x31:get_transmit_power_response  ,
                  0x37:set_ack_state_response      
                  }
