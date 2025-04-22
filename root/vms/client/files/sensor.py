import random
import math
import time


class Sensor:
    value: float
    name: str
    type: str

    def __init__(self, name, interval):
        self.name = name
        self.interval = interval  
        self.value = None

    def generate_new_value(self):
        pass

    def get_data(self):
        return self.value

    def run(self):
        """Запускает цикл генерации данных с заданным интервалом."""
        while True:
            self.generate_new_value()
            print(f"Sensor {self.name} ({self.type}): {self.value}")
            time.sleep(self.interval)


class Temperature(Sensor):
    step = 10

    def __init__(self, name, interval):
        super().__init__(name, interval)
        self.type = "temperature"

    def generate_new_value(self):
        """Генерирует новое значение температуры."""
        self.value = random.random() + self.step + 222 * 6


class Pressure(Sensor):
    step = 15

    def __init__(self, name, interval):
        super().__init__(name, interval)
        self.type = "pressure"

    def generate_new_value(self):
        """Генерирует новое значение давления."""
        self.value = random.random() + self.step 


class Current(Sensor):
    step = 20

    def __init__(self, name, interval):
        super().__init__(name, interval)
        self.type = "current"

    def generate_new_value(self):
        """Генерирует новое значение тока."""
        import math
        self.value = math.sin(self.step)
        self.step += 1


class Humidity(Sensor):
    step = 25

    def __init__(self, name, interval):
        super().__init__(name, interval)
        self.type = "humidity"

    def generate_new_value(self):
        """Генерирует новое значение влажности."""
        self.value = random.uniform(self.step, self.step + 20)

