#!/usr/bin/env python3
# practica2b_scroll_vertical.py

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()


lineas = [
    'Ingenieria en',
    'Sistemas Comput.',
    '--- TESOEM ---',
    'Sistemas Embebidos',
    'Aplicados a Moviles',
    'Alumno: Alan',
    'Grupo: 8S22',
    'Practica 2 - Scroll',
]

LINE_HEIGHT = 12

total_px = len(lineas) * LINE_HEIGHT

offset = 0

print('Scrolling vertical. Ctrl+C para salir.')


try:

    while True:

        with canvas(device) as draw:

            for i, linea in enumerate(lineas):

                y = i * LINE_HEIGHT - offset

                if -LINE_HEIGHT < y < device.height:

                    draw.text(
                        (2, y),
                        linea,
                        font=font,
                        fill=255
                    )

        offset += 1

        if offset >= total_px:
            offset = 0

        time.sleep(0.05)

except KeyboardInterrupt:

    device.cleanup()

    print('Programa finalizado.')
