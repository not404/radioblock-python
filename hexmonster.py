__author__ = 'egnoske'

## {{{ http://code.activestate.com/recipes/578025/ (r1)
# d2b.py
#
# Decimal to byte(s) and character/string to byte(s) converter.
# Any decimal number from 0 to 255 converted to b"\x??" format.
# Any standard ASCII string, something like "\x00Some String.\xFF" converted
# to b"\x00Some String.\xff". NOTE:- "FF" is displayed as "ff" on conversion
# but the end result is the same.
#
# NOTE:- The reverse, b"\x00Some String.\xff" converted to
# "\x00Some String.\xff", is easy and therefore not included in this function.
#
# What I needed......
# The function, sometext=chr(a+b), (where "a" could be for example 127 and
# "b" in this case is -127<=b<=128), capability is not easily possible with the
# b"string" byte(s) format so this function was devised.
#
# See here for an example of chr(a+b):-
# http://code.activestate.com/recipes/578013-amplitude-modulation-tremolo-was-an-audiosound-sni/?in=lang-python
#
# This new function uses NO import(s), nor any special programming style,
# but is written so that anyone can understand, (including kids), how it works.
# It does NOT need any special encoding or any other "Pythonic" requirements at all.
# It is not "elegant", as professionals may call it, but, it is functional.
#
# I have no idea at all as to the upper limit of ASCII string length it can
# handle, however it CAN handle a(n) "", (empty), string.
#
# ==========================================================================
#
# Python 3.1.3 (r313:86834, Nov 28 2010, 10:01:07)
# [GCC 4.4.5] on linux2
# Type "help", "copyright", "credits" or "license" for more information.
# >>> exec(open('/home/G0LCU/Desktop/Code/d2b.py').read())
# >>> a=78
# >>> type(a)
# <class 'int'>
# >>> b=d2b(a)
# >>> print(b)
# b'N'
# >>> type(b)
# <class 'bytes'>
# >>> text="\x00(C)2012, B.Walker, G0LCU.\xFF"
# >>> len(text)
# 27
# >>> type(text)
# <class 'str'>
# >>> newtext=t2b(text)
# >>> len(newtext)
# 27
# >>> print(newtext)
# b'\x00(C)2012, B.Walker, G0LCU.\xff'
# >>> type(newtext)
# <class 'bytes'>
#
# ============================================================================
#
# Copyright, (C)2012, B.Walker, G0LCU.
# Issued under GPL2 licence...
# Enjoy finding simple solutions to often very difficult problems.
#
# Requires Python Version 3.x.x only.
# Tested on Debian 6.0.0 using Python 3.1.3, and PCLinuxOS 2009 using Python 3.2.1.
# Also Tested on MS Windows Vista, 32 bit, using Python 3.0.1 and Python 3.2.2.

# Decimal number to byte(s) string converter.
def d2b(a,b=0):
    # "a" any decimal number between 0 to 255.
    # "b" is reserved, but for my usage is very useful, see above... ;o)
    # Don't allow any floating point numbers.
    a=int(a)
    b=int(b)
    decimal=a+b
    # Out of range checks forcing function to exit!
    if decimal<=-1 or decimal>=256:
        print("\nError in d2b(a,b=0) function, decimal integer out of range, (0 to 255)!\n")
        # FORCE a Python error to stop the function from proceeding; "FORCED_HALT" IS NOT DEFINED!
        print(FORCED_HALT)
    # Convert new decimal value 0 to 255 to b"\x??" value.
    if decimal==0: newbyte=b"\x00"
    if decimal==1: newbyte=b"\x01"
    if decimal==2: newbyte=b"\x02"
    if decimal==3: newbyte=b"\x03"
    if decimal==4: newbyte=b"\x04"
    if decimal==5: newbyte=b"\x05"
    if decimal==6: newbyte=b"\x06"
    if decimal==7: newbyte=b"\x07"
    if decimal==8: newbyte=b"\x08"
    if decimal==9: newbyte=b"\x09"
    if decimal==10: newbyte=b"\x0A"
    if decimal==11: newbyte=b"\x0B"
    if decimal==12: newbyte=b"\x0C"
    if decimal==13: newbyte=b"\x0D"
    if decimal==14: newbyte=b"\x0E"
    if decimal==15: newbyte=b"\x0F"
    if decimal==16: newbyte=b"\x10"
    if decimal==17: newbyte=b"\x11"
    if decimal==18: newbyte=b"\x12"
    if decimal==19: newbyte=b"\x13"
    if decimal==20: newbyte=b"\x14"
    if decimal==21: newbyte=b"\x15"
    if decimal==22: newbyte=b"\x16"
    if decimal==23: newbyte=b"\x17"
    if decimal==24: newbyte=b"\x18"
    if decimal==25: newbyte=b"\x19"
    if decimal==26: newbyte=b"\x1A"
    if decimal==27: newbyte=b"\x1B"
    if decimal==28: newbyte=b"\x1C"
    if decimal==29: newbyte=b"\x1D"
    if decimal==30: newbyte=b"\x1E"
    if decimal==31: newbyte=b"\x1F"
    if decimal==32: newbyte=b"\x20"
    if decimal==33: newbyte=b"\x21"
    if decimal==34: newbyte=b"\x22"
    if decimal==35: newbyte=b"\x23"
    if decimal==36: newbyte=b"\x24"
    if decimal==37: newbyte=b"\x25"
    if decimal==38: newbyte=b"\x26"
    if decimal==39: newbyte=b"\x27"
    if decimal==40: newbyte=b"\x28"
    if decimal==41: newbyte=b"\x29"
    if decimal==42: newbyte=b"\x2A"
    if decimal==43: newbyte=b"\x2B"
    if decimal==44: newbyte=b"\x2C"
    if decimal==45: newbyte=b"\x2D"
    if decimal==46: newbyte=b"\x2E"
    if decimal==47: newbyte=b"\x2F"
    if decimal==48: newbyte=b"\x30"
    if decimal==49: newbyte=b"\x31"
    if decimal==50: newbyte=b"\x32"
    if decimal==51: newbyte=b"\x33"
    if decimal==52: newbyte=b"\x34"
    if decimal==53: newbyte=b"\x35"
    if decimal==54: newbyte=b"\x36"
    if decimal==55: newbyte=b"\x37"
    if decimal==56: newbyte=b"\x38"
    if decimal==57: newbyte=b"\x39"
    if decimal==58: newbyte=b"\x3A"
    if decimal==59: newbyte=b"\x3B"
    if decimal==60: newbyte=b"\x3C"
    if decimal==61: newbyte=b"\x3D"
    if decimal==62: newbyte=b"\x3E"
    if decimal==63: newbyte=b"\x3F"
    if decimal==64: newbyte=b"\x40"
    if decimal==65: newbyte=b"\x41"
    if decimal==66: newbyte=b"\x42"
    if decimal==67: newbyte=b"\x43"
    if decimal==68: newbyte=b"\x44"
    if decimal==69: newbyte=b"\x45"
    if decimal==70: newbyte=b"\x46"
    if decimal==71: newbyte=b"\x47"
    if decimal==72: newbyte=b"\x48"
    if decimal==73: newbyte=b"\x49"
    if decimal==74: newbyte=b"\x4A"
    if decimal==75: newbyte=b"\x4B"
    if decimal==76: newbyte=b"\x4C"
    if decimal==77: newbyte=b"\x4D"
    if decimal==78: newbyte=b"\x4E"
    if decimal==79: newbyte=b"\x4F"
    if decimal==80: newbyte=b"\x50"
    if decimal==81: newbyte=b"\x51"
    if decimal==82: newbyte=b"\x52"
    if decimal==83: newbyte=b"\x53"
    if decimal==84: newbyte=b"\x54"
    if decimal==85: newbyte=b"\x55"
    if decimal==86: newbyte=b"\x56"
    if decimal==87: newbyte=b"\x57"
    if decimal==88: newbyte=b"\x58"
    if decimal==89: newbyte=b"\x59"
    if decimal==90: newbyte=b"\x5A"
    if decimal==91: newbyte=b"\x5B"
    if decimal==92: newbyte=b"\x5C"
    if decimal==93: newbyte=b"\x5D"
    if decimal==94: newbyte=b"\x5E"
    if decimal==95: newbyte=b"\x5F"
    if decimal==96: newbyte=b"\x60"
    if decimal==97: newbyte=b"\x61"
    if decimal==98: newbyte=b"\x62"
    if decimal==99: newbyte=b"\x63"
    if decimal==100: newbyte=b"\x64"
    if decimal==101: newbyte=b"\x65"
    if decimal==102: newbyte=b"\x66"
    if decimal==103: newbyte=b"\x67"
    if decimal==104: newbyte=b"\x68"
    if decimal==105: newbyte=b"\x69"
    if decimal==106: newbyte=b"\x6A"
    if decimal==107: newbyte=b"\x6B"
    if decimal==108: newbyte=b"\x6C"
    if decimal==109: newbyte=b"\x6D"
    if decimal==110: newbyte=b"\x6E"
    if decimal==111: newbyte=b"\x6F"
    if decimal==112: newbyte=b"\x70"
    if decimal==113: newbyte=b"\x71"
    if decimal==114: newbyte=b"\x72"
    if decimal==115: newbyte=b"\x73"
    if decimal==116: newbyte=b"\x74"
    if decimal==117: newbyte=b"\x75"
    if decimal==118: newbyte=b"\x76"
    if decimal==119: newbyte=b"\x77"
    if decimal==120: newbyte=b"\x78"
    if decimal==121: newbyte=b"\x79"
    if decimal==122: newbyte=b"\x7A"
    if decimal==123: newbyte=b"\x7B"
    if decimal==124: newbyte=b"\x7C"
    if decimal==125: newbyte=b"\x7D"
    if decimal==126: newbyte=b"\x7E"
    if decimal==127: newbyte=b"\x7F"
    if decimal==128: newbyte=b"\x80"
    if decimal==129: newbyte=b"\x81"
    if decimal==130: newbyte=b"\x82"
    if decimal==131: newbyte=b"\x83"
    if decimal==132: newbyte=b"\x84"
    if decimal==133: newbyte=b"\x85"
    if decimal==134: newbyte=b"\x86"
    if decimal==135: newbyte=b"\x87"
    if decimal==136: newbyte=b"\x88"
    if decimal==137: newbyte=b"\x89"
    if decimal==138: newbyte=b"\x8A"
    if decimal==139: newbyte=b"\x8B"
    if decimal==140: newbyte=b"\x8C"
    if decimal==141: newbyte=b"\x8D"
    if decimal==142: newbyte=b"\x8E"
    if decimal==143: newbyte=b"\x8F"
    if decimal==144: newbyte=b"\x90"
    if decimal==145: newbyte=b"\x91"
    if decimal==146: newbyte=b"\x92"
    if decimal==147: newbyte=b"\x93"
    if decimal==148: newbyte=b"\x94"
    if decimal==149: newbyte=b"\x95"
    if decimal==150: newbyte=b"\x96"
    if decimal==151: newbyte=b"\x97"
    if decimal==152: newbyte=b"\x98"
    if decimal==153: newbyte=b"\x99"
    if decimal==154: newbyte=b"\x9A"
    if decimal==155: newbyte=b"\x9B"
    if decimal==156: newbyte=b"\x9C"
    if decimal==157: newbyte=b"\x9D"
    if decimal==158: newbyte=b"\x9E"
    if decimal==159: newbyte=b"\x9F"
    if decimal==160: newbyte=b"\xA0"
    if decimal==161: newbyte=b"\xA1"
    if decimal==162: newbyte=b"\xA2"
    if decimal==163: newbyte=b"\xA3"
    if decimal==164: newbyte=b"\xA4"
    if decimal==165: newbyte=b"\xA5"
    if decimal==166: newbyte=b"\xA6"
    if decimal==167: newbyte=b"\xA7"
    if decimal==168: newbyte=b"\xA8"
    if decimal==169: newbyte=b"\xA9"
    if decimal==170: newbyte=b"\xAA"
    if decimal==171: newbyte=b"\xAB"
    if decimal==172: newbyte=b"\xAC"
    if decimal==173: newbyte=b"\xAD"
    if decimal==174: newbyte=b"\xAE"
    if decimal==175: newbyte=b"\xAF"
    if decimal==176: newbyte=b"\xB0"
    if decimal==177: newbyte=b"\xB1"
    if decimal==178: newbyte=b"\xB2"
    if decimal==179: newbyte=b"\xB3"
    if decimal==180: newbyte=b"\xB4"
    if decimal==181: newbyte=b"\xB5"
    if decimal==182: newbyte=b"\xB6"
    if decimal==183: newbyte=b"\xB7"
    if decimal==184: newbyte=b"\xB8"
    if decimal==185: newbyte=b"\xB9"
    if decimal==186: newbyte=b"\xBA"
    if decimal==187: newbyte=b"\xBB"
    if decimal==188: newbyte=b"\xBC"
    if decimal==189: newbyte=b"\xBD"
    if decimal==190: newbyte=b"\xBE"
    if decimal==191: newbyte=b"\xBF"
    if decimal==192: newbyte=b"\xC0"
    if decimal==193: newbyte=b"\xC1"
    if decimal==194: newbyte=b"\xC2"
    if decimal==195: newbyte=b"\xC3"
    if decimal==196: newbyte=b"\xC4"
    if decimal==197: newbyte=b"\xC5"
    if decimal==198: newbyte=b"\xC6"
    if decimal==199: newbyte=b"\xC7"
    if decimal==200: newbyte=b"\xC8"
    if decimal==201: newbyte=b"\xC9"
    if decimal==202: newbyte=b"\xCA"
    if decimal==203: newbyte=b"\xCB"
    if decimal==204: newbyte=b"\xCC"
    if decimal==205: newbyte=b"\xCD"
    if decimal==206: newbyte=b"\xCE"
    if decimal==207: newbyte=b"\xCF"
    if decimal==208: newbyte=b"\xD0"
    if decimal==209: newbyte=b"\xD1"
    if decimal==210: newbyte=b"\xD2"
    if decimal==211: newbyte=b"\xD3"
    if decimal==212: newbyte=b"\xD4"
    if decimal==213: newbyte=b"\xD5"
    if decimal==214: newbyte=b"\xD6"
    if decimal==215: newbyte=b"\xD7"
    if decimal==216: newbyte=b"\xD8"
    if decimal==217: newbyte=b"\xD9"
    if decimal==218: newbyte=b"\xDA"
    if decimal==219: newbyte=b"\xDB"
    if decimal==220: newbyte=b"\xDC"
    if decimal==221: newbyte=b"\xDD"
    if decimal==222: newbyte=b"\xDE"
    if decimal==223: newbyte=b"\xDF"
    if decimal==224: newbyte=b"\xE0"
    if decimal==225: newbyte=b"\xE1"
    if decimal==226: newbyte=b"\xE2"
    if decimal==227: newbyte=b"\xE3"
    if decimal==228: newbyte=b"\xE4"
    if decimal==229: newbyte=b"\xE5"
    if decimal==230: newbyte=b"\xE6"
    if decimal==231: newbyte=b"\xE7"
    if decimal==232: newbyte=b"\xE8"
    if decimal==233: newbyte=b"\xE9"
    if decimal==234: newbyte=b"\xEA"
    if decimal==235: newbyte=b"\xEB"
    if decimal==236: newbyte=b"\xEC"
    if decimal==237: newbyte=b"\xED"
    if decimal==238: newbyte=b"\xEE"
    if decimal==239: newbyte=b"\xEF"
    if decimal==240: newbyte=b"\xF0"
    if decimal==241: newbyte=b"\xF1"
    if decimal==242: newbyte=b"\xF2"
    if decimal==243: newbyte=b"\xF3"
    if decimal==244: newbyte=b"\xF4"
    if decimal==245: newbyte=b"\xF5"
    if decimal==246: newbyte=b"\xF6"
    if decimal==247: newbyte=b"\xF7"
    if decimal==248: newbyte=b"\xF8"
    if decimal==249: newbyte=b"\xF9"
    if decimal==250: newbyte=b"\xFA"
    if decimal==251: newbyte=b"\xFB"
    if decimal==252: newbyte=b"\xFC"
    if decimal==253: newbyte=b"\xFD"
    if decimal==254: newbyte=b"\xFE"
    if decimal==255: newbyte=b"\xFF"
    return newbyte

