import pywifi
from pywifi import const
import os
import subprocess
import re
import json
import time

from PySide6.QtGui import QPixmap, QIcon, QFont
from PySide6.QtCore import QSize, Qt, QTimer, QUrl

class WiFi():
    def __init__(self, window, os_name="Windows"):
        self.window = window
        self.os_name = os_name
        self.ssid = ""
        self.password = ""
        self.DISCONNECTED = 0
        self.CONNECTED = 1
        self.listener = None
        self.scaner_flag = False
        self.wifi = pywifi.PyWiFi()
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.ICON_DIR = os.path.join(self.BASE_DIR, "..",  'assets', 'icon')
        self.noSignal_icon = os.path.join( self.ICON_DIR, 'no-wifi.png')
        self.signal1_icon = os.path.join(self.ICON_DIR, 'signal1.png')
        self.signal2_icon = os.path.join(self.ICON_DIR, 'signal2.png')
        self.signal3_icon = os.path.join(self.ICON_DIR, 'signal3.png')
        self.signal4_icon = os.path.join(self.ICON_DIR, 'signal4.png')

    def get_current_wifi(self):
        if self.os_name == "Windows":
            try:
                out = subprocess.check_output('netsh wlan show interfaces').decode("utf-8")
                ssid_match = re.search(r'SSID\s+: (.+)', out)
                if ssid_match:
                    ssid = ssid_match.group(1)
                else:
                    ssid = "N/A"
                
                signal_match = re.search(r'Signal\s+: (.+)%', out)
                if signal_match:
                    signal = signal_match.group(1)
                else:
                    signal = "N/A"
                
                return WiFiInfo(ssid, signal)
                
            except subprocess.CalledProcessError:
                print("Error fetching WiFi information.")
                return WiFiInfo()
            
        elif self.os_name == "Linux":
            try:
                # ใช้ iwlist เพื่อดึงข้อมูลเกี่ยวกับเครือข่าย WiFi
                out = subprocess.check_output(['iwlist', 'wlan0', 'scan']).decode("utf-8")
                
                ssid_match = re.search(r'ESSID:"(.+)"', out)
                if ssid_match:
                    ssid = ssid_match.group(1)
                else:
                    ssid = "N/A"
                
                signal_match = re.search(r'Signal level=(-\d+) dBm', out)
                if signal_match:
                    signal = signal_match.group(1)
                else:
                    signal = "N/A"
                
                return WiFiInfo(ssid, signal)
                
            except subprocess.CalledProcessError:
                print("Error fetching WiFi information.")
                return WiFiInfo()

    def signal_icon(self):
        self.current_wifl = self.get_current_wifi()
        self.signal = self.current_wifl.signal

        if self.signal == "N/A":
            self.window.wifi_signal.setPixmap(QPixmap(self.noSignal_icon))
        elif int(self.signal) <= 25 :
            self.window.wifi_signal.setPixmap(QPixmap(self.signal1_icon))
        elif int(self.signal) <= 50 :
            self.window.wifi_signal.setPixmap(QPixmap(self.signal2_icon))
        elif int(self.signal) <= 75 :
            self.window.wifi_signal.setPixmap(QPixmap(self.signal3_icon))
        else:
            self.window.wifi_signal.setPixmap(QPixmap(self.signal4_icon))

    def show_signal_icon(self):
        print("Active Wifi")
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.signal_icon)
        self.timer.start()

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

class WiFiInfo:
    def __init__(self, ssid="N/A", signal="N/A"):
        self.ssid = ssid
        self.signal = signal