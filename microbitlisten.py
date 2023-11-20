import time
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
def something_Changed(response):
    print(response.event_type)
    print(response.data)
    
cred = credentials.Certificate("C:/Users/David Cummins/Downloads/david-6d9f5-firebase-adminsdk-y5nwf-40b213a236.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://david-6d9f5-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference().child('temperature_log')
my_ref = ref.listen(something_Changed)