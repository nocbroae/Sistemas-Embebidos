#!/usr/bin/env python3
# practica1b_texto_fuentes.py
# Uso de fuentes TrueType

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)


# Cargar fuentes
try:

    font_small = ImageFont.truetype(
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        10
    )

    font_medium = ImageFont.truetype(
        '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        14
    )

    font_large = ImageFont.truetype(
        '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        20
    )

except IOError:

    # Fuente por defecto
    font_small = ImageFont.load_default()
    font_medium = ImageFont.load_default()
    font_large = ImageFont.load_default()


# Dibujar contenido
with canvas(device) as draw:

    draw.text(
        (2, 0),
        'Texto Grande',
        font=font_large,
        fill=255
    )

    draw.text(
        (2, 22),
        'Texto Mediano',
        font=font_medium,
        fill=255
    )

    draw.text(
        (2, 40),
        'Texto pequeno - 10pt',
        font=font_small,
        fill=255
    )

    draw.text(
        (2, 52),
        'Default bitmap',
        font=ImageFont.load_default(),
        fill=255
    )

    # Mostrar durante 10 segundos
    time.sleep(10)
