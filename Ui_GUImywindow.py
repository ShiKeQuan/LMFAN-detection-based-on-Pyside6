# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'GUImywindow.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDoubleSpinBox,
    QFrame, QGroupBox, QHBoxLayout, QLabel,
    QMainWindow, QPushButton, QSizePolicy, QSplitter,
    QTabWidget, QVBoxLayout, QWidget)
import YOLOSHOWUI_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(637, 588)
        MainWindow.setMinimumSize(QSize(631, 486))
        MainWindow.setMaximumSize(QSize(50000, 50000))
        icon = QIcon()
        icon.addFile(u":/jiaoda/images/physics2.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 641, 591))
        self.tabWidget.setContextMenuPolicy(Qt.ContextMenuPolicy.DefaultContextMenu)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.label_school = QLabel(self.tab)
        self.label_school.setObjectName(u"label_school")
        self.label_school.setGeometry(QRect(450, 60, 161, 51))
        self.label_school.setPixmap(QPixmap(u":/jiaoda/images/swjtu.png"))
        self.label_school.setScaledContents(True)
        self.showwindow = QGroupBox(self.tab)
        self.showwindow.setObjectName(u"showwindow")
        self.showwindow.setGeometry(QRect(10, 120, 611, 301))
        font = QFont()
        font.setFamilies([u"Times New Roman"])
        font.setPointSize(12)
        font.setBold(True)
        self.showwindow.setFont(font)
        self.showwindow.setStyleSheet(u"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* \u5c06\u6807\u9898\u7f6e\u4e8e\u9876\u90e8\u4e2d\u592e */\n"
"    padding: 0 3px;\n"
"}")
        self.rightbox_main = QFrame(self.showwindow)
        self.rightbox_main.setObjectName(u"rightbox_main")
        self.rightbox_main.setGeometry(QRect(10, 20, 591, 271))
        self.rightbox_main.setStyleSheet(u"")
        self.rightbox_main.setFrameShape(QFrame.Shape.StyledPanel)
        self.rightbox_main.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.rightbox_main)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.splitter = QSplitter(self.rightbox_main)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Orientation.Horizontal)
        self.image_label_input = QLabel(self.splitter)
        self.image_label_input.setObjectName(u"image_label_input")
        self.image_label_input.setMinimumSize(QSize(200, 100))
        self.splitter.addWidget(self.image_label_input)
        self.image_label_output = QLabel(self.splitter)
        self.image_label_output.setObjectName(u"image_label_output")
        self.image_label_output.setMinimumSize(QSize(200, 100))
        self.splitter.addWidget(self.image_label_output)

        self.horizontalLayout_9.addWidget(self.splitter)

        self.showresult = QGroupBox(self.tab)
        self.showresult.setObjectName(u"showresult")
        self.showresult.setGeometry(QRect(10, 450, 611, 101))
        self.showresult.setFont(font)
        self.showresult.setStyleSheet(u"\n"
"QGroupBox {\n"
"    background-color: qlineargradient(spread:reflect, x1:1, y1:0.544, x2:1, y2:0, stop:0.384615 rgba(37, 157, 255, 230), stop:1 rgba(255, 255, 255, 255))}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* \u5c06\u6807\u9898\u7f6e\u4e8e\u9876\u90e8\u4e2d\u592e */\n"
"    padding: 0 3px;\n"
"}")
        self.Class_QF_2 = QFrame(self.showresult)
        self.Class_QF_2.setObjectName(u"Class_QF_2")
        self.Class_QF_2.setGeometry(QRect(60, 20, 90, 75))
        self.Class_QF_2.setMinimumSize(QSize(50, 30))
        self.Class_QF_2.setMaximumSize(QSize(1000, 80))
        self.Class_QF_2.setToolTipDuration(0)
        self.Class_QF_2.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color:qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0  #97D9E1,  stop:1   #8EC5FC);\n"
"border: 1px outset #97D9E1;\n"
"}\n"
"")
        self.Class_QF_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_QF_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.Class_QF_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.Class_QF_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 30))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(16)
        font1.setBold(True)
        font1.setItalic(True)
        font1.setUnderline(False)
        font1.setStrikeOut(False)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color: rgba(255, 255,255, 210);\n"
