# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'weight.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QGroupBox,
    QHBoxLayout, QLabel, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QSpacerItem, QStackedWidget,
    QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1024, 595)
        MainWindow.setStyleSheet(u"background-color: rgb(38, 38, 38);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMaximumSize(QSize(1024, 600))
        self.centralwidget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.screen_page = QWidget(self.centralwidget)
        self.screen_page.setObjectName(u"screen_page")
        self.verticalLayout_5 = QVBoxLayout(self.screen_page)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 0, 9, 0)
        self.widget = QWidget(self.screen_page)
        self.widget.setObjectName(u"widget")
        self.widget.setMinimumSize(QSize(0, 50))
        self.widget.setStyleSheet(u"background-color: rgb(100, 100, 100);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 8px;")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 0, 10, 0)
        self.frame_28 = QFrame(self.widget)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setEnabled(True)
        self.frame_28.setMinimumSize(QSize(0, 0))
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_28)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 75, 0)
        self.menu = QPushButton(self.frame_28)
        self.menu.setObjectName(u"menu")
        font = QFont()
        font.setPointSize(9)
        self.menu.setFont(font)
        self.menu.setCursor(QCursor(Qt.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u":/assets/icon/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/assets/icon/menu_open.png", QSize(), QIcon.Normal, QIcon.On)
        self.menu.setIcon(icon)
        self.menu.setIconSize(QSize(40, 40))
        self.menu.setCheckable(True)
        self.menu.setAutoExclusive(True)

        self.horizontalLayout_6.addWidget(self.menu)


        self.horizontalLayout.addWidget(self.frame_28)

        self.horizontalSpacer_5 = QSpacerItem(92, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.title = QLabel(self.widget)
        self.title.setObjectName(u"title")
        font1 = QFont()
        font1.setFamilies([u"Kanit"])
        font1.setPointSize(22)
        font1.setBold(True)
        self.title.setFont(font1)
        self.title.setStyleSheet(u"")
        self.title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.title)

        self.current_tabletID_1 = QLabel(self.widget)
        self.current_tabletID_1.setObjectName(u"current_tabletID_1")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_tabletID_1.sizePolicy().hasHeightForWidth())
        self.current_tabletID_1.setSizePolicy(sizePolicy)
        self.current_tabletID_1.setFont(font1)
        self.current_tabletID_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.current_tabletID_1)

        self.horizontalSpacer_4 = QSpacerItem(75, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.wifi_signal = QLabel(self.widget)
        self.wifi_signal.setObjectName(u"wifi_signal")
        self.wifi_signal.setMaximumSize(QSize(30, 30))
        self.wifi_signal.setPixmap(QPixmap(u":/assets/icon/no-wifi.png"))
        self.wifi_signal.setScaledContents(True)

        self.horizontalLayout.addWidget(self.wifi_signal)

        self.datetime_group_2 = QGroupBox(self.widget)
        self.datetime_group_2.setObjectName(u"datetime_group_2")
        font2 = QFont()
        font2.setPointSize(11)
        self.datetime_group_2.setFont(font2)
        self.datetime_group_2.setAlignment(Qt.AlignCenter)
        self.datetime_group = QVBoxLayout(self.datetime_group_2)
        self.datetime_group.setSpacing(0)
        self.datetime_group.setObjectName(u"datetime_group")
        self.datetime_group.setContentsMargins(0, 5, 0, 5)
        self.time_bar = QLabel(self.datetime_group_2)
        self.time_bar.setObjectName(u"time_bar")
        self.time_bar.setMaximumSize(QSize(100, 12))
        font3 = QFont()
        font3.setFamilies([u"Kanit"])
        font3.setPointSize(13)
        font3.setBold(False)
        self.time_bar.setFont(font3)
        self.time_bar.setAlignment(Qt.AlignCenter)

        self.datetime_group.addWidget(self.time_bar)

        self.date_bar = QLabel(self.datetime_group_2)
        self.date_bar.setObjectName(u"date_bar")
        self.date_bar.setMaximumSize(QSize(120, 12))
        self.date_bar.setFont(font3)
        self.date_bar.setAlignment(Qt.AlignCenter)

        self.datetime_group.addWidget(self.date_bar)


        self.horizontalLayout.addWidget(self.datetime_group_2)


        self.verticalLayout_5.addWidget(self.widget)

        self.stackedWidget = QStackedWidget(self.screen_page)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLayoutDirection(Qt.LeftToRight)
        self.stackedWidget.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(255, 255, 255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QGroupBox {\n"
"	border: none;\n"
"}\n"
"\n"
"#summary_weight_label_1, #summary_weight_label_2, #summary_average_label,  #summary_percent_label {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.verticalLayout_15 = QVBoxLayout(self.home_page)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.login_frame = QFrame(self.home_page)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setToolTipDuration(0)
        self.verticalLayout_7 = QVBoxLayout(self.login_frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 20)
        self.login_title = QFrame(self.login_frame)
        self.login_title.setObjectName(u"login_title")
        self.login_title.setMaximumSize(QSize(16777215, 80))
        self.login_title.setFrameShape(QFrame.StyledPanel)
        self.login_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.login_title)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(30, 0, 30, 0)
        self.rfid_alert = QLabel(self.login_title)
        self.rfid_alert.setObjectName(u"rfid_alert")
        self.rfid_alert.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setFamilies([u"Kanit"])
        font4.setPointSize(25)
        self.rfid_alert.setFont(font4)
        self.rfid_alert.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.rfid_alert.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.rfid_alert)


        self.verticalLayout_7.addWidget(self.login_title)

        self.scale_frame = QFrame(self.login_frame)
        self.scale_frame.setObjectName(u"scale_frame")
        self.horizontalLayout_5 = QHBoxLayout(self.scale_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 50, -1, 0)
        self.scale_img = QLabel(self.scale_frame)
        self.scale_img.setObjectName(u"scale_img")
        self.scale_img.setMaximumSize(QSize(300, 300))
        self.scale_img.setPixmap(QPixmap(u":/assets/images/scale.png"))
        self.scale_img.setScaledContents(True)
        self.scale_img.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.scale_img)


        self.verticalLayout_7.addWidget(self.scale_frame)

        self.rfid_frame = QFrame(self.login_frame)
        self.rfid_frame.setObjectName(u"rfid_frame")
        self.rfid_frame.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_4 = QHBoxLayout(self.rfid_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.rfid = QLabel(self.rfid_frame)
        self.rfid.setObjectName(u"rfid")
        self.rfid.setMaximumSize(QSize(370, 60))
        font5 = QFont()
        font5.setFamilies([u"Kanit"])
        font5.setPointSize(35)
        font5.setBold(True)
        self.rfid.setFont(font5)
        self.rfid.setStyleSheet(u"QLabel {\n"
"	color: rgb(100, 100, 100);\n"
"	border: solid;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-width: 3px;\n"
"	border-radius: 8px;\n"
"}")
        self.rfid.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_4.addWidget(self.rfid)


        self.verticalLayout_7.addWidget(self.rfid_frame)


        self.verticalLayout_15.addWidget(self.login_frame)

        self.stackedWidget.addWidget(self.home_page)
        self.weighing_page = QWidget()
        self.weighing_page.setObjectName(u"weighing_page")
        self.verticalLayout_11 = QVBoxLayout(self.weighing_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.weighing_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, -1)
        self.frame_11 = QFrame(self.frame)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMaximumSize(QSize(16777215, 50))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_57 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_57.setSpacing(10)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(5, 10, 5, 0)
        self.update_settings = QPushButton(self.frame_11)
        self.update_settings.setObjectName(u"update_settings")
        self.update_settings.setMaximumSize(QSize(350, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Kanit"])
        font6.setPointSize(18)
        font6.setBold(True)
        self.update_settings.setFont(font6)
        self.update_settings.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"border-radius: 10px;")

        self.horizontalLayout_57.addWidget(self.update_settings)

        self.clear_settings = QPushButton(self.frame_11)
        self.clear_settings.setObjectName(u"clear_settings")
        self.clear_settings.setMaximumSize(QSize(350, 16777215))
        self.clear_settings.setFont(font6)
        self.clear_settings.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 10px;")

        self.horizontalLayout_57.addWidget(self.clear_settings)

        self.reset_weighing = QPushButton(self.frame_11)
        self.reset_weighing.setObjectName(u"reset_weighing")
        self.reset_weighing.setMaximumSize(QSize(350, 16777215))
        self.reset_weighing.setFont(font6)
        self.reset_weighing.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_57.addWidget(self.reset_weighing)


        self.verticalLayout_37.addWidget(self.frame_11)

        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(100, 100, 100);\n"
"	border-radius: 15px;\n"
"	margin: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"	color: rgb(60, 60, 60);\n"
"	border: none;\n"
"	margin: 0;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.Productname_Label = QLabel(self.frame_10)
        self.Productname_Label.setObjectName(u"Productname_Label")
        self.Productname_Label.setGeometry(QRect(30, 20, 51, 31))
        font7 = QFont()
        font7.setFamilies([u"Kanit"])
        font7.setPointSize(14)
        self.Productname_Label.setFont(font7)
        self.Productname = QLabel(self.frame_10)
        self.Productname.setObjectName(u"Productname")
        self.Productname.setGeometry(QRect(80, 20, 221, 31))
        self.Productname.setFont(font7)
        self.Productname.setIndent(-1)
        self.Lot = QLabel(self.frame_10)
        self.Lot.setObjectName(u"Lot")
        self.Lot.setGeometry(QRect(110, 50, 131, 31))
        self.Lot.setFont(font7)
        self.Lot_Label = QLabel(self.frame_10)
        self.Lot_Label.setObjectName(u"Lot_Label")
        self.Lot_Label.setGeometry(QRect(30, 50, 81, 31))
        self.Lot_Label.setFont(font7)
        self.BalanceID = QLabel(self.frame_10)
        self.BalanceID.setObjectName(u"BalanceID")
        self.BalanceID.setGeometry(QRect(180, 80, 141, 31))
        self.BalanceID.setFont(font7)
        self.Balance_Label = QLabel(self.frame_10)
        self.Balance_Label.setObjectName(u"Balance_Label")
        self.Balance_Label.setGeometry(QRect(30, 80, 141, 31))
        self.Balance_Label.setFont(font7)
        self.TabletID = QLabel(self.frame_10)
        self.TabletID.setObjectName(u"TabletID")
        self.TabletID.setGeometry(QRect(120, 110, 61, 31))
        self.TabletID.setFont(font7)
        self.TabletID_Label = QLabel(self.frame_10)
        self.TabletID_Label.setObjectName(u"TabletID_Label")
        self.TabletID_Label.setGeometry(QRect(30, 110, 91, 31))
        self.TabletID_Label.setFont(font7)
        self.Weight10s = QLabel(self.frame_10)
        self.Weight10s.setObjectName(u"Weight10s")
        self.Weight10s.setGeometry(QRect(230, 140, 121, 31))
        self.Weight10s.setFont(font7)
        self.Weight10s.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.Weight10s_Label = QLabel(self.frame_10)
        self.Weight10s_Label.setObjectName(u"Weight10s_Label")
        self.Weight10s_Label.setGeometry(QRect(30, 140, 191, 31))
        self.Weight10s_Label.setFont(font7)
        self.Weight10sPer_Label = QLabel(self.frame_10)
        self.Weight10sPer_Label.setObjectName(u"Weight10sPer_Label")
        self.Weight10sPer_Label.setGeometry(QRect(30, 170, 241, 31))
        self.Weight10sPer_Label.setFont(font7)
        self.Weight10sPer = QLabel(self.frame_10)
        self.Weight10sPer.setObjectName(u"Weight10sPer")
        self.Weight10sPer.setGeometry(QRect(280, 170, 101, 31))
        self.Weight10sPer.setFont(font7)
        self.MeanWeightInhouse_Label = QLabel(self.frame_10)
        self.MeanWeightInhouse_Label.setObjectName(u"MeanWeightInhouse_Label")
        self.MeanWeightInhouse_Label.setGeometry(QRect(30, 200, 151, 31))
        self.MeanWeightInhouse_Label.setFont(font7)
        self.MeanWeightInhouse = QLabel(self.frame_10)
        self.MeanWeightInhouse.setObjectName(u"MeanWeightInhouse")
        self.MeanWeightInhouse.setGeometry(QRect(180, 200, 211, 31))
        self.MeanWeightInhouse.setFont(font7)
        self.MeanWeightREG = QLabel(self.frame_10)
        self.MeanWeightREG.setObjectName(u"MeanWeightREG")
        self.MeanWeightREG.setGeometry(QRect(330, 230, 201, 31))
        self.MeanWeightREG.setFont(font7)
        self.MeanWeightREG_Label = QLabel(self.frame_10)
        self.MeanWeightREG_Label.setObjectName(u"MeanWeightREG_Label")
        self.MeanWeightREG_Label.setGeometry(QRect(30, 230, 291, 31))
        self.MeanWeightREG_Label.setFont(font7)
        self.Thickness_Label = QLabel(self.frame_10)
        self.Thickness_Label.setObjectName(u"Thickness_Label")
        self.Thickness_Label.setGeometry(QRect(30, 260, 191, 31))
        self.Thickness_Label.setFont(font7)
        self.Thickness = QLabel(self.frame_10)
        self.Thickness.setObjectName(u"Thickness")
        self.Thickness.setGeometry(QRect(230, 260, 261, 31))
        self.Thickness.setFont(font7)
        self.Operator_Label = QLabel(self.frame_10)
        self.Operator_Label.setObjectName(u"Operator_Label")
        self.Operator_Label.setGeometry(QRect(30, 290, 101, 31))
        self.Operator_Label.setFont(font7)
        self.Operator = QLabel(self.frame_10)
        self.Operator.setObjectName(u"Operator")
        self.Operator.setGeometry(QRect(130, 290, 261, 31))
        self.Operator.setFont(font7)

        self.verticalLayout_37.addWidget(self.frame_10)


        self.verticalLayout_11.addWidget(self.frame)

        self.weight_group = QGroupBox(self.weighing_page)
        self.weight_group.setObjectName(u"weight_group")
        self.weight_group.setMinimumSize(QSize(0, 0))
        self.weight_group.setMaximumSize(QSize(16777215, 120))
        self.weight_group.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}\n"
"\n"
"#weight_1, #weight_2, #average {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#weight_label_1, #weight_label_2, #average_label {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"}")
        self.weight_group.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.horizontalLayout_12 = QHBoxLayout(self.weight_group)
        self.horizontalLayout_12.setSpacing(30)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(15, -1, 15, 10)
        self.weight_data_1 = QFrame(self.weight_group)
        self.weight_data_1.setObjectName(u"weight_data_1")
        self.weight_data_1.setLayoutDirection(Qt.LeftToRight)
        self.weight_data_1.setStyleSheet(u"")
        self.verticalLayout_8 = QVBoxLayout(self.weight_data_1)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.weight_label_1 = QLabel(self.weight_data_1)
        self.weight_label_1.setObjectName(u"weight_label_1")
        font8 = QFont()
        font8.setFamilies([u"Kanit"])
        font8.setPointSize(17)
        font8.setBold(True)
        self.weight_label_1.setFont(font8)
        self.weight_label_1.setLayoutDirection(Qt.LeftToRight)
        self.weight_label_1.setAutoFillBackground(False)
        self.weight_label_1.setStyleSheet(u"")
        self.weight_label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.weight_label_1)

        self.weight_1 = QLabel(self.weight_data_1)
        self.weight_1.setObjectName(u"weight_1")
        self.weight_1.setMinimumSize(QSize(0, 60))
        self.weight_1.setMaximumSize(QSize(16777215, 60))
        font9 = QFont()
        font9.setFamilies([u"Kanit"])
        font9.setPointSize(30)
        font9.setBold(True)
        self.weight_1.setFont(font9)
        self.weight_1.setStyleSheet(u"")
        self.weight_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.weight_1)


        self.horizontalLayout_12.addWidget(self.weight_data_1)

        self.weight_data_2 = QFrame(self.weight_group)
        self.weight_data_2.setObjectName(u"weight_data_2")
        self.weight_data_2.setLayoutDirection(Qt.LeftToRight)
        self.weight_data_2.setStyleSheet(u"")
        self.verticalLayout_9 = QVBoxLayout(self.weight_data_2)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.weight_label_2 = QLabel(self.weight_data_2)
        self.weight_label_2.setObjectName(u"weight_label_2")
        self.weight_label_2.setFont(font8)
        self.weight_label_2.setLayoutDirection(Qt.LeftToRight)
        self.weight_label_2.setAutoFillBackground(False)
        self.weight_label_2.setStyleSheet(u"")
        self.weight_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.weight_label_2)

        self.weight_2 = QLabel(self.weight_data_2)
        self.weight_2.setObjectName(u"weight_2")
        self.weight_2.setMinimumSize(QSize(0, 60))
        self.weight_2.setMaximumSize(QSize(16777215, 60))
        self.weight_2.setFont(font9)
        self.weight_2.setStyleSheet(u"")
        self.weight_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.weight_2)


        self.horizontalLayout_12.addWidget(self.weight_data_2)

        self.weight_data_3 = QFrame(self.weight_group)
        self.weight_data_3.setObjectName(u"weight_data_3")
        self.weight_data_3.setLayoutDirection(Qt.LeftToRight)
        self.weight_data_3.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.weight_data_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.average_label = QLabel(self.weight_data_3)
        self.average_label.setObjectName(u"average_label")
        self.average_label.setFont(font8)
        self.average_label.setLayoutDirection(Qt.LeftToRight)
        self.average_label.setAutoFillBackground(False)
        self.average_label.setStyleSheet(u"")
        self.average_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.average_label)

        self.average = QLabel(self.weight_data_3)
        self.average.setObjectName(u"average")
        self.average.setMinimumSize(QSize(0, 60))
        self.average.setMaximumSize(QSize(16777215, 60))
        self.average.setFont(font9)
        self.average.setStyleSheet(u"")
        self.average.setAlignment(Qt.AlignCenter)

        self.verticalLayout_10.addWidget(self.average)


        self.horizontalLayout_12.addWidget(self.weight_data_3)


        self.verticalLayout_11.addWidget(self.weight_group)

        self.stackedWidget.addWidget(self.weighing_page)
        self.thickness_page = QWidget()
        self.thickness_page.setObjectName(u"thickness_page")
        self.thickness_page.setStyleSheet(u"QGroupBox {\n"
"	border: none;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.thickness_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.thickness_main_group = QGroupBox(self.thickness_page)
        self.thickness_main_group.setObjectName(u"thickness_main_group")
        self.verticalLayout_13 = QVBoxLayout(self.thickness_main_group)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.thickness_title_groupBox = QGroupBox(self.thickness_main_group)
        self.thickness_title_groupBox.setObjectName(u"thickness_title_groupBox")
        self.thickness_title_groupBox.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_11 = QHBoxLayout(self.thickness_title_groupBox)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(30, 0, 30, 0)
        self.thickness_title = QLabel(self.thickness_title_groupBox)
        self.thickness_title.setObjectName(u"thickness_title")
        self.thickness_title.setMaximumSize(QSize(16777215, 50))
        self.thickness_title.setFont(font4)
        self.thickness_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.thickness_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.thickness_title)


        self.verticalLayout_13.addWidget(self.thickness_title_groupBox)

        self.frame_7 = QFrame(self.thickness_main_group)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_83 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalSpacer_6 = QSpacerItem(6, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_6)

        self.thicknes_group = QGroupBox(self.frame_7)
        self.thicknes_group.setObjectName(u"thicknes_group")
        self.thicknes_group.setMinimumSize(QSize(0, 0))
        self.thicknes_group.setMaximumSize(QSize(16777215, 400))
        self.thicknes_group.setStyleSheet(u"QPushButton {\n"
" 	border: none;\n"
"	color: rgb(100, 100, 100);\n"
"}")
        self.gridLayout = QGridLayout(self.thicknes_group)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(100)
        self.thickness_val_group_1 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_1.setObjectName(u"thickness_val_group_1")
        self.thickness_val_group_1.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_1.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_13 = QHBoxLayout(self.thickness_val_group_1)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_1 = QLabel(self.thickness_val_group_1)
        self.thickness_val_title_1.setObjectName(u"thickness_val_title_1")
        self.thickness_val_title_1.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_1.setMaximumSize(QSize(80, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Kanit"])
        font10.setPointSize(16)
        font10.setBold(False)
        font10.setItalic(False)
        font10.setUnderline(False)
        font10.setStrikeOut(False)
        self.thickness_val_title_1.setFont(font10)
        self.thickness_val_title_1.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_13.addWidget(self.thickness_val_title_1)

        self.thickness_val_frame_1 = QFrame(self.thickness_val_group_1)
        self.thickness_val_frame_1.setObjectName(u"thickness_val_frame_1")
        self.thickness_val_frame_1.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_1.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_1.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.thickness_val_frame_1)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.thickness_val_1 = QPushButton(self.thickness_val_frame_1)
        self.thickness_val_1.setObjectName(u"thickness_val_1")
        font11 = QFont()
        font11.setFamilies([u"Kanit"])
        font11.setPointSize(18)
        self.thickness_val_1.setFont(font11)
        self.thickness_val_1.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_14.addWidget(self.thickness_val_1)


        self.horizontalLayout_13.addWidget(self.thickness_val_frame_1)


        self.gridLayout.addWidget(self.thickness_val_group_1, 0, 0, 1, 1)

        self.thickness_val_group_6 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_6.setObjectName(u"thickness_val_group_6")
        self.thickness_val_group_6.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_6.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_23 = QHBoxLayout(self.thickness_val_group_6)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_6 = QLabel(self.thickness_val_group_6)
        self.thickness_val_title_6.setObjectName(u"thickness_val_title_6")
        self.thickness_val_title_6.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_6.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_6.setFont(font10)
        self.thickness_val_title_6.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_23.addWidget(self.thickness_val_title_6)

        self.thickness_val_frame_6 = QFrame(self.thickness_val_group_6)
        self.thickness_val_frame_6.setObjectName(u"thickness_val_frame_6")
        self.thickness_val_frame_6.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_6.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_6.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.thickness_val_frame_6)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.thickness_val_6 = QPushButton(self.thickness_val_frame_6)
        self.thickness_val_6.setObjectName(u"thickness_val_6")
        self.thickness_val_6.setFont(font11)
        self.thickness_val_6.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_24.addWidget(self.thickness_val_6)


        self.horizontalLayout_23.addWidget(self.thickness_val_frame_6)


        self.gridLayout.addWidget(self.thickness_val_group_6, 0, 1, 1, 1)

        self.thickness_val_group_2 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_2.setObjectName(u"thickness_val_group_2")
        self.thickness_val_group_2.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_2.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_15 = QHBoxLayout(self.thickness_val_group_2)
        self.horizontalLayout_15.setSpacing(0)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_2 = QLabel(self.thickness_val_group_2)
        self.thickness_val_title_2.setObjectName(u"thickness_val_title_2")
        self.thickness_val_title_2.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_2.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_2.setFont(font10)
        self.thickness_val_title_2.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.thickness_val_title_2)

        self.thickness_val_frame_2 = QFrame(self.thickness_val_group_2)
        self.thickness_val_frame_2.setObjectName(u"thickness_val_frame_2")
        self.thickness_val_frame_2.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_2.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_2.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.thickness_val_frame_2)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.thickness_val_2 = QPushButton(self.thickness_val_frame_2)
        self.thickness_val_2.setObjectName(u"thickness_val_2")
        self.thickness_val_2.setFont(font11)
        self.thickness_val_2.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_16.addWidget(self.thickness_val_2)


        self.horizontalLayout_15.addWidget(self.thickness_val_frame_2)


        self.gridLayout.addWidget(self.thickness_val_group_2, 1, 0, 1, 1)

        self.thickness_val_group_7 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_7.setObjectName(u"thickness_val_group_7")
        self.thickness_val_group_7.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_7.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_25 = QHBoxLayout(self.thickness_val_group_7)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_7 = QLabel(self.thickness_val_group_7)
        self.thickness_val_title_7.setObjectName(u"thickness_val_title_7")
        self.thickness_val_title_7.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_7.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_7.setFont(font10)
        self.thickness_val_title_7.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.thickness_val_title_7)

        self.thickness_val_frame_7 = QFrame(self.thickness_val_group_7)
        self.thickness_val_frame_7.setObjectName(u"thickness_val_frame_7")
        self.thickness_val_frame_7.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_7.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_7.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_26 = QHBoxLayout(self.thickness_val_frame_7)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.thickness_val_7 = QPushButton(self.thickness_val_frame_7)
        self.thickness_val_7.setObjectName(u"thickness_val_7")
        self.thickness_val_7.setFont(font11)
        self.thickness_val_7.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_26.addWidget(self.thickness_val_7)


        self.horizontalLayout_25.addWidget(self.thickness_val_frame_7)


        self.gridLayout.addWidget(self.thickness_val_group_7, 1, 1, 1, 1)

        self.thickness_val_group_3 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_3.setObjectName(u"thickness_val_group_3")
        self.thickness_val_group_3.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_3.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_17 = QHBoxLayout(self.thickness_val_group_3)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_3 = QLabel(self.thickness_val_group_3)
        self.thickness_val_title_3.setObjectName(u"thickness_val_title_3")
        self.thickness_val_title_3.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_3.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_3.setFont(font10)
        self.thickness_val_title_3.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.thickness_val_title_3)

        self.thickness_val_frame_3 = QFrame(self.thickness_val_group_3)
        self.thickness_val_frame_3.setObjectName(u"thickness_val_frame_3")
        self.thickness_val_frame_3.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_3.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_3.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.thickness_val_frame_3)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.thickness_val_3 = QPushButton(self.thickness_val_frame_3)
        self.thickness_val_3.setObjectName(u"thickness_val_3")
        self.thickness_val_3.setFont(font11)
        self.thickness_val_3.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_18.addWidget(self.thickness_val_3)


        self.horizontalLayout_17.addWidget(self.thickness_val_frame_3)


        self.gridLayout.addWidget(self.thickness_val_group_3, 2, 0, 1, 1)

        self.thickness_val_group_8 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_8.setObjectName(u"thickness_val_group_8")
        self.thickness_val_group_8.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_8.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_27 = QHBoxLayout(self.thickness_val_group_8)
        self.horizontalLayout_27.setSpacing(0)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_8 = QLabel(self.thickness_val_group_8)
        self.thickness_val_title_8.setObjectName(u"thickness_val_title_8")
        self.thickness_val_title_8.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_8.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_8.setFont(font10)
        self.thickness_val_title_8.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.thickness_val_title_8)

        self.thickness_val_frame_8 = QFrame(self.thickness_val_group_8)
        self.thickness_val_frame_8.setObjectName(u"thickness_val_frame_8")
        self.thickness_val_frame_8.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_8.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_8.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.thickness_val_frame_8)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.thickness_val_8 = QPushButton(self.thickness_val_frame_8)
        self.thickness_val_8.setObjectName(u"thickness_val_8")
        self.thickness_val_8.setFont(font11)
        self.thickness_val_8.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_28.addWidget(self.thickness_val_8)


        self.horizontalLayout_27.addWidget(self.thickness_val_frame_8)


        self.gridLayout.addWidget(self.thickness_val_group_8, 2, 1, 1, 1)

        self.thickness_val_group_4 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_4.setObjectName(u"thickness_val_group_4")
        self.thickness_val_group_4.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_4.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_19 = QHBoxLayout(self.thickness_val_group_4)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_4 = QLabel(self.thickness_val_group_4)
        self.thickness_val_title_4.setObjectName(u"thickness_val_title_4")
        self.thickness_val_title_4.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_4.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_4.setFont(font10)
        self.thickness_val_title_4.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.thickness_val_title_4)

        self.thickness_val_frame_4 = QFrame(self.thickness_val_group_4)
        self.thickness_val_frame_4.setObjectName(u"thickness_val_frame_4")
        self.thickness_val_frame_4.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_4.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_4.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.thickness_val_frame_4)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.thickness_val_4 = QPushButton(self.thickness_val_frame_4)
        self.thickness_val_4.setObjectName(u"thickness_val_4")
        self.thickness_val_4.setFont(font11)
        self.thickness_val_4.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_20.addWidget(self.thickness_val_4)


        self.horizontalLayout_19.addWidget(self.thickness_val_frame_4)


        self.gridLayout.addWidget(self.thickness_val_group_4, 3, 0, 1, 1)

        self.thickness_val_group_9 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_9.setObjectName(u"thickness_val_group_9")
        self.thickness_val_group_9.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_9.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_29 = QHBoxLayout(self.thickness_val_group_9)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_9 = QLabel(self.thickness_val_group_9)
        self.thickness_val_title_9.setObjectName(u"thickness_val_title_9")
        self.thickness_val_title_9.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_9.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_9.setFont(font10)
        self.thickness_val_title_9.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.thickness_val_title_9)

        self.thickness_val_frame_9 = QFrame(self.thickness_val_group_9)
        self.thickness_val_frame_9.setObjectName(u"thickness_val_frame_9")
        self.thickness_val_frame_9.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_9.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_9.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.thickness_val_frame_9)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.thickness_val_9 = QPushButton(self.thickness_val_frame_9)
        self.thickness_val_9.setObjectName(u"thickness_val_9")
        self.thickness_val_9.setFont(font11)
        self.thickness_val_9.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_30.addWidget(self.thickness_val_9)


        self.horizontalLayout_29.addWidget(self.thickness_val_frame_9)


        self.gridLayout.addWidget(self.thickness_val_group_9, 3, 1, 1, 1)

        self.thickness_val_group_5 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_5.setObjectName(u"thickness_val_group_5")
        self.thickness_val_group_5.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_5.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_21 = QHBoxLayout(self.thickness_val_group_5)
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_5 = QLabel(self.thickness_val_group_5)
        self.thickness_val_title_5.setObjectName(u"thickness_val_title_5")
        self.thickness_val_title_5.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_5.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_5.setFont(font10)
        self.thickness_val_title_5.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.thickness_val_title_5)

        self.thickness_val_frame_5 = QFrame(self.thickness_val_group_5)
        self.thickness_val_frame_5.setObjectName(u"thickness_val_frame_5")
        self.thickness_val_frame_5.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_5.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_5.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.thickness_val_frame_5)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.thickness_val_5 = QPushButton(self.thickness_val_frame_5)
        self.thickness_val_5.setObjectName(u"thickness_val_5")
        self.thickness_val_5.setFont(font11)
        self.thickness_val_5.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_22.addWidget(self.thickness_val_5)


        self.horizontalLayout_21.addWidget(self.thickness_val_frame_5)


        self.gridLayout.addWidget(self.thickness_val_group_5, 4, 0, 1, 1)

        self.thickness_val_group_10 = QGroupBox(self.thicknes_group)
        self.thickness_val_group_10.setObjectName(u"thickness_val_group_10")
        self.thickness_val_group_10.setMinimumSize(QSize(0, 0))
        self.thickness_val_group_10.setMaximumSize(QSize(16777215, 50))
        self.thickness_val_group_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_31 = QHBoxLayout(self.thickness_val_group_10)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.thickness_val_title_10 = QLabel(self.thickness_val_group_10)
        self.thickness_val_title_10.setObjectName(u"thickness_val_title_10")
        self.thickness_val_title_10.setMinimumSize(QSize(80, 0))
        self.thickness_val_title_10.setMaximumSize(QSize(80, 16777215))
        self.thickness_val_title_10.setFont(font10)
        self.thickness_val_title_10.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 15px;\n"
