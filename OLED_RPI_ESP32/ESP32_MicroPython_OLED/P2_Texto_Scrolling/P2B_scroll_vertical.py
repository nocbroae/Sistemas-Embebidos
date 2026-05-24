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

# Lista de datos simulados
noticias = [
    'Temp: 23 C',
    'Humedad: 65%',
    'Presion: 1013mb',
    'Velocidad: 12km/h',
    'Calidad aire: Buena',
    'UV Index: 3',
]

# Altura total del contenido
ALTURA_TOTAL = len(noticias) * 10 + 64

while True:
    for offset in range(ALTURA_TOTAL):

        oled.fill(0)

        for i, texto in enumerate(noticias):

            # Empieza abajo y sube
            y = i * 10 - offset + 64

            # Solo dibujar si está visible
            if -8 < y < 64:
                oled.text(texto, 2, y, 1)

        oled.show()

        time.sleep_ms(50)
