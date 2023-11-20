from PIL import Image
import imagehash
import os
import tkinter as tk
from tkinter import filedialog, ttk


class Eingabefenster:
    def __init__(self, fenster):
        self.fenster = fenster
        self.fenster.title("Duplikatserkennung")

        self.beschrieb = ttk.Label(
            fenster, text="Bitte wähle den Ordner mit den zu prüfenden Bildern:"
        )
        self.beschrieb.pack(pady=10)

        self.auswahl_pfad = ttk.Button(
            fenster, text="Ordner auswählen", command=self.ordner_waehlen
        )
        self.auswahl_pfad.pack(pady=10)

        self.auswahl_pfad_beschrieb = ttk.Label(fenster, text="")
        self.auswahl_pfad_beschrieb.pack(pady=10)

        self.pfad_speichern = ttk.Button(
            fenster, text="Ordner übernehmen", command=self.ordner_übernehmen
        )
        self.pfad_speichern.pack(pady=10)

        self.ausgewählter_dateipfad = None

    def ordner_waehlen(self):
        dateipfad = filedialog.askdirectory()
        if dateipfad:
            self.auswahl_pfad_beschrieb.config(text=dateipfad)
            self.ausgewählter_dateipfad = dateipfad

    def ordner_übernehmen(self):
        if self.ausgewählter_dateipfad:
            self.fenster.destroy()
            self.show_duplicate_images(self.ausgewählter_dateipfad)

    def show_duplicate_images(self, pfad):
        duplikate = find_duplicates(pfad)
        if duplikate:
            self.show_duplicates_in_gui(duplikate)
        else:
            self.display_message("Keine Duplikate gefunden!")

    def show_duplicates_in_gui(self, duplikate):
        self.duplikatfenster = tk.Tk()
        self.duplikatfenster.title("Gefundene Duplikate")

        self.duplikatliste = tk.Listbox(self.duplikatfenster, width=50, height=20)
        self.duplikatliste.pack(padx=10, pady=10)

        for pfad1, pfad2 in duplikate:
            self.duplikatliste.insert(
                tk.END,
                f"Das Bild {os.path.basename(pfad1)} ist ein Duplikat von {os.path.basename(pfad2)}",
            )

        self.duplikatfenster.mainloop()

    def display_message(self, message):
        self.ergebnisfenster = tk.Tk()
        self.ergebnisfenster.title("Ergebnis")
        label = ttk.Label(self.ergebnisfenster, text=message)
        label.pack(padx=10, pady=10)
        self.ergebnisfenster.mainloop()


def bildervergleich_100(bildx_path, bildy_path):
    bild1 = Image.open(bildx_path)
    bild2 = Image.open(bildy_path)

    if bild1.size != bild2.size:
        return False

    pixels1 = bild1.getdata()
    pixels2 = bild2.getdata()

    for p1, p2 in zip(pixels1, pixels2):
        if p1 != p2:
            return False

    return True


def find_duplicates(pfad):
    hashes = {}
    duplikate = []

    for foldername, subfolders, filenames in os.walk(pfad):
        for filename in filenames:
            if filename.lower().endswith((".png", ".jpg", ".jpeg", ".gif", ".bmp")):
                filepath = os.path.join(foldername, filename)
                try:
                    with Image.open(filepath) as img:
                        h = imagehash.average_hash(img)
                        if h in hashes:
                            duplikate.append((filename, os.path.basename(hashes[h])))
                        else:
                            hashes[h] = filepath
                except Exception as e:
                    print(f"Fehler beim Lesen von {filename}: {e}")
    return duplikate


if __name__ == "__main__":
    fenster = tk.Tk()
    gui = Eingabefenster(fenster)
    fenster.mainloop()
