import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy
from PyQt5.QtCore import *
import csv

class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("FinMin")
        self.resize(400, 600)
        
        label = QLabel()
        label.setText("Select File: ")  
        
        self.lineEdit = QLineEdit()
        self.lineEdit.setAlignment(Qt.AlignTop)
        
        button = QPushButton("Browse")
        button.clicked.connect(self.openFileNameDialog)
        
        gLayout = QGridLayout()
        gLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        gLayout.addWidget(label, 0, 0)
        gLayout.addWidget(self.lineEdit, 0, 1)
        gLayout.addWidget(button, 0, 2)
        self.setLayout(gLayout)
        
        calcButton  = QPushButton()
        calcButton.setText("Calculate")
        calcButton.clicked.connect(self.parseFile)
        
        self.label2 = QLabel()
        gLayout.addWidget(calcButton, 1, 0)
        gLayout.addWidget(self.label2, 1, 1)
          
        self.show()
        
    def parseFile(self):
        name = self.getFileName()
        
    def getFileName(self):
        return self.lineEdit.text()
        
    def createLabel(self):
        label = QLabel()
        label.setText("File Name") 
        return label
        
    def createEditLine(self):
        editBox = QLineEdit(self)
        return editBox
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,
                                                  "QFileDialog.getOpenFileName()", 
                                                  "",
                                                  "CSV Files (*.csv)", 
                                                  options=options)
        
        if fileName:
            self.lineEdit.setText(fileName)
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)", options=options)
        
        if fileName:
            self.lineEdit.setText(fileName)
                    
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    gui = GUI()
    
    #
    sys.exit(app.exec_())