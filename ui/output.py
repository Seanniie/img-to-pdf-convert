# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QProgressBar,
    QPushButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(260, 396)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 260, 71))
        self.label.setMinimumSize(QSize(0, 71))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)
        self.clickGridpushButton = QPushButton(Form)
        self.clickGridpushButton.setObjectName(u"clickGridpushButton")
        self.clickGridpushButton.setGeometry(QRect(80, 190, 91, 31))
        self.clickGridpushButton.setStyleSheet(u"font: 75 9pt \"Arial\";\n"
"font-weight: bold;")
        self.xLeftLineEdit = QLineEdit(Form)
        self.xLeftLineEdit.setObjectName(u"xLeftLineEdit")
        self.xLeftLineEdit.setGeometry(QRect(39, 95, 71, 21))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(19, 100, 14, 14))
        self.label_2.setStyleSheet(u"font-weight: bold;")
        self.yLeftLineEdit = QLineEdit(Form)
        self.yLeftLineEdit.setObjectName(u"yLeftLineEdit")
        self.yLeftLineEdit.setGeometry(QRect(39, 132, 71, 20))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(19, 137, 14, 14))
        self.label_3.setStyleSheet(u"text-align: center;\n"
"")
        self.progressBar = QProgressBar(Form)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(40, 350, 201, 21))
        self.progressBar.setValue(24)
        self.totalLabel = QLabel(Form)
        self.totalLabel.setObjectName(u"totalLabel")
        self.totalLabel.setGeometry(QRect(140, 300, 18, 12))
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(120, 300, 6, 12))
        self.currentLabel = QLabel(Form)
        self.currentLabel.setObjectName(u"currentLabel")
        self.currentLabel.setGeometry(QRect(90, 300, 18, 12))
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 250, 75, 23))
        self.pushButton.setStyleSheet(u"font: 75 9pt \"Arial\";\n"
"font-weight: bold;")
        self.stopPushButton = QPushButton(Form)
        self.stopPushButton.setObjectName(u"stopPushButton")
        self.stopPushButton.setGeometry(QRect(140, 250, 75, 23))
        self.stopPushButton.setStyleSheet(u"font-weight: bold;")
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 70, 56, 12))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(163, 70, 56, 12))
        self.xRightLineEdit = QLineEdit(Form)
        self.xRightLineEdit.setObjectName(u"xRightLineEdit")
        self.xRightLineEdit.setGeometry(QRect(152, 95, 71, 20))
        self.yRightLineEdit = QLineEdit(Form)
        self.yRightLineEdit.setObjectName(u"yRightLineEdit")
        self.yRightLineEdit.setGeometry(QRect(152, 132, 71, 20))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.label)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">\uc774\ubbf8\uc9c0 pdf \ubcc0\ud658\uae30</span></p></body></html>", None))
        self.clickGridpushButton.setText(QCoreApplication.translate("Form", u"\uc88c\ud45c\uc120\ud0dd\ud558\uae30", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">X:</p></body></html>", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:600;\">Y:</span></p></body></html>", None))
        self.totalLabel.setText(QCoreApplication.translate("Form", u"561", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"/", None))
        self.currentLabel.setText(QCoreApplication.translate("Form", u"131", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\uc2dc\uc791", None))
        self.stopPushButton.setText(QCoreApplication.translate("Form", u"\uc791\uc5c5\uc911\ub2e8", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\uc88c\uce21\uc0c1\ub2e8", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\uc6b0\uce21\ud558\ub2e8", None))
    # retranslateUi

