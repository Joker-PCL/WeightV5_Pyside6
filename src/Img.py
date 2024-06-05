from PySide6.QtCore import QTimer
from PySide6.QtGui import QPixmap
import os

class ShowImage():
    def __init__(self, window, paths):
        self.window = window
        self.tablet_front_img = window.tablet_front_img
        self.tablet_behind_img = window.tablet_behind_img
        self.paths = paths
        self.image_files = [f for f in os.listdir(paths) if os.path.isfile(os.path.join(paths, f))]
        self.image_index = 0
        
    def show(self, front_img, behind_img):
        self.window.tablet_front_img.setPixmap(QPixmap(front_img))
        self.window.tablet_behind_img.setPixmap(QPixmap(behind_img))
        
    def show_all(self):
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self._show_all)
        self.timer.start() 
    
    def _show_all(self):    
        if self.image_files:
            self.image_index += 1
            image_front_file = self.image_files[self.image_index]
            self.image_index += 1
            image_behind_file = self.image_files[self.image_index]
            
            image_front = os.path.join(self.paths, image_front_file)
            image_behind = os.path.join(self.paths, image_behind_file)
            
            self.show(image_front, image_behind)
            if(self.image_index == len(self.image_files) - 1):
                self.image_index = 0
