from sensor import DHT11Sensor
from display import LCDDisplay
from utils import delay


def main():
    sensor = DHT11Sensor()
    lcd = LCDDisplay(address=0x27)

    try:
        while True:
            temp, hum = sensor.read_data()

            if temp is not None and hum is not None:
                lcd.show_message(f"Temp: {temp:.1f}C", f"Hum: {hum:.1f}%")
                print(f"Temp: {temp:.1f}°C  Hum: {hum:.1f}%")
            else:
                lcd.show_message("Sensor", "sin lectura")
                print("Error al leer el sensor.")

            delay(2)

    except KeyboardInterrupt:
        print("\nPrograma detenido por el usuario.")
        lcd.clear()

    finally:
        sensor.close()


if __name__ == "__main__":
    main()