# Text/Character string to byte(s) string converter.
# "some_string" is any ASCII string including "\x??" characters as required.
def t2b(some_string):
    # Allocate an empty byte(s) string.
    new_byte_string=b""
    # Use the loop to build the byte(s) string from a standard string.
    for n in range(0,len(some_string),1):
        # Convert each _character_ in the string to a decimal number.
        decimal_number=ord(some_string[n])
        # Call the "d2b()" above function.
        d2b_character=d2b(decimal_number)
        # Build the byte(s) string one character at a time.
        new_byte_string=new_byte_string+d2b_character
    # The complete byte(s) string has now been converted.
    return new_byte_string


# Decimal number to HEX string converter.
def d2hexstr(decimal):
    newbyte = ''
    if decimal==0: newbyte='00'
    if decimal==1: newbyte='01'
    if decimal==2: newbyte='02'
    if decimal==3: newbyte='03'
    if decimal==4: newbyte='04'
    if decimal==5: newbyte='05'
    if decimal==6: newbyte='06'
    if decimal==7: newbyte='07'
    if decimal==8: newbyte='08'
    if decimal==9: newbyte='09'
    if decimal==10: newbyte='0A'
    if decimal==11: newbyte='0B'
    if decimal==12: newbyte='0C'
    if decimal==13: newbyte='0D'
    if decimal==14: newbyte='0E'
    if decimal==15: newbyte='0F'
    if decimal==16: newbyte='10'
    if decimal==17: newbyte='11'
    if decimal==18: newbyte='12'
    if decimal==19: newbyte='13'
    if decimal==20: newbyte='14'
    if decimal==21: newbyte='15'
    if decimal==22: newbyte='16'
    if decimal==23: newbyte='17'
    if decimal==24: newbyte='18'
    if decimal==25: newbyte='19'
    if decimal==26: newbyte='1A'
    if decimal==27: newbyte='1B'
    if decimal==28: newbyte='1C'
    if decimal==29: newbyte='1D'
    if decimal==30: newbyte='1E'
    if decimal==31: newbyte='1F'
    if decimal==32: newbyte='20'
    if decimal==33: newbyte='21'
    if decimal==34: newbyte='22'
    if decimal==35: newbyte='23'
    if decimal==36: newbyte='24'
    if decimal==37: newbyte='25'
    if decimal==38: newbyte='26'
    if decimal==39: newbyte='27'
    if decimal==40: newbyte='28'
    if decimal==41: newbyte='29'
    if decimal==42: newbyte='2A'
    if decimal==43: newbyte='2B'
    if decimal==44: newbyte='2C'
    if decimal==45: newbyte='2D'
    if decimal==46: newbyte='2E'
    if decimal==47: newbyte='2F'
    if decimal==48: newbyte='30'
    if decimal==49: newbyte='31'
    if decimal==50: newbyte='32'
    if decimal==51: newbyte='33'
    if decimal==52: newbyte='34'
    if decimal==53: newbyte='35'
    if decimal==54: newbyte='36'
    if decimal==55: newbyte='37'
    if decimal==56: newbyte='38'
    if decimal==57: newbyte='39'
    if decimal==58: newbyte='3A'
    if decimal==59: newbyte='3B'
    if decimal==60: newbyte='3C'
    if decimal==61: newbyte='3D'
    if decimal==62: newbyte='3E'
    if decimal==63: newbyte='3F'
    if decimal==64: newbyte='40'
    if decimal==65: newbyte='41'
    if decimal==66: newbyte='42'
    if decimal==67: newbyte='43'
    if decimal==68: newbyte='44'
    if decimal==69: newbyte='45'
    if decimal==70: newbyte='46'
    if decimal==71: newbyte='47'
    if decimal==72: newbyte='48'
    if decimal==73: newbyte='49'
    if decimal==74: newbyte='4A'
    if decimal==75: newbyte='4B'
    if decimal==76: newbyte='4C'
    if decimal==77: newbyte='4D'
    if decimal==78: newbyte='4E'
    if decimal==79: newbyte='4F'
    if decimal==80: newbyte='50'
    if decimal==81: newbyte='51'
    if decimal==82: newbyte='52'
    if decimal==83: newbyte='53'
    if decimal==84: newbyte='54'
    if decimal==85: newbyte='55'
    if decimal==86: newbyte='56'
    if decimal==87: newbyte='57'
    if decimal==88: newbyte='58'
    if decimal==89: newbyte='59'
    if decimal==90: newbyte='5A'
    if decimal==91: newbyte='5B'
    if decimal==92: newbyte='5C'
    if decimal==93: newbyte='5D'
    if decimal==94: newbyte='5E'
    if decimal==95: newbyte='5F'
    if decimal==96: newbyte='60'
    if decimal==97: newbyte='61'
    if decimal==98: newbyte='62'
    if decimal==99: newbyte='63'
    if decimal==100: newbyte='64'
    if decimal==101: newbyte='65'
    if decimal==102: newbyte='66'
    if decimal==103: newbyte='67'
    if decimal==104: newbyte='68'
    if decimal==105: newbyte='69'
    if decimal==106: newbyte='6A'
    if decimal==107: newbyte='6B'
    if decimal==108: newbyte='6C'
    if decimal==109: newbyte='6D'
    if decimal==110: newbyte='6E'
    if decimal==111: newbyte='6F'
    if decimal==112: newbyte='70'
    if decimal==113: newbyte='71'
    if decimal==114: newbyte='72'
    if decimal==115: newbyte='73'
    if decimal==116: newbyte='74'
    if decimal==117: newbyte='75'
    if decimal==118: newbyte='76'
    if decimal==119: newbyte='77'
    if decimal==120: newbyte='78'
    if decimal==121: newbyte='79'
    if decimal==122: newbyte='7A'
    if decimal==123: newbyte='7B'
    if decimal==124: newbyte='7C'
    if decimal==125: newbyte='7D'
    if decimal==126: newbyte='7E'
    if decimal==127: newbyte='7F'
    if decimal==128: newbyte='80'
    if decimal==129: newbyte='81'
    if decimal==130: newbyte='82'
    if decimal==131: newbyte='83'
    if decimal==132: newbyte='84'
    if decimal==133: newbyte='85'
    if decimal==134: newbyte='86'
    if decimal==135: newbyte='87'
    if decimal==136: newbyte='88'
    if decimal==137: newbyte='89'
    if decimal==138: newbyte='8A'
    if decimal==139: newbyte='8B'
    if decimal==140: newbyte='8C'
    if decimal==141: newbyte='8D'
    if decimal==142: newbyte='8E'
    if decimal==143: newbyte='8F'
    if decimal==144: newbyte='90'
    if decimal==145: newbyte='91'
    if decimal==146: newbyte='92'
    if decimal==147: newbyte='93'
    if decimal==148: newbyte='94'
    if decimal==149: newbyte='95'
    if decimal==150: newbyte='96'
    if decimal==151: newbyte='97'
    if decimal==152: newbyte='98'
    if decimal==153: newbyte='99'
    if decimal==154: newbyte='9A'
    if decimal==155: newbyte='9B'
    if decimal==156: newbyte='9C'
    if decimal==157: newbyte='9D'
    if decimal==158: newbyte='9E'
    if decimal==159: newbyte='9F'
    if decimal==160: newbyte='A0'
    if decimal==161: newbyte='A1'
    if decimal==162: newbyte='A2'
    if decimal==163: newbyte='A3'
    if decimal==164: newbyte='A4'
    if decimal==165: newbyte='A5'
    if decimal==166: newbyte='A6'
    if decimal==167: newbyte='A7'
    if decimal==168: newbyte='A8'
    if decimal==169: newbyte='A9'
    if decimal==170: newbyte='AA'
    if decimal==171: newbyte='AB'
    if decimal==172: newbyte='AC'
    if decimal==173: newbyte='AD'
    if decimal==174: newbyte='AE'
    if decimal==175: newbyte='AF'
    if decimal==176: newbyte='B0'
    if decimal==177: newbyte='B1'
    if decimal==178: newbyte='B2'
    if decimal==179: newbyte='B3'
    if decimal==180: newbyte='B4'
    if decimal==181: newbyte='B5'
    if decimal==182: newbyte='B6'
    if decimal==183: newbyte='B7'
    if decimal==184: newbyte='B8'
    if decimal==185: newbyte='B9'
    if decimal==186: newbyte='BA'
    if decimal==187: newbyte='BB'
    if decimal==188: newbyte='BC'
    if decimal==189: newbyte='BD'
    if decimal==190: newbyte='BE'
    if decimal==191: newbyte='BF'
    if decimal==192: newbyte='C0'
    if decimal==193: newbyte='C1'
    if decimal==194: newbyte='C2'
    if decimal==195: newbyte='C3'
    if decimal==196: newbyte='C4'
    if decimal==197: newbyte='C5'
    if decimal==198: newbyte='C6'
    if decimal==199: newbyte='C7'
    if decimal==200: newbyte='C8'
    if decimal==201: newbyte='C9'
    if decimal==202: newbyte='CA'
    if decimal==203: newbyte='CB'
    if decimal==204: newbyte='CC'
    if decimal==205: newbyte='CD'
    if decimal==206: newbyte='CE'
    if decimal==207: newbyte='CF'
    if decimal==208: newbyte='D0'
    if decimal==209: newbyte='D1'
    if decimal==210: newbyte='D2'
    if decimal==211: newbyte='D3'
    if decimal==212: newbyte='D4'
    if decimal==213: newbyte='D5'
    if decimal==214: newbyte='D6'
    if decimal==215: newbyte='D7'
    if decimal==216: newbyte='D8'
    if decimal==217: newbyte='D9'
    if decimal==218: newbyte='DA'
    if decimal==219: newbyte='DB'
    if decimal==220: newbyte='DC'
    if decimal==221: newbyte='DD'
    if decimal==222: newbyte='DE'
    if decimal==223: newbyte='DF'
    if decimal==224: newbyte='E0'
    if decimal==225: newbyte='E1'
    if decimal==226: newbyte='E2'
    if decimal==227: newbyte='E3'
    if decimal==228: newbyte='E4'
    if decimal==229: newbyte='E5'
    if decimal==230: newbyte='E6'
    if decimal==231: newbyte='E7'
    if decimal==232: newbyte='E8'
    if decimal==233: newbyte='E9'
    if decimal==234: newbyte='EA'
    if decimal==235: newbyte='EB'
    if decimal==236: newbyte='EC'
    if decimal==237: newbyte='ED'
    if decimal==238: newbyte='EE'
    if decimal==239: newbyte='EF'
    if decimal==240: newbyte='F0'
    if decimal==241: newbyte='F1'
    if decimal==242: newbyte='F2'
    if decimal==243: newbyte='F3'
    if decimal==244: newbyte='F4'
    if decimal==245: newbyte='F5'
    if decimal==246: newbyte='F6'
    if decimal==247: newbyte='F7'
    if decimal==248: newbyte='F8'
    if decimal==249: newbyte='F9'
    if decimal==250: newbyte='FA'
    if decimal==251: newbyte='FB'
    if decimal==252: newbyte='FC'
    if decimal==253: newbyte='FD'
    if decimal==254: newbyte='FE'
    if decimal==255: newbyte='FF'
    return newbyte


