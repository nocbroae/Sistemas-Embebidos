from machine import I2C, Pin
import ssd1306
import time


# Inicialización I2C
i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

# Inicialización OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)


def mostrar_info():
    oled.fill(0)
    oled.text('Sistema OK', 16, 20, 1)
    oled.text('T: 24.5 C', 20, 36, 1)
    oled.show()


def alerta(mensaje, repeticiones=5):
    for _ in range(repeticiones):

        # Fondo blanco, texto negro
        oled.fill(1)
        oled.text('! ALERTA !', 16, 8, 0)
        oled.text(mensaje, 0, 28, 0)
        oled.show()
        time.sleep_ms(300)

        # Fondo negro, texto blanco
        oled.fill(0)
        oled.text('! ALERTA !', 16, 8, 1)
        oled.text(mensaje, 0, 28, 1)
        oled.show()
        time.sleep_ms(300)


# Secuencia de demostración
mostrar_info()
time.sleep(2)

alerta('TEMP ALTA!')

mostrar_info()
