from PIL import Image
import os


INPUT_IMAGE = "logo.png"
OUTPUT_DIR = "assets"
OUTPUT_IMAGE = "logo.pbm"


def convertir_logo():
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    img = Image.open(INPUT_IMAGE).convert("1")
    img = img.resize((128, 64))

    output_path = os.path.join(OUTPUT_DIR, OUTPUT_IMAGE)
    img.save(output_path)

    print(f"Logo convertido correctamente: {output_path}")


if __name__ == "__main__":
    convertir_logo()