# byte number to integer converter.
def b2d(decimal):
    newbyte = 0
    if decimal==b"\x00": newbyte=0
    if decimal==b"\x01": newbyte=1
    if decimal==b"\x02": newbyte=2
    if decimal==b"\x03": newbyte=3
    if decimal==b"\x04": newbyte=4
    if decimal==b"\x05": newbyte=5
    if decimal==b"\x06": newbyte=6
    if decimal==b"\x07": newbyte=7
    if decimal==b"\x08": newbyte=8
    if decimal==b"\x09": newbyte=9
    if decimal==b"\x0A": newbyte=10
    if decimal==b"\x0B": newbyte=11
    if decimal==b"\x0C": newbyte=12
    if decimal==b"\x0D": newbyte=13
    if decimal==b"\x0E": newbyte=14
    if decimal==b"\x0F": newbyte=15
    if decimal==b"\x10": newbyte=16
    if decimal==b"\x11": newbyte=17
    if decimal==b"\x12": newbyte=18
    if decimal==b"\x13": newbyte=19
    if decimal==b"\x14": newbyte=20
    if decimal==b"\x15": newbyte=21
    if decimal==b"\x16": newbyte=22
    if decimal==b"\x17": newbyte=23
    if decimal==b"\x18": newbyte=24
    if decimal==b"\x19": newbyte=25
    if decimal==b"\x1A": newbyte=26
    if decimal==b"\x1B": newbyte=27
    if decimal==b"\x1C": newbyte=28
    if decimal==b"\x1D": newbyte=29
    if decimal==b"\x1E": newbyte=30
    if decimal==b"\x1F": newbyte=31
    if decimal==b"\x20": newbyte=32
    if decimal==b"\x21": newbyte=33
    if decimal==b"\x22": newbyte=34
    if decimal==b"\x23": newbyte=35
    if decimal==b"\x24": newbyte=36
    if decimal==b"\x25": newbyte=37
    if decimal==b"\x26": newbyte=38
    if decimal==b"\x27": newbyte=39
    if decimal==b"\x28": newbyte=40
    if decimal==b"\x29": newbyte=41
    if decimal==b"\x2A": newbyte=42
    if decimal==b"\x2B": newbyte=43
    if decimal==b"\x2C": newbyte=44
    if decimal==b"\x2D": newbyte=45
    if decimal==b"\x2E": newbyte=46
    if decimal==b"\x2F": newbyte=47
    if decimal==b"\x30": newbyte=48
    if decimal==b"\x31": newbyte=49
    if decimal==b"\x32": newbyte=50
    if decimal==b"\x33": newbyte=51
    if decimal==b"\x34": newbyte=52
    if decimal==b"\x35": newbyte=53
    if decimal==b"\x36": newbyte=54
    if decimal==b"\x37": newbyte=55
    if decimal==b"\x38": newbyte=56
    if decimal==b"\x39": newbyte=57
    if decimal==b"\x3A": newbyte=58
    if decimal==b"\x3B": newbyte=59
    if decimal==b"\x3C": newbyte=60
    if decimal==b"\x3D": newbyte=61
    if decimal==b"\x3E": newbyte=62
    if decimal==b"\x3F": newbyte=63
    if decimal==b"\x40": newbyte=64
    if decimal==b"\x41": newbyte=65
    if decimal==b"\x42": newbyte=66
    if decimal==b"\x43": newbyte=67
    if decimal==b"\x44": newbyte=68
    if decimal==b"\x45": newbyte=69
    if decimal==b"\x46": newbyte=70
    if decimal==b"\x47": newbyte=71
    if decimal==b"\x48": newbyte=72
    if decimal==b"\x49": newbyte=73
    if decimal==b"\x4A": newbyte=74
    if decimal==b"\x4B": newbyte=75
    if decimal==b"\x4C": newbyte=76
    if decimal==b"\x4D": newbyte=77
    if decimal==b"\x4E": newbyte=78
    if decimal==b"\x4F": newbyte=79
    if decimal==b"\x50": newbyte=80
    if decimal==b"\x51": newbyte=81
    if decimal==b"\x52": newbyte=82
    if decimal==b"\x53": newbyte=83
    if decimal==b"\x54": newbyte=84
    if decimal==b"\x55": newbyte=85
    if decimal==b"\x56": newbyte=86
    if decimal==b"\x57": newbyte=87
    if decimal==b"\x58": newbyte=88
    if decimal==b"\x59": newbyte=89
    if decimal==b"\x5A": newbyte=90
    if decimal==b"\x5B": newbyte=91
    if decimal==b"\x5C": newbyte=92
    if decimal==b"\x5D": newbyte=93
    if decimal==b"\x5E": newbyte=94
    if decimal==b"\x5F": newbyte=95
    if decimal==b"\x60": newbyte=96
    if decimal==b"\x61": newbyte=97
    if decimal==b"\x62": newbyte=98
    if decimal==b"\x63": newbyte=99
    if decimal==b"\x64": newbyte=100
    if decimal==b"\x65": newbyte=101
    if decimal==b"\x66": newbyte=102
    if decimal==b"\x67": newbyte=103
    if decimal==b"\x68": newbyte=104
    if decimal==b"\x69": newbyte=105
    if decimal==b"\x6A": newbyte=106
    if decimal==b"\x6B": newbyte=107
    if decimal==b"\x6C": newbyte=108
    if decimal==b"\x6D": newbyte=109
    if decimal==b"\x6E": newbyte=110
    if decimal==b"\x6F": newbyte=111
    if decimal==b"\x70": newbyte=112
    if decimal==b"\x71": newbyte=113
    if decimal==b"\x72": newbyte=114
    if decimal==b"\x73": newbyte=115
    if decimal==b"\x74": newbyte=116
    if decimal==b"\x75": newbyte=117
    if decimal==b"\x76": newbyte=118
    if decimal==b"\x77": newbyte=119
    if decimal==b"\x78": newbyte=120
    if decimal==b"\x79": newbyte=121
    if decimal==b"\x7A": newbyte=122
    if decimal==b"\x7B": newbyte=123
    if decimal==b"\x7C": newbyte=124
    if decimal==b"\x7D": newbyte=125
    if decimal==b"\x7E": newbyte=126
    if decimal==b"\x7F": newbyte=127
    if decimal==b"\x80": newbyte=128
    if decimal==b"\x81": newbyte=129
    if decimal==b"\x82": newbyte=130
    if decimal==b"\x83": newbyte=131
    if decimal==b"\x84": newbyte=132
    if decimal==b"\x85": newbyte=133
    if decimal==b"\x86": newbyte=134
    if decimal==b"\x87": newbyte=135
    if decimal==b"\x88": newbyte=136
    if decimal==b"\x89": newbyte=137
    if decimal==b"\x8A": newbyte=138
    if decimal==b"\x8B": newbyte=139
    if decimal==b"\x8C": newbyte=140
    if decimal==b"\x8D": newbyte=141
    if decimal==b"\x8E": newbyte=142
    if decimal==b"\x8F": newbyte=143
    if decimal==b"\x90": newbyte=144
    if decimal==b"\x91": newbyte=145
    if decimal==b"\x92": newbyte=146
    if decimal==b"\x93": newbyte=147
    if decimal==b"\x94": newbyte=148
    if decimal==b"\x95": newbyte=149
    if decimal==b"\x96": newbyte=150
    if decimal==b"\x97": newbyte=151
    if decimal==b"\x98": newbyte=152
    if decimal==b"\x99": newbyte=153
    if decimal==b"\x9A": newbyte=154
    if decimal==b"\x9B": newbyte=155
    if decimal==b"\x9C": newbyte=156
    if decimal==b"\x9D": newbyte=157
    if decimal==b"\x9E": newbyte=158
    if decimal==b"\x9F": newbyte=159
    if decimal==b"\xA0": newbyte=160
    if decimal==b"\xA1": newbyte=161
    if decimal==b"\xA2": newbyte=162
    if decimal==b"\xA3": newbyte=163
    if decimal==b"\xA4": newbyte=164
    if decimal==b"\xA5": newbyte=165
    if decimal==b"\xA6": newbyte=166
    if decimal==b"\xA7": newbyte=167
    if decimal==b"\xA8": newbyte=168
    if decimal==b"\xA9": newbyte=169
    if decimal==b"\xAA": newbyte=170
    if decimal==b"\xAB": newbyte=171
    if decimal==b"\xAC": newbyte=172
    if decimal==b"\xAD": newbyte=173
    if decimal==b"\xAE": newbyte=174
    if decimal==b"\xAF": newbyte=175
    if decimal==b"\xB0": newbyte=176
    if decimal==b"\xB1": newbyte=177
    if decimal==b"\xB2": newbyte=178
    if decimal==b"\xB3": newbyte=179
    if decimal==b"\xB4": newbyte=180
    if decimal==b"\xB5": newbyte=181
    if decimal==b"\xB6": newbyte=182
    if decimal==b"\xB7": newbyte=183
    if decimal==b"\xB8": newbyte=184
    if decimal==b"\xB9": newbyte=185
    if decimal==b"\xBA": newbyte=186
    if decimal==b"\xBB": newbyte=187
    if decimal==b"\xBC": newbyte=188
    if decimal==b"\xBD": newbyte=189
    if decimal==b"\xBE": newbyte=190
    if decimal==b"\xBF": newbyte=191
    if decimal==b"\xC0": newbyte=192
    if decimal==b"\xC1": newbyte=193
    if decimal==b"\xC2": newbyte=194
    if decimal==b"\xC3": newbyte=195
    if decimal==b"\xC4": newbyte=196
    if decimal==b"\xC5": newbyte=197
    if decimal==b"\xC6": newbyte=198
    if decimal==b"\xC7": newbyte=199
    if decimal==b"\xC8": newbyte=200
    if decimal==b"\xC9": newbyte=201
    if decimal==b"\xCA": newbyte=202
    if decimal==b"\xCB": newbyte=203
    if decimal==b"\xCC": newbyte=204
    if decimal==b"\xCD": newbyte=205
    if decimal==b"\xCE": newbyte=206
    if decimal==b"\xCF": newbyte=207
    if decimal==b"\xD0": newbyte=208
    if decimal==b"\xD1": newbyte=209
    if decimal==b"\xD2": newbyte=210
    if decimal==b"\xD3": newbyte=211
    if decimal==b"\xD4": newbyte=212
    if decimal==b"\xD5": newbyte=213
    if decimal==b"\xD6": newbyte=214
    if decimal==b"\xD7": newbyte=215
    if decimal==b"\xD8": newbyte=216
    if decimal==b"\xD9": newbyte=217
    if decimal==b"\xDA": newbyte=218
    if decimal==b"\xDB": newbyte=219
    if decimal==b"\xDC": newbyte=220
    if decimal==b"\xDD": newbyte=221
    if decimal==b"\xDE": newbyte=222
    if decimal==b"\xDF": newbyte=223
    if decimal==b"\xE0": newbyte=224
    if decimal==b"\xE1": newbyte=225
    if decimal==b"\xE2": newbyte=226
    if decimal==b"\xE3": newbyte=227
    if decimal==b"\xE4": newbyte=228
    if decimal==b"\xE5": newbyte=229
    if decimal==b"\xE6": newbyte=230
    if decimal==b"\xE7": newbyte=231
    if decimal==b"\xE8": newbyte=232
    if decimal==b"\xE9": newbyte=233
    if decimal==b"\xEA": newbyte=234
    if decimal==b"\xEB": newbyte=235
    if decimal==b"\xEC": newbyte=236
    if decimal==b"\xED": newbyte=237
    if decimal==b"\xEE": newbyte=238
    if decimal==b"\xEF": newbyte=239
    if decimal==b"\xF0": newbyte=240
    if decimal==b"\xF1": newbyte=241
    if decimal==b"\xF2": newbyte=242
    if decimal==b"\xF3": newbyte=243
    if decimal==b"\xF4": newbyte=244
    if decimal==b"\xF5": newbyte=245
    if decimal==b"\xF6": newbyte=246
    if decimal==b"\xF7": newbyte=247
    if decimal==b"\xF8": newbyte=248
    if decimal==b"\xF9": newbyte=249
    if decimal==b"\xFA": newbyte=250
    if decimal==b"\xFB": newbyte=251
    if decimal==b"\xFC": newbyte=252
    if decimal==b"\xFD": newbyte=253
    if decimal==b"\xFE": newbyte=254
    if decimal==b"\xFF": newbyte=255
    return newbyte

