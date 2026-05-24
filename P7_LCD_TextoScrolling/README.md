# P7 - LCD Texto Scrolling

Repositorio de práctica para utilizar una pantalla LCD 16x2 con interfaz I2C en Raspberry Pi, mostrando texto desplazable mediante Python.

## 🎯 Objetivo

Configurar y utilizar una pantalla LCD 16x2 con interfaz I2C en Raspberry Pi para mostrar texto desplazable, aplicando programación modular y buenas prácticas de desarrollo.

## 🧠 Competencias Desarrolladas

- Uso de pantalla LCD 16x2 con Raspberry Pi
- Comunicación mediante protocolo I2C
- Programación modular en Python
- Control de texto dinámico
- Manejo básico de periféricos externos

## 🧰 Materiales Requeridos

| Cantidad | Componente |
|----------|------------|
| 1 | Raspberry Pi |
| 1 | Pantalla LCD 16x2 con módulo I2C |
| 4 | Cables Dupont |
| 1 | Protoboard opcional |
| 1 | Fuente de alimentación para Raspberry Pi |

## 🔌 Diagrama de Conexión

| LCD I2C | Raspberry Pi |
|--------|--------------|
| GND | Pin físico 6 - GND |
| VCC | Pin físico 2 - 5V |
| SDA | Pin físico 3 - GPIO2 |
| SCL | Pin físico 5 - GPIO3 |

## ⚙️ Configuración del Entorno

Actualizar sistema:

```bash
sudo apt update
```

Instalar dependencias:

```bash
sudo apt install python3-pip -y
```

Instalar librerías necesarias:

```bash
pip3 install RPLCD
pip3 install smbus2
```

Instalar herramientas I2C:

```bash
sudo apt install i2c-tools -y
```

Verificar dirección I2C:

```bash
i2cdetect -y 1
```

Direcciones comunes:

```txt
0x27
0x3f
```

## 📁 Estructura del Proyecto

```txt
P7_LCD_TextoScrolling/
├── README.md
├── main.py
├── lcd_utils.py
└── requirements.txt
```

## ▶️ Ejecución

Ejecutar desde terminal:

```bash
python3 main.py
```

## 📊 Resultado Esperado

La pantalla LCD mostrará un mensaje inicial en la primera línea y un texto desplazable en la segunda línea.

```txt
LCD Inicializado
Texto scrolling
```

## 🧪 Actividades Realizadas

- Mostrar texto fijo en la primera línea
- Implementar texto desplazable en la segunda línea
- Ajustar la velocidad de desplazamiento
- Modularizar el control del LCD

## ✅ Buenas Prácticas Aplicadas

- ✔️ Código modular
- ✔️ Separación de responsabilidades
- ✔️ Reutilización mediante clases
- ✔️ Manejo de errores
- ✔️ Código limpio y legible

 <img width="875" height="407" alt="1e6b2479-5b98-4442-bb28-e7fa729a8f56" src="https://github.com/user-attachments/assets/83a9164e-9ad7-423e-9904-69e7ec7ce49a" />


## 👨‍💻 Autor

Alan Fernández  
Materia: Sistemas Embebidos
