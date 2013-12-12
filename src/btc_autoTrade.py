import sys
import json

from PyQt4 import QtGui, QtCore
from gui.mainwindow import Ui_MainWindow as Dlg
from http.btceapi import BTCApi
 

class Main():

    __dlg = None
    __mainWindow = None
    __btcAPI = None
    
    #Konstruktor
    def __init__(self):
        self.setupGui()
        self.setupSlots()
        self.__btcAPI = BTCApi()

    def setupGui(self):
        self.__dlg = Dlg()
        self.__mainWindow =  QtGui.QMainWindow()
        self.__dlg.setupUi(self.__mainWindow)
        self.__mainWindow.show()


    def setupSlots(self):
        self.__mainWindow.connect(self.__dlg.actionConnect, QtCore.SIGNAL('triggered()'),self.connect)     
        self.__mainWindow.connect(self.__dlg.actionBeenden, QtCore.SIGNAL('triggered()'),self.quit)     


    def connect(self):
        data = self.__btcAPI.getInfo()
        if  (1 == data['success']):
            self.setInitialValues(data)
            self.__dlg.label_status.setStyleSheet("QLabel { background-color : green; color : black; border: 1px dotted black}")
            self.__dlg.label_status.setText("Connected ")  
        
    def quit(self):
        self.__mainWindow.close()
        
    def setInitialValues(self,data):
        data = data['return']['funds']
        self.__dlg.fund_btc.setText(str(data['btc']))
        self.__dlg.fund_ltc.setText(str(data['ltc']))
        self.__dlg.fund_usd.setText(str(data['usd']))
        self.__dlg.fund_eur.setText(str(data['eur']))
        
        
def main():
    if len(sys.argv)==1:
        app = QtGui.QApplication(sys.argv)
        main = Main()
        sys.exit(app.exec_())

if __name__=='__main__':
    main()  

        
        
    