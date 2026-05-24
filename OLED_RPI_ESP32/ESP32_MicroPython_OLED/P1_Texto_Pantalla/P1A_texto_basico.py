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

# Limpiar pantalla
oled.fill(0)

# Título
oled.text('TESOEM', 36, 0, 1)

# Línea separadora
oled.line(0, 10, 127, 10, 1)

# Información
oled.text('Materia:', 0, 16, 1)
oled.text('Embebidos', 0, 26, 1)

oled.text('Alumno:', 0, 38, 1)
oled.text('Alan Fdz', 0, 48, 1)

# Actualizar pantalla
oled.show()
