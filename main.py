from PIL import Image
import imagehash
import os
import tkinter as tk
from tkinter import filedialog, ttk

import tkinter as tk
from tkinter import filedialog, ttk

class Eingabefenster:
    def __init__(self, fenster):
        self.fenster = fenster
        self.fenster.title("Duplikatserkennung")

        self.beschrieb = ttk.Label(fenster, text="Bitte wähle den Ordner mit den zu prüfenden Bildern:")
        self.beschrieb.pack(pady=10)

        self.auswahl_pfad = ttk.Button(fenster, text="Ordner auswählen", command=self.ordner_waehlen)
        self.auswahl_pfad.pack(pady=10)

        self.auswahl_pfad_beschrieb = ttk.Label(fenster, text="") # An dieser Stelle kann noch ein optionaler Beschrieb hinzugefügt werden
        self.auswahl_pfad_beschrieb.pack(pady=10)

        self.pfad_speichern = ttk.Button(fenster, text="Ordner übernehmen", command=self.ordner_übernehmen)
        self.pfad_speichern.pack(pady=10)

        self.ausgewählter_dateipfad = None

    def ordner_waehlen(self):
        dateipfad = filedialog.askdirectory()
        if dateipfad:  # Es wird geprüft, ob ein valabler Ordner ausgewählt wurde
            self.auswahl_pfad_beschrieb.config(text=dateipfad)
            self.ausgewählter_dateipfad = dateipfad

    def ordner_übernehmen(self): # Pfad des Ordners wird in einer Variable gespeichert
        if self.ausgewählter_dateipfad:
            global verzeichnis 
            verzeichnis = self.ausgewählter_dateipfad
            self.fenster.destroy()

def bildervergleich_100(bildx_path, bildy_path): # Funktion macht eine 100% Prüfung der Bilder (nur exakte Kopien werden identifiziert)
    # Die zu vergleichenden Bilder werden geöffnet
    bild1 = Image.open(bildx_path)
    bild2 = Image.open(bildy_path)

    # Abmessung "size" der beiden Bilder werden verglichen
    if bild1.size != bild2.size:
        return False

    # Jedes Pixel wird verglichen
    pixels1 = bild1.getdata()
    pixels2 = bild2.getdata()

    for p1, p2 in zip(pixels1, pixels2):
        if p1 != p2:
            return False

    return True

def alle_bilder_im_ordner_vergleichen(pfad): # alle Bilder im ausgewählten Verzeichnis werden gegeneinander geprüft
    bilder = [f for f in os.listdir(pfad) if os.path.isfile(os.path.join(pfad, f))]
    gefundene_duplikate = []

    for i in range(len(bilder)):
        for j in range(i+1, len(bilder)):
            bildx_path = os.path.join(pfad, bilder[i])
            bildy_path = os.path.join(pfad, bilder[j])

            if bildervergleich_100(bildx_path, bildy_path):
                gefundene_duplikate.append((bildx_path, bildy_path))

    return gefundene_duplikate

def find_duplicates(pfad): # Das Testing muss noch implementiert werden!
    hashes = {}
    duplikate = []
    
    for foldername, subfolders, filenames in os.walk(pfad):
        for filename in filenames:
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
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

def save_duplicates_to_txt(pfad, duplikat_liste):
    output_file = os.path.join(pfad, 'duplikate.txt')

    with open(output_file, 'w') as f:
        for dateiname1, dateiname2 in duplikat_liste:
            f.write(f"Die Datei {dateiname1} ist ein Duplikat von {dateiname2}\n")

    print(f"Die Duplikate wurden in {output_file} gespeichert.")

    
##################################################################################################################################################
if __name__ == "__main__":
    fenster = tk.Tk()
    gui = Eingabefenster(fenster)
    fenster.mainloop()

    duplikat_liste = find_duplicates(verzeichnis)
    for pfad1, pfad2 in duplikat_liste:
        print(f"Das Bild {pfad1} ist ein Duplikat von {pfad2}")

    save_duplicates_to_txt(verzeichnis, duplikat_liste)