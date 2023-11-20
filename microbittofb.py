import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import serial

ser = serial.Serial()
ser.baudrate = 115200
ser.port = "COM5"
ser.open()

cred = credentials.Certificate("C:/Users/David Cummins/Downloads/david-6d9f5-firebase-adminsdk-y5nwf-40b213a236.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://david-6d9f5-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()
ref.update({'temperature_log':''})
ref = db.reference().child('temperature_log')
source = input("Please input the source of this data: ")
while True:
    #print(type(ser.readline()))
    mb_temperature = str(ser.readline().decode('utf-8'))
    mb_temperature = mb_temperature.replace(" ","")
    mb_temperature = mb_temperature.replace("\r\n","")
    if mb_temperature.isdigit():
        ref.update({str(int(time.time())):{'Temperature':mb_temperature, 'Location':source}})
    else:
        print("check data source")