import pywifi
from pywifi import const
import os
import subprocess
import re
import json
import time

from PySide6.QtGui import QPixmap
from PySide6.QtCore import QThread, Signal


class GetWiFi(QThread):
    get = Signal()

    def __init__(self, os_name):
        super().__init__()
        self.os_name = os_name

    def run(self):
        while True:
            if self.os_name == "Windows":
                try:
                    output1 = subprocess.check_output(
                        "netsh wlan show interfaces"
                    ).decode("utf-8")
                    ssid_match = re.search(r"SSID\s+: (.+)", output1)
                    if ssid_match:
                        ssid = ssid_match.group(1)
                    else:
                        ssid = "N/A"

                    signal_match = re.search(r"Signal\s+: (.+)%", output1)
                    if signal_match:
                        signal = signal_match.group(1)
                    else:
                        signal = "N/A"

                    output_ping = subprocess.check_output(
                        "ping google.com -n 1"
                    ).decode("utf-8")
                    ping_match = re.search(r"Average = (.+?)ms", output_ping)
                    if ping_match:
                        ping = ping_match.group(1)
                    else:
                        ping = "N/A"

                    self.wifi_info(ssid, signal, ping)

                except subprocess.CalledProcessError:
                    print("Error fetching WiFi information.")
                    time.sleep(3)
                    self.wifi_info()

            elif self.os_name == "Linux":
                try:
                    # ใช้ iwlist เพื่อดึงข้อมูลเกี่ยวกับเครือข่าย WiFi
                    output1 = subprocess.check_output(
                        ["/usr/sbin/iwlist", "wlan0", "scan"]
                    ).decode("utf-8")
                    ssid_match = re.search(r'ESSID:"(.+)"', output1)
                    if ssid_match:
                        ssid = ssid_match.group(1)
                    else:
                        ssid = "N/A"

                    signal_match = re.search(r"Signal level=(-\d+) dBm", output1)
                    if signal_match:
                        signal = signal_match.group(1)
                    else:
                        signal = "N/A"

                    output_ping = subprocess.check_output(
                        ["ping", "-c", "1", "google.com"]
                    ).decode("utf-8")
                    ping_match = re.search(r"time=(\d+\.?\d*) ms", output_ping)
                    if ping_match:
                        ping = int(float(ping_match.group(1)))
                    else:
                        ping = "N/A"

                    self.wifi_info(ssid, signal, ping)

                except subprocess.CalledProcessError:
                    print("Error fetching WiFi information.")
                    self.wifi_info
                    time.sleep(5)

            time.sleep(1)

    def wifi_info(self, ssid="N/A", signal="N/A", ping="N/A"):
        self.ssid = ssid
        self.signal = signal
        self.ping = ping
        self.get.emit()


class WiFi(QThread):
    """การเชื่อมต่อไวไฟ"""

    def __init__(self, window, os_name="Windows"):
        super().__init__()
        self.signalWidget1 = window.wifi_signal
        self.signalWidget2 = window.wifi_signal_2
        self.ssidWidget = window.ssid
        self.pingWidget2 = window.ping
        self.os_name = os_name
        self.ssid = ""
        self.password = ""
        self.DISCONNECTED = 0
        self.CONNECTED = 1
        self.listener = None
        self.scaner_flag = False
        self.wifi = pywifi.PyWiFi()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ICON_DIR = os.path.join(self.BASE_DIR, "..", "assets", "icon")
        self.noSignal_icon = os.path.join(self.ICON_DIR, "no-wifi.png")
        self.signal1_icon = os.path.join(self.ICON_DIR, "signal1.png")
        self.signal2_icon = os.path.join(self.ICON_DIR, "signal2.png")
        self.signal3_icon = os.path.join(self.ICON_DIR, "signal3.png")
        self.signal4_icon = os.path.join(self.ICON_DIR, "signal4.png")
        self.no_internet_icon = os.path.join(self.ICON_DIR, "no_internet.png")

        self.getWiFi = GetWiFi(self.os_name)

    getWiFiResult = Signal()

    def signal_icon(self):
        self.current_wifi = self.getWiFi
        self.getWiFiResult.emit()
        self.ssid = self.current_wifi.ssid
        self.signal = self.current_wifi.signal
        self.ping = self.current_wifi.ping

        if self.ssid == "N/A":
            signal = self.noSignal_icon
        elif self.ping == "N/A":
            signal = self.no_internet_icon
        elif self.signal == "N/A":
            signal = self.noSignal_icon
        elif self.os_name == "Windows":
            if int(self.signal) <= 25:
                signal = self.signal1_icon
            elif int(self.signal) <= 50:
                signal = self.signal2_icon
            elif int(self.signal) <= 75:
                signal = self.signal3_icon
            else:
                signal = self.signal4_icon
        elif self.os_name == "Linux":
            if int(self.signal) <= -25:
                signal = self.signal4_icon
            elif int(self.signal) <= -50:
                signal = self.signal3_icon
            elif int(self.signal) <= -75:
                signal = self.signal2_icon
            else:
                signal = self.signal1_icon

        self.signalWidget1.setPixmap(QPixmap(signal))
        self.signalWidget2.setPixmap(QPixmap(signal))
        self.ssidWidget.setText(f"SSID: {self.ssid}")
        self.pingWidget2.setText(f"Ping: {self.ping} ms")

    def show_signal_icon(self):
        print("Active Wifi")
        self.getWiFi.get.connect(self.signal_icon)
        self.getWiFi.start()

    def scan_wifi_networks(self):
        iface = self.wifi.interfaces()[0]

        iface.scan()
        # time.sleep(5)  # รอเวลาสักครู่ให้แน่ใจว่าการสแกนเครือข่ายเสร็จสิ้น
        results = iface.scan_results()

        seen_ssids = set()
        sorted_results = sorted(results, key=lambda x: x.signal, reverse=True)
        wifi_lists = []
        for network in sorted_results:
            if network.ssid not in seen_ssids:
                wifi_info = {"SSID": network.ssid, "Signal_Strength": network.signal}
                print(wifi_info)
                wifi_lists.append(wifi_info)
                seen_ssids.add(network.ssid)

        wifi_json = {"wifi": wifi_lists}
        return json.dumps(wifi_json)

    def connect_to_wifi(self, ssid, password):
        print("Connecting to wifi...")
        iface = self.wifi.interfaces()[0]

        iface.disconnect()
        time.sleep(1)

        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password

        iface.remove_all_network_profiles()
        tmp_profile = iface.add_network_profile(profile)

        iface.connect(tmp_profile)
        time.sleep(5)

        if iface.status() == const.IFACE_CONNECTED:
            print(f"Connected to {ssid} successfully!")
            return self.CONNECTED
        else:
            print("Connection failed.")
            return self.DISCONNECTED
