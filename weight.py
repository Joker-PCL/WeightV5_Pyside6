from ui_weight import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
from PySide6.QtCore import QTimer
from PySide6.QtGui import QMovie
import os
from src.Alert import Alert
from src.api.Login import Login
from src.api.File import File

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
gif_file = os.path.join(BASE_DIR, 'assets', 'gif', 'connecting.gif')
packing_data_file = os.path.join(BASE_DIR, 'files', 'packing_data.json')

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.packing_data = File(packing_data_file)
        
        self.thickness_val = {}
        movie = QMovie(gif_file)
        self.process_img.setMovie(movie)
        movie.start()
        
        self.stackedWidget.setCurrentWidget(self.process_page)
        # self.stackedWidget.setCurrentWidget(self.home_page)
        self.show_sidebar.setHidden(True)
        self.home_2.setChecked(True)   
        
        self.RFID_alert = Alert(self.rfid_alert)      
        self.RFID = Login(self.rfid, self.RFID_alert)
        self.RFID.scan()
        self.home_1.clicked.connect(lambda: self.switch_to_Page(self.home_page))                    
        self.home_2.clicked.connect(lambda: self.switch_to_Page(self.home_page))
        
        self.manual_1.clicked.connect(lambda: self.switch_to_Page(self.manual_page))
        self.manual_2.clicked.connect(lambda: self.switch_to_Page(self.manual_page))

        self.setting_1.clicked.connect(lambda: self.switch_to_Page(self.setting_page))
        self.setting_2.clicked.connect(lambda: self.switch_to_Page(self.setting_page))
        
        self.develops_1.clicked.connect(lambda: self.switch_to_Page(self.develops_page))
        self.develops_2.clicked.connect(lambda: self.switch_to_Page(self.develops_page))
        
        self.signout_1.clicked.connect(self.logout)
        self.signout_2.clicked.connect(self.logout)
        
        ##########################  characteristics ##########################
        self.characteristics_nomal.clicked.connect(lambda: self.characteristics("ปกติ"))
        self.characteristics_abnomal.clicked.connect(lambda: self.characteristics("ผิดปกติ"))
        
        ##########################  develops page   ##########################
        self.weight_page_view.clicked.connect(lambda: self.switch_to_Page(self.weighing_page))
        self.thickness_page_view.clicked.connect(lambda: self.switch_to_Page(self.thickness_page))
        self.characteristics_page_view.clicked.connect(lambda: self.switch_to_Page(self.characteristics_page))
        self.summary_page_view.clicked.connect(lambda: self.switch_to_Page(self.summary_page))
        self.summary_page_view.clicked.connect(lambda: self.switch_to_Page(self.summary_page))
        self.button_exit_program.clicked.connect(lambda: self.switch_to_Page(self.process_page))
        
    def switch_to_Page(self, page):
        self.stackedWidget.setCurrentWidget(page)
 
    def logout(self):
        self.RFID.stop()
        QApplication.quit()
              
    def characteristics(self, selected):
        print(selected)
        
        