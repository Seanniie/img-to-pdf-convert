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
from PySide6.QtWidgets import (QApplication, QLabel, QRadioButton, QSizePolicy,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setEnabled(True)
        Form.resize(430, 368)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 430, 71))
        self.label.setMinimumSize(QSize(0, 71))
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setMargin(0)
        self.label_mode = QLabel(Form)
        self.label_mode.setObjectName(u"label_mode")
        self.label_mode.setGeometry(QRect(40, 80, 52, 16))
        self.radioButton_mouseClick = QRadioButton(Form)
        self.radioButton_mouseClick.setObjectName(u"radioButton_mouseClick")
        self.radioButton_mouseClick.setGeometry(QRect(145, 80, 75, 16))
        self.radioButton_drag = QRadioButton(Form)
        self.radioButton_drag.setObjectName(u"radioButton_drag")
        self.radioButton_drag.setGeometry(QRect(230, 80, 59, 16))
#if QT_CONFIG(shortcut)
        self.label.setBuddy(self.label)
#endif // QT_CONFIG(shortcut)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">\uc774\ubbf8\uc9c0 pdf \ubcc0\ud658\uae30</span></p></body></html>", None))
        self.label_mode.setText(QCoreApplication.translate("Form", u"<html><head/><body><p><span style=\" font-weight:600;\">\ubaa8\ub4dc\uc120\ud0dd</span></p></body></html>", None))
        self.radioButton_mouseClick.setText(QCoreApplication.translate("Form", u"\uc88c\ud45c \ud074\ub9ad", None))
        self.radioButton_drag.setText(QCoreApplication.translate("Form", u"\ub4dc\ub798\uadf8", None))
    # retranslateUi