"border-bottom-left-radius: 15px;")
        self.thickness_val_title_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.thickness_val_title_10)

        self.thickness_val_frame_10 = QFrame(self.thickness_val_group_10)
        self.thickness_val_frame_10.setObjectName(u"thickness_val_frame_10")
        self.thickness_val_frame_10.setMinimumSize(QSize(0, 0))
        self.thickness_val_frame_10.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 15px;\n"
"border-bottom-right-radius: 15px;")
        self.thickness_val_frame_10.setFrameShape(QFrame.StyledPanel)
        self.thickness_val_frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.thickness_val_frame_10)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.thickness_val_10 = QPushButton(self.thickness_val_frame_10)
        self.thickness_val_10.setObjectName(u"thickness_val_10")
        self.thickness_val_10.setFont(font11)
        self.thickness_val_10.setStyleSheet(u"border: none;\n"
"color: rgb(100, 100, 100);")

        self.horizontalLayout_32.addWidget(self.thickness_val_10)


        self.horizontalLayout_31.addWidget(self.thickness_val_frame_10)


        self.gridLayout.addWidget(self.thickness_val_group_10, 4, 1, 1, 1)


        self.horizontalLayout_83.addWidget(self.thicknes_group)

        self.horizontalSpacer_7 = QSpacerItem(6, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_83.addItem(self.horizontalSpacer_7)


        self.verticalLayout_13.addWidget(self.frame_7)

        self.thickness_button_group = QGroupBox(self.thickness_main_group)
        self.thickness_button_group.setObjectName(u"thickness_button_group")
        self.thickness_button_group.setMinimumSize(QSize(0, 0))
        self.thickness_button_group.setMaximumSize(QSize(16777215, 70))
        self.thickness_button_group.setStyleSheet(u"QPushButton {\n"
"	border-radius: 15px;\n"
"}|")
        self.horizontalLayout_9 = QHBoxLayout(self.thickness_button_group)
        self.horizontalLayout_9.setSpacing(10)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer)

        self.button_thickness_confirm = QPushButton(self.thickness_button_group)
        self.button_thickness_confirm.setObjectName(u"button_thickness_confirm")
        self.button_thickness_confirm.setMinimumSize(QSize(120, 50))
        self.button_thickness_confirm.setMaximumSize(QSize(120, 16777215))
        font12 = QFont()
        font12.setFamilies([u"Kanit"])
        font12.setPointSize(20)
        self.button_thickness_confirm.setFont(font12)
        self.button_thickness_confirm.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_thickness_confirm.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        icon1 = QIcon()
        icon1.addFile(u":/assets/icon/confirm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_thickness_confirm.setIcon(icon1)
        self.button_thickness_confirm.setIconSize(QSize(20, 20))

        self.horizontalLayout_9.addWidget(self.button_thickness_confirm)

        self.button_thickness_cancel = QPushButton(self.thickness_button_group)
        self.button_thickness_cancel.setObjectName(u"button_thickness_cancel")
        self.button_thickness_cancel.setMinimumSize(QSize(120, 50))
        self.button_thickness_cancel.setMaximumSize(QSize(120, 16777215))
        self.button_thickness_cancel.setFont(font12)
        self.button_thickness_cancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_thickness_cancel.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        icon2 = QIcon()
        icon2.addFile(u":/assets/icon/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_thickness_cancel.setIcon(icon2)
        self.button_thickness_cancel.setIconSize(QSize(25, 25))

        self.horizontalLayout_9.addWidget(self.button_thickness_cancel)


        self.verticalLayout_13.addWidget(self.thickness_button_group)


        self.verticalLayout_12.addWidget(self.thickness_main_group)

        self.stackedWidget.addWidget(self.thickness_page)
        self.thickness_keyboard = QWidget()
        self.thickness_keyboard.setObjectName(u"thickness_keyboard")
        self.verticalLayout_34 = QVBoxLayout(self.thickness_keyboard)
        self.verticalLayout_34.setSpacing(0)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.thickness_keyboard)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_35 = QVBoxLayout(self.widget_2)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_35.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.widget_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 300))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.thickness_title_groupBox_2 = QGroupBox(self.frame_4)
        self.thickness_title_groupBox_2.setObjectName(u"thickness_title_groupBox_2")
        self.thickness_title_groupBox_2.setMaximumSize(QSize(16777215, 80))
        self.horizontalLayout_60 = QHBoxLayout(self.thickness_title_groupBox_2)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalLayout_60.setContentsMargins(30, 0, 30, 0)
        self.thickness_input_title = QLabel(self.thickness_title_groupBox_2)
        self.thickness_input_title.setObjectName(u"thickness_input_title")
        self.thickness_input_title.setMaximumSize(QSize(16777215, 50))
        self.thickness_input_title.setFont(font4)
        self.thickness_input_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.thickness_input_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_60.addWidget(self.thickness_input_title)


        self.verticalLayout_3.addWidget(self.thickness_title_groupBox_2)

        self.frame_9 = QFrame(self.frame_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_9)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, -1, -1, 20)
        self.thickness_val_label = QLabel(self.frame_9)
        self.thickness_val_label.setObjectName(u"thickness_val_label")
        self.thickness_val_label.setMinimumSize(QSize(0, 50))
        self.thickness_val_label.setMaximumSize(QSize(16777215, 50))
        font13 = QFont()
        font13.setFamilies([u"Kanit"])
        font13.setPointSize(22)
        font13.setBold(True)
        font13.setUnderline(True)
        self.thickness_val_label.setFont(font13)
        self.thickness_val_label.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.thickness_val_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.thickness_val_label)

        self.thickness_val_input = QLabel(self.frame_9)
        self.thickness_val_input.setObjectName(u"thickness_val_input")
        font14 = QFont()
        font14.setFamilies([u"Kanit"])
        font14.setPointSize(50)
        font14.setBold(True)
        self.thickness_val_input.setFont(font14)
        self.thickness_val_input.setStyleSheet(u"color: rgb(100, 100, 100);\n"
"border: none;")
        self.thickness_val_input.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.thickness_val_input)


        self.verticalLayout_3.addWidget(self.frame_9)

        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(0, 250))
        self.frame_5.setMaximumSize(QSize(16777215, 250))
        self.frame_5.setStyleSheet(u"")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_63 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_63.setSpacing(0)
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.horizontalLayout_63.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(255, 255, 255, 128))
        brush1.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.frame_6.setPalette(palette)
        self.frame_6.setStyleSheet(u"QPushButton {\n"
"	width: 90px;\n"
"	height: 70px;\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    font-size: 40px;\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.frame_6.setFrameShadow(QFrame.Plain)
        self.frame_6.setLineWidth(3)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.key_1 = QPushButton(self.frame_6)
        self.key_1.setObjectName(u"key_1")
        font15 = QFont()
        font15.setFamilies([u"Kanit"])
        font15.setPointSize(20)
        font15.setWeight(QFont.Medium)
        self.key_1.setFont(font15)

        self.gridLayout_6.addWidget(self.key_1, 0, 0, 1, 1)

        self.key_2 = QPushButton(self.frame_6)
        self.key_2.setObjectName(u"key_2")
        self.key_2.setFont(font15)

        self.gridLayout_6.addWidget(self.key_2, 0, 1, 1, 1)

        self.key_3 = QPushButton(self.frame_6)
        self.key_3.setObjectName(u"key_3")
        self.key_3.setFont(font15)

        self.gridLayout_6.addWidget(self.key_3, 0, 2, 1, 1)

        self.key_4 = QPushButton(self.frame_6)
        self.key_4.setObjectName(u"key_4")
        self.key_4.setFont(font15)

        self.gridLayout_6.addWidget(self.key_4, 1, 0, 1, 1)

        self.key_5 = QPushButton(self.frame_6)
        self.key_5.setObjectName(u"key_5")
        self.key_5.setFont(font15)

        self.gridLayout_6.addWidget(self.key_5, 1, 1, 1, 1)

        self.key_6 = QPushButton(self.frame_6)
        self.key_6.setObjectName(u"key_6")
        self.key_6.setFont(font15)

        self.gridLayout_6.addWidget(self.key_6, 1, 2, 1, 1)

        self.key_7 = QPushButton(self.frame_6)
        self.key_7.setObjectName(u"key_7")
        self.key_7.setFont(font15)

        self.gridLayout_6.addWidget(self.key_7, 2, 0, 1, 1)

        self.key_8 = QPushButton(self.frame_6)
        self.key_8.setObjectName(u"key_8")
        self.key_8.setFont(font15)

        self.gridLayout_6.addWidget(self.key_8, 2, 1, 1, 1)

        self.key_9 = QPushButton(self.frame_6)
        self.key_9.setObjectName(u"key_9")
        self.key_9.setFont(font15)

        self.gridLayout_6.addWidget(self.key_9, 2, 2, 1, 1)

        self.key_dot = QPushButton(self.frame_6)
        self.key_dot.setObjectName(u"key_dot")
        self.key_dot.setMinimumSize(QSize(0, 0))
        self.key_dot.setMaximumSize(QSize(16777215, 150))
        font16 = QFont()
        font16.setPointSize(20)
        self.key_dot.setFont(font16)
        icon3 = QIcon()
        icon3.addFile(u":/assets/keyboard/record.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_dot.setIcon(icon3)
        self.key_dot.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.key_dot, 3, 0, 1, 1)

        self.key_0 = QPushButton(self.frame_6)
        self.key_0.setObjectName(u"key_0")
        self.key_0.setMinimumSize(QSize(0, 0))
        self.key_0.setMaximumSize(QSize(16777215, 150))
        self.key_0.setFont(font15)

        self.gridLayout_6.addWidget(self.key_0, 3, 1, 1, 1)

        self.key_backspace = QPushButton(self.frame_6)
        self.key_backspace.setObjectName(u"key_backspace")
        self.key_backspace.setMinimumSize(QSize(0, 0))
        self.key_backspace.setMaximumSize(QSize(16777215, 150))
        self.key_backspace.setFont(font16)
        icon4 = QIcon()
        icon4.addFile(u":/assets/keyboard/backspace.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_backspace.setIcon(icon4)
        self.key_backspace.setIconSize(QSize(30, 30))

        self.gridLayout_6.addWidget(self.key_backspace, 3, 2, 1, 1)


        self.horizontalLayout_63.addWidget(self.frame_6)

        self.frame_8 = QFrame(self.frame_5)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QPushButton {\n"
"	background-color: rgb(50, 50, 50);\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgb(100, 100, 100);\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_36 = QVBoxLayout(self.frame_8)
        self.verticalLayout_36.setSpacing(6)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.thickness_img = QLabel(self.frame_8)
        self.thickness_img.setObjectName(u"thickness_img")
        self.thickness_img.setPixmap(QPixmap(u":/assets/icon/thickness.png"))
        self.thickness_img.setAlignment(Qt.AlignCenter)

        self.verticalLayout_36.addWidget(self.thickness_img)

        self.key_enter = QPushButton(self.frame_8)
        self.key_enter.setObjectName(u"key_enter")
        self.key_enter.setMinimumSize(QSize(0, 52))
        font17 = QFont()
        font17.setFamilies([u"Kanit"])
        font17.setPointSize(20)
        font17.setWeight(QFont.Medium)
        font17.setItalic(False)
        self.key_enter.setFont(font17)
        self.key_enter.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/assets/keyboard/enter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_enter.setIcon(icon5)
        self.key_enter.setIconSize(QSize(30, 30))

        self.verticalLayout_36.addWidget(self.key_enter)

        self.key_cancel = QPushButton(self.frame_8)
        self.key_cancel.setObjectName(u"key_cancel")
        self.key_cancel.setMinimumSize(QSize(0, 52))
        self.key_cancel.setFont(font17)
        icon6 = QIcon()
        icon6.addFile(u":/assets/keyboard/cancel.png", QSize(), QIcon.Normal, QIcon.Off)
        self.key_cancel.setIcon(icon6)
        self.key_cancel.setIconSize(QSize(30, 30))

        self.verticalLayout_36.addWidget(self.key_cancel)


        self.horizontalLayout_63.addWidget(self.frame_8)


        self.verticalLayout_3.addWidget(self.frame_5)


        self.verticalLayout_35.addWidget(self.frame_4)


        self.verticalLayout_34.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.thickness_keyboard)
        self.characteristics_page = QWidget()
        self.characteristics_page.setObjectName(u"characteristics_page")
        self.verticalLayout_14 = QVBoxLayout(self.characteristics_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.thickness_frame_2 = QFrame(self.characteristics_page)
        self.thickness_frame_2.setObjectName(u"thickness_frame_2")
        self.thickness_frame_2.setMaximumSize(QSize(16777215, 80))
        self.thickness_frame_2.setFrameShape(QFrame.StyledPanel)
        self.thickness_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.thickness_frame_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(30, -1, 30, -1)
        self.thickness_title_2 = QLabel(self.thickness_frame_2)
        self.thickness_title_2.setObjectName(u"thickness_title_2")
        self.thickness_title_2.setMaximumSize(QSize(16777215, 50))
        self.thickness_title_2.setFont(font4)
        self.thickness_title_2.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.thickness_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.thickness_title_2)


        self.verticalLayout_14.addWidget(self.thickness_frame_2)

        self.characteristics_frame = QFrame(self.characteristics_page)
        self.characteristics_frame.setObjectName(u"characteristics_frame")
        self.characteristics_frame.setStyleSheet(u"QLabel {\n"
"	border: solid;\n"
"	border-width: 2px;\n"
"	border-color: rgb(111, 105, 37);\n"
"	border-radius: 15px;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	margin-top: 25px;\n"
"	border-radius: 15px;\n"
"}")
        self.characteristics_frame.setFrameShape(QFrame.StyledPanel)
        self.characteristics_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.characteristics_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setHorizontalSpacing(20)
        self.gridLayout_4.setVerticalSpacing(15)
        self.gridLayout_4.setContentsMargins(-1, -1, -1, 30)
        self.tablet_front_img = QLabel(self.characteristics_frame)
        self.tablet_front_img.setObjectName(u"tablet_front_img")
        self.tablet_front_img.setMinimumSize(QSize(250, 250))
        self.tablet_front_img.setMaximumSize(QSize(250, 250))
        self.tablet_front_img.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.tablet_front_img.setScaledContents(True)

        self.gridLayout_4.addWidget(self.tablet_front_img, 1, 0, 1, 1)

        self.characteristics_abnomal = QPushButton(self.characteristics_frame)
        self.characteristics_abnomal.setObjectName(u"characteristics_abnomal")
        self.characteristics_abnomal.setMinimumSize(QSize(120, 80))
        self.characteristics_abnomal.setFont(font12)
        self.characteristics_abnomal.setCursor(QCursor(Qt.PointingHandCursor))
        self.characteristics_abnomal.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.characteristics_abnomal.setIcon(icon2)
        self.characteristics_abnomal.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.characteristics_abnomal, 2, 1, 1, 1)

        self.characteristics_nomal = QPushButton(self.characteristics_frame)
        self.characteristics_nomal.setObjectName(u"characteristics_nomal")
        self.characteristics_nomal.setMinimumSize(QSize(120, 80))
        self.characteristics_nomal.setFont(font12)
        self.characteristics_nomal.setCursor(QCursor(Qt.PointingHandCursor))
        self.characteristics_nomal.setStyleSheet(u"background-color: rgb(0, 170, 0);")
        self.characteristics_nomal.setIcon(icon1)
        self.characteristics_nomal.setIconSize(QSize(30, 30))

        self.gridLayout_4.addWidget(self.characteristics_nomal, 2, 0, 1, 1)

        self.tablet_behind_img = QLabel(self.characteristics_frame)
        self.tablet_behind_img.setObjectName(u"tablet_behind_img")
        self.tablet_behind_img.setMinimumSize(QSize(250, 250))
        self.tablet_behind_img.setMaximumSize(QSize(250, 250))
        self.tablet_behind_img.setPixmap(QPixmap(u":/assets/icon/picture_default.png"))
        self.tablet_behind_img.setScaledContents(True)

        self.gridLayout_4.addWidget(self.tablet_behind_img, 1, 1, 1, 1)

        self.tablet_front_label = QLabel(self.characteristics_frame)
        self.tablet_front_label.setObjectName(u"tablet_front_label")
        self.tablet_front_label.setMaximumSize(QSize(16777215, 50))
        font18 = QFont()
        font18.setFamilies([u"Kanit"])
        font18.setPointSize(18)
        font18.setBold(False)
        font18.setUnderline(True)
        self.tablet_front_label.setFont(font18)
        self.tablet_front_label.setStyleSheet(u"border: none;\n"
"color: rgb(80, 80, 80);")
        self.tablet_front_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tablet_front_label, 0, 0, 1, 1)

        self.tablet_behind_label = QLabel(self.characteristics_frame)
        self.tablet_behind_label.setObjectName(u"tablet_behind_label")
        self.tablet_behind_label.setMaximumSize(QSize(16777215, 50))
        self.tablet_behind_label.setFont(font18)
        self.tablet_behind_label.setStyleSheet(u"border: none;\n"
"color: rgb(80, 80, 80);")
        self.tablet_behind_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_4.addWidget(self.tablet_behind_label, 0, 1, 1, 1)


        self.verticalLayout_14.addWidget(self.characteristics_frame)

        self.stackedWidget.addWidget(self.characteristics_page)
        self.summary_page = QWidget()
        self.summary_page.setObjectName(u"summary_page")
        self.summary_page.setStyleSheet(u"QGroupBox {\n"
"	border: none\n"
"}")
        self.verticalLayout_27 = QVBoxLayout(self.summary_page)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.weight_summary_main_group = QGroupBox(self.summary_page)
        self.weight_summary_main_group.setObjectName(u"weight_summary_main_group")
        self.verticalLayout_22 = QVBoxLayout(self.weight_summary_main_group)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 20)
        self.weight_summary_title_frame = QFrame(self.weight_summary_main_group)
        self.weight_summary_title_frame.setObjectName(u"weight_summary_title_frame")
        self.weight_summary_title_frame.setMaximumSize(QSize(16777215, 80))
        self.weight_summary_title_frame.setFrameShape(QFrame.StyledPanel)
        self.weight_summary_title_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.weight_summary_title_frame)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(10, 0, 10, 0)
        self.weight_summary_title = QLabel(self.weight_summary_title_frame)
        self.weight_summary_title.setObjectName(u"weight_summary_title")
        self.weight_summary_title.setMaximumSize(QSize(16777215, 50))
        self.weight_summary_title.setFont(font4)
        self.weight_summary_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.weight_summary_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.weight_summary_title)


        self.verticalLayout_22.addWidget(self.weight_summary_title_frame)

        self.weight_summary_group = QGroupBox(self.weight_summary_main_group)
        self.weight_summary_group.setObjectName(u"weight_summary_group")
        self.weight_summary_group.setMinimumSize(QSize(0, 0))
        self.weight_summary_group.setMaximumSize(QSize(16777215, 100))
        font19 = QFont()
        font19.setPointSize(5)
        self.weight_summary_group.setFont(font19)
        self.weight_summary_group.setStyleSheet(u"#summary_weight_1, #summary_weight_2, #summary_average, #summary_percent {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#summary_weight_label_1, #summary_weight_label_2, #summary_average_label,  #summary_percent_label {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"}")
        self.weight_summary_group.setAlignment(Qt.AlignBottom|Qt.AlignHCenter)
        self.horizontalLayout_35 = QHBoxLayout(self.weight_summary_group)
        self.horizontalLayout_35.setSpacing(20)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(10, 10, 10, 0)
        self.weight_summary_group_1 = QGroupBox(self.weight_summary_group)
        self.weight_summary_group_1.setObjectName(u"weight_summary_group_1")
        self.weight_summary_group_1.setLayoutDirection(Qt.LeftToRight)
        self.weight_summary_group_1.setStyleSheet(u"")
        self.verticalLayout_18 = QVBoxLayout(self.weight_summary_group_1)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.summary_weight_label_1 = QLabel(self.weight_summary_group_1)
        self.summary_weight_label_1.setObjectName(u"summary_weight_label_1")
        font20 = QFont()
        font20.setFamilies([u"Kanit"])
        font20.setPointSize(12)
        font20.setBold(True)
        self.summary_weight_label_1.setFont(font20)
        self.summary_weight_label_1.setLayoutDirection(Qt.LeftToRight)
        self.summary_weight_label_1.setAutoFillBackground(False)
        self.summary_weight_label_1.setStyleSheet(u"")
        self.summary_weight_label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.summary_weight_label_1)

        self.summary_weight_1 = QLabel(self.weight_summary_group_1)
        self.summary_weight_1.setObjectName(u"summary_weight_1")
        self.summary_weight_1.setMinimumSize(QSize(0, 50))
        self.summary_weight_1.setMaximumSize(QSize(16777215, 50))
        font21 = QFont()
        font21.setFamilies([u"Kanit"])
        font21.setPointSize(20)
        font21.setBold(True)
        self.summary_weight_1.setFont(font21)
        self.summary_weight_1.setStyleSheet(u"")
        self.summary_weight_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.summary_weight_1)


        self.horizontalLayout_35.addWidget(self.weight_summary_group_1)

        self.weight_summary_group_2 = QGroupBox(self.weight_summary_group)
        self.weight_summary_group_2.setObjectName(u"weight_summary_group_2")
        self.weight_summary_group_2.setLayoutDirection(Qt.LeftToRight)
        self.weight_summary_group_2.setStyleSheet(u"")
        self.verticalLayout_19 = QVBoxLayout(self.weight_summary_group_2)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.summary_weight_label_2 = QLabel(self.weight_summary_group_2)
        self.summary_weight_label_2.setObjectName(u"summary_weight_label_2")
        self.summary_weight_label_2.setFont(font20)
        self.summary_weight_label_2.setLayoutDirection(Qt.LeftToRight)
        self.summary_weight_label_2.setAutoFillBackground(False)
        self.summary_weight_label_2.setStyleSheet(u"")
        self.summary_weight_label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.summary_weight_label_2)

        self.summary_weight_2 = QLabel(self.weight_summary_group_2)
        self.summary_weight_2.setObjectName(u"summary_weight_2")
        self.summary_weight_2.setMinimumSize(QSize(0, 50))
        self.summary_weight_2.setMaximumSize(QSize(16777215, 50))
        self.summary_weight_2.setFont(font21)
        self.summary_weight_2.setStyleSheet(u"")
        self.summary_weight_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.summary_weight_2)


        self.horizontalLayout_35.addWidget(self.weight_summary_group_2)

        self.average_summary_group = QGroupBox(self.weight_summary_group)
        self.average_summary_group.setObjectName(u"average_summary_group")
        self.average_summary_group.setLayoutDirection(Qt.LeftToRight)
        self.average_summary_group.setStyleSheet(u"")
        self.verticalLayout_20 = QVBoxLayout(self.average_summary_group)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.summary_average_label = QLabel(self.average_summary_group)
        self.summary_average_label.setObjectName(u"summary_average_label")
        self.summary_average_label.setFont(font20)
        self.summary_average_label.setLayoutDirection(Qt.LeftToRight)
        self.summary_average_label.setAutoFillBackground(False)
        self.summary_average_label.setStyleSheet(u"")
        self.summary_average_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.summary_average_label)

        self.summary_average = QLabel(self.average_summary_group)
        self.summary_average.setObjectName(u"summary_average")
        self.summary_average.setMinimumSize(QSize(0, 50))
        self.summary_average.setMaximumSize(QSize(16777215, 50))
        self.summary_average.setFont(font21)
        self.summary_average.setStyleSheet(u"")
        self.summary_average.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.summary_average)


        self.horizontalLayout_35.addWidget(self.average_summary_group)

        self.percent_summary_group = QGroupBox(self.weight_summary_group)
        self.percent_summary_group.setObjectName(u"percent_summary_group")
        self.percent_summary_group.setLayoutDirection(Qt.LeftToRight)
        self.percent_summary_group.setStyleSheet(u"")
        self.verticalLayout_21 = QVBoxLayout(self.percent_summary_group)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.summary_percent_label = QLabel(self.percent_summary_group)
        self.summary_percent_label.setObjectName(u"summary_percent_label")
        self.summary_percent_label.setFont(font20)
        self.summary_percent_label.setLayoutDirection(Qt.LeftToRight)
        self.summary_percent_label.setAutoFillBackground(False)
        self.summary_percent_label.setStyleSheet(u"")
        self.summary_percent_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.summary_percent_label)

        self.summary_percent = QLabel(self.percent_summary_group)
        self.summary_percent.setObjectName(u"summary_percent")
        self.summary_percent.setMinimumSize(QSize(0, 50))
        self.summary_percent.setMaximumSize(QSize(16777215, 50))
        self.summary_percent.setFont(font21)
        self.summary_percent.setStyleSheet(u"")
        self.summary_percent.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.summary_percent)


        self.horizontalLayout_35.addWidget(self.percent_summary_group)


        self.verticalLayout_22.addWidget(self.weight_summary_group)


        self.verticalLayout_27.addWidget(self.weight_summary_main_group)

        self.thickness_summary_main_group = QGroupBox(self.summary_page)
        self.thickness_summary_main_group.setObjectName(u"thickness_summary_main_group")
        self.thickness_summary_main_group.setMinimumSize(QSize(0, 0))
        self.verticalLayout_25 = QVBoxLayout(self.thickness_summary_main_group)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 10)
        self.thickness_frame_title = QFrame(self.thickness_summary_main_group)
        self.thickness_frame_title.setObjectName(u"thickness_frame_title")
        self.thickness_frame_title.setMaximumSize(QSize(16777215, 80))
        self.thickness_frame_title.setFrameShape(QFrame.StyledPanel)
        self.thickness_frame_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_58 = QHBoxLayout(self.thickness_frame_title)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.thickness_summary_title = QLabel(self.thickness_frame_title)
        self.thickness_summary_title.setObjectName(u"thickness_summary_title")
        self.thickness_summary_title.setMaximumSize(QSize(16777215, 50))
        self.thickness_summary_title.setFont(font4)
        self.thickness_summary_title.setStyleSheet(u"background-color: rgb(0, 170, 127);\n"
"border-radius: 15px;")
        self.thickness_summary_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_58.addWidget(self.thickness_summary_title)


        self.verticalLayout_25.addWidget(self.thickness_frame_title)

        self.thickness_summary_group = QGroupBox(self.thickness_summary_main_group)
        self.thickness_summary_group.setObjectName(u"thickness_summary_group")
        self.thickness_summary_group.setAlignment(Qt.AlignCenter)
        self.gridLayout_2 = QGridLayout(self.thickness_summary_group)
        self.gridLayout_2.setSpacing(10)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(10, 0, 10, 10)
        self.thickness_summary_group_10 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_10.setObjectName(u"thickness_summary_group_10")
        self.thickness_summary_group_10.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_10.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_38 = QHBoxLayout(self.thickness_summary_group_10)
        self.horizontalLayout_38.setSpacing(0)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_10 = QLabel(self.thickness_summary_group_10)
        self.thickness_summary_title_10.setObjectName(u"thickness_summary_title_10")
        self.thickness_summary_title_10.setMinimumSize(QSize(55, 0))
        font22 = QFont()
        font22.setFamilies([u"Kanit"])
        font22.setPointSize(11)
        font22.setBold(False)
        font22.setItalic(False)
        font22.setUnderline(False)
        font22.setStrikeOut(False)
        self.thickness_summary_title_10.setFont(font22)
        self.thickness_summary_title_10.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_38.addWidget(self.thickness_summary_title_10)

        self.thickness_summary_frame_10 = QFrame(self.thickness_summary_group_10)
        self.thickness_summary_frame_10.setObjectName(u"thickness_summary_frame_10")
        self.thickness_summary_frame_10.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_10.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.thickness_summary_frame_10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.thickness_summary_10 = QLabel(self.thickness_summary_frame_10)
        self.thickness_summary_10.setObjectName(u"thickness_summary_10")
        font23 = QFont()
        font23.setFamilies([u"Kanit"])
        font23.setPointSize(12)
        self.thickness_summary_10.setFont(font23)
        self.thickness_summary_10.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_10.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_39.addWidget(self.thickness_summary_10)


        self.horizontalLayout_38.addWidget(self.thickness_summary_frame_10)


        self.gridLayout_2.addWidget(self.thickness_summary_group_10, 1, 4, 1, 1)

        self.thickness_summary_group_8 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_8.setObjectName(u"thickness_summary_group_8")
        self.thickness_summary_group_8.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_8.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_36 = QHBoxLayout(self.thickness_summary_group_8)
        self.horizontalLayout_36.setSpacing(0)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_8 = QLabel(self.thickness_summary_group_8)
        self.thickness_summary_title_8.setObjectName(u"thickness_summary_title_8")
        self.thickness_summary_title_8.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_8.setFont(font22)
        self.thickness_summary_title_8.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_36.addWidget(self.thickness_summary_title_8)

        self.thickness_summary_frame_8 = QFrame(self.thickness_summary_group_8)
        self.thickness_summary_frame_8.setObjectName(u"thickness_summary_frame_8")
        self.thickness_summary_frame_8.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_8.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.thickness_summary_frame_8)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.thickness_summary_8 = QLabel(self.thickness_summary_frame_8)
        self.thickness_summary_8.setObjectName(u"thickness_summary_8")
        self.thickness_summary_8.setFont(font23)
        self.thickness_summary_8.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_8.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_37.addWidget(self.thickness_summary_8)


        self.horizontalLayout_36.addWidget(self.thickness_summary_frame_8)


        self.gridLayout_2.addWidget(self.thickness_summary_group_8, 1, 2, 1, 1)

        self.thickness_summary_group_7 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_7.setObjectName(u"thickness_summary_group_7")
        self.thickness_summary_group_7.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_7.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_44 = QHBoxLayout(self.thickness_summary_group_7)
        self.horizontalLayout_44.setSpacing(0)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_7 = QLabel(self.thickness_summary_group_7)
        self.thickness_summary_title_7.setObjectName(u"thickness_summary_title_7")
        self.thickness_summary_title_7.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_7.setFont(font22)
        self.thickness_summary_title_7.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.thickness_summary_title_7)

        self.thickness_summary_frame_7 = QFrame(self.thickness_summary_group_7)
        self.thickness_summary_frame_7.setObjectName(u"thickness_summary_frame_7")
        self.thickness_summary_frame_7.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_7.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.thickness_summary_frame_7)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.thickness_summary_7 = QLabel(self.thickness_summary_frame_7)
        self.thickness_summary_7.setObjectName(u"thickness_summary_7")
        self.thickness_summary_7.setFont(font23)
        self.thickness_summary_7.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_45.addWidget(self.thickness_summary_7)


        self.horizontalLayout_44.addWidget(self.thickness_summary_frame_7)


        self.gridLayout_2.addWidget(self.thickness_summary_group_7, 1, 1, 1, 1)

        self.thickness_summary_group_9 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_9.setObjectName(u"thickness_summary_group_9")
        self.thickness_summary_group_9.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_9.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_40 = QHBoxLayout(self.thickness_summary_group_9)
        self.horizontalLayout_40.setSpacing(0)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_9 = QLabel(self.thickness_summary_group_9)
        self.thickness_summary_title_9.setObjectName(u"thickness_summary_title_9")
        self.thickness_summary_title_9.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_9.setFont(font22)
        self.thickness_summary_title_9.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_40.addWidget(self.thickness_summary_title_9)

        self.thickness_summary_frame_9 = QFrame(self.thickness_summary_group_9)
        self.thickness_summary_frame_9.setObjectName(u"thickness_summary_frame_9")
        self.thickness_summary_frame_9.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_9.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.thickness_summary_frame_9)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.summary_thickness_9 = QLabel(self.thickness_summary_frame_9)
        self.summary_thickness_9.setObjectName(u"summary_thickness_9")
        self.summary_thickness_9.setFont(font23)
        self.summary_thickness_9.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.summary_thickness_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_41.addWidget(self.summary_thickness_9)


        self.horizontalLayout_40.addWidget(self.thickness_summary_frame_9)


        self.gridLayout_2.addWidget(self.thickness_summary_group_9, 1, 3, 1, 1)

        self.thickness_summary_group_6 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_6.setObjectName(u"thickness_summary_group_6")
        self.thickness_summary_group_6.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_6.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_48 = QHBoxLayout(self.thickness_summary_group_6)
        self.horizontalLayout_48.setSpacing(0)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.horizontalLayout_48.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_6 = QLabel(self.thickness_summary_group_6)
        self.thickness_summary_title_6.setObjectName(u"thickness_summary_title_6")
        self.thickness_summary_title_6.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_6.setFont(font22)
        self.thickness_summary_title_6.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_48.addWidget(self.thickness_summary_title_6)

        self.thickness_summary_frame_6 = QFrame(self.thickness_summary_group_6)
        self.thickness_summary_frame_6.setObjectName(u"thickness_summary_frame_6")
        self.thickness_summary_frame_6.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_6.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.thickness_summary_frame_6)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.thickness_summary_6 = QLabel(self.thickness_summary_frame_6)
        self.thickness_summary_6.setObjectName(u"thickness_summary_6")
        self.thickness_summary_6.setFont(font23)
        self.thickness_summary_6.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_49.addWidget(self.thickness_summary_6)


        self.horizontalLayout_48.addWidget(self.thickness_summary_frame_6)


        self.gridLayout_2.addWidget(self.thickness_summary_group_6, 1, 0, 1, 1)

        self.thickness_summary_group_5 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_5.setObjectName(u"thickness_summary_group_5")
        self.thickness_summary_group_5.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_5.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_52 = QHBoxLayout(self.thickness_summary_group_5)
        self.horizontalLayout_52.setSpacing(0)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.horizontalLayout_52.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_5 = QLabel(self.thickness_summary_group_5)
        self.thickness_summary_title_5.setObjectName(u"thickness_summary_title_5")
        self.thickness_summary_title_5.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_5.setFont(font22)
        self.thickness_summary_title_5.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_52.addWidget(self.thickness_summary_title_5)

        self.thickness_summary_frame_5 = QFrame(self.thickness_summary_group_5)
        self.thickness_summary_frame_5.setObjectName(u"thickness_summary_frame_5")
        self.thickness_summary_frame_5.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_5.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_53 = QHBoxLayout(self.thickness_summary_frame_5)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.thickness_summary_5 = QLabel(self.thickness_summary_frame_5)
        self.thickness_summary_5.setObjectName(u"thickness_summary_5")
        self.thickness_summary_5.setFont(font23)
        self.thickness_summary_5.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_53.addWidget(self.thickness_summary_5)


        self.horizontalLayout_52.addWidget(self.thickness_summary_frame_5)


        self.gridLayout_2.addWidget(self.thickness_summary_group_5, 0, 4, 1, 1)

        self.thickness_summary_group_4 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_4.setObjectName(u"thickness_summary_group_4")
        self.thickness_summary_group_4.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_4.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_46 = QHBoxLayout(self.thickness_summary_group_4)
        self.horizontalLayout_46.setSpacing(0)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_4 = QLabel(self.thickness_summary_group_4)
        self.thickness_summary_title_4.setObjectName(u"thickness_summary_title_4")
        self.thickness_summary_title_4.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_4.setFont(font22)
        self.thickness_summary_title_4.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_46.addWidget(self.thickness_summary_title_4)

        self.thickness_summary_frame_4 = QFrame(self.thickness_summary_group_4)
        self.thickness_summary_frame_4.setObjectName(u"thickness_summary_frame_4")
        self.thickness_summary_frame_4.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_4.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.thickness_summary_frame_4)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.thickness_summary_4 = QLabel(self.thickness_summary_frame_4)
        self.thickness_summary_4.setObjectName(u"thickness_summary_4")
        self.thickness_summary_4.setFont(font23)
        self.thickness_summary_4.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.thickness_summary_4)


        self.horizontalLayout_46.addWidget(self.thickness_summary_frame_4)


        self.gridLayout_2.addWidget(self.thickness_summary_group_4, 0, 3, 1, 1)

        self.thickness_summary_group_3 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_3.setObjectName(u"thickness_summary_group_3")
        self.thickness_summary_group_3.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_3.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_54 = QHBoxLayout(self.thickness_summary_group_3)
        self.horizontalLayout_54.setSpacing(0)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalLayout_54.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_3 = QLabel(self.thickness_summary_group_3)
        self.thickness_summary_title_3.setObjectName(u"thickness_summary_title_3")
        self.thickness_summary_title_3.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_3.setFont(font22)
        self.thickness_summary_title_3.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_54.addWidget(self.thickness_summary_title_3)

        self.thickness_summary_frame_3 = QFrame(self.thickness_summary_group_3)
        self.thickness_summary_frame_3.setObjectName(u"thickness_summary_frame_3")
        self.thickness_summary_frame_3.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_3.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_55 = QHBoxLayout(self.thickness_summary_frame_3)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.thickness_summary_3 = QLabel(self.thickness_summary_frame_3)
        self.thickness_summary_3.setObjectName(u"thickness_summary_3")
        self.thickness_summary_3.setFont(font23)
        self.thickness_summary_3.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_55.addWidget(self.thickness_summary_3)


        self.horizontalLayout_54.addWidget(self.thickness_summary_frame_3)


        self.gridLayout_2.addWidget(self.thickness_summary_group_3, 0, 2, 1, 1)

        self.thickness_summary_group_2 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_2.setObjectName(u"thickness_summary_group_2")
        self.thickness_summary_group_2.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_2.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_42 = QHBoxLayout(self.thickness_summary_group_2)
        self.horizontalLayout_42.setSpacing(0)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalLayout_42.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_2 = QLabel(self.thickness_summary_group_2)
        self.thickness_summary_title_2.setObjectName(u"thickness_summary_title_2")
        self.thickness_summary_title_2.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_2.setFont(font22)
        self.thickness_summary_title_2.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_42.addWidget(self.thickness_summary_title_2)

        self.thickness_summary_frame_2 = QFrame(self.thickness_summary_group_2)
        self.thickness_summary_frame_2.setObjectName(u"thickness_summary_frame_2")
        self.thickness_summary_frame_2.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_2.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.thickness_summary_frame_2)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.thickness_summary_2 = QLabel(self.thickness_summary_frame_2)
        self.thickness_summary_2.setObjectName(u"thickness_summary_2")
        self.thickness_summary_2.setFont(font23)
        self.thickness_summary_2.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_43.addWidget(self.thickness_summary_2)


        self.horizontalLayout_42.addWidget(self.thickness_summary_frame_2)


        self.gridLayout_2.addWidget(self.thickness_summary_group_2, 0, 1, 1, 1)

        self.thickness_summary_group_1 = QGroupBox(self.thickness_summary_group)
        self.thickness_summary_group_1.setObjectName(u"thickness_summary_group_1")
        self.thickness_summary_group_1.setMinimumSize(QSize(0, 0))
        self.thickness_summary_group_1.setMaximumSize(QSize(16777215, 40))
        self.thickness_summary_group_1.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.horizontalLayout_50 = QHBoxLayout(self.thickness_summary_group_1)
        self.horizontalLayout_50.setSpacing(0)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.horizontalLayout_50.setContentsMargins(0, 0, 0, 0)
        self.thickness_summary_title_1 = QLabel(self.thickness_summary_group_1)
        self.thickness_summary_title_1.setObjectName(u"thickness_summary_title_1")
        self.thickness_summary_title_1.setMinimumSize(QSize(55, 0))
        self.thickness_summary_title_1.setFont(font22)
        self.thickness_summary_title_1.setStyleSheet(u"background-color: #0059fe;\n"
"border-top-left-radius: 8px;\n"
"border-bottom-left-radius: 8px;")
        self.thickness_summary_title_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_50.addWidget(self.thickness_summary_title_1)

        self.thickness_summary_frame_1 = QFrame(self.thickness_summary_group_1)
        self.thickness_summary_frame_1.setObjectName(u"thickness_summary_frame_1")
        font24 = QFont()
        font24.setPointSize(10)
        self.thickness_summary_frame_1.setFont(font24)
        self.thickness_summary_frame_1.setStyleSheet(u"border: solid;\n"
"border-width: 1px;\n"
"border-color: rgb(121, 121, 121);\n"
"border-top-right-radius: 8px;\n"
"border-bottom-right-radius: 8px;")
        self.thickness_summary_frame_1.setFrameShape(QFrame.StyledPanel)
        self.thickness_summary_frame_1.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_51 = QHBoxLayout(self.thickness_summary_frame_1)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.thickness_summary_1 = QLabel(self.thickness_summary_frame_1)
        self.thickness_summary_1.setObjectName(u"thickness_summary_1")
        self.thickness_summary_1.setFont(font23)
        self.thickness_summary_1.setStyleSheet(u"border: none;\n"
"color: rgb(72, 72, 72);")
        self.thickness_summary_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_51.addWidget(self.thickness_summary_1)


        self.horizontalLayout_50.addWidget(self.thickness_summary_frame_1)


        self.gridLayout_2.addWidget(self.thickness_summary_group_1, 0, 0, 1, 1)


        self.verticalLayout_25.addWidget(self.thickness_summary_group)

        self.timeout_main_group = QGroupBox(self.thickness_summary_main_group)
        self.timeout_main_group.setObjectName(u"timeout_main_group")
        self.timeout_main_group.setMinimumSize(QSize(0, 0))
        self.timeout_main_group.setMaximumSize(QSize(16777215, 100))
        self.timeout_main_group.setStyleSheet(u"#summary_min_thickness, #summary_max_thickness {\n"
"	background-color: rgb(255, 170, 0);\n"
"	border-bottom-left-radius: 15px;\n"
"	border-bottom-right-radius: 15px;\n"
"}\n"
"\n"
"#summary_min_thickness_label, #summary_max_thickness_label {\n"
"	background-color: rgb(80, 80, 80);\n"
"	border-top-left-radius: 15px;\n"
"	border-top-right-radius: 15px;\n"
"}")
        self.horizontalLayout_59 = QHBoxLayout(self.timeout_main_group)
        self.horizontalLayout_59.setSpacing(25)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(10, 0, 20, 10)
        self.thickness_min_frame = QFrame(self.timeout_main_group)
        self.thickness_min_frame.setObjectName(u"thickness_min_frame")
        self.thickness_min_frame.setMaximumSize(QSize(200, 16777215))
        self.thickness_min_frame.setLayoutDirection(Qt.LeftToRight)
        self.thickness_min_frame.setStyleSheet(u"")
        self.verticalLayout_23 = QVBoxLayout(self.thickness_min_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.summary_min_thickness_label = QLabel(self.thickness_min_frame)
        self.summary_min_thickness_label.setObjectName(u"summary_min_thickness_label")
        self.summary_min_thickness_label.setFont(font20)
        self.summary_min_thickness_label.setLayoutDirection(Qt.LeftToRight)
        self.summary_min_thickness_label.setAutoFillBackground(False)
        self.summary_min_thickness_label.setStyleSheet(u"")
        self.summary_min_thickness_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.summary_min_thickness_label)

        self.summary_min_thickness = QLabel(self.thickness_min_frame)
        self.summary_min_thickness.setObjectName(u"summary_min_thickness")
        self.summary_min_thickness.setMinimumSize(QSize(0, 50))
        self.summary_min_thickness.setMaximumSize(QSize(16777215, 50))
        self.summary_min_thickness.setFont(font21)
        self.summary_min_thickness.setStyleSheet(u"")
        self.summary_min_thickness.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.summary_min_thickness)


        self.horizontalLayout_59.addWidget(self.thickness_min_frame)

        self.thickness_max_frame = QFrame(self.timeout_main_group)
        self.thickness_max_frame.setObjectName(u"thickness_max_frame")
        self.thickness_max_frame.setMaximumSize(QSize(200, 16777215))
        self.thickness_max_frame.setLayoutDirection(Qt.LeftToRight)
        self.thickness_max_frame.setStyleSheet(u"")
        self.verticalLayout_24 = QVBoxLayout(self.thickness_max_frame)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.summary_max_thickness_label = QLabel(self.thickness_max_frame)
        self.summary_max_thickness_label.setObjectName(u"summary_max_thickness_label")
        self.summary_max_thickness_label.setFont(font20)
        self.summary_max_thickness_label.setLayoutDirection(Qt.LeftToRight)
        self.summary_max_thickness_label.setAutoFillBackground(False)
        self.summary_max_thickness_label.setStyleSheet(u"")
        self.summary_max_thickness_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.summary_max_thickness_label)

        self.summary_max_thickness = QLabel(self.thickness_max_frame)
        self.summary_max_thickness.setObjectName(u"summary_max_thickness")
        self.summary_max_thickness.setMinimumSize(QSize(0, 50))
        self.summary_max_thickness.setMaximumSize(QSize(16777215, 50))
        self.summary_max_thickness.setFont(font21)
        self.summary_max_thickness.setStyleSheet(u"")
        self.summary_max_thickness.setAlignment(Qt.AlignCenter)

        self.verticalLayout_24.addWidget(self.summary_max_thickness)


        self.horizontalLayout_59.addWidget(self.thickness_max_frame)

        self.timeout_group = QGroupBox(self.timeout_main_group)
        self.timeout_group.setObjectName(u"timeout_group")
        self.timeout_group.setMinimumSize(QSize(0, 0))
        self.timeout_group.setMaximumSize(QSize(16777215, 70))
        font25 = QFont()
        font25.setPointSize(1)
        self.timeout_group.setFont(font25)
        self.verticalLayout_26 = QVBoxLayout(self.timeout_group)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.timeout_title = QLabel(self.timeout_group)
        self.timeout_title.setObjectName(u"timeout_title")
        font26 = QFont()
        font26.setFamilies([u"Kanit"])
        font26.setPointSize(11)
        self.timeout_title.setFont(font26)
        self.timeout_title.setStyleSheet(u"color: rgb(80, 80, 80);")
        self.timeout_title.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.timeout_title)

        self.timeout = QLabel(self.timeout_group)
        self.timeout.setObjectName(u"timeout")
        self.timeout.setFont(font5)
        self.timeout.setStyleSheet(u"color: rgb(255, 0, 0);")
        self.timeout.setAlignment(Qt.AlignCenter)

        self.verticalLayout_26.addWidget(self.timeout)


        self.horizontalLayout_59.addWidget(self.timeout_group)

        self.button_exit = QPushButton(self.timeout_main_group)
        self.button_exit.setObjectName(u"button_exit")
        self.button_exit.setMinimumSize(QSize(65, 65))
        self.button_exit.setMaximumSize(QSize(65, 65))
        self.button_exit.setCursor(QCursor(Qt.PointingHandCursor))
        self.button_exit.setStyleSheet(u"border: none;")
        icon7 = QIcon()
        icon7.addFile(u":/assets/icon/exit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button_exit.setIcon(icon7)
        self.button_exit.setIconSize(QSize(60, 60))

        self.horizontalLayout_59.addWidget(self.button_exit)


        self.verticalLayout_25.addWidget(self.timeout_main_group)


        self.verticalLayout_27.addWidget(self.thickness_summary_main_group)

        self.stackedWidget.addWidget(self.summary_page)
        self.manual_page = QWidget()
        self.manual_page.setObjectName(u"manual_page")
        self.verticalLayout_6 = QVBoxLayout(self.manual_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.manual_title_group = QFrame(self.manual_page)
        self.manual_title_group.setObjectName(u"manual_title_group")
        self.manual_title_group.setMaximumSize(QSize(16777215, 80))
        self.manual_title_group.setFrameShape(QFrame.StyledPanel)
        self.manual_title_group.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.manual_title_group)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(30, 0, 30, 0)
        self.manual_title = QLabel(self.manual_title_group)
        self.manual_title.setObjectName(u"manual_title")
        self.manual_title.setMaximumSize(QSize(16777215, 50))
        self.manual_title.setFont(font4)
        self.manual_title.setStyleSheet(u"background-color: rgb(52, 157, 77);\n"
"border-radius: 15px;")
        self.manual_title.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.manual_title)


        self.verticalLayout_6.addWidget(self.manual_title_group)

        self.frame_3 = QFrame(self.manual_page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.groupBox_5 = QGroupBox(self.frame_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(60, 120, 120, 100))

        self.verticalLayout_6.addWidget(self.frame_3)

        self.stackedWidget.addWidget(self.manual_page)
        self.develops_page = QWidget()
        self.develops_page.setObjectName(u"develops_page")
        self.verticalLayout_31 = QVBoxLayout(self.develops_page)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_2 = QFrame(self.develops_page)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setStyleSheet(u"QLabel {\n"
"	color: rgb(100, 100, 100);\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.widget_3 = QWidget(self.frame_2)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_65 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.horizontalLayout_65.setContentsMargins(0, -1, 0, -1)
        self.groupBox_6 = QGroupBox(self.widget_3)
        self.groupBox_6.setObjectName(u"groupBox_6")
        self.groupBox_6.setMaximumSize(QSize(16777215, 100))
        font27 = QFont()
        font27.setFamilies([u"Kanit"])
        font27.setPointSize(14)
        font27.setBold(True)
        self.groupBox_6.setFont(font27)
        self.groupBox_6.setStyleSheet(u"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}")
        self.groupBox_6.setAlignment(Qt.AlignCenter)
        self.wifi_signal_2 = QLabel(self.groupBox_6)
        self.wifi_signal_2.setObjectName(u"wifi_signal_2")
        self.wifi_signal_2.setGeometry(QRect(20, 10, 80, 80))
        self.wifi_signal_2.setMinimumSize(QSize(80, 80))
        self.wifi_signal_2.setMaximumSize(QSize(80, 80))
        self.wifi_signal_2.setPixmap(QPixmap(u":/assets/icon/no-wifi.png"))
        self.wifi_signal_2.setScaledContents(True)
        self.ping = QLabel(self.groupBox_6)
        self.ping.setObjectName(u"ping")
        self.ping.setGeometry(QRect(120, 60, 171, 25))
        self.ping.setMinimumSize(QSize(0, 25))
        self.ping.setMaximumSize(QSize(16777215, 25))
        self.ping.setFont(font27)
        self.ping.setStyleSheet(u"color: rgb(100, 100, 100);")
        self.ssid = QLabel(self.groupBox_6)
        self.ssid.setObjectName(u"ssid")
        self.ssid.setGeometry(QRect(120, 30, 221, 25))
        self.ssid.setMinimumSize(QSize(0, 25))
        self.ssid.setMaximumSize(QSize(16777215, 25))
        self.ssid.setFont(font27)
        self.ssid.setStyleSheet(u"color: rgb(100, 100, 100);")

        self.horizontalLayout_65.addWidget(self.groupBox_6)

        self.groupBox_7 = QGroupBox(self.widget_3)
        self.groupBox_7.setObjectName(u"groupBox_7")
        self.groupBox_7.setMaximumSize(QSize(200, 100))
        self.groupBox_7.setFont(font27)
        self.groupBox_7.setStyleSheet(u"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}")
        self.groupBox_7.setAlignment(Qt.AlignCenter)
        self.wifi_signal_5 = QLabel(self.groupBox_7)
        self.wifi_signal_5.setObjectName(u"wifi_signal_5")
        self.wifi_signal_5.setGeometry(QRect(20, 30, 50, 50))
        self.wifi_signal_5.setMinimumSize(QSize(50, 50))
        self.wifi_signal_5.setMaximumSize(QSize(50, 50))
        self.wifi_signal_5.setPixmap(QPixmap(u":/assets/icon/machine.png"))
        self.wifi_signal_5.setScaledContents(True)
        self.current_tabletID_2 = QLabel(self.groupBox_7)
        self.current_tabletID_2.setObjectName(u"current_tabletID_2")
        self.current_tabletID_2.setGeometry(QRect(90, 35, 49, 41))
        self.current_tabletID_2.setFont(font21)

        self.horizontalLayout_65.addWidget(self.groupBox_7)


        self.verticalLayout_39.addWidget(self.widget_3)

        self.view_pages_group_2 = QGroupBox(self.frame_2)
        self.view_pages_group_2.setObjectName(u"view_pages_group_2")
        self.view_pages_group_2.setMinimumSize(QSize(0, 0))
        self.view_pages_group_2.setMaximumSize(QSize(16777215, 180))
        self.view_pages_group_2.setFont(font27)
        self.view_pages_group_2.setStyleSheet(u"QScrollArea {\n"
"	border: none;\n"
"}\n"
"\n"
"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.view_pages_group_2.setAlignment(Qt.AlignCenter)
        self.view_pages_group_2.setFlat(False)
        self.horizontalLayout_56 = QHBoxLayout(self.view_pages_group_2)
        self.horizontalLayout_56.setSpacing(15)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalLayout_56.setContentsMargins(15, 40, 15, 15)
        self.scrollArea = QScrollArea(self.view_pages_group_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(0, 130))
        self.scrollArea.setMaximumSize(QSize(16777215, 135))
        self.scrollArea.setStyleSheet(u"QGroupBox {\n"
"	min-width: 120px;\n"
"	max-width: 120px;\n"
"	min-height: 100px;\n"
"}")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 563, 130))
        self.horizontalLayout_64 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_56.addWidget(self.scrollArea)


        self.verticalLayout_39.addWidget(self.view_pages_group_2)


        self.verticalLayout_31.addWidget(self.frame_2)

        self.view_pages_group = QGroupBox(self.develops_page)
        self.view_pages_group.setObjectName(u"view_pages_group")
        self.view_pages_group.setMinimumSize(QSize(0, 180))
        self.view_pages_group.setMaximumSize(QSize(16777215, 180))
        self.view_pages_group.setFont(font27)
        self.view_pages_group.setStyleSheet(u"QGroupBox {\n"
"	border: solid;\n"
"	border-width: 1px;\n"
"	border-color: rgb(255, 170, 0);\n"
"	border-radius: 8px;\n"
"	color: #262626;\n"
"}\n"
"\n"
"QPushButton {\n"
"	border: none;\n"
"}\n"
"")
        self.view_pages_group.setAlignment(Qt.AlignCenter)
        self.view_pages_group.setFlat(False)
        self.horizontalLayout_7 = QHBoxLayout(self.view_pages_group)
        self.horizontalLayout_7.setSpacing(15)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(15, 40, 15, 15)
        self.groupBox = QGroupBox(self.view_pages_group)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font23)
        self.groupBox.setAlignment(Qt.AlignCenter)
        self.verticalLayout_16 = QVBoxLayout(self.groupBox)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(-1, -1, -1, 0)
        self.weight_page_view = QPushButton(self.groupBox)
        self.weight_page_view.setObjectName(u"weight_page_view")
        self.weight_page_view.setFont(font26)
        self.weight_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.weight_page_view.setLayoutDirection(Qt.LeftToRight)
        self.weight_page_view.setStyleSheet(u"")
        icon8 = QIcon()
        icon8.addFile(u":/assets/icon/weighing.png", QSize(), QIcon.Normal, QIcon.Off)
        self.weight_page_view.setIcon(icon8)
        self.weight_page_view.setIconSize(QSize(80, 80))
        self.weight_page_view.setAutoRepeat(False)

        self.verticalLayout_16.addWidget(self.weight_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.view_pages_group)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font23)
        self.groupBox_2.setAlignment(Qt.AlignCenter)
        self.verticalLayout_17 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.thickness_page_view = QPushButton(self.groupBox_2)
        self.thickness_page_view.setObjectName(u"thickness_page_view")
        self.thickness_page_view.setFont(font26)
        self.thickness_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.thickness_page_view.setLayoutDirection(Qt.LeftToRight)
        self.thickness_page_view.setStyleSheet(u"")
        icon9 = QIcon()
        icon9.addFile(u":/assets/icon/thickness.png", QSize(), QIcon.Normal, QIcon.Off)
        self.thickness_page_view.setIcon(icon9)
        self.thickness_page_view.setIconSize(QSize(80, 80))
        self.thickness_page_view.setAutoRepeat(False)

        self.verticalLayout_17.addWidget(self.thickness_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.view_pages_group)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font23)
        self.groupBox_3.setAlignment(Qt.AlignCenter)
        self.verticalLayout_29 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.characteristics_page_view = QPushButton(self.groupBox_3)
        self.characteristics_page_view.setObjectName(u"characteristics_page_view")
        self.characteristics_page_view.setFont(font26)
        self.characteristics_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.characteristics_page_view.setLayoutDirection(Qt.LeftToRight)
        self.characteristics_page_view.setStyleSheet(u"")
        icon10 = QIcon()
        icon10.addFile(u":/assets/icon/characteristics.png", QSize(), QIcon.Normal, QIcon.Off)
        self.characteristics_page_view.setIcon(icon10)
        self.characteristics_page_view.setIconSize(QSize(80, 80))
        self.characteristics_page_view.setAutoRepeat(False)

        self.verticalLayout_29.addWidget(self.characteristics_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox_3)

        self.groupBox_4 = QGroupBox(self.view_pages_group)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setFont(font23)
        self.groupBox_4.setAlignment(Qt.AlignCenter)
        self.verticalLayout_30 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.summary_page_view = QPushButton(self.groupBox_4)
        self.summary_page_view.setObjectName(u"summary_page_view")
        self.summary_page_view.setFont(font26)
        self.summary_page_view.setCursor(QCursor(Qt.PointingHandCursor))
        self.summary_page_view.setLayoutDirection(Qt.LeftToRight)
        self.summary_page_view.setStyleSheet(u"")
        icon11 = QIcon()
        icon11.addFile(u":/assets/icon/summary.png", QSize(), QIcon.Normal, QIcon.Off)
        self.summary_page_view.setIcon(icon11)
        self.summary_page_view.setIconSize(QSize(80, 80))
        self.summary_page_view.setAutoRepeat(False)

        self.verticalLayout_30.addWidget(self.summary_page_view)


        self.horizontalLayout_7.addWidget(self.groupBox_4)


        self.verticalLayout_31.addWidget(self.view_pages_group)

        self.stackedWidget.addWidget(self.develops_page)
        self.process_page = QWidget()
        self.process_page.setObjectName(u"process_page")
        self.horizontalLayout_61 = QHBoxLayout(self.process_page)
        self.horizontalLayout_61.setSpacing(0)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalLayout_61.setContentsMargins(0, 0, 0, 0)
        self.process_main_frame = QFrame(self.process_page)
        self.process_main_frame.setObjectName(u"process_main_frame")
        self.process_main_frame.setFrameShape(QFrame.StyledPanel)
        self.process_main_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.process_main_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.process_frame = QFrame(self.process_main_frame)
        self.process_frame.setObjectName(u"process_frame")
        self.process_frame.setFrameShape(QFrame.StyledPanel)
        self.process_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_32 = QVBoxLayout(self.process_frame)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.process_img_frame = QFrame(self.process_frame)
        self.process_img_frame.setObjectName(u"process_img_frame")
        self.process_img_frame.setFrameShape(QFrame.StyledPanel)
        self.process_img_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_62 = QHBoxLayout(self.process_img_frame)
        self.horizontalLayout_62.setSpacing(0)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.horizontalLayout_62.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(164, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_2)

        self.process_img = QLabel(self.process_img_frame)
        self.process_img.setObjectName(u"process_img")
        self.process_img.setMinimumSize(QSize(350, 350))
        self.process_img.setMaximumSize(QSize(300, 300))
        self.process_img.setPixmap(QPixmap(u":/assets/gif/connecting.gif"))
        self.process_img.setScaledContents(True)
        self.process_img.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_62.addWidget(self.process_img)

        self.horizontalSpacer_3 = QSpacerItem(163, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_62.addItem(self.horizontalSpacer_3)


        self.verticalLayout_32.addWidget(self.process_img_frame)

        self.process_label_line_1 = QLabel(self.process_frame)
        self.process_label_line_1.setObjectName(u"process_label_line_1")
        self.process_label_line_1.setMinimumSize(QSize(0, 30))
        self.process_label_line_1.setMaximumSize(QSize(16777215, 30))
        self.process_label_line_1.setFont(font4)
        self.process_label_line_1.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_1.setFrameShape(QFrame.NoFrame)
        self.process_label_line_1.setFrameShadow(QFrame.Plain)
        self.process_label_line_1.setLineWidth(1)
        self.process_label_line_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_1)

        self.process_label_line_2 = QLabel(self.process_frame)
        self.process_label_line_2.setObjectName(u"process_label_line_2")
        self.process_label_line_2.setMinimumSize(QSize(0, 30))
        self.process_label_line_2.setMaximumSize(QSize(16777215, 30))
        self.process_label_line_2.setFont(font11)
        self.process_label_line_2.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_2.setFrameShape(QFrame.NoFrame)
        self.process_label_line_2.setFrameShadow(QFrame.Plain)
        self.process_label_line_2.setLineWidth(1)
        self.process_label_line_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_2)

        self.process_label_line_3 = QLabel(self.process_frame)
        self.process_label_line_3.setObjectName(u"process_label_line_3")
        self.process_label_line_3.setMinimumSize(QSize(0, 30))
        self.process_label_line_3.setMaximumSize(QSize(16777215, 30))
        self.process_label_line_3.setFont(font11)
        self.process_label_line_3.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_3.setFrameShape(QFrame.NoFrame)
        self.process_label_line_3.setFrameShadow(QFrame.Plain)
        self.process_label_line_3.setLineWidth(1)
        self.process_label_line_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_3)

        self.process_label_line_4 = QLabel(self.process_frame)
        self.process_label_line_4.setObjectName(u"process_label_line_4")
        self.process_label_line_4.setMinimumSize(QSize(0, 30))
        self.process_label_line_4.setMaximumSize(QSize(16777215, 30))
        self.process_label_line_4.setFont(font7)
        self.process_label_line_4.setStyleSheet(u"color: rgb(128, 128, 128);")
        self.process_label_line_4.setFrameShape(QFrame.NoFrame)
        self.process_label_line_4.setFrameShadow(QFrame.Plain)
        self.process_label_line_4.setLineWidth(1)
        self.process_label_line_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_32.addWidget(self.process_label_line_4)


        self.verticalLayout_33.addWidget(self.process_frame)


        self.horizontalLayout_61.addWidget(self.process_main_frame)

        self.stackedWidget.addWidget(self.process_page)

        self.verticalLayout_5.addWidget(self.stackedWidget)


        self.gridLayout_3.addWidget(self.screen_page, 0, 2, 1, 1)

        self.show_sidebar = QWidget(self.centralwidget)
        self.show_sidebar.setObjectName(u"show_sidebar")
        self.show_sidebar.setEnabled(True)
        self.show_sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton {\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color: rgb(0, 150, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.show_sidebar)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, 0, 0, -1)
        self.profile_img1 = QLabel(self.show_sidebar)
        self.profile_img1.setObjectName(u"profile_img1")
        self.profile_img1.setMinimumSize(QSize(80, 80))
        self.profile_img1.setMaximumSize(QSize(80, 80))
        self.profile_img1.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img1.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.profile_img1)

        self.label_3 = QLabel(self.show_sidebar)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font21)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_2.addWidget(self.label_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(20)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.home_1 = QPushButton(self.show_sidebar)
        self.home_1.setObjectName(u"home_1")
        font28 = QFont()
        font28.setFamilies([u"Kanit"])
        font28.setPointSize(12)
        font28.setBold(False)
        self.home_1.setFont(font28)
        self.home_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/assets/icon/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_1.setIcon(icon12)
        self.home_1.setIconSize(QSize(40, 40))
        self.home_1.setCheckable(True)
        self.home_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.home_1)

        self.manual_1 = QPushButton(self.show_sidebar)
        self.manual_1.setObjectName(u"manual_1")
        self.manual_1.setFont(font23)
        self.manual_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon13 = QIcon()
        icon13.addFile(u":/assets/icon/manual_1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manual_1.setIcon(icon13)
        self.manual_1.setIconSize(QSize(40, 40))
        self.manual_1.setCheckable(True)
        self.manual_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.manual_1)

        self.develops_1 = QPushButton(self.show_sidebar)
        self.develops_1.setObjectName(u"develops_1")
        self.develops_1.setFont(font26)
        self.develops_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/assets/icon/developer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.develops_1.setIcon(icon14)
        self.develops_1.setIconSize(QSize(50, 50))
        self.develops_1.setCheckable(True)
        self.develops_1.setAutoExclusive(True)

        self.verticalLayout_2.addWidget(self.develops_1)


        self.verticalLayout_4.addLayout(self.verticalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)

        self.signout_1 = QPushButton(self.show_sidebar)
        self.signout_1.setObjectName(u"signout_1")
        font29 = QFont()
        font29.setFamilies([u"Kanit"])
        font29.setPointSize(12)
        font29.setStrikeOut(False)
        font29.setKerning(True)
        self.signout_1.setFont(font29)
        self.signout_1.setCursor(QCursor(Qt.PointingHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/assets/icon/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.signout_1.setIcon(icon15)
        self.signout_1.setIconSize(QSize(50, 50))
#if QT_CONFIG(shortcut)
        self.signout_1.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.signout_1)

        self.restart = QPushButton(self.show_sidebar)
        self.restart.setObjectName(u"restart")
        self.restart.setFont(font29)
        self.restart.setCursor(QCursor(Qt.PointingHandCursor))
        icon16 = QIcon()
        icon16.addFile(u":/assets/icon/restart.png", QSize(), QIcon.Normal, QIcon.Off)
        self.restart.setIcon(icon16)
        self.restart.setIconSize(QSize(50, 50))
#if QT_CONFIG(shortcut)
        self.restart.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.restart)

        self.shutdown = QPushButton(self.show_sidebar)
        self.shutdown.setObjectName(u"shutdown")
        self.shutdown.setFont(font29)
        self.shutdown.setCursor(QCursor(Qt.PointingHandCursor))
        icon17 = QIcon()
        icon17.addFile(u":/assets/icon/shutdown1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.shutdown.setIcon(icon17)
        self.shutdown.setIconSize(QSize(50, 50))
#if QT_CONFIG(shortcut)
        self.shutdown.setShortcut(u"Ctrl+S")
#endif // QT_CONFIG(shortcut)

        self.verticalLayout_4.addWidget(self.shutdown)


        self.gridLayout_3.addWidget(self.show_sidebar, 0, 1, 1, 1)

        self.hide_sidebar = QWidget(self.centralwidget)
        self.hide_sidebar.setObjectName(u"hide_sidebar")
        self.hide_sidebar.setStyleSheet(u"QWidget {\n"
"	background-color: rgb(0, 150, 255);\n"
"	border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	height: 30px;\n"
"	border: none;\n"
"	border-radius: 10px;\n"
"	padding: 15px;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"	background-color: #f5fafe;\n"
"	color: rgb(0, 150, 255);\n"
"	font-weight: bold;\n"
"}")
        self.gridLayout_5 = QGridLayout(self.hide_sidebar)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(9, 9, 9, 9)
        self.signout_2 = QPushButton(self.hide_sidebar)
        self.signout_2.setObjectName(u"signout_2")
        self.signout_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.signout_2.setIcon(icon15)
        self.signout_2.setIconSize(QSize(50, 50))

        self.gridLayout_5.addWidget(self.signout_2, 3, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 297, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_5.addItem(self.verticalSpacer, 2, 0, 1, 1)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.profile_img2 = QLabel(self.hide_sidebar)
        self.profile_img2.setObjectName(u"profile_img2")
        self.profile_img2.setMinimumSize(QSize(80, 80))
        self.profile_img2.setMaximumSize(QSize(80, 80))
        self.profile_img2.setPixmap(QPixmap(u":/assets/images/polipharm.png"))
        self.profile_img2.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.profile_img2)


        self.gridLayout_5.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(-1, 20, -1, -1)
        self.home_2 = QPushButton(self.hide_sidebar)
        self.home_2.setObjectName(u"home_2")
        self.home_2.setMinimumSize(QSize(5, 0))
        self.home_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.home_2.setIcon(icon12)
        self.home_2.setIconSize(QSize(40, 40))
        self.home_2.setCheckable(True)
        self.home_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_2)

        self.manual_2 = QPushButton(self.hide_sidebar)
        self.manual_2.setObjectName(u"manual_2")
        self.manual_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.manual_2.setIcon(icon13)
        self.manual_2.setIconSize(QSize(40, 40))
        self.manual_2.setCheckable(True)
        self.manual_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.manual_2)

        self.develops_2 = QPushButton(self.hide_sidebar)
        self.develops_2.setObjectName(u"develops_2")
        self.develops_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.develops_2.setIcon(icon14)
        self.develops_2.setIconSize(QSize(50, 50))
        self.develops_2.setCheckable(True)
        self.develops_2.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.develops_2)


        self.gridLayout_5.addLayout(self.verticalLayout, 1, 0, 1, 1)


        self.gridLayout_3.addWidget(self.hide_sidebar, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.menu.toggled.connect(self.show_sidebar.setVisible)
        self.menu.toggled.connect(self.hide_sidebar.setHidden)
        self.develops_2.toggled.connect(self.develops_1.setChecked)
        self.develops_1.toggled.connect(self.develops_2.setChecked)
        self.manual_1.toggled.connect(self.manual_2.setChecked)
        self.manual_2.toggled.connect(self.manual_1.setChecked)
        self.home_2.toggled.connect(self.home_1.setChecked)
        self.home_1.toggled.connect(self.home_2.setChecked)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.menu.setText("")
        self.title.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e30\u0e1a\u0e1a\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e0a\u0e31\u0e48\u0e07\u0e2d\u0e2d\u0e19\u0e44\u0e25\u0e19\u0e4c", None))
        self.current_tabletID_1.setText(QCoreApplication.translate("MainWindow", u"(TXX)", None))
        self.wifi_signal.setText("")
        self.time_bar.setText(QCoreApplication.translate("MainWindow", u"HH:MM:SS", None))
        self.date_bar.setText(QCoreApplication.translate("MainWindow", u"DD/MM/YYYY", None))
        self.rfid_alert.setText(QCoreApplication.translate("MainWindow", u"\u0e41\u0e2a\u0e01\u0e19\u0e1a\u0e31\u0e15\u0e23\u0e1e\u0e19\u0e31\u0e01\u0e07\u0e32\u0e19", None))
        self.scale_img.setText("")
        self.rfid.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.update_settings.setText(QCoreApplication.translate("MainWindow", u"\u0e2d\u0e31\u0e1e\u0e40\u0e14\u0e17\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.clear_settings.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e49\u0e32\u0e07\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e15\u0e31\u0e49\u0e07\u0e04\u0e48\u0e32", None))
        self.reset_weighing.setText(QCoreApplication.translate("MainWindow", u"\u0e23\u0e35\u0e40\u0e0b\u0e47\u0e15\u0e01\u0e32\u0e23\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.Productname_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e37\u0e48\u0e2d\u0e22\u0e32", None))
        self.Productname.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.Lot.setText(QCoreApplication.translate("MainWindow", u"XXXXXXX", None))
        self.Lot_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e02\u0e17\u0e35\u0e48\u0e1c\u0e25\u0e34\u0e15", None))
        self.BalanceID.setText(QCoreApplication.translate("MainWindow", u"XXXXXXX", None))
        self.Balance_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e0a\u0e31\u0e48\u0e07\u0e2b\u0e21\u0e32\u0e22\u0e40\u0e25\u0e02", None))
        self.TabletID.setText(QCoreApplication.translate("MainWindow", u"XXX", None))
        self.TabletID_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01", None))
        self.Weight10s.setText(QCoreApplication.translate("MainWindow", u"XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.Weight10s_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e15\u0e32\u0e21\u0e17\u0e24\u0e29\u0e0e\u0e35 10 \u0e40\u0e21\u0e47\u0e14", None))
        self.Weight10sPer_Label.setText(QCoreApplication.translate("MainWindow", u"% \u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e1a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e1a\u0e19\u0e17\u0e35\u0e48\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a", None))
        self.Weight10sPer.setText(QCoreApplication.translate("MainWindow", u"XX.XXX %", None))
        self.MeanWeightInhouse_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01 10 \u0e40\u0e21\u0e47\u0e14", None))
        self.MeanWeightInhouse.setText(QCoreApplication.translate("MainWindow", u"XX.XXX - XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.MeanWeightREG.setText(QCoreApplication.translate("MainWindow", u"XX.XXX - XX.XXX \u0e01\u0e23\u0e31\u0e21", None))
        self.MeanWeightREG_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e48\u0e27\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e1a\u0e35\u0e48\u0e22\u0e07\u0e40\u0e1a\u0e19\u0e17\u0e35\u0e48\u0e01\u0e0f\u0e2b\u0e21\u0e32\u0e22\u0e22\u0e2d\u0e21\u0e23\u0e31\u0e1a", None))
        self.Thickness_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e48\u0e32\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32(Thickness)", None))
        self.Thickness.setText(QCoreApplication.translate("MainWindow", u"XX.XX - XX.XX \u0e21\u0e34\u0e25\u0e25\u0e34\u0e40\u0e21\u0e15\u0e23(mm.)", None))
        self.Operator_Label.setText(QCoreApplication.translate("MainWindow", u"\u0e1c\u0e39\u0e49\u0e1b\u0e0f\u0e34\u0e1a\u0e31\u0e15\u0e34\u0e07\u0e32\u0e19", None))
        self.Operator.setText(QCoreApplication.translate("MainWindow", u"XXXXXXXXXX", None))
        self.weight_label_1.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e31\u0e48\u0e07\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48 1", None))
        self.weight_1.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.weight_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e31\u0e48\u0e07\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48 2", None))
        self.weight_2.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.average_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", None))
        self.average.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.thickness_title.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e07\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.thickness_val_title_1.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 1", None))
        self.thickness_val_1.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_6.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 6", None))
        self.thickness_val_6.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_2.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 2", None))
        self.thickness_val_2.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_7.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 7", None))
        self.thickness_val_7.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_3.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 3", None))
        self.thickness_val_3.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_8.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 8", None))
        self.thickness_val_8.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_4.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 4", None))
        self.thickness_val_4.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_9.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 9", None))
        self.thickness_val_9.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_5.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 5", None))
        self.thickness_val_5.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_val_title_10.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 10", None))
        self.thickness_val_10.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.button_thickness_confirm.setText(QCoreApplication.translate("MainWindow", u" \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.button_thickness_cancel.setText(QCoreApplication.translate("MainWindow", u" \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.thickness_input_title.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e07\u0e1a\u0e31\u0e19\u0e17\u0e36\u0e01\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.thickness_val_label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 1", None))
        self.thickness_val_input.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.key_1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.key_2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.key_3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.key_4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.key_5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.key_6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.key_7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.key_8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.key_9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.key_dot.setText("")
        self.key_0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.key_backspace.setText("")
        self.thickness_img.setText("")
        self.key_enter.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e37\u0e19\u0e22\u0e31\u0e19", None))
        self.key_cancel.setText(QCoreApplication.translate("MainWindow", u"  \u0e22\u0e01\u0e40\u0e25\u0e34\u0e01", None))
        self.thickness_title_2.setText(QCoreApplication.translate("MainWindow", u"\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.tablet_front_img.setText("")
        self.characteristics_abnomal.setText(QCoreApplication.translate("MainWindow", u"\u0e1c\u0e34\u0e14\u0e1b\u0e01\u0e15\u0e34", None))
        self.characteristics_nomal.setText(QCoreApplication.translate("MainWindow", u"\u0e1b\u0e01\u0e15\u0e34", None))
        self.tablet_behind_img.setText("")
        self.tablet_front_label.setText(QCoreApplication.translate("MainWindow", u"\u0e14\u0e49\u0e32\u0e19\u0e2b\u0e19\u0e49\u0e32", None))
        self.tablet_behind_label.setText(QCoreApplication.translate("MainWindow", u"\u0e14\u0e49\u0e32\u0e19\u0e2b\u0e25\u0e31\u0e07", None))
        self.weight_summary_main_group.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.weight_summary_title.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e23\u0e38\u0e1b\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e01\u0e32\u0e23\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.summary_weight_label_1.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e31\u0e48\u0e07\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48 1", None))
        self.summary_weight_1.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.summary_weight_label_2.setText(QCoreApplication.translate("MainWindow", u"\u0e0a\u0e31\u0e48\u0e07\u0e04\u0e23\u0e31\u0e49\u0e07\u0e17\u0e35\u0e48 2", None))
        self.summary_weight_2.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.summary_average_label.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", None))
        self.summary_average.setText(QCoreApplication.translate("MainWindow", u"XX.XXX", None))
        self.summary_percent_label.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e1b\u0e2d\u0e23\u0e4c\u0e40\u0e0b\u0e47\u0e19\u0e15\u0e4c\u0e40\u0e09\u0e25\u0e35\u0e48\u0e22", None))
        self.summary_percent.setText(QCoreApplication.translate("MainWindow", u"XX.XX%", None))
        self.thickness_summary_title.setText(QCoreApplication.translate("MainWindow", u"\u0e2a\u0e23\u0e38\u0e1b\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.thickness_summary_title_10.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 10", None))
        self.thickness_summary_10.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_8.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 8", None))
        self.thickness_summary_8.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_7.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 7", None))
        self.thickness_summary_7.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_9.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 9", None))
        self.summary_thickness_9.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_6.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 6", None))
        self.thickness_summary_6.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_5.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 5", None))
        self.thickness_summary_5.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_4.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 4", None))
        self.thickness_summary_4.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_3.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 3", None))
        self.thickness_summary_3.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_2.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 2", None))
        self.thickness_summary_2.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.thickness_summary_title_1.setText(QCoreApplication.translate("MainWindow", u"\u0e40\u0e21\u0e47\u0e14\u0e17\u0e35\u0e48 1", None))
        self.thickness_summary_1.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.summary_min_thickness_label.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32\u0e15\u0e48\u0e33\u0e2a\u0e38\u0e14", None))
        self.summary_min_thickness.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.summary_max_thickness_label.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32\u0e2a\u0e39\u0e07\u0e2a\u0e38\u0e14", None))
        self.summary_max_thickness.setText(QCoreApplication.translate("MainWindow", u"XX.XX", None))
        self.timeout_title.setText(QCoreApplication.translate("MainWindow", u"\u0e19\u0e31\u0e1a\u0e40\u0e27\u0e25\u0e32\u0e16\u0e2d\u0e22\u0e2b\u0e25\u0e31\u0e07", None))
        self.timeout.setText(QCoreApplication.translate("MainWindow", u"180 s.", None))
        self.button_exit.setText("")
        self.manual_title.setText(QCoreApplication.translate("MainWindow", u"\u0e04\u0e39\u0e48\u0e21\u0e37\u0e2d\u0e01\u0e32\u0e23\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"GroupBox", None))
        self.groupBox_6.setTitle(QCoreApplication.translate("MainWindow", u"\u0e01\u0e32\u0e23\u0e40\u0e0a\u0e37\u0e48\u0e2d\u0e21\u0e15\u0e48\u0e2d\u0e44\u0e27\u0e44\u0e1f", None))
        self.wifi_signal_2.setText("")
        self.ping.setText(QCoreApplication.translate("MainWindow", u"Ping: 00 ms", None))
        self.ssid.setText(QCoreApplication.translate("MainWindow", u"SSID: XXXXXXXXXXX", None))
        self.groupBox_7.setTitle(QCoreApplication.translate("MainWindow", u"\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01", None))
        self.wifi_signal_5.setText("")
        self.current_tabletID_2.setText(QCoreApplication.translate("MainWindow", u"T01", None))
        self.view_pages_group_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0e23\u0e32\u0e22\u0e01\u0e32\u0e23\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01 (\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e40\u0e04\u0e23\u0e37\u0e48\u0e2d\u0e07\u0e15\u0e2d\u0e01\u0e17\u0e35\u0e48\u0e1b\u0e0f\u0e34\u0e1a\u0e15\u0e34\u0e07\u0e32\u0e19)", None))
        self.view_pages_group.setTitle(QCoreApplication.translate("MainWindow", u"\u0e40\u0e25\u0e37\u0e2d\u0e01\u0e14\u0e39\u0e2b\u0e19\u0e49\u0e32\u0e40\u0e21\u0e19\u0e39\u0e01\u0e32\u0e23\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e0a\u0e31\u0e48\u0e07\u0e19\u0e49\u0e33\u0e2b\u0e19\u0e31\u0e01", None))
        self.weight_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.weight_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e1b\u0e49\u0e2d\u0e19\u0e04\u0e27\u0e32\u0e21\u0e2b\u0e19\u0e32", None))
        self.thickness_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.thickness_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e25\u0e31\u0e01\u0e29\u0e13\u0e30\u0e40\u0e21\u0e47\u0e14\u0e22\u0e32", None))
        self.characteristics_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.characteristics_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u0e2b\u0e19\u0e49\u0e32\u0e2a\u0e23\u0e38\u0e1b\u0e02\u0e49\u0e2d\u0e21\u0e39\u0e25", None))
        self.summary_page_view.setText("")
#if QT_CONFIG(shortcut)
        self.summary_page_view.setShortcut("")
#endif // QT_CONFIG(shortcut)
        self.process_img.setText("")
        self.process_label_line_1.setText(QCoreApplication.translate("MainWindow", u"ONLINE WEIGHING SYSTEM", None))
        self.process_label_line_2.setText(QCoreApplication.translate("MainWindow", u"Created by Nattapon pondonko", None))
        self.process_label_line_3.setText(QCoreApplication.translate("MainWindow", u"Engineering Department", None))
        self.process_label_line_4.setText("")
        self.profile_img1.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"WEIGHT V1", None))
        self.home_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e2b\u0e19\u0e49\u0e32\u0e2b\u0e25\u0e31\u0e01", None))
        self.manual_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e27\u0e34\u0e18\u0e35\u0e43\u0e0a\u0e49\u0e07\u0e32\u0e19", None))
        self.develops_1.setText(QCoreApplication.translate("MainWindow", u"Develops ", None))
        self.signout_1.setText(QCoreApplication.translate("MainWindow", u"  \u0e2d\u0e2d\u0e01\u0e08\u0e32\u0e01\u0e23\u0e30\u0e1a\u0e1a", None))
        self.restart.setText(QCoreApplication.translate("MainWindow", u"  \u0e23\u0e35\u0e2a\u0e15\u0e32\u0e23\u0e4c\u0e17", None))
        self.shutdown.setText(QCoreApplication.translate("MainWindow", u"  \u0e1b\u0e34\u0e14\u0e42\u0e1b\u0e23\u0e41\u0e01\u0e23\u0e21", None))
        self.signout_2.setText("")
        self.profile_img2.setText("")
        self.home_2.setText("")
        self.manual_2.setText("")
        self.develops_2.setText("")
    # retranslateUi

