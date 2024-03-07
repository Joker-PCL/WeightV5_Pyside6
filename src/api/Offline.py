from PySide6.QtCore import QSize, Qt, QTimer, QUrl

class OnloadPage():
    def __init__(self, display):
        self.display = display
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.print_text)
        self.timer.start()
        
    # def print_text(self, text):