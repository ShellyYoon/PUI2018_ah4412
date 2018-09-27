# Python file to import bus data from MTA and output stop information

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

# set arguments to be entered into url
apikey = sys.argv[1]
busline = sys.argv[2]
csv_name = sys.argv[3]

# set url to retrieve data
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s"%(apikey, busline)

# retrieve data and save as dictionary
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)

# save some names to shorten later commands
VA = dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
#OC = VA[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]
#LAT = VA[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
#LONG = VA[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
#STNAME = OC['StopPointName']
#STATUS = OC['Extensions']['Distances']['PresentableDistance']


# open csv to write
fout = open(csv_name, "w")
    
# write selected data to csv
for i, value in enumerate(VA):
    thisline = "%s,%s,%s,%s" %(VA[i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'],VA[i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'],VA[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['StopPointName'],VA[i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][0]['Extensions']['Distances']['PresentableDistance'])
    fout.write(thisline.strip(',')+"\n")