# Hex string to decimal integer converter.
def hexstr2d(hexstr):
    decimal = 0
    if hexstr=='0x00': decimal=0
    if hexstr=='0x01': decimal=1
    if hexstr=='0x02': decimal=2
    if hexstr=='0x03': decimal=3
    if hexstr=='0x04': decimal=4
    if hexstr=='0x05': decimal=5
    if hexstr=='0x06': decimal=6
    if hexstr=='0x07': decimal=7
    if hexstr=='0x08': decimal=8
    if hexstr=='0x09': decimal=9
    if hexstr=='0x0A': decimal=10
    if hexstr=='0x0B': decimal=11
    if hexstr=='0x0C': decimal=12
    if hexstr=='0x0D': decimal=13
    if hexstr=='0x0E': decimal=14
    if hexstr=='0x0F': decimal=15
    if hexstr=='0x10': decimal=16
    if hexstr=='0x11': decimal=17
    if hexstr=='0x12': decimal=18
    if hexstr=='0x13': decimal=19
    if hexstr=='0x14': decimal=20
    if hexstr=='0x15': decimal=21
    if hexstr=='0x16': decimal=22
    if hexstr=='0x17': decimal=23
    if hexstr=='0x18': decimal=24
    if hexstr=='0x19': decimal=25
    if hexstr=='0x1A': decimal=26
    if hexstr=='0x1B': decimal=27
    if hexstr=='0x1C': decimal=28
    if hexstr=='0x1D': decimal=29
    if hexstr=='0x1E': decimal=30
    if hexstr=='0x1F': decimal=31
    if hexstr=='0x20': decimal=32
    if hexstr=='0x21': decimal=33
    if hexstr=='0x22': decimal=34
    if hexstr=='0x23': decimal=35
    if hexstr=='0x24': decimal=36
    if hexstr=='0x25': decimal=37
    if hexstr=='0x26': decimal=38
    if hexstr=='0x27': decimal=39
    if hexstr=='0x28': decimal=40
    if hexstr=='0x29': decimal=41
    if hexstr=='0x2A': decimal=42
    if hexstr=='0x2B': decimal=43
    if hexstr=='0x2C': decimal=44
    if hexstr=='0x2D': decimal=45
    if hexstr=='0x2E': decimal=46
    if hexstr=='0x2F': decimal=47
    if hexstr=='0x30': decimal=48
    if hexstr=='0x31': decimal=49
    if hexstr=='0x32': decimal=50
    if hexstr=='0x33': decimal=51
    if hexstr=='0x34': decimal=52
    if hexstr=='0x35': decimal=53
    if hexstr=='0x36': decimal=54
    if hexstr=='0x37': decimal=55
    if hexstr=='0x38': decimal=56
    if hexstr=='0x39': decimal=57
    if hexstr=='0x3A': decimal=58
    if hexstr=='0x3B': decimal=59
    if hexstr=='0x3C': decimal=60
    if hexstr=='0x3D': decimal=61
    if hexstr=='0x3E': decimal=62
    if hexstr=='0x3F': decimal=63
    if hexstr=='0x40': decimal=64
    if hexstr=='0x41': decimal=65
    if hexstr=='0x42': decimal=66
    if hexstr=='0x43': decimal=67
    if hexstr=='0x44': decimal=68
    if hexstr=='0x45': decimal=69
    if hexstr=='0x46': decimal=70
    if hexstr=='0x47': decimal=71
    if hexstr=='0x48': decimal=72
    if hexstr=='0x49': decimal=73
    if hexstr=='0x4A': decimal=74
    if hexstr=='0x4B': decimal=75
    if hexstr=='0x4C': decimal=76
    if hexstr=='0x4D': decimal=77
    if hexstr=='0x4E': decimal=78
    if hexstr=='0x4F': decimal=79
    if hexstr=='0x50': decimal=80
    if hexstr=='0x51': decimal=81
    if hexstr=='0x52': decimal=82
    if hexstr=='0x53': decimal=83
    if hexstr=='0x54': decimal=84
    if hexstr=='0x55': decimal=85
    if hexstr=='0x56': decimal=86
    if hexstr=='0x57': decimal=87
    if hexstr=='0x58': decimal=88
    if hexstr=='0x59': decimal=89
    if hexstr=='0x5A': decimal=90
    if hexstr=='0x5B': decimal=91
    if hexstr=='0x5C': decimal=92
    if hexstr=='0x5D': decimal=93
    if hexstr=='0x5E': decimal=94
    if hexstr=='0x5F': decimal=95
    if hexstr=='0x60': decimal=96
    if hexstr=='0x61': decimal=97
    if hexstr=='0x62': decimal=98
    if hexstr=='0x63': decimal=99
    if hexstr=='0x64': decimal=100
    if hexstr=='0x65': decimal=101
    if hexstr=='0x66': decimal=102
    if hexstr=='0x67': decimal=103
    if hexstr=='0x68': decimal=104
    if hexstr=='0x69': decimal=105
    if hexstr=='0x6A': decimal=106
    if hexstr=='0x6B': decimal=107
    if hexstr=='0x6C': decimal=108
    if hexstr=='0x6D': decimal=109
    if hexstr=='0x6E': decimal=110
    if hexstr=='0x6F': decimal=111
    if hexstr=='0x70': decimal=112
    if hexstr=='0x71': decimal=113
    if hexstr=='0x72': decimal=114
    if hexstr=='0x73': decimal=115
    if hexstr=='0x74': decimal=116
    if hexstr=='0x75': decimal=117
    if hexstr=='0x76': decimal=118
    if hexstr=='0x77': decimal=119
    if hexstr=='0x78': decimal=120
    if hexstr=='0x79': decimal=121
    if hexstr=='0x7A': decimal=122
    if hexstr=='0x7B': decimal=123
    if hexstr=='0x7C': decimal=124
    if hexstr=='0x7D': decimal=125
    if hexstr=='0x7E': decimal=126
    if hexstr=='0x7F': decimal=127
    if hexstr=='0x80': decimal=128
    if hexstr=='0x81': decimal=129
    if hexstr=='0x82': decimal=130
    if hexstr=='0x83': decimal=131
    if hexstr=='0x84': decimal=132
    if hexstr=='0x85': decimal=133
    if hexstr=='0x86': decimal=134
    if hexstr=='0x87': decimal=135
    if hexstr=='0x88': decimal=136
    if hexstr=='0x89': decimal=137
    if hexstr=='0x8A': decimal=138
    if hexstr=='0x8B': decimal=139
    if hexstr=='0x8C': decimal=140
    if hexstr=='0x8D': decimal=141
    if hexstr=='0x8E': decimal=142
    if hexstr=='0x8F': decimal=143
    if hexstr=='0x90': decimal=144
    if hexstr=='0x91': decimal=145
    if hexstr=='0x92': decimal=146
    if hexstr=='0x93': decimal=147
    if hexstr=='0x94': decimal=148
    if hexstr=='0x95': decimal=149
    if hexstr=='0x96': decimal=150
    if hexstr=='0x97': decimal=151
    if hexstr=='0x98': decimal=152
    if hexstr=='0x99': decimal=153
    if hexstr=='0x9A': decimal=154
    if hexstr=='0x9B': decimal=155
    if hexstr=='0x9C': decimal=156
    if hexstr=='0x9D': decimal=157
    if hexstr=='0x9E': decimal=158
    if hexstr=='0x9F': decimal=159
    if hexstr=='0xA0': decimal=160
    if hexstr=='0xA1': decimal=161
    if hexstr=='0xA2': decimal=162
    if hexstr=='0xA3': decimal=163
    if hexstr=='0xA4': decimal=164
    if hexstr=='0xA5': decimal=165
    if hexstr=='0xA6': decimal=166
    if hexstr=='0xA7': decimal=167
    if hexstr=='0xA8': decimal=168
    if hexstr=='0xA9': decimal=169
    if hexstr=='0xAA': decimal=170
    if hexstr=='0xAB': decimal=171
    if hexstr=='0xAC': decimal=172
    if hexstr=='0xAD': decimal=173
    if hexstr=='0xAE': decimal=174
    if hexstr=='0xAF': decimal=175
    if hexstr=='0xB0': decimal=176
    if hexstr=='0xB1': decimal=177
    if hexstr=='0xB2': decimal=178
    if hexstr=='0xB3': decimal=179
    if hexstr=='0xB4': decimal=180
    if hexstr=='0xB5': decimal=181
    if hexstr=='0xB6': decimal=182
    if hexstr=='0xB7': decimal=183
    if hexstr=='0xB8': decimal=184
    if hexstr=='0xB9': decimal=185
    if hexstr=='0xBA': decimal=186
    if hexstr=='0xBB': decimal=187
    if hexstr=='0xBC': decimal=188
    if hexstr=='0xBD': decimal=189
    if hexstr=='0xBE': decimal=190
    if hexstr=='0xBF': decimal=191
    if hexstr=='0xC0': decimal=192
    if hexstr=='0xC1': decimal=193
    if hexstr=='0xC2': decimal=194
    if hexstr=='0xC3': decimal=195
    if hexstr=='0xC4': decimal=196
    if hexstr=='0xC5': decimal=197
    if hexstr=='0xC6': decimal=198
    if hexstr=='0xC7': decimal=199
    if hexstr=='0xC8': decimal=200
    if hexstr=='0xC9': decimal=201
    if hexstr=='0xCA': decimal=202
    if hexstr=='0xCB': decimal=203
    if hexstr=='0xCC': decimal=204
    if hexstr=='0xCD': decimal=205
    if hexstr=='0xCE': decimal=206
    if hexstr=='0xCF': decimal=207
    if hexstr=='0xD0': decimal=208
    if hexstr=='0xD1': decimal=209
    if hexstr=='0xD2': decimal=210
    if hexstr=='0xD3': decimal=211
    if hexstr=='0xD4': decimal=212
    if hexstr=='0xD5': decimal=213
    if hexstr=='0xD6': decimal=214
    if hexstr=='0xD7': decimal=215
    if hexstr=='0xD8': decimal=216
    if hexstr=='0xD9': decimal=217
    if hexstr=='0xDA': decimal=218
    if hexstr=='0xDB': decimal=219
    if hexstr=='0xDC': decimal=220
    if hexstr=='0xDD': decimal=221
    if hexstr=='0xDE': decimal=222
    if hexstr=='0xDF': decimal=223
    if hexstr=='0xE0': decimal=224
    if hexstr=='0xE1': decimal=225
    if hexstr=='0xE2': decimal=226
    if hexstr=='0xE3': decimal=227
    if hexstr=='0xE4': decimal=228
    if hexstr=='0xE5': decimal=229
    if hexstr=='0xE6': decimal=230
    if hexstr=='0xE7': decimal=231
    if hexstr=='0xE8': decimal=232
    if hexstr=='0xE9': decimal=233
    if hexstr=='0xEA': decimal=234
    if hexstr=='0xEB': decimal=235
    if hexstr=='0xEC': decimal=236
    if hexstr=='0xED': decimal=237
    if hexstr=='0xEE': decimal=238
    if hexstr=='0xEF': decimal=239
    if hexstr=='0xF0': decimal=240
    if hexstr=='0xF1': decimal=241
    if hexstr=='0xF2': decimal=242
    if hexstr=='0xF3': decimal=243
    if hexstr=='0xF4': decimal=244
    if hexstr=='0xF5': decimal=245
    if hexstr=='0xF6': decimal=246
    if hexstr=='0xF7': decimal=247
    if hexstr=='0xF8': decimal=248
    if hexstr=='0xF9': decimal=249
    if hexstr=='0xFA': decimal=250
    if hexstr=='0xFB': decimal=251
    if hexstr=='0xFC': decimal=252
    if hexstr=='0xFD': decimal=253
    if hexstr=='0xFE': decimal=254
    if hexstr=='0xFF': decimal=255
    return decimal


