import random
import time
import json
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=DataHub.azure-devices.net;DeviceId=virtualSensor;SharedAccessKey=2eZEOJyZhtZO7TzndUoPKlnnggp2rxrl246DK+Y4MAw="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_data():
    # generate random values
    temperature = random.uniform(15.0, 30.0)
    humidity = random.uniform(30.0, 70.0)

    # Сreate message
    data = {
        "temperature": temperature,
        "humidity": humidity
    }
    message = Message(json.dumps(data))

     # send data
    client.send_message(message)
    print(f"Message sent: {data}")


# send every 15 sec
try:
    while True:
        send_data()
        time.sleep(15)
except KeyboardInterrupt:
    print("Close")
finally:
    client.shutdown()