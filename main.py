from PIL import Image
import imagehash
import os
import tkinter as tk
from tkinter import filedialog, ttk


class InputWindow:
    def __init__(self, window):
        # Initialisieren von GUI-Komponenten
        self.window = window
        self.window.title("Duplikatserkennung")

        # Ordner auswählen
        self.description = ttk.Label(
            window, text="Bitte wähle den Ordner mit den zu prüfenden Bildern:"
        )
        self.description.pack(pady=10)

        # Ordner öffenen (Knopf)
        self.selectPath = ttk.Button(
            window, text="Ordner auswählen", command=self.select_folder
        )
        self.selectPath.pack(pady=10)

        self.selectPathDescription = ttk.Label(window, text="")
        self.selectPathDescription.pack(pady=10)

        # Bestätigung Ordner (Knopf)
        self.safePath = ttk.Button(
            window, text="Ordner übernehmen", command=self.adopt_folder
        )
        self.safePath.pack(pady=10)

        # Variable zum speichern des ausgewählten Pfades
        self.selectFilePath = None

    def select_folder(self):
        file_path = filedialog.askdirectory()
        if file_path:
            self.selectPathDescription.config(text=file_path)
            self.selectFilePath = file_path

    def adopt_folder(self):
        if self.selectFilePath:
            self.window.destroy()
            self.show_duplicates_images(self.selectFilePath)

    def show_duplicates_images(self, pfad):
        duplicate = find_duplicates(pfad)
        if duplicate:
            self.show_duplicates_in_gui(duplicate)
        else:
            self.display_message("Keine Duplikate gefunden!")

    def show_duplicates_in_gui(self, duplicates):
        self.duplicatesWindow = tk.Tk()
        self.duplicatesWindow.title("Gefundene Duplikate")

        self.duplicateList = tk.Listbox(self.duplicatesWindow, width=50, height=20)
        self.duplicateList.pack(padx=10, pady=10)

        for path1, path2 in duplicates:
            self.duplicateList.insert(
                tk.END,
                f"Das Bild {os.path.basename(path1)} ist ein Duplikat von {os.path.basename(path2)}",
            )

        self.duplicatesWindow.mainloop()

    def display_message(self, message):
        self.resultWindow = tk.Tk()
        self.resultWindow.title("Ergebnis")
        label = ttk.Label(self.resultWindow, text=message)
        label.pack(padx=10, pady=10)
        self.resultWindow.mainloop()


def image_comparison_100(pictureX_path, pictureY_path):
    picture1 = Image.open(pictureX_path)
    picture2 = Image.open(pictureY_path)

    if picture1.size != picture2.size:
        return False

    pixels1 = picture1.getdata()
    pixels2 = picture2.getdata()

    for p1, p2 in zip(pixels1, pixels2):
        if p1 != p2:
            return False

    return True


def find_duplicates(path):
    hashes = {}
    duplicates = []

    for folder_name, subfolders, file_names in os.walk(path):
        for filename in file_names:
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                filepath = os.path.join(folder_name, filename)
                try:
                    with Image.open(filepath) as img:
                        h = imagehash.average_hash(img)
                        if h in hashes:
                            duplicates.append((filename, os.path.basename(hashes[h])))
                        else:
                            hashes[h] = filepath
                except Exception as e:
                    print(f"Fehler beim Lesen von {filename}: {e}")
    return duplicates


if __name__ == "__main__":
    # Hauptteil der Software um das GUI zu initialisieren
    window = tk.Tk()
    gui = InputWindow(window)
    window.mainloop()
