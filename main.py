import sys
from PipeDectectinUI import Ui_PipeDectection
from PyQt5.QtWidgets import QApplication,QMainWindow
from setting import Setting

if __name__=='__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_PipeDectection()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
     #Setting.setting_init()
     



