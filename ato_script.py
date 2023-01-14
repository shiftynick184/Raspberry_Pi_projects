# ATO - LOW script  WIP

import machine
from machine import Pin
import network
from Onesignal import SMS_Messenger
import time
from time import sleep
from Onesignal import Notifier

#defines messager service outlined in Onesignal.py library
messenger =SMS_Messenger ("OneSiganl App ID",
                          "OneSignal App API Key",
                         ["Twilio Number"], # the number that messages are sent from in Twilio account
                          "ATO Bot",
                          "en")

#Network Parameters
ssid = "Network Name"
password = "Network Password"

#defines connection function
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
#print(water_detector.value()) - used in testing to determine the signal output in Thonny IDE

while True:
    for i in range(1):
        if water_detector.value() == 0: 
            sleep(0.5)
        # when no water detected, value is 1.  Sends a text message and the starts a 6hr timer before sending subsequent message. If container is filled past sensor, messages stop    
        else:
            messenger.send_text("The ATO water level is LOW - Top off the Tank",["OneSignal Subscribed User number"])
            time.sleep(21600)  
            
        break
