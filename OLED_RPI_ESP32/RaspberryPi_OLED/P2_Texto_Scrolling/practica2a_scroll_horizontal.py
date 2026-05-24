#!/usr/bin/env python3
# practica2a_scroll_horizontal.py

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()

mensaje = ' >>> TESOEM - Sistemas Embebidos 2025 <<< '

# Aproximación de ancho
ancho_texto = len(mensaje) * 6

print('Scrolling horizontal. Ctrl+C para salir.')

pos_x = device.width


try:

    while True:

        with canvas(device) as draw:

            draw.text(
                (pos_x, 28),
                mensaje,
                font=font,
                fill=255
            )

        pos_x -= 3

        if pos_x < -ancho_texto:
            pos_x = device.width

        time.sleep(0.03)

except KeyboardInterrupt:

    device.cleanup()

    print('Programa finalizado.')
