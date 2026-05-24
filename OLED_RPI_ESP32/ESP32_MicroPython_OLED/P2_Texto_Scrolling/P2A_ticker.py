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

# Mensaje a desplazar
mensaje = ' >>> TESOEM - Sistemas Embebidos - ISC 2025 <<< '

# Posición inicial fuera de pantalla
pos_x = 128

while True:
    oled.fill(0)

    oled.text(mensaje, pos_x, 28, 1)

    oled.show()

    # Velocidad del desplazamiento
    pos_x -= 3

    # Reiniciar cuando el texto salga completamente
    if pos_x < -(len(mensaje) * 8):
        pos_x = 128

    time.sleep_ms(40)
