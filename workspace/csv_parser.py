import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QAction, QFileDialog, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QGridLayout, QPushButton, QSizePolicy, QTextEdit, QMessageBox
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont
import csv

class Calculations(QWidget):
    def __init__(self):
        super().__init__()
        
        # Font for field labels
        labelFont = QFont()
        labelFont.setFamily('Helvetica [Cronyx]')
        labelFont.setPointSize(8)
        labelFont.setWeight(QFont.DemiBold)
        
        # Font for field values
        valueFont = QFont()
        valueFont.setFamily('Courier')
        valueFont.setPointSize(8)
        valueFont.setWeight(QFont.Courier)        
        
        self.setWindowTitle("Tax Calculation")
        self.resize(400, 600) 
        self.vatlabel = QLabel("VAT")
        self.vatlabel.setFont(labelFont)
        
        self.vatvalue = QLabel()
        self.vatvalue.setFont(valueFont)
        hLayout = QHBoxLayout()
        hLayout.addWidget(self.vatlabel)
        hLayout.addWidget(self.vatvalue)
        hLayout.setAlignment(Qt.AlignTop | Qt.AlignLeft)
        
        vLayout = QVBoxLayout()
        vLayout.addLayout(hLayout)
        
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
            self.dialog.vatvalue.setText(str(vat))
            self.dialog.show()
        
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

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.fileNames = []
        self.dialog = Calculations()
        self.initUI()
        
    def initUI(self):
        
        self.setWindowTitle("FinMin Home")
        self.resize(400, 250)
        
        self.setCentralWidget(QWidget())
        
        lBankStatements = QLabel("Business Bank Statements")
        uploadButton = QPushButton("Upload")
        uploadButton.clicked.connect(self.openFileNameDialog)
        
        bankStatementLayer = QHBoxLayout()
        bankStatementLayer.setAlignment(Qt.AlignTop | Qt.AlignCenter)
        bankStatementLayer.addWidget(lBankStatements)
        bankStatementLayer.addWidget(uploadButton)
        
        vatButton = QPushButton("VAT")
        
        corpTaxButton = QPushButton("Corp Tax")
        
        hLayout = QHBoxLayout()
        hLayout.addWidget(vatButton)
        hLayout.addWidget(corpTaxButton)
        
        vLayout = QVBoxLayout()
        vLayout.addLayout(bankStatementLayer)
        vLayout.addLayout(hLayout)
        
        self.centralWidget().setLayout(vLayout)
        self.show()
        QMessageBox.about(self, "Welcome!", "Welcome to FinMin Evaluation version")
        
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
            QMessageBox.about(self, "Bank Statements", str)       
        
        
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    #gui = GUI()
    mainWin = MainWindow()
    
    #
    sys.exit(app.exec_())