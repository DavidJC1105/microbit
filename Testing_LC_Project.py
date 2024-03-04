import time
import matplotlib
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from datetime import datetime

waste = 0
counter = 0
percent = 0
percentage = 0

cred = credentials.Certificate("C:/Users/David Cummins/Downloads/lc-project-457ba-firebase-adminsdk-fwptw-6720404649.json")
firebase_admin.initialize_app(cred,{'databaseURL': 'https://lc-project-457ba-default-rtdb.europe-west1.firebasedatabase.app/'})
ref = db.reference()
#ref.update({'study_time':''})
ref = db.reference().child('study_time')
#source = input("Please input the study location: ")
data = ref.order_by_child('Location').get()
#print (type(data))
wasteminutes = []
totaltime = []
location = []
times = []
count = 0
"""
for timestamp, session_data in data.items():
    timestamp = int(timestamp)
    formatted_timestamp = datetime.fromtimestamp(timestamp).strftime('%H:%M:%S %d-%m-%Y')
    print("At this time and date, this was the data for your study session: ", formatted_timestamp)
    
    for key, value in session_data.items():
        print(key, "is:", value)
    
    print("\n")
"""

for key,value in data.items():
    if value['Location'] not in location:
        location.append(value['Location'])
for i in range(len(location)):
    times.append(0)
    wasteminutes.append(0)
    totaltime.append(0)
for k,v in data.items():
    times.append(k)
for key,value in data.items():
    if value['Location'] == location[count]:
        wasteminutes[count]+=value['Wasted_Time(minutes)']
        totaltime[count]+=value['study_time(minutes)']
    else:
        count = count + 1
        wasteminutes[count]+=value['Wasted_Time(minutes)']
        totaltime[count]+=(value['study_time(minutes)']-value['Wasted_Time(minutes)'])
    #print(value['Location'])
    #wasteminutes.append(value['Wasted_Time(minutes)'])
    #totaltime.append(value['study_time(minutes)'])
   
#print(location)
#print(wasteminutes)
dl =0
times[dl:len(wasteminutes)] = []
#print(times)
#print(totaltime)
lowest_value = wasteminutes[0]

for num in wasteminutes:
    # If the current number is lower than the lowest_value, update lowest_value
    if num < lowest_value:
        lowest_value = num
        
#print(lowest_value)       
totalwaste = []
for key, value in data.items():
    wastedtime = value.get('Wasted_Time(minutes)')
    if wastedtime is not None:
        totalwaste.append(wastedtime)

#print(totalwaste)       
totalminutes = []
for key, value in data.items():
    totaltimes = value.get('study_time(minutes)')
    if totaltimes is not None:
        totalminutes.append(totaltimes)     

#print(totalminutes)


def find_lowest_time_and_waste(totalwaste, times):
    min_total_waste = min(totalwaste)  # Find the minimum total waste
    lowest_times = []  # Initialize a list to store all times with the lowest total waste

    # Iterate through the totalwaste list
    for index, waste in enumerate(totalwaste):
        if waste == min_total_waste:  # If the current total waste is equal to the minimum
            lowest_times.append(times[index])  # Add the corresponding time to the list

    # Return the list of times and the minimum total waste
    return lowest_times, min_total_waste


lowest_times, lowest_total_waste = find_lowest_time_and_waste(totalwaste, times)

def find_highest_time_and_waste(totalwaste, times):
    max_total_waste = max(totalwaste)  # Find the minimum total waste
    highest_times = []  # Initialize a list to store all times with the lowest total waste

    # Iterate through the totalwaste list
    for index, waste in enumerate(totalwaste):
        if waste == max_total_waste:  # If the current total waste is equal to the minimum
            highest_times.append(times[index])  # Add the corresponding time to the list

    # Return the list of times and the minimum total waste
    return highest_times, max_total_waste


highest_times, max_total_waste = find_highest_time_and_waste(totalwaste, times)

total_minutes_list = []

# Iterate over the times list and fetch corresponding total minutes values
for timestamp in times_list:
    # Query Firebase to get the corresponding total minutes value
    total_minutes = ref.child('your_data_node').child(str(int(timestamp))).get()
    
    # Append the total minutes value to the list
    total_minutes_list.append(total_minutes)

# Print the list of total minutes values
print("Total minutes values corresponding to the timestamps:", total_minutes_list)

