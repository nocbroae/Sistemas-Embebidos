import adafruit_dht
import board


class DHT11Reader:
    def __init__(self, pin=board.D17):
        self.sensor = adafruit_dht.DHT11(pin)

    def read(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity

            if temperature is None or humidity is None:
                return None, None

            return temperature, humidity

        except RuntimeError:
            return None, None

    def close(self):
        self.sensor.exit()
