#!/usr/bin/env python3
# practica3a_estilos_texto.py

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

from PIL import ImageFont

import time


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()


with canvas(device) as draw:

    # Texto normal
    draw.text(
        (2, 2),
        'Texto Normal',
        font=font,
        fill=255
    )

    # Texto invertido
    draw.rectangle(
        [(2, 16), (125, 30)],
        outline=255,
        fill=255
    )

    draw.text(
        (4, 18),
        'Texto Invertido',
        font=font,
        fill=0
    )

    # Texto con borde
    draw.rectangle(
        [(2, 34), (125, 48)],
        outline=255,
        fill=0
    )

    draw.text(
        (10, 36),
        'Texto con Borde',
        font=font,
        fill=255
    )

    # Texto con sombra
    draw.text(
        (3, 52),
        'Con Sombra!',
        font=font,
        fill=128
    )

    draw.text(
        (2, 51),
        'Con Sombra!',
        font=font,
        fill=255
    )

    time.sleep(5)


device.cleanup()
