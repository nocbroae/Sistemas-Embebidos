import adafruit_dht
import board


class DHT11Sensor:
    def __init__(self, pin=board.D17):
        self.sensor = adafruit_dht.DHT11(pin)

    def read_data(self):
        try:
            temperature = self.sensor.temperature
            humidity = self.sensor.humidity

            if temperature is None or humidity is None:
                return None, None

            return temperature, humidity

        except RuntimeError as e:
            print(f"[WARN] Lectura fallida: {e}")
            return None, None

    def close(self):
        self.sensor.exit()
