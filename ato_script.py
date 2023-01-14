# ATO - LOW script  WIP

import machine
from machine import Pin
import network
from Onesignal import SMS_Messenger
import time
from time import sleep
from Onesignal import Notifier

messenger =SMS_Messenger ("d44181ad-de37-410f-a285-7f47b0a9fc04",
                          "NjJjZDlkZTItOWU1YS00OTJmLThhZDMtZjM3ZWZjYTA2ODM4",
                         ["+16693382499"],
                          "ATO Bot",
                          "en")

#messenger.send_text("The ATO water level is LOW - Top off the Tank",["+17657448305"])

ssid = "It Burns When IP"
password = "Tr0utK0d@9711"

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]    
    print(f"Connected on {ip}")
    #return ip

try:
    connect()
    
except KeyboardInterrupt:
    machine.reset()
''' 
   Define sensors inputs
'''

water_detector = Pin(20, Pin.IN, Pin.PULL_UP)
print(water_detector.value())

while True:
    for i in range(1):
        if water_detector.value() == 0:
            sleep(0.5)
            
        else:
            messenger.send_text("The ATO water level is LOW - Top off the Tank",["+17657448305"])
            time.sleep(21600)
        break
