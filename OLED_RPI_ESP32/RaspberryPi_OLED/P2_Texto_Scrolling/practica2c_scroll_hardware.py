#!/usr/bin/env python3
# practica2c_scroll_hardware.py

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont
import time


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()


# Dibujar contenido
with canvas(device) as draw:

    draw.text(
        (10, 10),
        'TESOEM',
        font=font,
        fill=255
    )

    draw.text(
        (10, 25),
        'Scroll HW',
        font=font,
        fill=255
    )

    draw.text(
        (10, 40),
        'SSD1306 cmd',
        font=font,
        fill=255
    )


# Activar scroll hardware
device.serial.data([
    0x26,
    0x00,
    0x00,
    0x00,
    0x07,
    0x00,
    0xFF,
    0x2F,
])

print('Scroll hardware activo. Ctrl+C para detener.')


try:

    time.sleep(15)

except KeyboardInterrupt:

    pass


# Detener scroll
device.serial.data([0x2E])

device.cleanup()

print('Scroll hardware detenido.')
