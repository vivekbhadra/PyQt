import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy, QTextEdit, QMessageBox
from PyQt5.QtCore import *
import csv

class Calculations(QWidget):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Tax Calculation")
        self.resize(400, 600) 
        self.slabel = QLabel()
        
        vLayout = QVBoxLayout()
        vLayout.setAlignment(Qt.AlignCenter | Qt.AlignLeft)
        vLayout.addWidget(self.slabel)
        
        self.setLayout(vLayout)
        
        
class GUI(QWidget):
    def __init__(self):
        super().__init__()
        
        self.dialog = Calculations()
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle("FinMin")
        self.resize(400, 600)
        
        label = QLabel()
        label.setText("Please select your business bank statements ")  
        
        browseButton = QPushButton("Browse")
        browseButton.clicked.connect(self.openFileNameDialog)
        
        gLayout = QGridLayout() 
        gLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        gLayout.addWidget(label, 0, 0)
        gLayout.addWidget(browseButton, 0, 1)
        
        self.textLabel = QLabel(margin=20)
        gLayout.addWidget(self.textLabel, 1, 0)
        
        runButton  = QPushButton()
        runButton.setText("Run")
        runButton.clicked.connect(self.parseFile)
        
        hLayout = QHBoxLayout() 
        hLayout.setAlignment(Qt.AlignBottom | Qt.AlignCenter)
        hLayout.addWidget(runButton)
        
        layout = QVBoxLayout()
        layout.addLayout(gLayout)
        layout.addLayout(hLayout)
        
        self.setLayout(layout)
        self.show()
        
    def parseFile(self):
        if self.fileNames:
            grandTotal = 0.0
            vat = 0.0
            for filename in self.fileNames:
                fileTotal = 0.0
                with open(filename, newline='') as csvfile:
                    print(filename)
                    reader = csv.DictReader(csvfile)
                    
                    for row in reader:
                        strVal = row['Paid In']
                        if strVal:
                            fltVal = float(strVal)
                            fileTotal = fileTotal + fltVal
                    print(fileTotal)
                grandTotal = grandTotal + fileTotal
                vat = grandTotal * 0.165
            print ("VAT: {0:.2f}".format(vat))
            self.dialog.slabel.setText(str(vat))
            self.dialog.show()
            
            
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
        self.fileNames, _ = QFileDialog.getOpenFileNames(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)", options=options)
        
        if self.fileNames:
            str = ""
            for file in self.fileNames:
                try:
                    str = str + file + "\n"
                except Exception as e:
                    message = QMessageBox(f"Could not set file: {e}")
                    message.show()
            self.textLabel.setText(str)
                    
                    
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    gui = GUI()
    
    #
    sys.exit(app.exec_())