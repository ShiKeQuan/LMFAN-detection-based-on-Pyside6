# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUIresultwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QPushButton, QSizePolicy, QSpacerItem, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
import YOLOSHOWUI_rc

class Ui_ResultsWindow(object):
    def setupUi(self, ResultsWindow):
        if not ResultsWindow.objectName():
            ResultsWindow.setObjectName(u"ResultsWindow")
        ResultsWindow.resize(421, 500)
        icon = QIcon()
        icon.addFile(u":/jiaoda/images/physics2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        ResultsWindow.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(ResultsWindow)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.table_widget = QTableWidget(ResultsWindow)
        if (self.table_widget.columnCount() < 4):
            self.table_widget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_widget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table_widget.horizontalHeader().setStretchLastSection(True)

        self.verticalLayout.addWidget(self.table_widget)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.remove_button = QPushButton(ResultsWindow)
        self.remove_button.setObjectName(u"remove_button")

        self.horizontalLayout.addWidget(self.remove_button)

        self.clear_button = QPushButton(ResultsWindow)
        self.clear_button.setObjectName(u"clear_button")

        self.horizontalLayout.addWidget(self.clear_button)

        self.save_button = QPushButton(ResultsWindow)
        self.save_button.setObjectName(u"save_button")

        self.horizontalLayout.addWidget(self.save_button)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(ResultsWindow)

        QMetaObject.connectSlotsByName(ResultsWindow)
    # setupUi

    def retranslateUi(self, ResultsWindow):
        ResultsWindow.setWindowTitle(QCoreApplication.translate("ResultsWindow", u"\u9762\u5411SAR\u56fe\u50cf\u8230\u8239\u76ee\u6807\u7684\u591a\u5c3a\u5ea6\u8f7b\u91cf\u5316\u68c0\u6d4b\u7814\u7a76-\u68c0\u6d4b\u7ed3\u679c  Shi Kequan", None))
        ___qtablewidgetitem = self.table_widget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("ResultsWindow", u"\u56fe\u7247\u540d\u5b57", None));
        ___qtablewidgetitem1 = self.table_widget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("ResultsWindow", u"\u56fe\u7247\u5c3a\u5bf8", None));
        ___qtablewidgetitem2 = self.table_widget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("ResultsWindow", u"\u68c0\u6d4b\u5185\u5bb9", None));
        ___qtablewidgetitem3 = self.table_widget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("ResultsWindow", u"\u63a8\u7406\u901f\u5ea6 (ms)", None));
        self.remove_button.setText(QCoreApplication.translate("ResultsWindow", u"Remove", None))
        self.clear_button.setText(QCoreApplication.translate("ResultsWindow", u"Clear", None))
        self.save_button.setText(QCoreApplication.translate("ResultsWindow", u"Save", None))
    # retranslateUi

