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

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(577, 684)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtGui.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 551, 541))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")
        self.comboBoxCOMPort = QtGui.QComboBox(self.tab)
        self.comboBoxCOMPort.setGeometry(QtCore.QRect(90, 20, 211, 26))
        self.comboBoxCOMPort.setObjectName("comboBoxCOMPort")
        self.pushButton_2 = QtGui.QPushButton(self.tab)
        self.pushButton_2.setGeometry(QtCore.QRect(0, 120, 121, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setGeometry(QtCore.QRect(10, 50, 71, 16))
        self.label_7.setObjectName("label_7")
        self.textEditRx = QtGui.QTextEdit(self.tab)
        self.textEditRx.setGeometry(QtCore.QRect(20, 210, 512, 100))
        self.textEditRx.setObjectName("textEditRx")
        self.line = QtGui.QFrame(self.tab)
        self.line.setGeometry(QtCore.QRect(10, 170, 521, 16))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setGeometry(QtCore.QRect(10, 20, 62, 16))
        self.label_6.setObjectName("label_6")
        self.comboBoxBAUDRate = QtGui.QComboBox(self.tab)
        self.comboBoxBAUDRate.setGeometry(QtCore.QRect(90, 50, 211, 26))
        self.comboBoxBAUDRate.setObjectName("comboBoxBAUDRate")
        self.line_3 = QtGui.QFrame(self.tab)
        self.line_3.setGeometry(QtCore.QRect(10, 320, 521, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(0, 80, 121, 32))
        self.pushButton.setObjectName("pushButton")
        self.textEditTx = QtGui.QTextEdit(self.tab)
        self.textEditTx.setGeometry(QtCore.QRect(20, 360, 512, 100))
        self.textEditTx.setObjectName("textEditTx")
        self.label_5 = QtGui.QLabel(self.tab)
        self.label_5.setGeometry(QtCore.QRect(20, 190, 62, 16))
        self.label_5.setObjectName("label_5")
        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setGeometry(QtCore.QRect(20, 340, 62, 16))
        self.label_8.setObjectName("label_8")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.lineEditSecurityKey = QtGui.QLineEdit(self.tab_2)
        self.lineEditSecurityKey.setGeometry(QtCore.QRect(110, 110, 113, 22))
        self.lineEditSecurityKey.setObjectName("lineEditSecurityKey")
        self.lineEditChannel = QtGui.QLineEdit(self.tab_2)
        self.lineEditChannel.setGeometry(QtCore.QRect(110, 20, 113, 22))
        self.lineEditChannel.setObjectName("lineEditChannel")
        self.label_2 = QtGui.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(10, 50, 62, 16))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(10, 110, 81, 16))
        self.label_4.setObjectName("label_4")
        self.lineEditAddress = QtGui.QLineEdit(self.tab_2)
        self.lineEditAddress.setGeometry(QtCore.QRect(110, 50, 113, 22))
        self.lineEditAddress.setObjectName("lineEditAddress")
        self.lineEditPANID = QtGui.QLineEdit(self.tab_2)
        self.lineEditPANID.setGeometry(QtCore.QRect(110, 80, 113, 22))
        self.lineEditPANID.setObjectName("lineEditPANID")
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(100, 140, 131, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(10, 80, 62, 16))
        self.label_3.setObjectName("label_3")
        self.label = QtGui.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(10, 20, 62, 16))
        self.label.setObjectName("label")
        self.checkBoxChannelAck = QtGui.QCheckBox(self.tab_2)
        self.checkBoxChannelAck.setGeometry(QtCore.QRect(230, 20, 101, 20))
        self.checkBoxChannelAck.setCheckable(True)
        self.checkBoxChannelAck.setObjectName("checkBoxChannelAck")
        self.checkBoxAddressOK = QtGui.QCheckBox(self.tab_2)
        self.checkBoxAddressOK.setGeometry(QtCore.QRect(230, 50, 101, 20))
        self.checkBoxAddressOK.setCheckable(True)
        self.checkBoxAddressOK.setObjectName("checkBoxAddressOK")
        self.checkBoxPanIdOK = QtGui.QCheckBox(self.tab_2)
        self.checkBoxPanIdOK.setGeometry(QtCore.QRect(230, 80, 101, 20))
        self.checkBoxPanIdOK.setCheckable(True)
        self.checkBoxPanIdOK.setObjectName("checkBoxPanIdOK")
        self.checkBoxSecurityKey = QtGui.QCheckBox(self.tab_2)
        self.checkBoxSecurityKey.setGeometry(QtCore.QRect(230, 110, 121, 20))
        self.checkBoxSecurityKey.setCheckable(True)
        self.checkBoxSecurityKey.setObjectName("checkBoxSecurityKey")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.comboBoxCmd = QtGui.QComboBox(self.tab_3)
        self.comboBoxCmd.setGeometry(QtCore.QRect(160, 10, 281, 26))
        self.comboBoxCmd.setObjectName("comboBoxCmd")
        self.label_9 = QtGui.QLabel(self.tab_3)
        self.label_9.setGeometry(QtCore.QRect(20, 15, 141, 21))
        self.label_9.setObjectName("label_9")
        self.lineEditStartByte = QtGui.QLineEdit(self.tab_3)
        self.lineEditStartByte.setGeometry(QtCore.QRect(43, 70, 41, 22))
        self.lineEditStartByte.setReadOnly(True)
        self.lineEditStartByte.setObjectName("lineEditStartByte")
        self.label_10 = QtGui.QLabel(self.tab_3)
        self.label_10.setGeometry(QtCore.QRect(32, 50, 62, 16))
        self.label_10.setObjectName("label_10")
        self.lineEditSizeByte = QtGui.QLineEdit(self.tab_3)
        self.lineEditSizeByte.setGeometry(QtCore.QRect(96, 70, 41, 22))
        self.lineEditSizeByte.setReadOnly(True)
        self.lineEditSizeByte.setObjectName("lineEditSizeByte")
        self.label_11 = QtGui.QLabel(self.tab_3)
        self.label_11.setGeometry(QtCore.QRect(103, 50, 30, 16))
        self.label_11.setObjectName("label_11")
        self.lineEditCmdId = QtGui.QLineEdit(self.tab_3)
        self.lineEditCmdId.setGeometry(QtCore.QRect(144, 70, 42, 22))
        self.lineEditCmdId.setReadOnly(True)
        self.lineEditCmdId.setObjectName("lineEditCmdId")
        self.label_12 = QtGui.QLabel(self.tab_3)
        self.label_12.setGeometry(QtCore.QRect(142, 50, 51, 16))
        self.label_12.setObjectName("label_12")
        self.lineEditCRC = QtGui.QLineEdit(self.tab_3)
        self.lineEditCRC.setGeometry(QtCore.QRect(470, 70, 64, 22))
        self.lineEditCRC.setReadOnly(True)
        self.lineEditCRC.setObjectName("lineEditCRC")
        self.label_13 = QtGui.QLabel(self.tab_3)
        self.label_13.setGeometry(QtCore.QRect(484, 50, 31, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtGui.QLabel(self.tab_3)
        self.label_14.setGeometry(QtCore.QRect(298, 50, 51, 16))
        self.label_14.setObjectName("label_14")
        self.lineEditPayload = QtGui.QLineEdit(self.tab_3)
        self.lineEditPayload.setGeometry(QtCore.QRect(200, 70, 261, 22))
        self.lineEditPayload.setAutoFillBackground(False)
        self.lineEditPayload.setReadOnly(True)
        self.lineEditPayload.setObjectName("lineEditPayload")
        self.stackedWidget = QtGui.QStackedWidget(self.tab_3)
        self.stackedWidget.setGeometry(QtCore.QRect(20, 110, 501, 111))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtGui.QWidget()
        self.page.setObjectName("page")
        self.stackedWidget.addWidget(self.page)
        self.twoByteCmd = QtGui.QWidget()
        self.twoByteCmd.setObjectName("twoByteCmd")
        self.label_26 = QtGui.QLabel(self.twoByteCmd)
        self.label_26.setGeometry(QtCore.QRect(20, 0, 121, 16))
        self.label_26.setObjectName("label_26")
        self.comboBoxCmdOption = QtGui.QComboBox(self.twoByteCmd)
        self.comboBoxCmdOption.setGeometry(QtCore.QRect(10, 20, 256, 26))
        self.comboBoxCmdOption.setObjectName("comboBoxCmdOption")
        self.label_x = QtGui.QLabel(self.twoByteCmd)
        self.label_x.setGeometry(QtCore.QRect(240, 0, 161, 16))
        self.label_x.setObjectName("label_x")
        self.stackedWidget.addWidget(self.twoByteCmd)
        self.threeByteCmd = QtGui.QWidget()
        self.threeByteCmd.setObjectName("threeByteCmd")
        self.label3Byte = QtGui.QLabel(self.threeByteCmd)
        self.label3Byte.setGeometry(QtCore.QRect(20, 0, 151, 16))
        self.label3Byte.setLineWidth(3)
        self.label3Byte.setObjectName("label3Byte")
        self.lineEditThisAddress = QtGui.QLineEdit(self.threeByteCmd)
        self.lineEditThisAddress.setGeometry(QtCore.QRect(20, 20, 131, 22))
        self.lineEditThisAddress.setWhatsThis("")
        self.lineEditThisAddress.setObjectName("lineEditThisAddress")
        self.stackedWidget.addWidget(self.threeByteCmd)
        self.fourByteCmd = QtGui.QWidget()
        self.fourByteCmd.setObjectName("fourByteCmd")
        self.label_28 = QtGui.QLabel(self.fourByteCmd)
        self.label_28.setGeometry(QtCore.QRect(20, 0, 201, 16))
        self.label_28.setLineWidth(3)
        self.label_28.setObjectName("label_28")
        self.lineEditSleep = QtGui.QLineEdit(self.fourByteCmd)
        self.lineEditSleep.setGeometry(QtCore.QRect(20, 20, 131, 22))
        self.lineEditSleep.setInputMask("")
        self.lineEditSleep.setObjectName("lineEditSleep")
        self.stackedWidget.addWidget(self.fourByteCmd)
        self.UART = QtGui.QWidget()
        self.UART.setObjectName("UART")
        self.label_15 = QtGui.QLabel(self.UART)
        self.label_15.setGeometry(QtCore.QRect(20, 0, 62, 16))
        self.label_15.setObjectName("label_15")
        self.comboBoxDataBits = QtGui.QComboBox(self.UART)
        self.comboBoxDataBits.setGeometry(QtCore.QRect(10, 20, 80, 26))
        self.comboBoxDataBits.setObjectName("comboBoxDataBits")
        self.label_16 = QtGui.QLabel(self.UART)
        self.label_16.setGeometry(QtCore.QRect(120, 0, 41, 16))
        self.label_16.setObjectName("label_16")
        self.comboBoxParity = QtGui.QComboBox(self.UART)
        self.comboBoxParity.setGeometry(QtCore.QRect(100, 20, 80, 26))
        self.comboBoxParity.setObjectName("comboBoxParity")
        self.label_17 = QtGui.QLabel(self.UART)
        self.label_17.setGeometry(QtCore.QRect(200, 0, 62, 16))
        self.label_17.setObjectName("label_17")
        self.comboBoxStopBits = QtGui.QComboBox(self.UART)
        self.comboBoxStopBits.setGeometry(QtCore.QRect(190, 20, 81, 26))
        self.comboBoxStopBits.setObjectName("comboBoxStopBits")
        self.label_18 = QtGui.QLabel(self.UART)
        self.label_18.setGeometry(QtCore.QRect(290, 0, 62, 16))
        self.label_18.setObjectName("label_18")
        self.comboBoxBaudRate = QtGui.QComboBox(self.UART)
        self.comboBoxBaudRate.setGeometry(QtCore.QRect(280, 20, 121, 26))
        self.comboBoxBaudRate.setObjectName("comboBoxBaudRate")
        self.stackedWidget.addWidget(self.UART)
        self.Data = QtGui.QWidget()
        self.Data.setObjectName("Data")
        self.label_19 = QtGui.QLabel(self.Data)
        self.label_19.setGeometry(QtCore.QRect(20, 0, 131, 16))
        self.label_19.setObjectName("label_19")
        self.lineEditDestAddr = QtGui.QLineEdit(self.Data)
        self.lineEditDestAddr.setGeometry(QtCore.QRect(30, 20, 113, 22))
        self.lineEditDestAddr.setObjectName("lineEditDestAddr")
        self.label_20 = QtGui.QLabel(self.Data)
        self.label_20.setGeometry(QtCore.QRect(200, 0, 51, 16))
        self.label_20.setObjectName("label_20")
        self.comboBoxOptions = QtGui.QComboBox(self.Data)
        self.comboBoxOptions.setGeometry(QtCore.QRect(150, 17, 161, 26))
        self.comboBoxOptions.setObjectName("comboBoxOptions")
        self.label_21 = QtGui.QLabel(self.Data)
        self.label_21.setGeometry(QtCore.QRect(340, 0, 62, 16))
        self.label_21.setObjectName("label_21")
        self.lineEditHandle = QtGui.QLineEdit(self.Data)
        self.lineEditHandle.setGeometry(QtCore.QRect(320, 20, 113, 22))
        self.lineEditHandle.setObjectName("lineEditHandle")
        self.label_22 = QtGui.QLabel(self.Data)
        self.label_22.setGeometry(QtCore.QRect(20, 50, 51, 16))
        self.label_22.setObjectName("label_22")
        self.lineEditUserPayload = QtGui.QLineEdit(self.Data)
        self.lineEditUserPayload.setGeometry(QtCore.QRect(80, 50, 351, 22))
        self.lineEditUserPayload.setObjectName("lineEditUserPayload")
        self.pushButtonClear = QtGui.QPushButton(self.Data)
        self.pushButtonClear.setGeometry(QtCore.QRect(410, 80, 91, 32))
        self.pushButtonClear.setObjectName("pushButtonClear")
        self.progressBar = QtGui.QProgressBar(self.Data)
        self.progressBar.setGeometry(QtCore.QRect(80, 80, 311, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.stackedWidget.addWidget(self.Data)
        self.label_23 = QtGui.QLabel(self.tab_3)
        self.label_23.setGeometry(QtCore.QRect(20, 230, 131, 16))
        self.label_23.setObjectName("label_23")
        self.lineEditFrameToSend = QtGui.QLineEdit(self.tab_3)
        self.lineEditFrameToSend.setGeometry(QtCore.QRect(20, 250, 511, 22))
        self.lineEditFrameToSend.setObjectName("lineEditFrameToSend")
        self.pushButtonTxFrame = QtGui.QPushButton(self.tab_3)
        self.pushButtonTxFrame.setGeometry(QtCore.QRect(420, 280, 114, 32))
        self.pushButtonTxFrame.setObjectName("pushButtonTxFrame")
        self.label_25 = QtGui.QLabel(self.tab_3)
        self.label_25.setGeometry(QtCore.QRect(20, 310, 141, 16))
        self.label_25.setObjectName("label_25")
        self.textEditRfResponse = QtGui.QTextEdit(self.tab_3)
        self.textEditRfResponse.setGeometry(QtCore.QRect(20, 330, 511, 161))
        self.textEditRfResponse.setObjectName("textEditRfResponse")
        self.tabWidget.addTab(self.tab_3, "")
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 580, 114, 32))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 577, 26))
        self.menuBar.setObjectName("menuBar")
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName("mainToolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(5)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("MainWindow", "Close COM Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "BAUD Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "COM Port", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setToolTip(QtGui.QApplication.translate("MainWindow", "additonal settings are \'8,N,1\'...", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("MainWindow", "Open COM Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Serial RX", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Serial TX", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("MainWindow", "COM Port", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Security Key", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("MainWindow", "Configure Node", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "PANID", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Channel", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxChannelAck.setText(QtGui.QApplication.translate("MainWindow", "Channel OK", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxAddressOK.setText(QtGui.QApplication.translate("MainWindow", "Address OK", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxPanIdOK.setText(QtGui.QApplication.translate("MainWindow", "PANID OK", None, QtGui.QApplication.UnicodeUTF8))
        self.checkBoxSecurityKey.setText(QtGui.QApplication.translate("MainWindow", "Security Key OK", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("MainWindow", "Node setup", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Command Selection:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditStartByte.setText(QtGui.QApplication.translate("MainWindow", "0xAB", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "Start Byte", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "CMD ID", None, QtGui.QApplication.UnicodeUTF8))
        self.label_13.setText(QtGui.QApplication.translate("MainWindow", "CRC", None, QtGui.QApplication.UnicodeUTF8))
        self.label_14.setText(QtGui.QApplication.translate("MainWindow", "Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.label_26.setText(QtGui.QApplication.translate("MainWindow", "Command Option:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_x.setText(QtGui.QApplication.translate("MainWindow", "label_x", None, QtGui.QApplication.UnicodeUTF8))
        self.label3Byte.setText(QtGui.QApplication.translate("MainWindow", "This Node\'s Address:", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditThisAddress.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter an address in the form \'12CD\'.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_28.setText(QtGui.QApplication.translate("MainWindow", "Sleep Interval (milliseconds):", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditSleep.setToolTip(QtGui.QApplication.translate("MainWindow", "Enter the number of miliseconds to sleep.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_15.setText(QtGui.QApplication.translate("MainWindow", "Data Bits", None, QtGui.QApplication.UnicodeUTF8))
        self.label_16.setText(QtGui.QApplication.translate("MainWindow", "Parity", None, QtGui.QApplication.UnicodeUTF8))
        self.label_17.setText(QtGui.QApplication.translate("MainWindow", "Stop Bits", None, QtGui.QApplication.UnicodeUTF8))
        self.label_18.setText(QtGui.QApplication.translate("MainWindow", "Baud Rate", None, QtGui.QApplication.UnicodeUTF8))
        self.label_19.setText(QtGui.QApplication.translate("MainWindow", "Destination Address", None, QtGui.QApplication.UnicodeUTF8))
        self.label_20.setText(QtGui.QApplication.translate("MainWindow", "Options", None, QtGui.QApplication.UnicodeUTF8))
        self.label_21.setText(QtGui.QApplication.translate("MainWindow", "Handle", None, QtGui.QApplication.UnicodeUTF8))
        self.label_22.setText(QtGui.QApplication.translate("MainWindow", "Payload", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonClear.setText(QtGui.QApplication.translate("MainWindow", "Clear", None, QtGui.QApplication.UnicodeUTF8))
        self.label_23.setText(QtGui.QApplication.translate("MainWindow", "Serial fame to send:", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonTxFrame.setText(QtGui.QApplication.translate("MainWindow", "Send Frame", None, QtGui.QApplication.UnicodeUTF8))
        self.label_25.setText(QtGui.QApplication.translate("MainWindow", "RadioBlock Response:", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), QtGui.QApplication.translate("MainWindow", "Command Frame Constructor", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))


import sys
def show_mainwindow(app, MainWindow):
    MainWindow.setWindowTitle('RadioBlocks Commander')
    MainWindow.setWindowIcon(QtGui.QIcon('favicon.ico'))
    MainWindow.show()

