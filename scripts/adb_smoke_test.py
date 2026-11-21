import subprocess
from pathlib import Path

# Serial del dispositivo: el mismo que usabas con "adb -s"
DEVICE = "127.0.0.1:5555"


def adb(*args: str) -> bytes:
    """Ejecuta un comando adb contra nuestro dispositivo y devuelve su salida en bytes."""
    result = subprocess.run(
        ["adb", "-s", DEVICE, *args],
        capture_output=True,
        check=True,
    )
    return result.stdout


def main() -> None:
    # 1. Captura de pantalla: los bytes del PNG llegan directo por stdout
    png_bytes = adb("exec-out", "screencap", "-p")

    output = Path("samples/from_python.png")
    output.parent.mkdir(exist_ok=True)
    output.write_bytes(png_bytes)
    print(f"Captura guardada en {output} ({len(png_bytes)} bytes)")

    # 2. Tap en el botón Misiones
    adb("shell", "input", "tap", "640", "1135")
    print("Tap enviado en (640, 1135)")


if __name__ == "__main__":
    main()