"text-align:center;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_5.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_5.setIndent(0)

        self.verticalLayout.addWidget(self.label_5)

        self.line_6 = QFrame(self.Class_QF_2)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setMaximumSize(QSize(16777215, 1))
        self.line_6.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_6.setFrameShape(QFrame.Shape.HLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_6)

        self.Class_num = QLabel(self.Class_QF_2)
        self.Class_num.setObjectName(u"Class_num")
        self.Class_num.setMinimumSize(QSize(0, 30))
        self.Class_num.setMaximumSize(QSize(16777215, 30))
        font2 = QFont()
        font2.setFamilies([u"Microsoft YaHei UI"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.Class_num.setFont(font2)
        self.Class_num.setStyleSheet(u"color: rgb(0, 196, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.Class_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.Class_num)

        self.Class_QF_3 = QFrame(self.showresult)
        self.Class_QF_3.setObjectName(u"Class_QF_3")
        self.Class_QF_3.setGeometry(QRect(210, 20, 90, 75))
        self.Class_QF_3.setMinimumSize(QSize(50, 30))
        self.Class_QF_3.setMaximumSize(QSize(1000, 80))
        self.Class_QF_3.setToolTipDuration(0)
        self.Class_QF_3.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color:qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0  #97D9E1,  stop:1   #8EC5FC);\n"
"border: 1px outset #97D9E1;\n"
"}\n"
"")
        self.Class_QF_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_QF_3.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Class_QF_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_6 = QLabel(self.Class_QF_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 30))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(16)
        font3.setBold(True)
        font3.setItalic(True)
        self.label_6.setFont(font3)
        self.label_6.setStyleSheet(u"color: rgba(255, 255,255, 210);\n"
"text-align:center;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_6.setIndent(0)

        self.verticalLayout_2.addWidget(self.label_6)

        self.line_7 = QFrame(self.Class_QF_3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setMaximumSize(QSize(16777215, 1))
        self.line_7.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_7.setFrameShape(QFrame.Shape.HLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_2.addWidget(self.line_7)

        self.Target_num = QLabel(self.Class_QF_3)
        self.Target_num.setObjectName(u"Target_num")
        self.Target_num.setMinimumSize(QSize(0, 30))
        self.Target_num.setMaximumSize(QSize(16777215, 30))
        self.Target_num.setFont(font2)
        self.Target_num.setStyleSheet(u"color: rgb(0, 196, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.Target_num.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_2.addWidget(self.Target_num)

        self.Class_QF_4 = QFrame(self.showresult)
        self.Class_QF_4.setObjectName(u"Class_QF_4")
        self.Class_QF_4.setGeometry(QRect(360, 20, 90, 75))
        self.Class_QF_4.setMinimumSize(QSize(50, 30))
        self.Class_QF_4.setMaximumSize(QSize(1000, 80))
        self.Class_QF_4.setToolTipDuration(0)
        self.Class_QF_4.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color:qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0  #97D9E1,  stop:1   #8EC5FC);\n"
"border: 1px outset #97D9E1;\n"
"}\n"
"")
        self.Class_QF_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_QF_4.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.Class_QF_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_7 = QLabel(self.Class_QF_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMaximumSize(QSize(16777215, 30))
        self.label_7.setFont(font3)
        self.label_7.setStyleSheet(u"color: rgba(255, 255,255, 210);\n"
"text-align:center;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_7.setMidLineWidth(-1)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_7.setWordWrap(False)
        self.label_7.setIndent(0)

        self.verticalLayout_3.addWidget(self.label_7)

        self.line_8 = QFrame(self.Class_QF_4)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setMaximumSize(QSize(16777215, 1))
        self.line_8.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_8.setFrameShape(QFrame.Shape.HLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_3.addWidget(self.line_8)

        self.fps_label = QLabel(self.Class_QF_4)
        self.fps_label.setObjectName(u"fps_label")
        self.fps_label.setMinimumSize(QSize(0, 30))
        self.fps_label.setMaximumSize(QSize(16777215, 30))
        self.fps_label.setFont(font2)
        self.fps_label.setStyleSheet(u"color: rgb(0, 196, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.fps_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_3.addWidget(self.fps_label)

        self.Class_QF_5 = QFrame(self.showresult)
        self.Class_QF_5.setObjectName(u"Class_QF_5")
        self.Class_QF_5.setGeometry(QRect(510, 20, 90, 75))
        self.Class_QF_5.setMinimumSize(QSize(50, 30))
        self.Class_QF_5.setMaximumSize(QSize(1000, 80))
        self.Class_QF_5.setToolTipDuration(0)
        self.Class_QF_5.setStyleSheet(u"QFrame#Class_QF{\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 15px;\n"
"background-color:qradialgradient(cx:0, cy:0, radius:1, fx:0.1, fy:0.1, stop:0  #97D9E1,  stop:1   #8EC5FC);\n"
"border: 1px outset #97D9E1;\n"
"}\n"
"")
        self.Class_QF_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.Class_QF_5.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.Class_QF_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_8 = QLabel(self.Class_QF_5)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 30))
        self.label_8.setFont(font3)
        self.label_8.setStyleSheet(u"color: rgba(255, 255,255, 210);\n"
"text-align:center;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_8.setMidLineWidth(-1)
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_8.setWordWrap(False)
        self.label_8.setIndent(0)

        self.verticalLayout_4.addWidget(self.label_8)

        self.line_9 = QFrame(self.Class_QF_5)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setMaximumSize(QSize(16777215, 1))
        self.line_9.setStyleSheet(u"background-color: rgba(255, 255, 255, 89);")
        self.line_9.setFrameShape(QFrame.Shape.HLine)
        self.line_9.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_4.addWidget(self.line_9)

        self.Model_label = QLabel(self.Class_QF_5)
        self.Model_label.setObjectName(u"Model_label")
        self.Model_label.setMinimumSize(QSize(0, 30))
        self.Model_label.setMaximumSize(QSize(16777215, 30))
        self.Model_label.setFont(font2)
        self.Model_label.setStyleSheet(u"color: rgb(0, 196, 255);\n"
"font: 10pt \"Microsoft YaHei UI\";")
        self.Model_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.Model_label)

        self.pushButton_un = QPushButton(self.showresult)
        self.pushButton_un.setObjectName(u"pushButton_un")
        self.pushButton_un.setGeometry(QRect(460, 20, 50, 75))
        icon1 = QIcon()
        icon1.addFile(u":/statusbarVS/images/newsize/modelBarVS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_un.setIcon(icon1)
        self.pushButton_un.setIconSize(QSize(40, 40))
        self.pushButton_un_2 = QPushButton(self.showresult)
        self.pushButton_un_2.setObjectName(u"pushButton_un_2")
        self.pushButton_un_2.setGeometry(QRect(310, 20, 50, 75))
        icon2 = QIcon()
        icon2.addFile(u":/statusbarVS/images/newsize/fpsBarVS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_un_2.setIcon(icon2)
        self.pushButton_un_2.setIconSize(QSize(40, 40))
        self.pushButton_un_3 = QPushButton(self.showresult)
        self.pushButton_un_3.setObjectName(u"pushButton_un_3")
        self.pushButton_un_3.setGeometry(QRect(160, 20, 50, 75))
        icon3 = QIcon()
        icon3.addFile(u":/statusbarVS/images/newsize/targetBarVS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_un_3.setIcon(icon3)
        self.pushButton_un_3.setIconSize(QSize(40, 40))
        self.pushButton_un_4 = QPushButton(self.showresult)
        self.pushButton_un_4.setObjectName(u"pushButton_un_4")
        self.pushButton_un_4.setEnabled(True)
        self.pushButton_un_4.setGeometry(QRect(10, 20, 50, 75))
        icon4 = QIcon()
        icon4.addFile(u":/statusbarVS/images/newsize/classesBarVS.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_un_4.setIcon(icon4)
        self.pushButton_un_4.setIconSize(QSize(40, 40))
        self.status_label = QLabel(self.tab)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(20, 425, 821, 21))
        font4 = QFont()
        font4.setFamilies([u"Times New Roman"])
        font4.setPointSize(11)
        font4.setBold(True)
        self.status_label.setFont(font4)
        self.Parameters = QGroupBox(self.tab)
        self.Parameters.setObjectName(u"Parameters")
        self.Parameters.setGeometry(QRect(10, 60, 411, 51))
        self.Parameters.setFont(font)
        self.Parameters.setStyleSheet(u"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top center; /* \u5c06\u6807\u9898\u7f6e\u4e8e\u9876\u90e8\u4e2d\u592e */\n"
"    padding: 0 3px;\n"
"}")
        self.doubleSpinBox_IOU = QDoubleSpinBox(self.Parameters)
        self.doubleSpinBox_IOU.setObjectName(u"doubleSpinBox_IOU")
        self.doubleSpinBox_IOU.setGeometry(QRect(70, 20, 87, 22))
        font5 = QFont()
        font5.setFamilies([u"Times New Roman"])
        font5.setPointSize(10)
        font5.setBold(True)
        self.doubleSpinBox_IOU.setFont(font5)
        self.doubleSpinBox_IOU.setMaximum(1.000000000000000)
        self.doubleSpinBox_IOU.setSingleStep(0.010000000000000)
        self.doubleSpinBox_IOU.setValue(0.500000000000000)
        self.doubleSpinBox_Conf = QDoubleSpinBox(self.Parameters)
        self.doubleSpinBox_Conf.setObjectName(u"doubleSpinBox_Conf")
        self.doubleSpinBox_Conf.setGeometry(QRect(220, 20, 87, 22))
        self.doubleSpinBox_Conf.setFont(font5)
        self.doubleSpinBox_Conf.setMaximum(1.000000000000000)
        self.doubleSpinBox_Conf.setSingleStep(0.010000000000000)
        self.doubleSpinBox_Conf.setValue(0.350000000000000)
        self.label_IOU = QLabel(self.Parameters)
        self.label_IOU.setObjectName(u"label_IOU")
        self.label_IOU.setGeometry(QRect(10, 20, 70, 21))
        self.label_IOU.setMaximumSize(QSize(16777215, 30))
        self.label_IOU.setFont(font1)
        self.label_IOU.setStyleSheet(u"color: rgba(255, 255,255, 210);\n"
"text-align:center;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_IOU.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_IOU.setIndent(0)
        self.label_Conf = QLabel(self.Parameters)
        self.label_Conf.setObjectName(u"label_Conf")
        self.label_Conf.setGeometry(QRect(160, 20, 70, 21))
        self.label_Conf.setMaximumSize(QSize(16777215, 30))
        self.label_Conf.setFont(font1)
        self.label_Conf.setStyleSheet(u"color: rgba(255, 255,255, 210);\n"
"text-align:center;\n"
"font: 700 italic 16pt \"Segoe UI\";")
        self.label_Conf.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_Conf.setIndent(0)
        self.checkBox_obb = QCheckBox(self.Parameters)
        self.checkBox_obb.setObjectName(u"checkBox_obb")
        self.checkBox_obb.setGeometry(QRect(320, 10, 91, 41))
        font6 = QFont()
        font6.setFamilies([u"Segoe UI"])
        font6.setPointSize(12)
        font6.setBold(True)
        font6.setItalic(True)
        self.checkBox_obb.setFont(font6)
        self.checkBox_obb.setStyleSheet(u"QCheckBox {\n"
"    color: #18b6ff; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QCheckBox::indicator {\n"
"	width: 25px;\n"
"	height: 25px;\n"
"}\n"
"\n"
"QCheckBox::indicator:unchecked {\n"
"	image: url(:/jiaoda/images/check_off.png);\n"
"}\n"
" \n"
"QCheckBox::indicator:checked {\n"
"	image: url(:/jiaoda/images/check_on.png);\n"
"}\n"
"")
        self.layoutWidget = QWidget(self.tab)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 621, 58))
        self.horizontalLayout_1 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.horizontalLayout_1.setContentsMargins(0, 0, 0, 0)
        self.label_Task = QLabel(self.layoutWidget)
        self.label_Task.setObjectName(u"label_Task")
        self.label_Task.setMaximumSize(QSize(40, 30))
        self.label_Task.setFont(font6)
        self.label_Task.setStyleSheet(u"color: #18b6ff; /* \u6587\u5b57\u989c\u8272 */\n"
"")

        self.horizontalLayout_1.addWidget(self.label_Task)

        self.comboBox_choose_task = QComboBox(self.layoutWidget)
        self.comboBox_choose_task.addItem("")
        self.comboBox_choose_task.addItem("")
        self.comboBox_choose_task.setObjectName(u"comboBox_choose_task")
        self.comboBox_choose_task.setMinimumSize(QSize(50, 30))

        self.horizontalLayout_1.addWidget(self.comboBox_choose_task)

        self.btn_select_model = QPushButton(self.layoutWidget)
        self.btn_select_model.setObjectName(u"btn_select_model")
        self.btn_select_model.setMinimumSize(QSize(60, 30))
        self.btn_select_model.setIcon(icon1)

        self.horizontalLayout_1.addWidget(self.btn_select_model)

        self.btn_select_image = QPushButton(self.layoutWidget)
        self.btn_select_image.setObjectName(u"btn_select_image")
        self.btn_select_image.setMinimumSize(QSize(50, 30))
        icon5 = QIcon()
        icon5.addFile(u":/leftbox/images/newsize/folder.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_select_image.setIcon(icon5)

        self.horizontalLayout_1.addWidget(self.btn_select_image)

        self.btn_detect = QPushButton(self.layoutWidget)
        self.btn_detect.setObjectName(u"btn_detect")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_detect.sizePolicy().hasHeightForWidth())
        self.btn_detect.setSizePolicy(sizePolicy)
        self.btn_detect.setMinimumSize(QSize(50, 30))
        self.btn_detect.setMaximumSize(QSize(70, 30))
        icon6 = QIcon()
        icon6.addFile(u":/rightbox/images/newsize/play.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_detect.setIcon(icon6)

        self.horizontalLayout_1.addWidget(self.btn_detect)

        self.src_Result_tab = QPushButton(self.layoutWidget)
        self.src_Result_tab.setObjectName(u"src_Result_tab")
        sizePolicy.setHeightForWidth(self.src_Result_tab.sizePolicy().hasHeightForWidth())
        self.src_Result_tab.setSizePolicy(sizePolicy)
        self.src_Result_tab.setMinimumSize(QSize(50, 30))
        self.src_Result_tab.setMaximumSize(QSize(16777215, 16777215))
        icon7 = QIcon()
        icon7.addFile(u":/leftbox/images/newsize/table.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.src_Result_tab.setIcon(icon7)
        self.src_Result_tab.setIconSize(QSize(16, 16))

        self.horizontalLayout_1.addWidget(self.src_Result_tab)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u9762\u5411SAR\u56fe\u50cf\u8230\u8239\u76ee\u6807\u7684\u591a\u5c3a\u5ea6\u8f7b\u91cf\u5316\u68c0\u6d4b\u7814\u7a76-\u53ef\u89c6\u5316\u64cd\u4f5c\u5e73\u53f0  Shi Kequan", None))
        self.label_school.setText("")
        self.showwindow.setTitle(QCoreApplication.translate("MainWindow", u"Show window", None))
        self.image_label_input.setText("")
        self.image_label_output.setText("")
        self.showresult.setTitle(QCoreApplication.translate("MainWindow", u"Results", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aaaaff;\">Classes</span></p></body></html>", None))
        self.Class_num.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aaaaff;\">Targets</span></p></body></html>", None))
        self.Target_num.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aaaaff;\">Fps</span></p></body></html>", None))
        self.fps_label.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#aaaaff;\">Model</span></p></body></html>", None))
        self.Model_label.setText("")
        self.pushButton_un.setText("")
        self.pushButton_un_2.setText("")
        self.pushButton_un_3.setText("")
        self.pushButton_un_4.setText("")
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"Status: Ready", None))
        self.Parameters.setTitle(QCoreApplication.translate("MainWindow", u"Setting Json", None))
        self.label_IOU.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#18b6ff;\">IoU:</span></p></body></html>", None))
        self.label_Conf.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt; color:#18b6ff;\">Conf:</span></p></body></html>", None))
#if QT_CONFIG(tooltip)
        self.checkBox_obb.setToolTip(QCoreApplication.translate("MainWindow", u"If you want to detect objects with rotation? Yes or No.", None))
#endif // QT_CONFIG(tooltip)
        self.checkBox_obb.setText(QCoreApplication.translate("MainWindow", u"Obb", None))
        self.label_Task.setText(QCoreApplication.translate("MainWindow", u"Task:", None))
        self.comboBox_choose_task.setItemText(0, QCoreApplication.translate("MainWindow", u"CNN-LMFAN", None))
        self.comboBox_choose_task.setItemText(1, QCoreApplication.translate("MainWindow", u"ViT-LMFAN", None))

        self.btn_select_model.setText(QCoreApplication.translate("MainWindow", u"Select Model (.pt)", None))
        self.btn_select_image.setText(QCoreApplication.translate("MainWindow", u"Select Image", None))
        self.btn_detect.setText(QCoreApplication.translate("MainWindow", u"Detect", None))
        self.src_Result_tab.setText(QCoreApplication.translate("MainWindow", u"    Result Tab  ", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"\u5de5\u4f5c\u68c0\u6d4b\u5e73\u53f0", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"\u5173\u4e8e", None))
    # retranslateUi

