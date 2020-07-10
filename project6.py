import time
import sys
import ibmiotf.application
import ibmiotf.device
import random
#Provide your IBM Watson Device Credentials
organization = "v1eeqi"
deviceType = "DHT11"
deviceId = "123456"
authMethod = "token"
authToken = "123456789"


def myCommandCallback(cmd):
        print("Command received: %s" % cmd.data)#Commands
        print(type(cmd.data))
        i==cmd.data['command']
        if i=='switchon':
            print("switch is on")
        elif i=='switchoff':
            print("switch is off")
        

try:
	deviceOptions = {"org": organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token": authToken}
	deviceCli = ibmiotf.device.Client(deviceOptions)
	#..............................................
	
except Exception as e:
	print("Caught exception connecting device: %s" % str(e))
	sys.exit()

# Connect and send a datapoint "hello" with value "world" into the cloud as an event of type "greeting" 10 times
deviceCli.connect()

while True:
        
        hum=random.randint(10, 40)
        #print(hum)
        temp =random.randint(30, 80)
        #Send Temperature,Humidity,vibration,current value to IBM Watson
        vib = random.randint(50,100)

        curr = random.randint(5,30)
        data = { 'Temperature' : temp, 'Humidity': hum ,'Vibration':vib , 'Current':curr }
        #print (data)
        def myOnPublishCallback():
            print ("Published Temperature = %s C" % temp, "Humidity = %s %%" % hum,"Vibration= %s HZ" % vib ,"Current = %s AMP" % curr, "to IBM Watson")

        success = deviceCli.publishEvent("DHT11", "json", data, qos=0, on_publish=myOnPublishCallback)
        if not success:
            print("Not connected to IoTF")
        time.sleep(2)
        
        deviceCli.commandCallback = myCommandCallback

# Disconnect the device and application from the cloud
deviceCli.disconnect()
