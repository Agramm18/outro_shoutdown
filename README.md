# Windows Shutdown Outro

A small Python script that plays an outro song when shutting down the system and shows a countdown before killing important processes.

## Features

* Plays the Outro song from the Outro trend and shutdowns your PC Automaticly by the drop.
* Automatically starts a Windows shutdown timer (60 seconds).
* Displays a countdown with messages in the terminal.
* Force-closes selected processes (`code.exe`, `powershell.exe`, `explorer.exe`, `cmd.exe`).

## Requirements

* **Python 3.8+**
* **pygame** library

Install dependencies:

```bash
pip install pygame
```

## Usage

1. Update the path in the script:

   ```python
   song_path = os.path.join("path", "to", "outro_song.mp3")
   ```
2. Run the script from the terminal:

   ```bash
   python shutdown_outro.py
   ```
3. Type `quit` to start the sequence.

## How It Works

* After typing `quit`, the music will start playing.
* A Windows shutdown command with a 60-second timer is executed.
* The script shows status messages and a countdown in the terminal.
* At the end, defined programs are force-killed.

## Important ⚠️

* This script **only works on Windows** (uses `shutdown` and `taskkill`).
* Be careful: processes are **forcefully terminated** – make sure you save your work first!

---

Do you want me to also add a section about **building a standalone `.exe`** (with `pyinstaller`) so you don’t need Python installed?
