'''
Created on 15.12.2013

@author: scarcross
'''
from mainwindow import Ui_MainWindow
from pyqtgraph.Qt import QtGui, QtCore
from PyQt4.QtGui  import QTableWidget, QTableWidgetItem


class MyGUI(QtGui.QMainWindow, Ui_MainWindow):
    
    TABLE_HORI_HEADER = ["Zeit", "Vorgang", "Preis"]
    __synch = None
    __mainWindow = None
    __api = None

    def __init__(self, Synchronize=None, BTCApi = None):
        QtGui.QMainWindow.__init__(self)
        self.__synch = Synchronize
        self.__api = BTCApi
        self.setupUi(self)
        self.setupSlots()
        
        self.logTable.setColumnCount(3)
        self.logTable.setHorizontalHeaderLabels(self.TABLE_HORI_HEADER)
        
    
     
    def setupSlots(self):
        self.connect(self.dSBAmountLTC, QtCore.SIGNAL('valueChanged(double)'),self.checkValueLTC)     
        self.connect(self.dSBFee, QtCore.SIGNAL('valueChanged(double)'),self.checkValueFees)      
        self.connect(self.actionConnect, QtCore.SIGNAL('triggered()'),self.tryConnect)     
        #self.connect(self.cB_updateInterval, QtCore.SIGNAL('currentIndexChanged(int)'),self.quit())   

    def tryConnect(self):
        self.__api.connect()
        self.setInitialValues()
        self.label_status.setStyleSheet("QLabel { background-color : green; color : black; border: 1px dotted black}")
        self.label_status.setText("Connected ")

    def setInitialValues(self):
       ''' data = self.__api.getInfo()
        data = data[BTCEStatic.JSON_RETURN][BTCEStatic.JSON_FUNDS]
        self.fund_btc.setText(str(data[BTCEStatic.JSON_BTC]))
        self.fund_ltc.setText(str(data[BTCEStatic.JSON_LTC]))
        self.fund_usd.setText(str(data[BTCEStatic.JSON_USD]))
        self.fund_eur.setText(str(data[BTCEStatic.JSON_EUR]))'''

    def checkValueLTC(self):
        print ("Kack")  
        
    def checkValueFees(self):
        print ("Kack")  
   
    def quit(self):
        self.close()
        
        
    def addTableRow(self, entries):
        
        self.logTable.setRowCount(len(entries))
        self.logTable.setColumnCount(len(entries[0]))
        
        for i, row in enumerate(entries):
            for j, col in enumerate(row):
                item = QTableWidgetItem(col)
                self.logTable.setItem(i, j, item)
    
    