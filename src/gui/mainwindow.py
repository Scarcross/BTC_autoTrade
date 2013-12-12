# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created: Thu Dec 12 22:10:55 2013
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1023, 616)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_status = QtGui.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(880, 530, 91, 21))
        self.label_status.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_status.setAutoFillBackground(False)
        self.label_status.setStyleSheet(_fromUtf8("background-color :red; color : black;border: 1px dotted black"))
        self.label_status.setIndent(6)
        self.label_status.setOpenExternalLinks(False)
        self.label_status.setObjectName(_fromUtf8("label_status"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(190, 10, 781, 391))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 151, 391))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 420, 151, 141))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_btc = QtGui.QLabel(self.groupBox_3)
        self.label_btc.setGeometry(QtCore.QRect(10, 20, 31, 21))
        self.label_btc.setObjectName(_fromUtf8("label_btc"))
        self.label_ltc = QtGui.QLabel(self.groupBox_3)
        self.label_ltc.setGeometry(QtCore.QRect(10, 50, 31, 21))
        self.label_ltc.setObjectName(_fromUtf8("label_ltc"))
        self.label_eur = QtGui.QLabel(self.groupBox_3)
        self.label_eur.setGeometry(QtCore.QRect(10, 110, 31, 21))
        self.label_eur.setObjectName(_fromUtf8("label_eur"))
        self.fund_ltc = QtGui.QLabel(self.groupBox_3)
        self.fund_ltc.setGeometry(QtCore.QRect(40, 50, 31, 21))
        self.fund_ltc.setText(_fromUtf8(""))
        self.fund_ltc.setObjectName(_fromUtf8("fund_ltc"))
        self.fund_btc = QtGui.QLabel(self.groupBox_3)
        self.fund_btc.setGeometry(QtCore.QRect(40, 20, 31, 21))
        self.fund_btc.setText(_fromUtf8(""))
        self.fund_btc.setObjectName(_fromUtf8("fund_btc"))
        self.label_usd = QtGui.QLabel(self.centralwidget)
        self.label_usd.setGeometry(QtCore.QRect(20, 500, 31, 21))
        self.label_usd.setObjectName(_fromUtf8("label_usd"))
        self.fund_usd = QtGui.QLabel(self.centralwidget)
        self.fund_usd.setGeometry(QtCore.QRect(50, 500, 31, 21))
        self.fund_usd.setText(_fromUtf8(""))
        self.fund_usd.setObjectName(_fromUtf8("fund_usd"))
        self.fund_eur = QtGui.QLabel(self.centralwidget)
        self.fund_eur.setGeometry(QtCore.QRect(50, 530, 31, 21))
        self.fund_eur.setText(_fromUtf8(""))
        self.fund_eur.setObjectName(_fromUtf8("fund_eur"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1023, 18))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuMen = QtGui.QMenu(self.menubar)
        self.menuMen.setObjectName(_fromUtf8("menuMen"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.actionConnect = QtGui.QAction(MainWindow)
        self.actionConnect.setObjectName(_fromUtf8("actionConnect"))
        self.actionBeenden = QtGui.QAction(MainWindow)
        self.actionBeenden.setObjectName(_fromUtf8("actionBeenden"))
        self.menuMen.addAction(self.actionConnect)
        self.menuMen.addSeparator()
        self.menuMen.addAction(self.actionBeenden)
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "BTC_autoTrade", None))
        self.label_status.setText(_translate("MainWindow", "Disconnected", None))
        self.groupBox.setTitle(_translate("MainWindow", "Chart", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Preferences", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Funds", None))
        self.label_btc.setText(_translate("MainWindow", "BTC", None))
        self.label_ltc.setText(_translate("MainWindow", "LTC", None))
        self.label_eur.setText(_translate("MainWindow", "EUR", None))
        self.label_usd.setText(_translate("MainWindow", "USD", None))
        self.menuMen.setTitle(_translate("MainWindow", "Menü", None))
        self.actionConnect.setText(_translate("MainWindow", "Connect", None))
        self.actionBeenden.setText(_translate("MainWindow", "Beenden", None))

