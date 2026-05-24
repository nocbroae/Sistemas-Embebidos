import csv
import os
from datetime import datetime


def save_data(temperature, humidity, filename="data.csv"):
    file_exists = os.path.exists(filename)

    with open(filename, mode="a", newline="") as file:
        writer = csv.writer(file)

        if not file_exists:
            writer.writerow(["fecha_hora", "temperatura", "humedad"])

        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            temperature,
            humidity
        ])
