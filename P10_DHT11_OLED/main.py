import time
from sensors.dht11_reader import DHT11Reader
from display.oled_display import OLEDDisplay
from utils.data_logger import save_data


def main():
    sensor = DHT11Reader()
    display = OLEDDisplay()

    try:
        while True:
            temperature, humidity = sensor.read()

            if temperature is not None and humidity is not None:
                display.update(temperature, humidity)
                save_data(temperature, humidity)

                print(f"Temp: {temperature:.1f}°C  Hum: {humidity:.1f}%")
            else:
                display.show_error()
                print("Error al leer el sensor.")

            time.sleep(2)

    except KeyboardInterrupt:
        display.clear()
        sensor.close()
        print("\nPrograma finalizado.")


if __name__ == "__main__":
    main()
