import random
import time
from azure.iot.device import IoTHubDeviceClient, Message

CONNECTION_STRING = "HostName=DataHub.azure-devices.net;DeviceId=virtualSensor;SharedAccessKey=2eZEOJyZhtZO7TzndUoPKlnnggp2rxrl246DK+Y4MAw="

client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

def send_data():
    # generate random values
    temperature = random.uniform(15.0, 30.0)
    humidity = random.uniform(30.0, 70.0)

    # Сcreate message
    data = {
        "temperature": temperature,
        "humidity": humidity
    }
    message = Message(str(data))

     # send data
    client.send_message(message)
    print(f"Message was sent: Temperature = {temperature:.2f} °C, Humidity = {humidity:.2f}%")


# send every 15 sec
try:
    while True:
        send_data()
        time.sleep(15)
except KeyboardInterrupt:
    print("Завершение отправки данных")
finally:
    client.shutdown()