from PySide6.QtCore import QThread, Signal, Slot
import serial


class Weighing(QThread):
    get = Signal(dict)

    def __init__(self, serial=None, widget: dict ={"weight1", "weight2", "average"}):
        super().__init__()
        self.serial = serial
        self.widget_weight = [widget["weight1"], widget["weight2"]]
        self.widget_average = widget["average"]

    @Slot(dict)
    def run(self):
        weighingData = {}
        weighing = []
        # อ่านค่าจาก port rs232
        # w = self.serial.readline()
        # currentWeight = str(random.uniform(0.155,0.165))
        while len(weighing) < 2:
            currentWeight = input("Weight: ")
            # currentWeight = w.decode("ascii", errors="ignore")
            currentWeight = currentWeight.replace("?", "").strip().upper()
            currentWeight = currentWeight.replace("G", "").strip()
            currentWeight = currentWeight.replace("N", "").strip()
            currentWeight = currentWeight.replace("S", "").strip()
            currentWeight = currentWeight.replace("T,", "").strip()  # AND FX
            currentWeight = currentWeight.replace("G", "").strip()  # AND FX
            currentWeight = currentWeight.replace("+", "").strip()
            weight = round(float(currentWeight), 3)
            weighing.append(weight)

            weighingData[f"weight{len(weighing)}"] = weight
            self.widget_weight[len(weighing) - 1].setText(f"{weight:.3f}")

            weighingData["average"] = round(float(sum(weighing) / len(weighing)), 3)
            self.widget_average.setText(f"{weighingData['average']:.3f}")

        self.get.emit(weighingData)  # ส่งสัญญาณความคืบหน้า
