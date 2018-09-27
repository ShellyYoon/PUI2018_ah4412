# Python file to import bus data from MTA and output specific information about a bus line

# keep compatibility between python2 and python3
from __future__ import print_function

# import necessary modules
import os
import json
import sys
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib

# set variables to be entered into url
apikey = sys.argv[1]
busline = sys.argv[2]

# set url to retrieve data
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, busline)

# print url
print(url)

# retrieve data and save as dictionary
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

# save some names to shorten later commands
VMD = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery']
pub_bl = VMD[0]['VehicleActivity'][0]['MonitoredVehicleJourney']['PublishedLineName']


# print bus line number
print("Bus Line: ", pub_bl)

# print number of active vehicles
print("Number of Active Buses: ", len(VMD))

# run for loop to print each vehicle's location
for i in range(len(VMD)):
    print("Bus ", i, "is at latitude ", VMD[i]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'], " and longitude ", VMD[i]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])
             
             
             
