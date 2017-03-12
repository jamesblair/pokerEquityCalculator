import sys # We need sys so that we can pass argv to QApplication
from PySide.QtGui import *  
from PySide.QtCore import *
from pokerGuiAllPlayers import Ui_MainWindow
import calculatorClass

class mainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setupUi(self)
        self.assignWidgets()
	
	
    def assignWidgets(self):      
        self.btnCalculate.clicked.connect(self.showOdds)
        	
    def showOdds(self):
        cards = {}
        cards[0] = [str(self.leP1C1.text()),str(self.leP1C2.text())]
        cards[1] = [str(self.leP2C1.text()),str(self.leP2C2.text())]
        cards[2] = [str(self.leP3C1.text()),str(self.leP3C2.text())]
        cards[3] = [str(self.leP4C1.text()),str(self.leP4C2.text())]
        cards[4] = [str(self.leP5C1.text()),str(self.leP5C2.text())]
        cards[5] = [str(self.leP6C1.text()),str(self.leP6C2.text())]
        cards[6] = [str(self.leP7C1.text()),str(self.leP7C2.text())]        
        cards[7] = [str(self.leP8C1.text()),str(self.leP8C2.text())]        
        cards[8] = [str(self.leP9C1.text()),str(self.leP9C2.text())]
        if str(self.leFlop1.text()) and str(self.leFlop2.text()) and str(self.leFlop3.text()):
            cards['flop'] = [str(self.leFlop1.text()),str(self.leFlop2.text()),str(self.leFlop3.text())]
        if str(self.leTurn.text()):
            cards['turn'] = [str(self.leTurn.text())]
        if str(self.leRiver.text()):
            cards['turn'] = [str(self.leRiver.text())]
        win,draw = calculatorClass.monteCarloSimulationDict(cards,int(self.leNum.text()),int(self.leSims.text()))
        self.leCalculateWin.setText(str(100*win))
        self.leCalculateDraw.setText(str(100*draw))
	
    def closeEvent(self, event):    
        reply = QMessageBox.question(self, 'Message',
           "Are you sure to quit?", QMessageBox.Yes | 
           QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore() 					
				
if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWin = mainWindow()
	mainWin.show()
	ret = app.exec_()
	sys.exit( ret )