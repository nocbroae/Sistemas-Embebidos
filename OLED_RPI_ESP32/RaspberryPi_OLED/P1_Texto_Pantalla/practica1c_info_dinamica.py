#!/usr/bin/env python3
# practica1c_info_dinamica.py
# Información dinámica del sistema

from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from luma.core.render import canvas
from PIL import ImageFont

import time
import datetime
import subprocess


# Inicialización
serial = i2c(port=1, address=0x3C)
device = ssd1306(serial)

font = ImageFont.load_default()


def get_cpu_temp():
    """
    Obtiene temperatura del CPU
    """

    result = subprocess.run(
        ['vcgencmd', 'measure_temp'],
        capture_output=True,
        text=True
    )

    return result.stdout.strip().replace('temp=', '')


def get_ip_address():
    """
    Obtiene dirección IP
    """

    result = subprocess.run(
        ['hostname', '-I'],
        capture_output=True,
        text=True
    )

    return result.stdout.split()[0] if result.stdout else 'N/A'


print('Mostrando informacion del sistema...')


try:

    while True:

        now = datetime.datetime.now().strftime('%H:%M:%S')

        temp = get_cpu_temp()

        ip = get_ip_address()

        with canvas(device) as draw:

            draw.text(
                (0, 0),
                'Raspberry Pi 3',
                font=font,
                fill=255
            )

            draw.line(
                [(0, 10), (127, 10)],
                fill=255
            )

            draw.text(
                (0, 14),
                f'Hora: {now}',
                font=font,
                fill=255
            )

            draw.text(
                (0, 26),
                f'Temp: {temp}',
                font=font,
                fill=255
            )

            draw.text(
                (0, 38),
                f'IP: {ip}',
                font=font,
                fill=255
            )

            draw.text(
                (0, 50),
                'TESOEM - 2025',
                font=font,
                fill=255
            )

        time.sleep(1)

except KeyboardInterrupt:

    device.cleanup()

    print('Display apagado correctamente.')
