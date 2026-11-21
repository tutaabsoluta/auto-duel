# PocketBot — Roadmap y checklist

## Fases
- [x] **Fase 0** – Definición y reglas → ver [SCOPE.md](SCOPE.md)
- [x] **Fase 1** – Entorno + ADB (captura y tap desde Python)
- [ ] **Fase 2** – Device Adapter (`Device` / `FakeDevice`)
- [ ] **Fase 3** – Visión básica (template matching)
- [ ] **Fase 4** – Reconocimiento de pantallas (máquina de estados)
- [ ] **Fase 5** – Lectura del estado de la partida (`GameState`, OCR)
- [ ] **Fase 6** – Motor de estrategia (Python puro, con tests)
- [ ] **Fase 7** – Ejecutor de acciones (`Action` → taps + verificación)
- [ ] **Fase 8** – Orquestador + robustez
- [ ] **Fase 9** – Herramientas y observabilidad
- [ ] **Fase 10** – Mejoras opcionales

## Pendientes
- Copiar a SCOPE.md las cláusulas relevantes de los Términos de Uso del juego.

## Known issues
- BlueStacks expone dos seriales (`127.0.0.1:5555` y `emulator-5554`): siempre hay que usar `-s`.
- Si ADB responde `error: closed`, el interruptor de ADB en BlueStacks está apagado.
- En PowerShell 5.1, `adb exec-out ... > archivo` corrompe los datos binarios. Hay que leer los bytes desde Python.

## Decisiones de arquitectura
| Decisión | Elección | Motivo |
|---|---|---|
| Lenguaje | Python + venv | Ecosistema de visión; venv viene con Python |
| Control | ADB | Independiente de la ventana de Windows y determinista |
| Coordenadas | 720×1280 vertical | Es lo que devuelve `screencap` |
| Primer acceso a ADB | `subprocess` sin dependencias | Es transparente y fácil de entender; se puede revisar en la Fase 2 |
| Scope | Solo contra la IA, sin PvP | Ver SCOPE.md |
