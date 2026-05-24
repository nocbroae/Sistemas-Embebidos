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

# Dirección I2C del OLED
ADDR = 0x3C


def cmd(c):
    i2c.writeto(ADDR, bytes([0x00, c]))


# Mostrar contenido inicial
oled.fill(0)
oled.text('SCROLL HW', 16, 28, 1)
oled.show()

time.sleep(1)

# Activar scroll horizontal hacia la derecha
cmd(0x26)   # Scroll horizontal derecha
cmd(0x00)   # Byte dummy
cmd(0x00)   # Página inicial
cmd(0x00)   # Intervalo
cmd(0x07)   # Página final
cmd(0x00)   # Byte dummy
cmd(0xFF)   # Byte dummy
cmd(0x2F)   # Activar scroll

time.sleep(5)

# Detener scroll
cmd(0x2E)

oled.fill(0)
oled.text('Scroll OFF', 12, 28, 1)
oled.show()