# Hex string to hex byte converter.
def hex2hexstr(hexstr):
    hexbyte = 0
    if hexstr=='0x00': hexbyte=b"\x00"
    if hexstr=='0x01': hexbyte=b"\x01"
    if hexstr=='0x02': hexbyte=b"\x02"
    if hexstr=='0x03': hexbyte=b"\x03"
    if hexstr=='0x04': hexbyte=b"\x04"
    if hexstr=='0x05': hexbyte=b"\x05"
    if hexstr=='0x06': hexbyte=b"\x06"
    if hexstr=='0x07': hexbyte=b"\x07"
    if hexstr=='0x08': hexbyte=b"\x08"
    if hexstr=='0x09': hexbyte=b"\x09"
    if hexstr=='0x0A': hexbyte=b"\x0A"
    if hexstr=='0x0B': hexbyte=b"\x0B"
    if hexstr=='0x0C': hexbyte=b"\x0C"
    if hexstr=='0x0D': hexbyte=b"\x0D"
    if hexstr=='0x0E': hexbyte=b"\x0E"
    if hexstr=='0x0F': hexbyte=b"\x0F"
    if hexstr=='0x10': hexbyte=b"\x10"
    if hexstr=='0x11': hexbyte=b"\x11"
    if hexstr=='0x12': hexbyte=b"\x12"
    if hexstr=='0x13': hexbyte=b"\x13"
    if hexstr=='0x14': hexbyte=b"\x14"
    if hexstr=='0x15': hexbyte=b"\x15"
    if hexstr=='0x16': hexbyte=b"\x16"
    if hexstr=='0x17': hexbyte=b"\x17"
    if hexstr=='0x18': hexbyte=b"\x18"
    if hexstr=='0x19': hexbyte=b"\x19"
    if hexstr=='0x1A': hexbyte=b"\x1A"
    if hexstr=='0x1B': hexbyte=b"\x1B"
    if hexstr=='0x1C': hexbyte=b"\x1C"
    if hexstr=='0x1D': hexbyte=b"\x1D"
    if hexstr=='0x1E': hexbyte=b"\x1E"
    if hexstr=='0x1F': hexbyte=b"\x1F"
    if hexstr=='0x20': hexbyte=b"\x20"
    if hexstr=='0x21': hexbyte=b"\x21"
    if hexstr=='0x22': hexbyte=b"\x22"
    if hexstr=='0x23': hexbyte=b"\x23"
    if hexstr=='0x24': hexbyte=b"\x24"
    if hexstr=='0x25': hexbyte=b"\x25"
    if hexstr=='0x26': hexbyte=b"\x26"
    if hexstr=='0x27': hexbyte=b"\x27"
    if hexstr=='0x28': hexbyte=b"\x28"
    if hexstr=='0x29': hexbyte=b"\x29"
    if hexstr=='0x2A': hexbyte=b"\x2A"
    if hexstr=='0x2B': hexbyte=b"\x2B"
    if hexstr=='0x2C': hexbyte=b"\x2C"
    if hexstr=='0x2D': hexbyte=b"\x2D"
    if hexstr=='0x2E': hexbyte=b"\x2E"
    if hexstr=='0x2F': hexbyte=b"\x2F"
    if hexstr=='0x30': hexbyte=b"\x30"
    if hexstr=='0x31': hexbyte=b"\x31"
    if hexstr=='0x32': hexbyte=b"\x32"
    if hexstr=='0x33': hexbyte=b"\x33"
    if hexstr=='0x34': hexbyte=b"\x34"
    if hexstr=='0x35': hexbyte=b"\x35"
    if hexstr=='0x36': hexbyte=b"\x36"
    if hexstr=='0x37': hexbyte=b"\x37"
    if hexstr=='0x38': hexbyte=b"\x38"
    if hexstr=='0x39': hexbyte=b"\x39"
    if hexstr=='0x3A': hexbyte=b"\x3A"
    if hexstr=='0x3B': hexbyte=b"\x3B"
    if hexstr=='0x3C': hexbyte=b"\x3C"
    if hexstr=='0x3D': hexbyte=b"\x3D"
    if hexstr=='0x3E': hexbyte=b"\x3E"
    if hexstr=='0x3F': hexbyte=b"\x3F"
    if hexstr=='0x40': hexbyte=b"\x40"
    if hexstr=='0x41': hexbyte=b"\x41"
    if hexstr=='0x42': hexbyte=b"\x42"
    if hexstr=='0x43': hexbyte=b"\x43"
    if hexstr=='0x44': hexbyte=b"\x44"
    if hexstr=='0x45': hexbyte=b"\x45"
    if hexstr=='0x46': hexbyte=b"\x46"
    if hexstr=='0x47': hexbyte=b"\x47"
    if hexstr=='0x48': hexbyte=b"\x48"
    if hexstr=='0x49': hexbyte=b"\x49"
    if hexstr=='0x4A': hexbyte=b"\x4A"
    if hexstr=='0x4B': hexbyte=b"\x4B"
    if hexstr=='0x4C': hexbyte=b"\x4C"
    if hexstr=='0x4D': hexbyte=b"\x4D"
    if hexstr=='0x4E': hexbyte=b"\x4E"
    if hexstr=='0x4F': hexbyte=b"\x4F"
    if hexstr=='0x50': hexbyte=b"\x50"
    if hexstr=='0x51': hexbyte=b"\x51"
    if hexstr=='0x52': hexbyte=b"\x52"
    if hexstr=='0x53': hexbyte=b"\x53"
    if hexstr=='0x54': hexbyte=b"\x54"
    if hexstr=='0x55': hexbyte=b"\x55"
    if hexstr=='0x56': hexbyte=b"\x56"
    if hexstr=='0x57': hexbyte=b"\x57"
    if hexstr=='0x58': hexbyte=b"\x58"
    if hexstr=='0x59': hexbyte=b"\x59"
    if hexstr=='0x5A': hexbyte=b"\x5A"
    if hexstr=='0x5B': hexbyte=b"\x5B"
    if hexstr=='0x5C': hexbyte=b"\x5C"
    if hexstr=='0x5D': hexbyte=b"\x5D"
    if hexstr=='0x5E': hexbyte=b"\x5E"
    if hexstr=='0x5F': hexbyte=b"\x5F"
    if hexstr=='0x60': hexbyte=b"\x60"
    if hexstr=='0x61': hexbyte=b"\x61"
    if hexstr=='0x62': hexbyte=b"\x62"
    if hexstr=='0x63': hexbyte=b"\x63"
    if hexstr=='0x64': hexbyte=b"\x64"
    if hexstr=='0x65': hexbyte=b"\x65"
    if hexstr=='0x66': hexbyte=b"\x66"
    if hexstr=='0x67': hexbyte=b"\x67"
    if hexstr=='0x68': hexbyte=b"\x68"
    if hexstr=='0x69': hexbyte=b"\x69"
    if hexstr=='0x6A': hexbyte=b"\x6A"
    if hexstr=='0x6B': hexbyte=b"\x6B"
    if hexstr=='0x6C': hexbyte=b"\x6C"
    if hexstr=='0x6D': hexbyte=b"\x6D"
    if hexstr=='0x6E': hexbyte=b"\x6E"
    if hexstr=='0x6F': hexbyte=b"\x6F"
    if hexstr=='0x70': hexbyte=b"\x70"
    if hexstr=='0x71': hexbyte=b"\x71"
    if hexstr=='0x72': hexbyte=b"\x72"
    if hexstr=='0x73': hexbyte=b"\x73"
    if hexstr=='0x74': hexbyte=b"\x74"
    if hexstr=='0x75': hexbyte=b"\x75"
    if hexstr=='0x76': hexbyte=b"\x76"
    if hexstr=='0x77': hexbyte=b"\x77"
    if hexstr=='0x78': hexbyte=b"\x78"
    if hexstr=='0x79': hexbyte=b"\x79"
    if hexstr=='0x7A': hexbyte=b"\x7A"
    if hexstr=='0x7B': hexbyte=b"\x7B"
    if hexstr=='0x7C': hexbyte=b"\x7C"
    if hexstr=='0x7D': hexbyte=b"\x7D"
    if hexstr=='0x7E': hexbyte=b"\x7E"
    if hexstr=='0x7F': hexbyte=b"\x7F"
    if hexstr=='0x80': hexbyte=b"\x80"
    if hexstr=='0x81': hexbyte=b"\x81"
    if hexstr=='0x82': hexbyte=b"\x82"
    if hexstr=='0x83': hexbyte=b"\x83"
    if hexstr=='0x84': hexbyte=b"\x84"
    if hexstr=='0x85': hexbyte=b"\x85"
    if hexstr=='0x86': hexbyte=b"\x86"
    if hexstr=='0x87': hexbyte=b"\x87"
    if hexstr=='0x88': hexbyte=b"\x88"
    if hexstr=='0x89': hexbyte=b"\x89"
    if hexstr=='0x8A': hexbyte=b"\x8A"
    if hexstr=='0x8B': hexbyte=b"\x8B"
    if hexstr=='0x8C': hexbyte=b"\x8C"
    if hexstr=='0x8D': hexbyte=b"\x8D"
    if hexstr=='0x8E': hexbyte=b"\x8E"
    if hexstr=='0x8F': hexbyte=b"\x8F"
    if hexstr=='0x90': hexbyte=b"\x90"
    if hexstr=='0x91': hexbyte=b"\x91"
    if hexstr=='0x92': hexbyte=b"\x92"
    if hexstr=='0x93': hexbyte=b"\x93"
    if hexstr=='0x94': hexbyte=b"\x94"
    if hexstr=='0x95': hexbyte=b"\x95"
    if hexstr=='0x96': hexbyte=b"\x96"
    if hexstr=='0x97': hexbyte=b"\x97"
    if hexstr=='0x98': hexbyte=b"\x98"
    if hexstr=='0x99': hexbyte=b"\x99"
    if hexstr=='0x9A': hexbyte=b"\x9A"
    if hexstr=='0x9B': hexbyte=b"\x9B"
    if hexstr=='0x9C': hexbyte=b"\x9C"
    if hexstr=='0x9D': hexbyte=b"\x9D"
    if hexstr=='0x9E': hexbyte=b"\x9E"
    if hexstr=='0x9F': hexbyte=b"\x9F"
    if hexstr=='0xA0': hexbyte=b"\xA0"
    if hexstr=='0xA1': hexbyte=b"\xA1"
    if hexstr=='0xA2': hexbyte=b"\xA2"
    if hexstr=='0xA3': hexbyte=b"\xA3"
    if hexstr=='0xA4': hexbyte=b"\xA4"
    if hexstr=='0xA5': hexbyte=b"\xA5"
    if hexstr=='0xA6': hexbyte=b"\xA6"
    if hexstr=='0xA7': hexbyte=b"\xA7"
    if hexstr=='0xA8': hexbyte=b"\xA8"
    if hexstr=='0xA9': hexbyte=b"\xA9"
    if hexstr=='0xAA': hexbyte=b"\xAA"
    if hexstr=='0xAB': hexbyte=b"\xAB"
    if hexstr=='0xAC': hexbyte=b"\xAC"
    if hexstr=='0xAD': hexbyte=b"\xAD"
    if hexstr=='0xAE': hexbyte=b"\xAE"
    if hexstr=='0xAF': hexbyte=b"\xAF"
    if hexstr=='0xB0': hexbyte=b"\xB0"
    if hexstr=='0xB1': hexbyte=b"\xB1"
    if hexstr=='0xB2': hexbyte=b"\xB2"
    if hexstr=='0xB3': hexbyte=b"\xB3"
    if hexstr=='0xB4': hexbyte=b"\xB4"
    if hexstr=='0xB5': hexbyte=b"\xB5"
    if hexstr=='0xB6': hexbyte=b"\xB6"
    if hexstr=='0xB7': hexbyte=b"\xB7"
    if hexstr=='0xB8': hexbyte=b"\xB8"
    if hexstr=='0xB9': hexbyte=b"\xB9"
    if hexstr=='0xBA': hexbyte=b"\xBA"
    if hexstr=='0xBB': hexbyte=b"\xBB"
    if hexstr=='0xBC': hexbyte=b"\xBC"
    if hexstr=='0xBD': hexbyte=b"\xBD"
    if hexstr=='0xBE': hexbyte=b"\xBE"
    if hexstr=='0xBF': hexbyte=b"\xBF"
    if hexstr=='0xC0': hexbyte=b"\xC0"
    if hexstr=='0xC1': hexbyte=b"\xC1"
    if hexstr=='0xC2': hexbyte=b"\xC2"
    if hexstr=='0xC3': hexbyte=b"\xC3"
    if hexstr=='0xC4': hexbyte=b"\xC4"
    if hexstr=='0xC5': hexbyte=b"\xC5"
    if hexstr=='0xC6': hexbyte=b"\xC6"
    if hexstr=='0xC7': hexbyte=b"\xC7"
    if hexstr=='0xC8': hexbyte=b"\xC8"
    if hexstr=='0xC9': hexbyte=b"\xC9"
    if hexstr=='0xCA': hexbyte=b"\xCA"
    if hexstr=='0xCB': hexbyte=b"\xCB"
    if hexstr=='0xCC': hexbyte=b"\xCC"
    if hexstr=='0xCD': hexbyte=b"\xCD"
    if hexstr=='0xCE': hexbyte=b"\xCE"
    if hexstr=='0xCF': hexbyte=b"\xCF"
    if hexstr=='0xD0': hexbyte=b"\xD0"
    if hexstr=='0xD1': hexbyte=b"\xD1"
    if hexstr=='0xD2': hexbyte=b"\xD2"
    if hexstr=='0xD3': hexbyte=b"\xD3"
    if hexstr=='0xD4': hexbyte=b"\xD4"
    if hexstr=='0xD5': hexbyte=b"\xD5"
    if hexstr=='0xD6': hexbyte=b"\xD6"
    if hexstr=='0xD7': hexbyte=b"\xD7"
    if hexstr=='0xD8': hexbyte=b"\xD8"
    if hexstr=='0xD9': hexbyte=b"\xD9"
    if hexstr=='0xDA': hexbyte=b"\xDA"
    if hexstr=='0xDB': hexbyte=b"\xDB"
    if hexstr=='0xDC': hexbyte=b"\xDC"
    if hexstr=='0xDD': hexbyte=b"\xDD"
    if hexstr=='0xDE': hexbyte=b"\xDE"
    if hexstr=='0xDF': hexbyte=b"\xDF"
    if hexstr=='0xE0': hexbyte=b"\xE0"
    if hexstr=='0xE1': hexbyte=b"\xE1"
    if hexstr=='0xE2': hexbyte=b"\xE2"
    if hexstr=='0xE3': hexbyte=b"\xE3"
    if hexstr=='0xE4': hexbyte=b"\xE4"
    if hexstr=='0xE5': hexbyte=b"\xE5"
    if hexstr=='0xE6': hexbyte=b"\xE6"
    if hexstr=='0xE7': hexbyte=b"\xE7"
    if hexstr=='0xE8': hexbyte=b"\xE8"
    if hexstr=='0xE9': hexbyte=b"\xE9"
    if hexstr=='0xEA': hexbyte=b"\xEA"
    if hexstr=='0xEB': hexbyte=b"\xEB"
    if hexstr=='0xEC': hexbyte=b"\xEC"
    if hexstr=='0xED': hexbyte=b"\xED"
    if hexstr=='0xEE': hexbyte=b"\xEE"
    if hexstr=='0xEF': hexbyte=b"\xEF"
    if hexstr=='0xF0': hexbyte=b"\xF0"
    if hexstr=='0xF1': hexbyte=b"\xF1"
    if hexstr=='0xF2': hexbyte=b"\xF2"
    if hexstr=='0xF3': hexbyte=b"\xF3"
    if hexstr=='0xF4': hexbyte=b"\xF4"
    if hexstr=='0xF5': hexbyte=b"\xF5"
    if hexstr=='0xF6': hexbyte=b"\xF6"
    if hexstr=='0xF7': hexbyte=b"\xF7"
    if hexstr=='0xF8': hexbyte=b"\xF8"
    if hexstr=='0xF9': hexbyte=b"\xF9"
    if hexstr=='0xFA': hexbyte=b"\xFA"
    if hexstr=='0xFB': hexbyte=b"\xFB"
    if hexstr=='0xFC': hexbyte=b"\xFC"
    if hexstr=='0xFD': hexbyte=b"\xFD"
    if hexstr=='0xFE': hexbyte=b"\xFE"
    if hexstr=='0xFF': hexbyte=b"\xFF"
    return hexbyte

