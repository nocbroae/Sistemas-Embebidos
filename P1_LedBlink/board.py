#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

LED_PIN = 12  # Pin físico 12

try:
    # Configuración
    GPIO.setmode(GPIO.BOARD)
    GPIO.setwarnings(False)
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

    print("Control de LED iniciado (Modo BOARD)")
    print(f"Usando Pin físico {LED_PIN}")
    print("Presiona Ctrl+C para salir")

    contador = 0

    # Loop con ciclos
    while contador < 10:
        for _ in range(3):
            GPIO.output(LED_PIN, GPIO.HIGH)
            time.sleep(0.2)
            GPIO.output(LED_PIN, GPIO.LOW)
            time.sleep(0.2)

        time.sleep(1)
        contador += 1
        print(f"Ciclo {contador}/10 completado")

except KeyboardInterrupt:
    print("\nPrograma interrumpido")

finally:
    GPIO.cleanup()
    print("Sistema apagado correctamente")
