import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

class GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle("Hello PyQt")
        self.resize(400, 600)
            
if __name__ == "__main__": 
    app = QApplication(sys.argv)
    gui = GUI()

    #win.resize(400, 600)

    gui.show()
    sys.exit(app.exec_())