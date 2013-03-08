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

import ui_RB
import sys
import time 

from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtGui import QColor, QTextCursor
from threading import Thread, Timer
from multiprocessing import Queue   
from support import *
from com_handler import comHandler

try:
    from PySide.QtCore import QString
except ImportError:
    # we are using Python3 so QString is not defined
    QString = type("")

INTERVAL = 1

class RB_MainWindow(QMainWindow, ui_RB.Ui_MainWindow):
    def __init__(self, parent=None):
        super(RB_MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.ctrlQueue = Queue()
        self.respQueue = Queue()
        
        # Create Com object
        self.ComHandler = comHandler(self.ctrlQueue,self.respQueue)
        self.ComHandler.start()

        #Wait for comport information
        while self.respQueue.empty():
            pass

        # Set up connects    
        QObject.connect(self.comboBoxCmd, SIGNAL("currentIndexChanged(QString)"), self.processComboBoxCmd)
        QObject.connect(self.comboBoxCmd, SIGNAL("activated(QString)"), self.processComboBoxCmd)
        QObject.connect(self.comboBoxCmdOption, SIGNAL("currentIndexChanged(QString)"), self.processComboBoxCmdOption)
        QObject.connect(self,SIGNAL("triggered()"),self.closeEvent)

        # update port information
        self.portinfo = self.respQueue.get()['ports']
        for item in self.portinfo:
            self.comboBoxCOMPort.addItem(item)
    
        # Create a list of typical BAUD rates and populate the Combo Box with those.
        self.baudarray = ['9600','14400','19200','28800','38400','57600','115200','230400','256000']
        self.comboBoxBAUDRate.addItems(self.baudarray)
        self.comboBoxBAUDRate.setCurrentIndex(6)
        self.stackedWidget.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.pushButtonTxFrame.setEnabled(False)
        self.txframe = []

        self.timer = QTimer()
        QObject.connect(self.timer, SIGNAL("timeout()"), self.checkRx)
        self.timer.start(INTERVAL)

        self.textEditRx.setTextColor(QColor("blue"))
        self.textEditTx.setTextColor(QColor("green"))
        self.textEditRfResponse.setTextColor(QColor("blue"))
        self.processComboBoxCmd(self.comboBoxCmd.currentText())
        self.progressBar.setValue(float(9*100)/127)
        self.lineEditUserPayload.setEnabled(False)

    def checkRx (self):
        while not(self.respQueue.empty()):
            rx = self.respQueue.get()

            if rx.keys()[0] == "rxframe":
                self.textEditRx.append(getTimeStamp() + getHexString(rx["rxframe"]))

            elif rx.keys()[0] == "rxframedesc":
                if "Timeout" in rx["rxframedesc"]:
                    self.textEditRfResponse.setTextColor(QColor("red"))
                    self.textEditRfResponse.append(rx["rxframedesc"])
                else:  # strip off hex data
                    descOnly = rx["rxframedesc"].split("( AB")[0]
                    self.textEditRfResponse.append(descOnly)
                self.textEditRfResponse.setTextColor(QColor("blue"))

            elif rx.keys()[0] == "comlock":
                if rx.values()[0] == True:
                    self.comboBoxBAUDRate.setEnabled(False)
                    self.comboBoxCOMPort.setEnabled(False)
                else:
                    self.comboBoxBAUDRate.setEnabled(True)
                    self.comboBoxCOMPort.setEnabled(True)

            elif rx.keys()[0] == "baudrate_update":
                baudrate = rx.values()[0]
                idx = self.baudarray.index(str(baudrate))
                self.comboBoxBAUDRate.setCurrentIndex(idx)
                
    @Slot("")
    def on_openComButton_clicked (self):
        if self.ComHandler.serial_port.isOpen():
            self.ComHandler.closeComPort()
            self.pushButtonTxFrame.setEnabled(False)
            self.openComButton.setText("Open COM Port")
        else:
            self.ComHandler.openComPort(str(self.comboBoxCOMPort.currentText()), int(self.comboBoxBAUDRate.currentText()))
            self.pushButtonTxFrame.setEnabled(True)
            self.openComButton.setText("Close COM Port")

    def closeEvent (self, event):
        self.ComHandler.quit()
        self.timer.stop()
        if DEBUG:
            print("kill timer")
        self.close()

    @Slot("")    
    def on_pushButtonTxFrame_clicked(self):
        if str(self.comboBoxCmd.currentText()) == 'set_uart_mode_request':
            db = str(self.comboBoxDataBits.currentText())
            par = str(self.comboBoxParity.currentText())
            sb = str(self.comboBoxStopBits.currentText())
            br = str(self.comboBoxBaudRate.currentText())
            self.txframe = self.ComHandler.buildCommand(str(self.cmd),[db,par,sb,br])
            self.updateGUI(self.txframe)
            
        if len(self.txframe) > 0:
            self.ComHandler.sendFrame(self.txframe)
            self.textEditTx.append(getTimeStamp() + getHexString(self.txframe))
            if DEBUG:
                print "send frame"
        else:
            newPalette = QPalette()
            if "data" in str(self.comboBoxCmd.currentText()):
                newPalette.setColor(self.lineEditUserPayload.backgroundRole(), Qt.yellow)
                self.lineEditUserPayload.setPalette(newPalette)

            newPalette.setColor(self.lineEditDestAddr.backgroundRole(), Qt.yellow)
            self.lineEditDestAddr.setPalette(newPalette)

            newPalette.setColor(self.lineEditThisAddress.backgroundRole(), Qt.yellow)
            self.lineEditThisAddress.setPalette(newPalette)

            newPalette.setColor(self.lineEditSleep.backgroundRole(), Qt.yellow)
            self.lineEditSleep.setPalette(newPalette)

            newPalette.setColor(self.lineEditSecurity.backgroundRole(), Qt.yellow)
            self.lineEditSecurity.setPalette(newPalette)

            QMessageBox.warning(self,self.tr("Warning: Invalid Argument/s"),self.tr("Command requires highlighted parameters \t\t"))

            newPalette.setColor(self.lineEditUserPayload.backgroundRole(), Qt.white)
            self.lineEditUserPayload.setPalette(newPalette)

            newPalette.setColor(self.lineEditDestAddr.backgroundRole(), Qt.white)
            self.lineEditDestAddr.setPalette(newPalette)

            newPalette.setColor(self.lineEditThisAddress.backgroundRole(), Qt.white)
            self.lineEditThisAddress.setPalette(newPalette)

            newPalette.setColor(self.lineEditSleep.backgroundRole(), Qt.white)
            self.lineEditSleep.setPalette(newPalette)

            newPalette.setColor(self.lineEditSecurity.backgroundRole(), Qt.white)
            self.lineEditSecurity.setPalette(newPalette)


            if DEBUG:
                print "no frame to tx"
            pass

    @Slot("")    
    def on_pushButtonClearRf_clicked(self):
        self.textEditRfResponse.setText("")

    @Slot("")    
    def on_pushButtonClearRx_clicked(self):
        self.textEditRx.setText("")

    @Slot("")    
    def on_pushButtonClearTx_clicked(self):
        self.textEditTx.setText("")

    @Slot("")
    def on_lineEditUserPayload_editingFinished(self):
        pass

    @Slot("")
    def on_lineEditUserPayload_textChanged(self):
        self.progressBar.setValue( float(100 * (9 + (len(str(self.lineEditUserPayload.text()))/2) )) /127  )
        self.lineEditFrameToSend.setText("")
        self.lineEditSizeByte.setText("")
        self.txframe = [] 

    @Slot("")
    def on_lineEditThisAddress_textChanged(self):
        self.lineEditFrameToSend.setText("")
        self.txframe = [] 

    @Slot("")
    def on_lineEditSecurity_textChanged(self):
        self.lineEditFrameToSend.setText("")
        self.txframe = [] 

    @Slot("")
    def on_lineEditSleep_textChanged(self):
        self.lineEditFrameToSend.setText("")
        self.txframe = [] 

    @Slot("")
    def on_lineEditDestAddr_textChanged(self):
        self.lineEditFrameToSend.setText("")
        self.txframe = [] 
        
    @Slot("")
    def on_lineEditUserPayload_editingFinished(self):
        if DEBUG:
            print "on_lineEditUserPayload_editingFinished"

        if len(str(self.lineEditUserPayload.text())) > 0 and self.payloadValid() == False:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr("Payload should be an hexadecimal string up to 118 bytes long\t\t"))
                self.lineEditUserPayload.setText("")
                self.lineEditUserPayload.setFocus()
                return

        elif len(str(self.lineEditDestAddr.text())) > 0 and self.addressValid() == False:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr("Destination address should be an integer from 0 to 0xffff\t\t"))
                self.lineEditDestAddr.setText()
                self.lineEditDestAddr.setFocus()
                return

        elif self.payloadValid() and self.addressValid():
            #[destination, options, handle, data]
            self.txframe = self.ComHandler.buildCommand (str(self.cmd),[str(self.lineEditDestAddr.text()), \
                                                              str(self.comboBoxOptions.currentText()),         \
                                                              str(self.comboBoxHandle.currentText()),         \
                                                              str(self.lineEditUserPayload.text()).lower()])     
            if DEBUG:
                print self.txframe
            self.updateGUI(self.txframe)

    @Slot("")
    def on_lineEditDestAddr_editingFinished(self):
        if len(str(self.lineEditDestAddr.text())) > 0 and self.addressValid() == False:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr("Destination address should be an integer from 0 to 0xffff\t\t"))
                self.lineEditDestAddr.setText()
                self.lineEditDestAddr.setFocus()
                return

        elif len(str(self.lineEditUserPayload.text())) > 0 and self.payloadValid() == False:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr("Payload should be an hexadecimal string up to 118 bytes long\t\t"))
                self.lineEditUserPayload.setText("")
                self.lineEditUserPayload.setFocus()
                return

        elif self.payloadValid() and self.addressValid():
            #[destination, options, handle, data]
            self.txframe = self.ComHandler.buildCommand (str(self.cmd),[str(self.lineEditDestAddr.text()), \
                                                              str(self.comboBoxOptions.currentText()),         \
                                                              str(self.comboBoxHandle.currentText()),         \
                                                              str(self.lineEditUserPayload.text()).lower()])     
            if DEBUG: 
                print self.txframe
            self.updateGUI(self.txframe)

    def payloadValid (self):
        valid = False
        if str(self.lineEditUserPayload.text()).startswith("0x"):
            if (isHexString(str(self.lineEditUserPayload.text())[2:])) and \
                len(str(self.lineEditUserPayload.text())) <= (PAYLOAD_MAX_LEN + 2):
                valid = True

        if len(str(self.lineEditUserPayload.text())) <= (PAYLOAD_MAX_LEN/2):
            valid = True
        return valid

    def securityValid (self):
        valid = False
        if str(self.lineEditSecurity.text()).startswith("0x"):
            if (isHexString(str(self.lineEditSecurity.text()))) and \
                len(str(self.lineEditSecurity.text())) == (SEC_KEY_LEN + 2):
                valid = True
                
        if len(str(self.lineEditSecurity.text())) == (SEC_KEY_LEN/2):
            valid = True
        print valid
        return valid

    def addressValid (self):
        if len(str(self.lineEditDestAddr.text()) ) == 0 :
            return False
        address = getIntValue(str(self.lineEditDestAddr.text()))
        if address <= 0xffff:
            return True
        return False

    @Slot("")
    def on_lineEditThisAddress_editingFinished(self):
        if DEBUG:
            print "on_lineEditThisAddress_editingFinished"
        if len(str(self.lineEditThisAddress.text())) > 0 :
            parameter = "Address"
            if "panid" in str(self.comboBoxCmd.currentText()):
                parameter = "PAN ID"
            if getIntValue(str(self.lineEditThisAddress.text()))== -1 or \
                getIntValue(str(self.lineEditThisAddress.text())) > 0xffff:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr(parameter + " argument should be an integer from 0 to 0xffff\t\t"))
                self.lineEditThisAddress.setText("")
                self.lineEditThisAddress.setFocus()
                return

            self.txframe = self.ComHandler.buildCommand (self.cmd,str(self.lineEditThisAddress.text()))
            if DEBUG:
                print self.txframe
            self.updateGUI(self.txframe)
        else:
            self.lineEditFrameToSend.setText("")
            self.txframe = [] 

    @Slot("")
    def on_lineEditSleep_editingFinished(self):
        if DEBUG:
            print "on_lineEditThisAddress_editingFinished"
        if len(str(self.lineEditSleep.text())) > 0 :
            if getIntValue(str(self.lineEditSleep.text()))== -1:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr("Sleep argument should be an integer from 0 to 0xffffffff\t\t"))
                self.lineEditSleep.setText("")
                self.lineEditSleep.setFocus()
                return
        
            self.txframe = self.ComHandler.buildCommand (self.cmd,str(self.lineEditSleep.text()))
            if DEBUG:
                print self.txframe
            self.updateGUI(self.txframe)
        else:
            self.lineEditFrameToSend.setText("")
            self.txframe = [] 

    @Slot("")
    def on_lineEditSecurity_editingFinished (self):
        if DEBUG:
            print "on_lineEditSecurity_editingFinished"
        if len(str(self.lineEditSecurity.text()))> 0:
            if self.securityValid():
                self.txframe = self.ComHandler.buildCommand (self.cmd,str(self.lineEditSecurity.text()))
                if DEBUG:
                    print self.txframe
                self.updateGUI(self.txframe)

            else:
                QMessageBox.warning(self,self.tr("Warning: Invalid Argument"),self.tr("security key argument should be a 32-length hex string\t\t"))
                self.lineEditSecurity.setText("")
                self.lineEditSecurity.setFocus()                    
                return


    def processComboBoxCmd(self,par):
        self.txframe = []
        self.comboBoxCmdOption.blockSignals(True)
        self.cleanGUI()
        self.lineEditUserPayload.setEnabled(False)
        #par = par.replace("cmd_tx_","")
        self.cmd = str(par)
        if par in TX_SB_COMMANDS.keys():
            self.stackedWidget.setCurrentIndex(0)
            self.txframe = self.ComHandler.buildCommand (str(par),[])
            if DEBUG:
                print self.txframe
            self.updateGUI(self.txframe)

        elif par == "set_address_request":
            self.stackedWidget.setCurrentIndex(2)
            self.label3Byte.setText('Set This Node\'s Address: ')

        elif par == "set_panid_request":
            self.stackedWidget.setCurrentIndex(2)
            self.label3Byte.setText('Set This Node\'s PAN ID: ')

        elif par == "set_security_key_request":
            self.stackedWidget.setCurrentIndex(6)
            self.label3Byte.setText('Set 16-byte-long security key : ')

        elif par == "sleep_request":
            self.stackedWidget.setCurrentIndex(3)

        elif par == "send_data_request":
            self.stackedWidget.setCurrentIndex(5)
            handle = []
            for el in range(0,256):
                handle.append(str(el))
            self.comboBoxHandle.addItems(handle)

        elif par == "set_uart_mode_request":
            self.stackedWidget.setCurrentIndex(4)
            self.populateUartCombos()
        else:   
            self.stackedWidget.setCurrentIndex(1)
            self.populateCombo(par)
        self.comboBoxCmdOption.blockSignals(False)
        
        if par == "send_data_request":
            self.lineEditUserPayload.setEnabled(True)
        else:
            self.lineEditUserPayload.setText("")

    def populateUartCombos(self):
        self.comboBoxDataBits.addItems(['5','6','7','8'])
        self.comboBoxDataBits.setCurrentIndex(3)
        self.comboBoxParity.addItems(["none","even","odd","force_0","force_1"])
        self.comboBoxParity.setCurrentIndex(0)
        self.comboBoxStopBits.addItems(['1','2'])
        self.comboBoxStopBits.setCurrentIndex(0)
        self.comboBoxBaudRate.addItems(['9600','14400','19200','28800','38400','57600','115200','230400','256000'])
        self.comboBoxBaudRate.setCurrentIndex(6)

    def processComboBoxCmdOption(self,option):
        if self.cmd == "set_transmit_power_request":
            option = self.comboBoxCmdOption.currentIndex()
        self.txframe = self.ComHandler.buildCommand (self.cmd,str(option))
        if DEBUG:
            print self.txframe
        self.updateGUI(self.txframe)

    def updateGUI (self,frame):
        self.lineEditSizeByte.setText(str(frame[1]))
        self.lineEditCmdId.setText(getHexString([frame[2]]))
        self.lineEditCRC.setText(getHexString(frame[-2:]))
        self.lineEditFrameToSend.setText(getHexString(frame))
        if DEBUG:
            print "updateGUI"

    def cleanGUI(self):
        self.lineEditSizeByte.setText("")
        self.lineEditCmdId.setText("")
        self.lineEditCRC.setText("")
        self.lineEditFrameToSend.setText("")
        self.lineEditThisAddress.setText("")
        self.lineEditSleep.setText("")

    def populateCombo (self,par):
        self.comboBoxCmdOption.clear()
        if par == "set_channel_request":
            for i in range(11,26):
                self.comboBoxCmdOption.addItem(str(i))
                
        elif par == "set_ack_state_request":
            self.comboBoxCmdOption.addItem("enable")
            self.comboBoxCmdOption.addItem("disable")
            
        elif par == "set_led_state_request":
            self.comboBoxCmdOption.addItems(["off","on","toggle"])

        elif par == "set_receiver_state_request":
            self.comboBoxCmdOption.addItems(["off","on"])

        elif par == "set_transmit_power_request":
            cmdList = ['+3.0 dBm', '+2.8 dBm', '+2.3 dBm', '+1.8 dBm', '+1.3 dBm', '+0.7 dBm', '0 dBm',
                       '-1.0 dBm', '-2.0 dBm', '-3.0 dBm', '-4.0 dBm', '-5.0 dBm',
                       '-7.0 dBm', '-9.0 dBm', '-12.0 dBm', '-17.0 dBm']
            self.comboBoxCmdOption.addItems(cmdList)

        elif par == "settings_request":
            self.comboBoxCmdOption.addItems(["save","restore"])

        self.comboBoxOptions.setCurrentIndex(0)
        self.processComboBoxCmdOption(self.comboBoxCmdOption.currentText())
        # Build frame and show in GUI

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    form = RB_MainWindow()
    form.show()

    app.exec_()



