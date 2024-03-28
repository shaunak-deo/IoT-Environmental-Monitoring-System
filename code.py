import paho.mqtt.publish as publish
import random
import time
import datetime

# ThingSpeak Channel ID.
MQTT_CHANNEL_ID = ""

# Hostname of ThingSpeak MQTT broker.
MQTT_HOST = "mqtt3.thingspeak.com"

# MQTT credentials for the device
MQTT_CLIENT_ID = ""
MQTT_USERNAME  = ""
MQTT_PASSWORD  = ""

TRANSPORT = "websockets"
PORT = 80

# Create the TOPIC string.
TOPIC = "channels/" + MQTT_CHANNEL_ID + "/publish"

class EnvironmentalStation:
    def __init__(self):
        self.temperature_range = (-50, 50)
        self.humidity_range = (0, 100)
        self.co2_range = (300, 2000)

    def generate_sensor_data(self):
        """Generate random sensor values for temperature, humidity, and CO2."""
        temperature = random.uniform(*self.temperature_range)
        humidity = random.uniform(*self.humidity_range)
        co2 = random.uniform(*self.co2_range)
        return temperature, humidity, co2

def publish_sensor_data():
    station = EnvironmentalStation()

    while True:
        temperature, humidity, co2 = station.generate_sensor_data()

        # Build the payload string.
        payload = f'field1={temperature}&field2={humidity}&field3={co2}'

        # Log the payload and MQTT details.
        print(f'{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")} Writing Payload= {payload} to host= {MQTT_HOST} clientID= {MQTT_CLIENT_ID}')

        # Attempt to publish the sensor data.
        publish.single(TOPIC, payload, hostname=MQTT_HOST, transport=TRANSPORT, port=PORT, client_id=MQTT_CLIENT_ID, auth={'username':MQTT_USERNAME,'password':MQTT_PASSWORD})

        time.sleep(5)

if __name__ == '__main__':
    publish_sensor_data()