# hexstr number to byte converter.
def hexstr2b(hexstr):
    newbyte = ''
    if hexstr =='00': newbyte=b"\x00"
    if hexstr =='01': newbyte=b"\x01"
    if hexstr =='02': newbyte=b"\x02"
    if hexstr =='03': newbyte=b"\x03"
    if hexstr =='04': newbyte=b"\x04"
    if hexstr =='05': newbyte=b"\x05"
    if hexstr =='06': newbyte=b"\x06"
    if hexstr =='07': newbyte=b"\x07"
    if hexstr =='08': newbyte=b"\x08"
    if hexstr =='09': newbyte=b"\x09"
    if hexstr =='0A': newbyte=b"\x0A"
    if hexstr =='0B': newbyte=b"\x0B"
    if hexstr =='0C': newbyte=b"\x0C"
    if hexstr =='0D': newbyte=b"\x0D"
    if hexstr =='0E': newbyte=b"\x0E"
    if hexstr =='0F': newbyte=b"\x0F"
    if hexstr =='10': newbyte=b"\x10"
    if hexstr =='11': newbyte=b"\x11"
    if hexstr =='12': newbyte=b"\x12"
    if hexstr =='13': newbyte=b"\x13"
    if hexstr =='14': newbyte=b"\x14"
    if hexstr =='15': newbyte=b"\x15"
    if hexstr =='16': newbyte=b"\x16"
    if hexstr =='17': newbyte=b"\x17"
    if hexstr =='18': newbyte=b"\x18"
    if hexstr =='19': newbyte=b"\x19"
    if hexstr =='1A': newbyte=b"\x1A"
    if hexstr =='1B': newbyte=b"\x1B"
    if hexstr =='1C': newbyte=b"\x1C"
    if hexstr =='1D': newbyte=b"\x1D"
    if hexstr =='1E': newbyte=b"\x1E"
    if hexstr =='1F': newbyte=b"\x1F"
    if hexstr =='20': newbyte=b"\x20"
    if hexstr =='21': newbyte=b"\x21"
    if hexstr =='22': newbyte=b"\x22"
    if hexstr =='23': newbyte=b"\x23"
    if hexstr =='24': newbyte=b"\x24"
    if hexstr =='25': newbyte=b"\x25"
    if hexstr =='26': newbyte=b"\x26"
    if hexstr =='27': newbyte=b"\x27"
    if hexstr =='28': newbyte=b"\x28"
    if hexstr =='29': newbyte=b"\x29"
    if hexstr =='2A': newbyte=b"\x2A"
    if hexstr =='2B': newbyte=b"\x2B"
    if hexstr =='2C': newbyte=b"\x2C"
    if hexstr =='2D': newbyte=b"\x2D"
    if hexstr =='2E': newbyte=b"\x2E"
    if hexstr =='2F': newbyte=b"\x2F"
    if hexstr =='30': newbyte=b"\x30"
    if hexstr =='31': newbyte=b"\x31"
    if hexstr =='32': newbyte=b"\x32"
    if hexstr =='33': newbyte=b"\x33"
    if hexstr =='34': newbyte=b"\x34"
    if hexstr =='35': newbyte=b"\x35"
    if hexstr =='36': newbyte=b"\x36"
    if hexstr =='37': newbyte=b"\x37"
    if hexstr =='38': newbyte=b"\x38"
    if hexstr =='39': newbyte=b"\x39"
    if hexstr =='3A': newbyte=b"\x3A"
    if hexstr =='3B': newbyte=b"\x3B"
    if hexstr =='3C': newbyte=b"\x3C"
    if hexstr =='3D': newbyte=b"\x3D"
    if hexstr =='3E': newbyte=b"\x3E"
    if hexstr =='3F': newbyte=b"\x3F"
    if hexstr =='40': newbyte=b"\x40"
    if hexstr =='41': newbyte=b"\x41"
    if hexstr =='42': newbyte=b"\x42"
    if hexstr =='43': newbyte=b"\x43"
    if hexstr =='44': newbyte=b"\x44"
    if hexstr =='45': newbyte=b"\x45"
    if hexstr =='46': newbyte=b"\x46"
    if hexstr =='47': newbyte=b"\x47"
    if hexstr =='48': newbyte=b"\x48"
    if hexstr =='49': newbyte=b"\x49"
    if hexstr =='4A': newbyte=b"\x4A"
    if hexstr =='4B': newbyte=b"\x4B"
    if hexstr =='4C': newbyte=b"\x4C"
    if hexstr =='4D': newbyte=b"\x4D"
    if hexstr =='4E': newbyte=b"\x4E"
    if hexstr =='4F': newbyte=b"\x4F"
    if hexstr =='50': newbyte=b"\x50"
    if hexstr =='51': newbyte=b"\x51"
    if hexstr =='52': newbyte=b"\x52"
    if hexstr =='53': newbyte=b"\x53"
    if hexstr =='54': newbyte=b"\x54"
    if hexstr =='55': newbyte=b"\x55"
    if hexstr =='56': newbyte=b"\x56"
    if hexstr =='57': newbyte=b"\x57"
    if hexstr =='58': newbyte=b"\x58"
    if hexstr =='59': newbyte=b"\x59"
    if hexstr =='5A': newbyte=b"\x5A"
    if hexstr =='5B': newbyte=b"\x5B"
    if hexstr =='5C': newbyte=b"\x5C"
    if hexstr =='5D': newbyte=b"\x5D"
    if hexstr =='5E': newbyte=b"\x5E"
    if hexstr =='5F': newbyte=b"\x5F"
    if hexstr =='60': newbyte=b"\x60"
    if hexstr =='61': newbyte=b"\x61"
    if hexstr =='62': newbyte=b"\x62"
    if hexstr =='63': newbyte=b"\x63"
    if hexstr =='64': newbyte=b"\x64"
    if hexstr =='65': newbyte=b"\x65"
    if hexstr =='66': newbyte=b"\x66"
    if hexstr =='67': newbyte=b"\x67"
    if hexstr =='68': newbyte=b"\x68"
    if hexstr =='69': newbyte=b"\x69"
    if hexstr =='6A': newbyte=b"\x6A"
    if hexstr =='6B': newbyte=b"\x6B"
    if hexstr =='6C': newbyte=b"\x6C"
    if hexstr =='6D': newbyte=b"\x6D"
    if hexstr =='6E': newbyte=b"\x6E"
    if hexstr =='6F': newbyte=b"\x6F"
    if hexstr =='70': newbyte=b"\x70"
    if hexstr =='71': newbyte=b"\x71"
    if hexstr =='72': newbyte=b"\x72"
    if hexstr =='73': newbyte=b"\x73"
    if hexstr =='74': newbyte=b"\x74"
    if hexstr =='75': newbyte=b"\x75"
    if hexstr =='76': newbyte=b"\x76"
    if hexstr =='77': newbyte=b"\x77"
    if hexstr =='78': newbyte=b"\x78"
    if hexstr =='79': newbyte=b"\x79"
    if hexstr =='7A': newbyte=b"\x7A"
    if hexstr =='7B': newbyte=b"\x7B"
    if hexstr =='7C': newbyte=b"\x7C"
    if hexstr =='7D': newbyte=b"\x7D"
    if hexstr =='7E': newbyte=b"\x7E"
    if hexstr =='7F': newbyte=b"\x7F"
    if hexstr =='80': newbyte=b"\x80"
    if hexstr =='81': newbyte=b"\x81"
    if hexstr =='82': newbyte=b"\x82"
    if hexstr =='83': newbyte=b"\x83"
    if hexstr =='84': newbyte=b"\x84"
    if hexstr =='85': newbyte=b"\x85"
    if hexstr =='86': newbyte=b"\x86"
    if hexstr =='87': newbyte=b"\x87"
    if hexstr =='88': newbyte=b"\x88"
    if hexstr =='89': newbyte=b"\x89"
    if hexstr =='8A': newbyte=b"\x8A"
    if hexstr =='8B': newbyte=b"\x8B"
    if hexstr =='8C': newbyte=b"\x8C"
    if hexstr =='8D': newbyte=b"\x8D"
    if hexstr =='8E': newbyte=b"\x8E"
    if hexstr =='8F': newbyte=b"\x8F"
    if hexstr =='90': newbyte=b"\x90"
    if hexstr =='91': newbyte=b"\x91"
    if hexstr =='92': newbyte=b"\x92"
    if hexstr =='93': newbyte=b"\x93"
    if hexstr =='94': newbyte=b"\x94"
    if hexstr =='95': newbyte=b"\x95"
    if hexstr =='96': newbyte=b"\x96"
    if hexstr =='97': newbyte=b"\x97"
    if hexstr =='98': newbyte=b"\x98"
    if hexstr =='99': newbyte=b"\x99"
    if hexstr =='9A': newbyte=b"\x9A"
    if hexstr =='9B': newbyte=b"\x9B"
    if hexstr =='9C': newbyte=b"\x9C"
    if hexstr =='9D': newbyte=b"\x9D"
    if hexstr =='9E': newbyte=b"\x9E"
    if hexstr =='9F': newbyte=b"\x9F"
    if hexstr =='A0': newbyte=b"\xA0"
    if hexstr =='A1': newbyte=b"\xA1"
    if hexstr =='A2': newbyte=b"\xA2"
    if hexstr =='A3': newbyte=b"\xA3"
    if hexstr =='A4': newbyte=b"\xA4"
    if hexstr =='A5': newbyte=b"\xA5"
    if hexstr =='A6': newbyte=b"\xA6"
    if hexstr =='A7': newbyte=b"\xA7"
    if hexstr =='A8': newbyte=b"\xA8"
    if hexstr =='A9': newbyte=b"\xA9"
    if hexstr =='AA': newbyte=b"\xAA"
    if hexstr =='AB': newbyte=b"\xAB"
    if hexstr =='AC': newbyte=b"\xAC"
    if hexstr =='AD': newbyte=b"\xAD"
    if hexstr =='AE': newbyte=b"\xAE"
    if hexstr =='AF': newbyte=b"\xAF"
    if hexstr =='B0': newbyte=b"\xB0"
    if hexstr =='B1': newbyte=b"\xB1"
    if hexstr =='B2': newbyte=b"\xB2"
    if hexstr =='B3': newbyte=b"\xB3"
    if hexstr =='B4': newbyte=b"\xB4"
    if hexstr =='B5': newbyte=b"\xB5"
    if hexstr =='B6': newbyte=b"\xB6"
    if hexstr =='B7': newbyte=b"\xB7"
    if hexstr =='B8': newbyte=b"\xB8"
    if hexstr =='B9': newbyte=b"\xB9"
    if hexstr =='BA': newbyte=b"\xBA"
    if hexstr =='BB': newbyte=b"\xBB"
    if hexstr =='BC': newbyte=b"\xBC"
    if hexstr =='BD': newbyte=b"\xBD"
    if hexstr =='BE': newbyte=b"\xBE"
    if hexstr =='BF': newbyte=b"\xBF"
    if hexstr =='C0': newbyte=b"\xC0"
    if hexstr =='C1': newbyte=b"\xC1"
    if hexstr =='C2': newbyte=b"\xC2"
    if hexstr =='C3': newbyte=b"\xC3"
    if hexstr =='C4': newbyte=b"\xC4"
    if hexstr =='C5': newbyte=b"\xC5"
    if hexstr =='C6': newbyte=b"\xC6"
    if hexstr =='C7': newbyte=b"\xC7"
    if hexstr =='C8': newbyte=b"\xC8"
    if hexstr =='C9': newbyte=b"\xC9"
    if hexstr =='CA': newbyte=b"\xCA"
    if hexstr =='CB': newbyte=b"\xCB"
    if hexstr =='CC': newbyte=b"\xCC"
    if hexstr =='CD': newbyte=b"\xCD"
    if hexstr =='CE': newbyte=b"\xCE"
    if hexstr =='CF': newbyte=b"\xCF"
    if hexstr =='D0': newbyte=b"\xD0"
    if hexstr =='D1': newbyte=b"\xD1"
    if hexstr =='D2': newbyte=b"\xD2"
    if hexstr =='D3': newbyte=b"\xD3"
    if hexstr =='D4': newbyte=b"\xD4"
    if hexstr =='D5': newbyte=b"\xD5"
    if hexstr =='D6': newbyte=b"\xD6"
    if hexstr =='D7': newbyte=b"\xD7"
    if hexstr =='D8': newbyte=b"\xD8"
    if hexstr =='D9': newbyte=b"\xD9"
    if hexstr =='DA': newbyte=b"\xDA"
    if hexstr =='DB': newbyte=b"\xDB"
    if hexstr =='DC': newbyte=b"\xDC"
    if hexstr =='DD': newbyte=b"\xDD"
    if hexstr =='DE': newbyte=b"\xDE"
    if hexstr =='DF': newbyte=b"\xDF"
    if hexstr =='E0': newbyte=b"\xE0"
    if hexstr =='E1': newbyte=b"\xE1"
    if hexstr =='E2': newbyte=b"\xE2"
    if hexstr =='E3': newbyte=b"\xE3"
    if hexstr =='E4': newbyte=b"\xE4"
    if hexstr =='E5': newbyte=b"\xE5"
    if hexstr =='E6': newbyte=b"\xE6"
    if hexstr =='E7': newbyte=b"\xE7"
    if hexstr =='E8': newbyte=b"\xE8"
    if hexstr =='E9': newbyte=b"\xE9"
    if hexstr =='EA': newbyte=b"\xEA"
    if hexstr =='EB': newbyte=b"\xEB"
    if hexstr =='EC': newbyte=b"\xEC"
    if hexstr =='ED': newbyte=b"\xED"
    if hexstr =='EE': newbyte=b"\xEE"
    if hexstr =='EF': newbyte=b"\xEF"
    if hexstr =='F0': newbyte=b"\xF0"
    if hexstr =='F1': newbyte=b"\xF1"
    if hexstr =='F2': newbyte=b"\xF2"
    if hexstr =='F3': newbyte=b"\xF3"
    if hexstr =='F4': newbyte=b"\xF4"
    if hexstr =='F5': newbyte=b"\xF5"
    if hexstr =='F6': newbyte=b"\xF6"
    if hexstr =='F7': newbyte=b"\xF7"
    if hexstr =='F8': newbyte=b"\xF8"
    if hexstr =='F9': newbyte=b"\xF9"
    if hexstr =='FA': newbyte=b"\xFA"
    if hexstr =='FB': newbyte=b"\xFB"
    if hexstr =='FC': newbyte=b"\xFC"
    if hexstr =='FD': newbyte=b"\xFD"
    if hexstr =='FE': newbyte=b"\xFE"
    if hexstr =='FF': newbyte=b"\xFF"
    return newbyte


