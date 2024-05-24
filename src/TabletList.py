from PySide6.QtWidgets import QPushButton, QGroupBox, QVBoxLayout
from PySide6.QtCore import QCoreApplication, Qt, QSize
from PySide6.QtGui import QMovie, QFont, QCursor, QIcon

class TabletList():
    def __init__(self, window, settingsFile, tabletID):
        self.window = window
        self.current_tabletID_1 = self.window.current_tabletID_1
        self.current_tabletID_2 = self.window.current_tabletID_2
        self.settingsFile = settingsFile
        font2 = QFont()
        font2.setFamilies([u"Kanit"])
        font2.setPointSize(12)

        font3 = QFont()
        font3.setFamilies([u"Kanit"])
        font3.setPointSize(11)

        self.qbox = QGroupBox(self.window.scrollAreaWidgetContents)
        self.qbox.setObjectName(f"QBoxTablet{tabletID}")
        self.qbox.setFont(font2)
        self.qbox.setAlignment(Qt.AlignCenter)
        self.qbox.setTitle(f"เครื่องตอก {tabletID}")
        vertical_layout = QVBoxLayout(self.qbox)
        vertical_layout.setObjectName(f"verticalLayout_{tabletID}")
        vertical_layout.setContentsMargins(-1, -1, -1, 0)
        vertical_layout.setSpacing(20)

        self.button = QPushButton(self.qbox)
        self.button.setObjectName(f"tablet{tabletID}")
        self.button.setFont(font3)
        self.button.setCursor(QCursor(Qt.PointingHandCursor))
        self.button.setLayoutDirection(Qt.LeftToRight)
        icon14 = QIcon()
        icon14.addFile(u":/assets/icon/machine.png", QSize(), QIcon.Normal, QIcon.Off)
        self.button.setIcon(icon14)
        self.button.setIconSize(QSize(60, 60))
        self.button.setAutoRepeat(False)
        
        vertical_layout.addWidget(self.button)
        self.window.horizontalLayout_64.addWidget(self.qbox)
        self.button.clicked.connect(lambda: self.setCurrentTablet(self.qbox))

    def setCurrentTablet(self, qbox: QGroupBox):
        tablet_title = qbox.title()
        tabletID = tablet_title.split('เครื่องตอก ')[1]
        self.current_tabletID_1.setText(f"({tabletID})")
        self.current_tabletID_2.setText(tabletID)
        settings = self.settingsFile.read()
        settings["TabletID"] = tabletID
        self.settingsFile.write(settings)
                