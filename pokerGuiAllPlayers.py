# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pokerGuiAllPlayers.ui'
#
# Created: Sat Jan 14 21:57:05 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(908, 720)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.leP1C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP1C1.setGeometry(QtCore.QRect(120, 130, 51, 31))
        self.leP1C1.setObjectName("leP1C1")
        self.leNum = QtGui.QLineEdit(self.centralwidget)
        self.leNum.setGeometry(QtCore.QRect(260, 450, 121, 31))
        self.leNum.setObjectName("leNum")
        self.textEditNumSims = QtGui.QTextEdit(self.centralwidget)
        self.textEditNumSims.setGeometry(QtCore.QRect(60, 490, 181, 31))
        self.textEditNumSims.setObjectName("textEditNumSims")
        self.leSims = QtGui.QLineEdit(self.centralwidget)
        self.leSims.setGeometry(QtCore.QRect(260, 490, 121, 31))
        self.leSims.setObjectName("leSims")
        self.btnCalculate = QtGui.QPushButton(self.centralwidget)
        self.btnCalculate.setGeometry(QtCore.QRect(450, 490, 161, 31))
        self.btnCalculate.setObjectName("btnCalculate")
        self.leCalculateWin = QtGui.QLineEdit(self.centralwidget)
        self.leCalculateWin.setGeometry(QtCore.QRect(640, 490, 101, 31))
        self.leCalculateWin.setObjectName("leCalculateWin")
        self.textEditPlayer1 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer1.setGeometry(QtCore.QRect(100, 100, 131, 31))
        self.textEditPlayer1.setObjectName("textEditPlayer1")
        self.leP1C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP1C2.setGeometry(QtCore.QRect(170, 130, 51, 31))
        self.leP1C2.setObjectName("leP1C2")
        self.textEditNumOpps = QtGui.QTextEdit(self.centralwidget)
        self.textEditNumOpps.setGeometry(QtCore.QRect(70, 450, 171, 31))
        self.textEditNumOpps.setObjectName("textEditNumOpps")
        self.leP2C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP2C2.setGeometry(QtCore.QRect(380, 80, 51, 31))
        self.leP2C2.setObjectName("leP2C2")
        self.textEditPlayer2 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer2.setGeometry(QtCore.QRect(310, 50, 161, 31))
        self.textEditPlayer2.setObjectName("textEditPlayer2")
        self.leP2C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP2C1.setGeometry(QtCore.QRect(330, 80, 51, 31))
        self.leP2C1.setObjectName("leP2C1")
        self.leP3C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP3C2.setGeometry(QtCore.QRect(590, 80, 51, 31))
        self.leP3C2.setObjectName("leP3C2")
        self.textEditPlayer3 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer3.setGeometry(QtCore.QRect(520, 50, 161, 31))
        self.textEditPlayer3.setObjectName("textEditPlayer3")
        self.leP3C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP3C1.setGeometry(QtCore.QRect(540, 80, 51, 31))
        self.leP3C1.setObjectName("leP3C1")
        self.leP4C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP4C2.setGeometry(QtCore.QRect(770, 160, 51, 31))
        self.leP4C2.setObjectName("leP4C2")
        self.textEditPlayer4 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer4.setGeometry(QtCore.QRect(660, 130, 171, 31))
        self.textEditPlayer4.setObjectName("textEditPlayer4")
        self.leP4C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP4C1.setGeometry(QtCore.QRect(720, 160, 51, 31))
        self.leP4C1.setObjectName("leP4C1")
        self.leP5C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP5C2.setGeometry(QtCore.QRect(760, 290, 51, 31))
        self.leP5C2.setObjectName("leP5C2")
        self.textEditPlayer5 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer5.setGeometry(QtCore.QRect(650, 260, 171, 31))
        self.textEditPlayer5.setObjectName("textEditPlayer5")
        self.leP5C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP5C1.setGeometry(QtCore.QRect(710, 290, 51, 31))
        self.leP5C1.setObjectName("leP5C1")
        self.leP6C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP6C2.setGeometry(QtCore.QRect(620, 390, 51, 31))
        self.leP6C2.setObjectName("leP6C2")
        self.textEditPlayer6 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer6.setGeometry(QtCore.QRect(550, 360, 161, 31))
        self.textEditPlayer6.setObjectName("textEditPlayer6")
        self.leP6C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP6C1.setGeometry(QtCore.QRect(570, 390, 51, 31))
        self.leP6C1.setObjectName("leP6C1")
        self.leP7C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP7C2.setGeometry(QtCore.QRect(420, 390, 51, 31))
        self.leP7C2.setObjectName("leP7C2")
        self.textEditPlayer7 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer7.setGeometry(QtCore.QRect(350, 360, 151, 31))
        self.textEditPlayer7.setObjectName("textEditPlayer7")
        self.leP7C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP7C1.setGeometry(QtCore.QRect(370, 390, 51, 31))
        self.leP7C1.setObjectName("leP7C1")
        self.leP8C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP8C2.setGeometry(QtCore.QRect(240, 360, 51, 31))
        self.leP8C2.setObjectName("leP8C2")
        self.textEditPlayer8 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer8.setGeometry(QtCore.QRect(170, 330, 181, 31))
        self.textEditPlayer8.setObjectName("textEditPlayer8")
        self.leP8C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP8C1.setGeometry(QtCore.QRect(190, 360, 51, 31))
        self.leP8C1.setObjectName("leP8C1")
        self.leP9C2 = QtGui.QLineEdit(self.centralwidget)
        self.leP9C2.setGeometry(QtCore.QRect(130, 240, 51, 31))
        self.leP9C2.setObjectName("leP9C2")
        self.leP9C1 = QtGui.QLineEdit(self.centralwidget)
        self.leP9C1.setGeometry(QtCore.QRect(80, 240, 51, 31))
        self.leP9C1.setObjectName("leP9C1")
        self.textEditPlayer9 = QtGui.QTextEdit(self.centralwidget)
        self.textEditPlayer9.setGeometry(QtCore.QRect(50, 210, 171, 31))
        self.textEditPlayer9.setObjectName("textEditPlayer9")
        self.textEditWinPer = QtGui.QTextEdit(self.centralwidget)
        self.textEditWinPer.setGeometry(QtCore.QRect(630, 450, 121, 31))
        self.textEditWinPer.setObjectName("textEditWinPer")
        self.textEditDrawPer = QtGui.QTextEdit(self.centralwidget)
        self.textEditDrawPer.setGeometry(QtCore.QRect(760, 450, 131, 31))
        self.textEditDrawPer.setObjectName("textEditDrawPer")
        self.leCalculateDraw = QtGui.QLineEdit(self.centralwidget)
        self.leCalculateDraw.setGeometry(QtCore.QRect(770, 490, 101, 31))
        self.leCalculateDraw.setObjectName("leCalculateDraw")
        self.leFlop2 = QtGui.QLineEdit(self.centralwidget)
        self.leFlop2.setGeometry(QtCore.QRect(290, 220, 51, 31))
        self.leFlop2.setObjectName("leFlop2")
        self.leFlop1 = QtGui.QLineEdit(self.centralwidget)
        self.leFlop1.setGeometry(QtCore.QRect(240, 220, 51, 31))
        self.leFlop1.setObjectName("leFlop1")
        self.textEditFlop = QtGui.QTextEdit(self.centralwidget)
        self.textEditFlop.setGeometry(QtCore.QRect(290, 190, 51, 31))
        self.textEditFlop.setObjectName("textEditFlop")
        self.leTurn = QtGui.QLineEdit(self.centralwidget)
        self.leTurn.setGeometry(QtCore.QRect(440, 220, 51, 31))
        self.leTurn.setObjectName("leTurn")
        self.leFlop3 = QtGui.QLineEdit(self.centralwidget)
        self.leFlop3.setGeometry(QtCore.QRect(340, 220, 51, 31))
        self.leFlop3.setObjectName("leFlop3")
        self.textEditTurn = QtGui.QTextEdit(self.centralwidget)
        self.textEditTurn.setGeometry(QtCore.QRect(440, 190, 51, 31))
        self.textEditTurn.setObjectName("textEditTurn")
        self.textEditRiver = QtGui.QTextEdit(self.centralwidget)
        self.textEditRiver.setGeometry(QtCore.QRect(570, 190, 51, 31))
        self.textEditRiver.setObjectName("textEditRiver")
        self.leRiver = QtGui.QLineEdit(self.centralwidget)
        self.leRiver.setGeometry(QtCore.QRect(570, 220, 51, 31))
        self.leRiver.setObjectName("leRiver")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditNumSims.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Number of Simulations</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.btnCalculate.setText(QtGui.QApplication.translate("MainWindow", "Calculate Odds", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer1.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Your Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditNumOpps.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Number of Opponents</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer2.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent One Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer3.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Two Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer4.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Three Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer5.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Four Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer6.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Five Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer7.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Six Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer8.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Seven Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditPlayer9.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Opponent Eigth Cards</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditWinPer.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Win percentage</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditDrawPer.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Draw Percentage</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditFlop.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Flop</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditTurn.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">Turn</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.textEditRiver.setHtml(QtGui.QApplication.translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:8pt;\">River</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