# Hex string to hex string converter.
def hexstr2hexstr(hexstr):
    hexbyte = 0
    if hexstr=='0x00': hexbyte='\x00'
    if hexstr=='0x01': hexbyte='\x01'
    if hexstr=='0x02': hexbyte='\x02'
    if hexstr=='0x03': hexbyte='\x03'
    if hexstr=='0x04': hexbyte='\x04'
    if hexstr=='0x05': hexbyte='\x05'
    if hexstr=='0x06': hexbyte='\x06'
    if hexstr=='0x07': hexbyte='\x07'
    if hexstr=='0x08': hexbyte='\x08'
    if hexstr=='0x09': hexbyte='\x09'
    if hexstr=='0x0A': hexbyte='\x0A'
    if hexstr=='0x0B': hexbyte='\x0B'
    if hexstr=='0x0C': hexbyte='\x0C'
    if hexstr=='0x0D': hexbyte='\x0D'
    if hexstr=='0x0E': hexbyte='\x0E'
    if hexstr=='0x0F': hexbyte='\x0F'
    if hexstr=='0x10': hexbyte='\x10'
    if hexstr=='0x11': hexbyte='\x11'
    if hexstr=='0x12': hexbyte='\x12'
    if hexstr=='0x13': hexbyte='\x13'
    if hexstr=='0x14': hexbyte='\x14'
    if hexstr=='0x15': hexbyte='\x15'
    if hexstr=='0x16': hexbyte='\x16'
    if hexstr=='0x17': hexbyte='\x17'
    if hexstr=='0x18': hexbyte='\x18'
    if hexstr=='0x19': hexbyte='\x19'
    if hexstr=='0x1A': hexbyte='\x1A'
    if hexstr=='0x1B': hexbyte='\x1B'
    if hexstr=='0x1C': hexbyte='\x1C'
    if hexstr=='0x1D': hexbyte='\x1D'
    if hexstr=='0x1E': hexbyte='\x1E'
    if hexstr=='0x1F': hexbyte='\x1F'
    if hexstr=='0x20': hexbyte='\x20'
    if hexstr=='0x21': hexbyte='\x21'
    if hexstr=='0x22': hexbyte='\x22'
    if hexstr=='0x23': hexbyte='\x23'
    if hexstr=='0x24': hexbyte='\x24'
    if hexstr=='0x25': hexbyte='\x25'
    if hexstr=='0x26': hexbyte='\x26'
    if hexstr=='0x27': hexbyte='\x27'
    if hexstr=='0x28': hexbyte='\x28'
    if hexstr=='0x29': hexbyte='\x29'
    if hexstr=='0x2A': hexbyte='\x2A'
    if hexstr=='0x2B': hexbyte='\x2B'
    if hexstr=='0x2C': hexbyte='\x2C'
    if hexstr=='0x2D': hexbyte='\x2D'
    if hexstr=='0x2E': hexbyte='\x2E'
    if hexstr=='0x2F': hexbyte='\x2F'
    if hexstr=='0x30': hexbyte='\x30'
    if hexstr=='0x31': hexbyte='\x31'
    if hexstr=='0x32': hexbyte='\x32'
    if hexstr=='0x33': hexbyte='\x33'
    if hexstr=='0x34': hexbyte='\x34'
    if hexstr=='0x35': hexbyte='\x35'
    if hexstr=='0x36': hexbyte='\x36'
    if hexstr=='0x37': hexbyte='\x37'
    if hexstr=='0x38': hexbyte='\x38'
    if hexstr=='0x39': hexbyte='\x39'
    if hexstr=='0x3A': hexbyte='\x3A'
    if hexstr=='0x3B': hexbyte='\x3B'
    if hexstr=='0x3C': hexbyte='\x3C'
    if hexstr=='0x3D': hexbyte='\x3D'
    if hexstr=='0x3E': hexbyte='\x3E'
    if hexstr=='0x3F': hexbyte='\x3F'
    if hexstr=='0x40': hexbyte='\x40'
    if hexstr=='0x41': hexbyte='\x41'
    if hexstr=='0x42': hexbyte='\x42'
    if hexstr=='0x43': hexbyte='\x43'
    if hexstr=='0x44': hexbyte='\x44'
    if hexstr=='0x45': hexbyte='\x45'
    if hexstr=='0x46': hexbyte='\x46'
    if hexstr=='0x47': hexbyte='\x47'
    if hexstr=='0x48': hexbyte='\x48'
    if hexstr=='0x49': hexbyte='\x49'
    if hexstr=='0x4A': hexbyte='\x4A'
    if hexstr=='0x4B': hexbyte='\x4B'
    if hexstr=='0x4C': hexbyte='\x4C'
    if hexstr=='0x4D': hexbyte='\x4D'
    if hexstr=='0x4E': hexbyte='\x4E'
    if hexstr=='0x4F': hexbyte='\x4F'
    if hexstr=='0x50': hexbyte='\x50'
    if hexstr=='0x51': hexbyte='\x51'
    if hexstr=='0x52': hexbyte='\x52'
    if hexstr=='0x53': hexbyte='\x53'
    if hexstr=='0x54': hexbyte='\x54'
    if hexstr=='0x55': hexbyte='\x55'
    if hexstr=='0x56': hexbyte='\x56'
    if hexstr=='0x57': hexbyte='\x57'
    if hexstr=='0x58': hexbyte='\x58'
    if hexstr=='0x59': hexbyte='\x59'
    if hexstr=='0x5A': hexbyte='\x5A'
    if hexstr=='0x5B': hexbyte='\x5B'
    if hexstr=='0x5C': hexbyte='\x5C'
    if hexstr=='0x5D': hexbyte='\x5D'
    if hexstr=='0x5E': hexbyte='\x5E'
    if hexstr=='0x5F': hexbyte='\x5F'
    if hexstr=='0x60': hexbyte='\x60'
    if hexstr=='0x61': hexbyte='\x61'
    if hexstr=='0x62': hexbyte='\x62'
    if hexstr=='0x63': hexbyte='\x63'
    if hexstr=='0x64': hexbyte='\x64'
    if hexstr=='0x65': hexbyte='\x65'
    if hexstr=='0x66': hexbyte='\x66'
    if hexstr=='0x67': hexbyte='\x67'
    if hexstr=='0x68': hexbyte='\x68'
    if hexstr=='0x69': hexbyte='\x69'
    if hexstr=='0x6A': hexbyte='\x6A'
    if hexstr=='0x6B': hexbyte='\x6B'
    if hexstr=='0x6C': hexbyte='\x6C'
    if hexstr=='0x6D': hexbyte='\x6D'
    if hexstr=='0x6E': hexbyte='\x6E'
    if hexstr=='0x6F': hexbyte='\x6F'
    if hexstr=='0x70': hexbyte='\x70'
    if hexstr=='0x71': hexbyte='\x71'
    if hexstr=='0x72': hexbyte='\x72'
    if hexstr=='0x73': hexbyte='\x73'
    if hexstr=='0x74': hexbyte='\x74'
    if hexstr=='0x75': hexbyte='\x75'
    if hexstr=='0x76': hexbyte='\x76'
    if hexstr=='0x77': hexbyte='\x77'
    if hexstr=='0x78': hexbyte='\x78'
    if hexstr=='0x79': hexbyte='\x79'
    if hexstr=='0x7A': hexbyte='\x7A'
    if hexstr=='0x7B': hexbyte='\x7B'
    if hexstr=='0x7C': hexbyte='\x7C'
    if hexstr=='0x7D': hexbyte='\x7D'
    if hexstr=='0x7E': hexbyte='\x7E'
    if hexstr=='0x7F': hexbyte='\x7F'
    if hexstr=='0x80': hexbyte='\x80'
    if hexstr=='0x81': hexbyte='\x81'
    if hexstr=='0x82': hexbyte='\x82'
    if hexstr=='0x83': hexbyte='\x83'
    if hexstr=='0x84': hexbyte='\x84'
    if hexstr=='0x85': hexbyte='\x85'
    if hexstr=='0x86': hexbyte='\x86'
    if hexstr=='0x87': hexbyte='\x87'
    if hexstr=='0x88': hexbyte='\x88'
    if hexstr=='0x89': hexbyte='\x89'
    if hexstr=='0x8A': hexbyte='\x8A'
    if hexstr=='0x8B': hexbyte='\x8B'
    if hexstr=='0x8C': hexbyte='\x8C'
    if hexstr=='0x8D': hexbyte='\x8D'
    if hexstr=='0x8E': hexbyte='\x8E'
    if hexstr=='0x8F': hexbyte='\x8F'
    if hexstr=='0x90': hexbyte='\x90'
    if hexstr=='0x91': hexbyte='\x91'
    if hexstr=='0x92': hexbyte='\x92'
    if hexstr=='0x93': hexbyte='\x93'
    if hexstr=='0x94': hexbyte='\x94'
    if hexstr=='0x95': hexbyte='\x95'
    if hexstr=='0x96': hexbyte='\x96'
    if hexstr=='0x97': hexbyte='\x97'
    if hexstr=='0x98': hexbyte='\x98'
    if hexstr=='0x99': hexbyte='\x99'
    if hexstr=='0x9A': hexbyte='\x9A'
    if hexstr=='0x9B': hexbyte='\x9B'
    if hexstr=='0x9C': hexbyte='\x9C'
    if hexstr=='0x9D': hexbyte='\x9D'
    if hexstr=='0x9E': hexbyte='\x9E'
    if hexstr=='0x9F': hexbyte='\x9F'
    if hexstr=='0xA0': hexbyte='\xA0'
    if hexstr=='0xA1': hexbyte='\xA1'
    if hexstr=='0xA2': hexbyte='\xA2'
    if hexstr=='0xA3': hexbyte='\xA3'
    if hexstr=='0xA4': hexbyte='\xA4'
    if hexstr=='0xA5': hexbyte='\xA5'
    if hexstr=='0xA6': hexbyte='\xA6'
    if hexstr=='0xA7': hexbyte='\xA7'
    if hexstr=='0xA8': hexbyte='\xA8'
    if hexstr=='0xA9': hexbyte='\xA9'
    if hexstr=='0xAA': hexbyte='\xAA'
    if hexstr=='0xAB': hexbyte='\xAB'
    if hexstr=='0xAC': hexbyte='\xAC'
    if hexstr=='0xAD': hexbyte='\xAD'
    if hexstr=='0xAE': hexbyte='\xAE'
    if hexstr=='0xAF': hexbyte='\xAF'
    if hexstr=='0xB0': hexbyte='\xB0'
    if hexstr=='0xB1': hexbyte='\xB1'
    if hexstr=='0xB2': hexbyte='\xB2'
    if hexstr=='0xB3': hexbyte='\xB3'
    if hexstr=='0xB4': hexbyte='\xB4'
    if hexstr=='0xB5': hexbyte='\xB5'
    if hexstr=='0xB6': hexbyte='\xB6'
    if hexstr=='0xB7': hexbyte='\xB7'
    if hexstr=='0xB8': hexbyte='\xB8'
    if hexstr=='0xB9': hexbyte='\xB9'
    if hexstr=='0xBA': hexbyte='\xBA'
    if hexstr=='0xBB': hexbyte='\xBB'
    if hexstr=='0xBC': hexbyte='\xBC'
    if hexstr=='0xBD': hexbyte='\xBD'
    if hexstr=='0xBE': hexbyte='\xBE'
    if hexstr=='0xBF': hexbyte='\xBF'
    if hexstr=='0xC0': hexbyte='\xC0'
    if hexstr=='0xC1': hexbyte='\xC1'
    if hexstr=='0xC2': hexbyte='\xC2'
    if hexstr=='0xC3': hexbyte='\xC3'
    if hexstr=='0xC4': hexbyte='\xC4'
    if hexstr=='0xC5': hexbyte='\xC5'
    if hexstr=='0xC6': hexbyte='\xC6'
    if hexstr=='0xC7': hexbyte='\xC7'
    if hexstr=='0xC8': hexbyte='\xC8'
    if hexstr=='0xC9': hexbyte='\xC9'
    if hexstr=='0xCA': hexbyte='\xCA'
    if hexstr=='0xCB': hexbyte='\xCB'
    if hexstr=='0xCC': hexbyte='\xCC'
    if hexstr=='0xCD': hexbyte='\xCD'
    if hexstr=='0xCE': hexbyte='\xCE'
    if hexstr=='0xCF': hexbyte='\xCF'
    if hexstr=='0xD0': hexbyte='\xD0'
    if hexstr=='0xD1': hexbyte='\xD1'
    if hexstr=='0xD2': hexbyte='\xD2'
    if hexstr=='0xD3': hexbyte='\xD3'
    if hexstr=='0xD4': hexbyte='\xD4'
    if hexstr=='0xD5': hexbyte='\xD5'
    if hexstr=='0xD6': hexbyte='\xD6'
    if hexstr=='0xD7': hexbyte='\xD7'
    if hexstr=='0xD8': hexbyte='\xD8'
    if hexstr=='0xD9': hexbyte='\xD9'
    if hexstr=='0xDA': hexbyte='\xDA'
    if hexstr=='0xDB': hexbyte='\xDB'
    if hexstr=='0xDC': hexbyte='\xDC'
    if hexstr=='0xDD': hexbyte='\xDD'
    if hexstr=='0xDE': hexbyte='\xDE'
    if hexstr=='0xDF': hexbyte='\xDF'
    if hexstr=='0xE0': hexbyte='\xE0'
    if hexstr=='0xE1': hexbyte='\xE1'
    if hexstr=='0xE2': hexbyte='\xE2'
    if hexstr=='0xE3': hexbyte='\xE3'
    if hexstr=='0xE4': hexbyte='\xE4'
    if hexstr=='0xE5': hexbyte='\xE5'
    if hexstr=='0xE6': hexbyte='\xE6'
    if hexstr=='0xE7': hexbyte='\xE7'
    if hexstr=='0xE8': hexbyte='\xE8'
    if hexstr=='0xE9': hexbyte='\xE9'
    if hexstr=='0xEA': hexbyte='\xEA'
    if hexstr=='0xEB': hexbyte='\xEB'
    if hexstr=='0xEC': hexbyte='\xEC'
    if hexstr=='0xED': hexbyte='\xED'
    if hexstr=='0xEE': hexbyte='\xEE'
    if hexstr=='0xEF': hexbyte='\xEF'
    if hexstr=='0xF0': hexbyte='\xF0'
    if hexstr=='0xF1': hexbyte='\xF1'
    if hexstr=='0xF2': hexbyte='\xF2'
    if hexstr=='0xF3': hexbyte='\xF3'
    if hexstr=='0xF4': hexbyte='\xF4'
    if hexstr=='0xF5': hexbyte='\xF5'
    if hexstr=='0xF6': hexbyte='\xF6'
    if hexstr=='0xF7': hexbyte='\xF7'
    if hexstr=='0xF8': hexbyte='\xF8'
    if hexstr=='0xF9': hexbyte='\xF9'
    if hexstr=='0xFA': hexbyte='\xFA'
    if hexstr=='0xFB': hexbyte='\xFB'
    if hexstr=='0xFC': hexbyte='\xFC'
    if hexstr=='0xFD': hexbyte='\xFD'
    if hexstr=='0xFE': hexbyte='\xFE'
    if hexstr=='0xFF': hexbyte='\xFF'
    return hexbyte

# End of d2b() function...
# Enjoy finding simple solutions to often very difficult problems... ;o)
## end of http://code.activestate.com/recipes/578025/ }}}