#print(lowest_total_waste)
mintimes = []
for timestamp in lowest_times:
    timestamp_value = float(timestamp)  # Convert timestamp to float
    study_time = data[timestamp]['study_time(minutes)']  # Fetch corresponding study time
    #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_value))  # Format timestamp
    mintimes.append(study_time)
    #print("At", timestamp, "the study time was", study_time, "minutes.")

Location_interpret = []
for spot in lowest_times:
    spot_value = float(spot)  # Convert timestamp to float
    study_spot = data[spot]['Location']  # Fetch corresponding study time
    #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_value))  # Format timestamp
    Location_interpret.append(study_spot)
    #print("At", timestamp, "the study time was", study_time, "minutes.")
    
maxtimes = []
for timestamp in highest_times:
    timestamp_value = float(timestamp)  # Convert timestamp to float
    study_time = data[timestamp]['study_time(minutes)']  # Fetch corresponding study time
    #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_value))  # Format timestamp
    maxtimes.append(study_time)
    #print("At", timestamp, "the study time was", study_time, "minutes.")

Location_interpret_max = []
for spot in highest_times:
    spot_value = float(spot)  # Convert timestamp to float
    study_spot = data[spot]['Location']  # Fetch corresponding study time
    #formatted_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp_value))  # Format timestamp
    Location_interpret_max.append(study_spot)
    #print("At", timestamp, "the study time was", study_time, "minutes.")
#
#print(Location_interpret)
#print(type(lowest_times))
#print("The time(s) with the lowest total waste is:", lowest_times)
#print("The corresponding total waste is:", lowest_total_waste)
ind = 0
starttime = []
for start in mintimes:
    start = int(mintimes[ind])
    starttime.append(start*60)
    ind = ind+1
    if ind == len(mintimes):
        break
#print (starttime)

ind_max=0
starttime_max = []
for start in maxtimes:
    start = int(maxtimes[ind_max])
    starttime_max.append(start*60)
    ind_max = ind_max+1
    if ind == len(maxtimes):
        break
#print (starttime)

formatted_times = []  # Initialize a list to collect formatted times

starting = 0
for eachtime in lowest_times:
    eachtime = int(eachtime) - starttime[starting]  # Assuming starttime is another list
    formatted_time = datetime.fromtimestamp(eachtime).strftime('%H:%M:%S')
    formatted_times.append(formatted_time)  # Collect formatted time in the list
    starting += 1

formatted_times_max = []  # Initialize a list to collect formatted times

starting_max = 0
for eachtime in highest_times:
    eachtime = int(eachtime) - starttime_max[starting_max]  # Assuming starttime is another list
    formatted_time_max = datetime.fromtimestamp(eachtime).strftime('%H:%M:%S')
    formatted_times_max.append(formatted_time_max)  # Collect formatted time in the list
    starting_max += 1

# Print the collected formatted times
print("You started your best study sessions at these times and in these locations:")
time_place = 0
inde = 0
while time_place != len(formatted_times):
    print(formatted_times[inde],' in ',Location_interpret[inde],'and you only wasted ',lowest_total_waste,'minute(s)')
    inde = inde+1
    time_place = time_place+1

print('I recommend you study in any of these locations at these time where possible for optimal results')
print('\n')
print("You started your worst study sessions at these times and in these locations:")
time_place_max = 0
inde_max = 0
while time_place_max != len(formatted_times_max):
    print(formatted_times_max[inde_max],' in ',Location_interpret_max[inde_max],'and you wasted ',max_total_waste,'minute(s)')
    inde_max = inde_max+1
    time_place_max = time_place_max+1

print('I recommend you avoid studying in any of these locations at these time where possible for optimal results')

'''
import matplotlib.pyplot as plt
import numpy as np

# data from https://allisonhorst.github.io/palmerpenguins/

study_space = location
amountoftime = {
    "The amount of wasted time": wasteminutes,
    "Total time spent studying": totaltime,
}
width = 0.5

fig, ax = plt.subplots()
bottom = np.zeros(len(location))

for boolean, amountoftime in amountoftime.items():
    p = ax.bar(study_space, amountoftime, width, label=boolean, bottom=bottom)
    bottom += amountoftime

ax.set_title("The ratio of wasted time in regards to total time in minutes spent studying")
ax.legend(loc="upper right")

plt.show()
'''