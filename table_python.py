from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5.QtWidgets import QTableWidgetItem

# Bu proje sinir ağları dahil edilerek  hücre şekli,sayısı ve histogram grafiği gibi bilgileri içeren tablodan oluşacaktır.

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
      
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 110, 631, 192))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(8)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 70, 221, 31))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.PlainText)
        self.label.setObjectName("label")
        self.pushButton_goster = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_goster.setGeometry(QtCore.QRect(550, 370, 101, 28))
        self.pushButton_goster.setObjectName("pushButton_goster")
        self.pushButton_veri = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_veri.setGeometry(QtCore.QRect(550, 420, 101, 28))
        self.pushButton_veri.setObjectName("pushButton_veri")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

       # Connect the button click signal to the corresponding slot
        self.pushButton_goster.clicked.connect(self.on_pushButton_goster_clicked)

    # ... (remaining code)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "hücre tipi"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "hücre büyüklüğü"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "ort.h.büyüklüğü"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "top.h.sayısı"))
        self.label.setText(_translate("MainWindow", "Hücre Bilgileri"))
        self.pushButton_goster.setText(_translate("MainWindow", "göster"))
        self.pushButton_veri.setText(_translate("MainWindow", "ekle"))
        
    def display_image(self):
        resim = cv2.imread("kokh.png")
            # Ensure the image is not None
        # assert resim is not None, "Image file could not be read, check with os.path.exists()"
        #     # Resize the image to fit the window
        # resim = cv2.resize(resim, (self.tableWidget.width(), self.tableWidget.height()))
        cv2.imshow("kok hucre", resim)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
         
    def plot_histogram(self):
        img = cv2.imread('kokh.png', cv2.IMREAD_GRAYSCALE)
        assert img is not None, "file could not be read, check with os.path.exists()"
        plt.hist(img.ravel(), 256, [0, 256])
        plt.show()
        
    def on_pushButton_goster_clicked(self):
        self.display_image()
        self.plot_histogram()
        # self.on_pushButton_veri_clicked()
        rowPosition = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.insertRow(rowPosition)
        self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem("Ifhfhf"))
        self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem("Hücre Tipi"))
        self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem("Hücre Büyüklüğü"))
        self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem("Ort. H. Büyüklüğü"))
        self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem("Toplam H. Sayısı"))    
        
       
    # def on_pushButton_veri_clicked(self):
    #     # Yeni bir satır ekleyin
    #     rowPosition = self.tableWidget.rowCount()
    #     self.tableWidget.insertRow(rowPosition)

    #     # Örnek veri ekleyin (bu kısmı kendi verilerinizle değiştirebilirsiniz)
        
    #     self.tableWidget.setItem(rowPosition, 0, QTableWidgetItem("Ifhfhf"))
    #     self.tableWidget.setItem(rowPosition, 1, QTableWidgetItem("Hücre Tipi"))
    #     self.tableWidget.setItem(rowPosition, 2, QTableWidgetItem("Hücre Büyüklüğü"))
    #     self.tableWidget.setItem(rowPosition, 3, QTableWidgetItem("Ort. H. Büyüklüğü"))
    #     self.tableWidget.setItem(rowPosition, 4, QTableWidgetItem("Toplam H. Sayısı"))    
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
