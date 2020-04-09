import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Window")
        self.resize(400, 600)
        self.move(10, 20)
        
        self.openFileNameDialog()
        self.show()
        
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","CSV Files (*.csv)", options=options)
        
        if fileName:
            print(fileName)
                    
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    gui = GUI()
    
    #
    sys.exit(app.exec_())