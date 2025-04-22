import paho.mqtt.client as paho
import time
import logging
from os import environ
from files.sensor import *

# Настройка логирования
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Настройка переменных среды
broker = environ.get("SIM_HOST", "localhost")
port = int(environ.get("SIM_PORT", 1883))
name = environ.get("SIM_NAME", "sensor")
period = int(environ.get("SIM_PERIOD", 1))  # SIM_PERIOD используется как interval
type_sim = environ.get("SIM_TYPE", "temperature")

# Проверка допустимых типов датчиков
sensors = {
    "temperature": Temperature,
    "pressure": Pressure,
    "current": Current,
    "humidity": Humidity
}
if type_sim not in sensors:
    raise ValueError(f"Unknown sensor type: {type_sim}. Allowed types: {list(sensors.keys())}")

# Создание экземпляра датчика
sensor = sensors[type_sim](name=name, interval=period) 

# Callback для публикации
def on_publish(client, userdata, result):
    print(f"Data published successfully: {userdata}")

# Подключение к брокеру
client = paho.Client(sensor.name)
client.on_publish = on_publish
try:
    client.connect(broker, port)
except Exception as e:
    logging.error(f"Failed to connect to broker: {e}")
    exit(1)

# Публикация данных
while True:
    try:
        sensor.generate_new_value()
        topic = f"sensors/{sensor.type}/{sensor.name}"
        ret = client.publish("sensors/" + sensor.type + "/" + sensor.name, sensor.get_data())
    except Exception as e:
        logging.error(f"Error during publishing: {e}")
    time.sleep(period)