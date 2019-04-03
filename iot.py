import json
import random
import datetime
import boto3
import time
import sys
import math

radius = 233                         #Choose your own radius
radiusInDegrees=radius/111300
r = radiusInDegrees
#x0 = 40.84
x0 = 19.0170
#y0 = -73.87
y0 = 72.8570
x = 0
y = 0

#deviceNames = ['SBS01', 'SBS02', 'SBS03', 'SBS04', 'SBS05']
iot = boto3.client('iot-data')


# generate Flow values
def getFlowValues():
    data = {}
    data['deviceParameter'] = 'GPS-Coordinates'
    data['deviceId'] = 'GPS' + str(random.randint(1, 1000))
    data['deviceValue'] = random.randint(1, 1000)
    #data['deviceId'] = random.choice(deviceNames)
    data['dateTime'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data['Latitude'] = getLatitude(x)
    data['Longitude'] = getLongitude(y)
    return data

def getLongitude(y):

    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    y = w * math.sin(t)
    yLong = y + y0
    return yLong

def getLatitude(x):

    u = float(random.uniform(0.0, 1.0))
    v = float(random.uniform(0.0, 1.0))
    w = r * math.sqrt(u)
    t = 2 * math.pi * v
    x = w * math.cos(t)
    xLat = x + x0
    return xLat

# Generate each parameter's data input in varying proportions
while True:
    time.sleep(1)
    rnd = random.random()
    if (0 <= rnd < 1):
        data = json.dumps(getFlowValues())
        print(data)
        response = iot.publish(
            topic='stpl_rat_poc_vts_data_topic',
            payload=data
        )


