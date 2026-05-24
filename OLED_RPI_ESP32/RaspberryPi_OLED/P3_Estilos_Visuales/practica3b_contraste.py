#!/usr/bin/env python3
# practica3b_contraste.py

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas

from PIL import ImageFont

import time


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()

print('Demostracion de contraste.')


# Ciclo de contraste
for _ in range(2):

    # Aumentar contraste
    for nivel in range(0, 256, 16):

        device.contrast(nivel)

        with canvas(device) as draw:

            draw.text(
                (5, 2),
                f'Contraste: {nivel}',
                font=font,
                fill=255
            )

            draw.rectangle(
                [(5, 14), (120, 25)],
                outline=255
            )

            barra = 5 + int(nivel / 2)

            draw.rectangle(
                [(5, 14), (barra, 25)],
                outline=255,
                fill=255
            )

            draw.text(
                (5, 35),
                'Min ---- Max',
                font=font,
                fill=255
            )

        time.sleep(0.1)

    # Disminuir contraste
    for nivel in range(255, -1, -16):

        device.contrast(nivel)

        time.sleep(0.05)


# Restaurar contraste medio
device.contrast(128)

device.cleanup()
