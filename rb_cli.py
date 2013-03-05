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

import cmd
import serial
import shlex
import time 
    
from threading import Thread
from multiprocessing import Process, Queue
from support import *
from com_handler import comHandler

# Messages defines
INTRO = '''----------------------------------------
Radio Block commander\r\nVersion 1.0
Enter "help" for available commands
----------------------------------------'''

ctrlQueue = Queue()
respQueue = Queue()

DEBUG = 0

def command(com_open_required=True):
    """a decorator for handling authentication and exceptions"""
    def decorate(f):
        def wrapper(self, args):
            if com_open_required and not(self.com_port_active):
                self.stdout.write("Please open com port before entering commands\n")
                return
            try:
                return f(self, *args)
            except:
                print "Please check command usage"

        wrapper.__doc__ = f.__doc__
        return wrapper
    return decorate


#-------------------------------------------------------------------------
# Console Class
#-------------------------------------------------------------------------
class RBTerm(cmd.Cmd):
    def __init__(self,ctrlq,respq):
        self.prompt = ""
        self.doc_header = "Radio Block available commands (type help <command>):"
        self.ctrlQ = ctrlq
        self.respQ = respq
        self.com_port_active = False
        cmd.Cmd.__init__(self)

        self.ComHandler = comHandler(ctrlQueue,respQueue)
        self.ComHandler.start()

        #Wait for comport information
        while respq.empty():
            pass
        self.portinfo = respq.get()['ports']

    # ---------------------------------------------------------------------------
    # COM PORT COMMANDS
    # ---------------------------------------------------------------------------
    @command(com_open_required=False)
    def do_open_port (self, comport, databits=8, parity='N', stopbits=1, baudrate=115200):
        if comport in self.portinfo:
            self.ctrlQ.put(['open',[comport,databits,parity,stopbits,baudrate]])
            self.com_port_active = True

        else:
            self.help_open_port()
        return

    @command()            
    def do_close_port (self):
        self.ctrlQ.put(['close',[]])


    # ---------------------------------------------------------------------------
    # LENGTH 1  COMMANDS - Tx commands with no parameters 
    # ---------------------------------------------------------------------------
	
    @command()
    def do_test(self):
        frame = self.ComHandler.sendCommand("test_request",[])
        
    @command()
    def do_reset(self):
        frame = self.ComHandler.sendCommand("reset_request",[])

    @command()
    def do_get_address(self):
        frame = self.ComHandler.sendCommand("get_address_request",[])

    @command()
    def do_get_panid(self): 
        frame = self.ComHandler.sendCommand("get_panid_request",[])

    @command()
    def do_get_channel(self):   
        frame = self.ComHandler.sendCommand("get_channel_request",[])

    @command()
    def do_get_receiver_state(self):
        frame = self.ComHandler.sendCommand("get_receiver_state_request",[])

    @command()
    def do_get_transmit_power(self):
        frame = self.ComHandler.sendCommand("get_transmit_power_request",[])

    @command()
    def do_get_ack_state(self):
        frame = self.ComHandler.sendCommand("get_ack_state_request",[])

    # ---------------------------------------------------------------------------
    # LENGTH 1  COMMANDS - Tx commands with no parameters - Help Functions
    # ---------------------------------------------------------------------------
    def help_test (self):
        print 'This command is used to check the communication channel and performs no'
        print 'other actions.'
        print 'A Test Response frame is sent back from the module as the result of '
        print 'execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> test_request'
        

    def help_open_port (self):
        print 'This command opens selected port to start communication with the module.\n'
        print '\tParameters: comport and baudrate'
        print '\tUsage: RB Commander> open_port COM1 115200'
        print '\tAvailable ports are:'
        print '\t','  '.join(self.portinfo)
        
                
    def help_reset(self):
        print 'This command is used to reset the board\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> reset'


    def help_get_address(self):
        print 'This command is used to request the module\'s address'
        print 'A Get Address Response frame is sent back from the module as the'
        print 'result of execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> get_address'


    def help_get_panid(self): 
        print 'This command is used to request the module\'s PANID'
        print 'A Get PANID Response frame is sent back from the module as the'
        print 'result of execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> get_panid'


    def help_get_channel(self):   
        print 'This command is used to request the module\'s channel'
        print 'A Get Channel Response frame is sent back from the module as the'
        print 'result of execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> get_channel'


    def help_get_receiver_state(self):
        print 'This command is used to request the module\'s receiver state'
        print 'A Get Reveiver State Response frame is sent back from the module'
        print 'as the result of execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> get_receiver_state'


    def help_get_transmit_power(self):
        print 'This command is used to request the module\'s transmit power'
        print 'A Get Transmit Power Response frame is sent back from the module'
        print 'as the result of execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> get_transmit_power'


    def help_get_ack_state(self):
        print 'This command is used to request the module\'s ack state'
        print 'A Get Ack State Response frame is sent back from the module as '
        print 'the result of execution of this command.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> get_ack_state'

                        
    # ---------------------------------------------------------------------------
    # LENGTH 2 and 3 COMMANDS
    # ---------------------------------------------------------------------------
    @command()
    def do_settings(self,saverestore):
        frame = self.ComHandler.sendCommand("settings_request",saverestore)

    @command()
    def do_set_channel(self,channel):
        frame = self.ComHandler.sendCommand("set_channel_request",channel)

    @command()
    def do_set_receiver_state(self,state):
        frame = self.ComHandler.sendCommand("set_receiver_state_request",channel)

    @command()
    def do_set_transmit_power(self,power):
        frame = self.ComHandler.sendCommand("set_transmit_power_request",power)

    @command()
    def do_set_ack_state(self,state):
        frame = self.ComHandler.sendCommand("set_ack_state_request",state)

    @command()
    def do_set_led_state(self,state):
        frame = self.ComHandler.sendCommand("set_led_state_request",state)

    @command()
    def do_set_address(self,address):
        frame = self.ComHandler.sendCommand("set_address_request",address)

    @command()
    def do_set_panid(self,address):
        frame = self.ComHandler.sendCommand("set_panid_request",address)

    @command()
    def do_sleep(self,timems):
        frame = self.ComHandler.sendCommand("sleep_request",timems)

    @command()
    def do_set_security_key(self,seckey):
        frame = self.ComHandler.sendCommand("set_security_key_request",seckey)

    @command()
    def do_set_uart_mode(self,databits,parity,stopbits,baudrate):
        print 'set_uart_mode',databits,parity,stopbits,baudrate
        frame = self.ComHandler.sendCommand("set_uart_mode_request",[databits,parity,stopbits,baudrate])

    @command()
    def do_send_data(self,destination, options, handle, data):
        print 'send_data',destination, options, handle, data
        frame = self.ComHandler.sendCommand("send_data_request",[destination, options, handle, data])

    # ---------------------------------------------------------------------------
    # LENGTH 2 and 3 COMMANDS - Help Functions
    # ---------------------------------------------------------------------------
    def help_settings(self):
        print 'This command is used save current settings or restore default settings to the module\n'
        print '\tParameters: save|restore'
        print '\tUsage: RB Commander> settings save'

    def help_set_channel(self):
        print 'This command is used to set the channel of the module\n'
        print '\tParameters: channel number (11..25)'
        print '\tUsage: RB Commander> set_channel 20'

    def help_set_receiver_state(self):
        print 'This command is used to set the receiver state of the module\n'
        print '\tParameters: on|off'
        print '\tUsage: RB Commander> set_receiver_state off'

    def help_set_transmit_power(self):
        print 'This command is used to set the transmit power of the module\n'
        print '\tParameters: 0 (+3 dBm) to 15 (-17 dBm)'
        print '\tUsage: RB Commander> set_transmit_power 5'

    def help_set_ack_state(self):
        print 'This command is used to enable or disable acknowledgments for incoming frames.\n'
        print '\tParameters: enable|disable'
        print '\tUsage: RB Commander> set_ack_state ena'

    def help_set_led_state(self):
        print 'This command is used to set the LED state.\n'
        print '\tParameters: off|on|toggle'
        print '\tUsage: RB Commander> set_led_state on'

    def help_set_address(self):
        print 'This command is used to set the address of the module.\n'
        print '\tParameters: address in decimal or hexadecimal format (preceded by "0x")'
        print '\tUsage: RB Commander> set_address 0x1234' 

    def help_set_panid(self):
        print 'This command is used to set the PAN Id of the module.\n'
        print '\tParameters: address in decimal or hexadecimal format (preceded by "0x")'
        print '\tUsage: RB Commander> set_address 65500' 

    def help_sleep (self):
        print 'This command is used to sleep the module.\n'
        print '\tParameters: time in ms in decimal or hexadecimal format \n\t(preceded by "0x")'
        print '\tUsage: RB Commander> sleep 3600000' 
    
    def help_set_security_key (self):
        print 'This command is used to set the security key.\n'
        print '\tParameters: key in hexadecimal format without spaces")'
        print '\tUsage: RB Commander> set_security_key aabb1234555599abccccdddd11113121' 
            
    def help_set_uart_mode (self):
        print "This command is used to set module's COM parameters.\n"
        print '\tParameters: bits, parity, stopbits and baudrate'
        print '\tbits: 5,6,7 or 8 bits per byte'
        print '\tparity: none even odd force_0 force_1'
        print '\tstopbits: 1 or 2'
        print '\tbaudrate: 0 for auto and baudrates from 50 to 400K. Check datasheet for valid baudrates'
        print '\tUsage: RB Commander> set_uart_mode 8 none 1 115200' 

    def help_send_data (self):
        print "This command is used to send data.\n"
        print '\tParameters: destination, options, handle and payload'
        print '\tdestination: address of target module in decimal or hexadecimal format'
        print '\toptions: none ack or security'
        print '\thandle: sequence number to associate with data confirmation command'
        print '\tpayload: data to send as a hexadecimal string (max 118 bytes)'
        print '\tUsage: RB Commander> send_data 0x1122 ack 15 aabbcc01' 

    def help_quit (self):
        print 'This command terminates the program.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> quit' 

    def do_quit(self, line):
        self.stdout.write('\n')
        self.stdout.write('Exiting Radio Block commander...\n')
        self.ctrlQ.put(['quit',[]])
        return True

    #def help_help (self):
    #    print 'This help :-)\n'

    def help_close_port (self):
        print 'This command closes the comport.\n'
        print '\tParameters: none'
        print '\tUsage: RB Commander> close_port' 
    
    def emptyline(self):
        pass

    def parseline(self, line):
        parts = shlex.split(line)
        if len(parts) == 0:
            return None, None, line
        else:
            return parts[0], parts[1:], line

    def do_help(self, arg):
        if arg:
            # XXX check arg syntax
            try:
                print '\n',arg[0]
                print '-'*len(arg[0])
                func = getattr(self, 'help_' + arg[0])
            except AttributeError:
                self.stdout.write("%s\n"%str(self.nohelp % (arg[0],)))
                return
            func()
        else:
            names = self.get_names()
            cmds_doc = []
            cmds_undoc = []
            help = {}
            for name in names:
                if name[:5] == 'help_':
                    help[name[5:]]=1
            names.sort()
            # There can be duplicates if routines overridden
            prevname = ''
            for name in names:
                if name[:3] == 'do_':
                    if name == prevname:
                        continue
                    prevname = name
                    cmd=name[3:]
                    if cmd in help:
                        cmds_doc.append(cmd)
                        del help[cmd]
                    elif getattr(self, name).__doc__:
                        cmds_doc.append(cmd)
                    else:
                        cmds_undoc.append(cmd)
            self.stdout.write("%s\n"%str(self.doc_leader))
            self.print_topics(self.doc_header,   cmds_doc,   15,80)
            self.print_topics(self.misc_header,  help.keys(),15,80)
            #self.print_topics(self.undoc_header, cmds_undoc, 15,80)

            
    def cmdloop(self, intro=None):
        """Repeatedly issue a prompt, accept input, parse an initial prefix
        off the received input, and dispatch to action methods, passing them
        the remainder of the line as argument.
        """
        self.preloop()
        if self.use_rawinput and self.completekey:
            try:
                import readline
                self.old_completer = readline.get_completer()
                readline.set_completer(self.complete)
                readline.parse_and_bind(self.completekey+": complete")
            except ImportError:
                pass
        try:
            if intro is not None:
                self.intro = intro
            if self.intro:
                self.stdout.write(str(self.intro)+"\n")
            stop = None
            while not stop:
                if self.cmdqueue:
                    line = self.cmdqueue.pop(0) 
                    self.stdout.write( "pop" )

                else:
                    if self.use_rawinput:
                        try:
                            line = raw_input(self.prompt)
                        except EOFError:
                            line = 'EOF'
                            #self.stdout.write("exception")
                    else:
                        if line != 'EOF':
                            self.stdout.write(self.prompt)
                            self.stdout.flush()
                        line = self.stdin.readline()
                        if not len(line):
                            line = 'EOF'
                        else:
                            line = line.rstrip('\r\n')
                #if line != 'EOF':
                line = self.precmd(line)
                stop = self.onecmd(line)
                stop = self.postcmd(stop, line)
                    #self.stdout.write(line)
                #time.sleep(3)

            self.postloop()

        finally:
            if self.use_rawinput and self.completekey:
                try:
                    import readline
                    readline.set_completer(self.old_completer)
                except ImportError:
                    pass


def initTerm (ctrlQueue,respQueue):
    term = RBTerm(ctrlQueue,respQueue)
    term.cmdloop(INTRO)


def main():
    
    threads = []
    t = Thread(target=initTerm, args=(ctrlQueue,respQueue))
    t.name = "User Command Loop"
    threads.append(t)
    t.start()

if __name__ == '__main__':
    main()

