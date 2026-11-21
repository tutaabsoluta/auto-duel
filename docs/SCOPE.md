# PocketBot — Scope (Fase 0)

## Juego
- Pokémon TCG Pocket, ejecutado en BlueStacks 5 (Android).

## Modo
- **Dentro del scope:** duelos contra la IA del juego (modo solo).
- **Fuera del scope:** PvP contra jugadores reales.
- **Fuera del scope:** evadir la detección de bots o del anti-cheat, y modificar el cliente.

## Cuenta y riesgo
- Se usa una cuenta terciaria, separada de la principal.
- Automatizar probablemente viola los Términos de Uso del juego. El dueño del proyecto acepta el riesgo de ban para esa cuenta.
- Pendiente: leer los Términos de Uso dentro del juego (Menú → Otros → Términos de Uso) y anotar aquí las cláusulas relevantes.

## Emulador
- Resolución de BlueStacks: 1280×720, a 240 DPI.
- Lo que manda es lo que devuelve `adb exec-out screencap`, no el tamaño de la ventana en el escritorio. Se verifica en la Fase 1.
- Esta configuración no se cambia una vez que haya plantillas de imagen (Fase 3).

## Enfoque técnico
- Automatización determinista: ADB + OpenCV + OCR local, sin APIs de pago.
- El motor de estrategia es independiente de BlueStacks y de ADB.
- Gran parte del desarrollo se hace sobre capturas guardadas (`FakeDevice`), no en vivo.
