from PySide6.QtCore import QThread, Signal, Slot
import serial


class Weighing(QThread):
    """
    คลาสสำหรับอ่านค่าจากเครื่องชั่งน้ำหนัก \n
    โดยรับค่าจาก port rs232 และส่งค่ากลับไปยังคลาสอื่นๆ \n
    โดยส่งค่ากลับมาในรูปแบบข้อมูล dict ดังนี้    \n
    { \n
        "weight1": 0.000, \n
        "weight2": 0.000, \n
        "average": 0.000 \n
    } \n
    """

    get = Signal(dict)
    hidden = Signal(bool)

    def __init__(
        self,
        port=None,
        baudrate=9600,
        settingsFile=None,
        widget: dict = {"weight1", "weight2", "average"},
    ):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.settingsFile = settingsFile
        self.widget_weight = [widget["weight1"], widget["weight2"]]
        self.widget_average = widget["average"]

    def weightOutOfRange(self, widget, weight):
        initial_text = widget.text()
        initial_style = widget.styleSheet()
        inRange_style = f"{initial_style} color: rgb(0, 170, 127);"
        outOffRange_style = f"{initial_style} color: rgb(255, 17, 17);"
        widget.setText(f"{weight:.3f}")

        if weight <= 1:
            widget.setStyleSheet(inRange_style)
        else:
            widget.setStyleSheet(outOffRange_style)

    @Slot(dict, bool)
    def run(self):
        # self.serial = serial.Serial(port=self.port, baudrate=self.baudrate)
        weighingData = {}
        self.weighing = []

        # อ่านค่าจาก port rs232
        # currentWeight = str(random.uniform(0.155,0.165))

        while len(self.weighing) < 2:
            try:
                # readSerial = self.serial.readline()
                currentWeight = input("Weight: ")
                # currentWeight = readSerial.decode("ascii", errors="ignore")
                currentWeight = currentWeight.replace("?", "").strip().upper()
                currentWeight = currentWeight.replace("G", "").strip()
                currentWeight = currentWeight.replace("N", "").strip()
                currentWeight = currentWeight.replace("S", "").strip()
                currentWeight = currentWeight.replace("T,", "").strip()  # AND FX
                currentWeight = currentWeight.replace("G", "").strip()  # AND FX
                currentWeight = currentWeight.replace("+", "").strip()
                weight = round(float(currentWeight), 3)
                self.weighing.append(weight)
                print(f"Weight{len(self.weighing)}: {weight:.3f}")

                weighingData[f"weight{len(self.weighing)}"] = weight

                currentWidget = self.widget_weight[len(self.weighing) - 1]
                self.weightOutOfRange(currentWidget, weight)

                average = round(float(sum(self.weighing) / len(self.weighing)), 3)
                weighingData["average"] = average
                self.weightOutOfRange(self.widget_average, average)

                self.hidden.emit(True)
            
            except Exception as e:
                continue

        # self.serial.close()
        self.get.emit(weighingData)
