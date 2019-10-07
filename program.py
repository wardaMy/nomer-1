import sys 
from PyQt5 import QtWidgets, QtCore 
class demowind(QtWidgets.QWidget):     
	def __init__(self, parent=None):         
		QtWidgets.QWidget.__init__(self, parent) 
		self.setGeometry(350, 100, 350, 100)         
		self.setWindowTitle('Demo window')         
		self.quit = QtWidgets.QPushButton('Close', self)         
		self.quit.setGeometry(70, 30, 50, 50)         
		self.quit.clicked.connect(self.close)    
		self.quit2 = QtWidgets.QPushButton('Close', self)         
		self.quit2.setGeometry(200, 30, 50, 50)         
		self.quit2.clicked.connect(self.close)
app = QtWidgets.QApplication(sys.argv) 
dw = demowind() 
dw.show() 
sys.exit(app.exec_()) 
