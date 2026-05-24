from machine import I2C, Pin
import ssd1306


# Inicialización I2C
i2c = I2C(
    0,
    scl=Pin(22),
    sda=Pin(21),
    freq=400000
)

# Inicialización OLED
oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)

# Panel de título
oled.fill_rect(0, 0, 128, 14, 1)
oled.text('TESOEM ISC', 16, 3, 0)

# Separador
oled.line(0, 15, 127, 15, 1)

# Panel de datos
oled.text('CPU:', 0, 20, 1)
oled.text('78%', 40, 20, 1)

oled.text('RAM:', 0, 32, 1)
oled.text('45%', 40, 32, 1)

# Barra CPU
oled.rect(64, 20, 60, 8, 1)
oled.fill_rect(65, 21, int(58 * 0.78), 6, 1)

# Barra RAM
oled.rect(64, 32, 60, 8, 1)
oled.fill_rect(65, 33, int(58 * 0.45), 6, 1)

# Pie de página invertido
oled.fill_rect(0, 52, 128, 12, 1)
oled.text('v1.0 Activo', 12, 54, 0)

oled.show()
