from PIL import Image
import imagehash
import os
import tkinter as tk
from tkinter import filedialog, ttk


class InputWindow:
    def __init__(self,window):
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
            #Das OutputWindow wird geöffnet
            OutputWindow(self.selectFilePath).run()

class DuplicateFinder:
    def __init__(self, path):
        self.path = path

    def find_duplicates_hash(self):
        hashes = {}
        duplicates = []

        for folder_name, subfolders, file_names in os.walk(self.path):
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
    
    #def funktion_2(self):
    #def funktion_3(self):
    #def funktion_4(self):
    #def funktion_5(self):

class OutputWindow:
    def __init__(self, path):
        self.window = tk.Tk()
        self.window.title("Ergebnisse")
        self.show_duplicates_images(path)

    def show_duplicates_images(self, path):
    # Klasse für die Duplikatsfindung wird aufgerufen => es werden verschiedene Funktionen angewendet
        finder = DuplicateFinder(path)
        duplicates_hash = finder.find_duplicates_hash()
        #duplicates_2= finder.funktion2()
        #duplicates_3= finder.funktion3()
        #duplicates_4= finder.funktion4()
        #duplicates_5= finder.funktion5()
        if duplicates_hash:
            self.show_duplicates(duplicates_hash)
        else:
            self.display_message("Keine Duplikate gefunden!")

    def display_message(self, message):
        label = ttk.Label(self.window, text=message)
        label.pack(padx=10, pady=10)

    def show_duplicates(self, duplicates):
        duplicate_list = tk.Listbox(self.window, width=50, height=20)
        duplicate_list.pack(padx=10, pady=10)

        for path1, path2 in duplicates:
            duplicate_list.insert(tk.END, f"Das Bild {os.path.basename(path1)} ist ein Duplikat von {os.path.basename(path2)}")

    def run(self):
        self.window.mainloop()

###############################################################################################################################

if __name__ == "__main__":
    # Hauptteil der Software um das GUI zu initialisieren
    window = tk.Tk()
    gui = InputWindow(window)
    window.mainloop()
