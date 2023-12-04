from PIL import Image
from tkinter import filedialog, ttk
from skimage import io, measure, color
from skimage.metrics import structural_similarity
from skimage.transform import resize
import imagehash
import tkinter as tk
import os
import numpy as np

class InputWindow:
 
   
    def __init__(self,window):
        # Initialisieren von GUI-Komponenten
        self.window = window
        self.window.title("Duplikatserkennung")
        
        # Fenstergröße festlegen
        window_width = 800
        window_height = 600
        self.window.geometry(f"{window_width}x{window_height}")

        # Bildschirmauflösung ermitteln
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()

        # Berechnen der x und y Koordinaten, um das Fenster in der Mitte des Bildschirms zu zentrieren
        x = int((screen_width / 2) - (window_width / 2))
        y = int((screen_height / 2) - (window_height / 2))

        # Fensterposition einstellen, um es in der Mitte des Bildschirms zu platzieren
        self.window.geometry(f"{window_width}x{window_height}+{x}+{y}")

        # Ordner auswählen
        
        self.description = ttk.Label(
            window, text="Bitte wähle den Ordner mit den zu prüfenden Bildern:"
        )
        self.description.pack(pady=(100, 1))

        # Ordner öffenen (Knopf)
        self.selectPath = ttk.Button(
            window, text="Ordner auswählen", command=self.select_folder
        )
        self.selectPath.pack(pady=1)

        self.selectPathDescription = ttk.Label(window, text="")
        self.selectPathDescription.pack(pady=10)

        # Dropdown-Liste zur Auswahl der Duplikatserkennungsmethode
        self.method_var = tk.StringVar()
        self.method_var.set("Hash basierte Erkennung")
        self.method_label = ttk.Label(window, text="Duplikatserkennungsmethode:")
        self.method_label.pack(pady=10)
        self.method_dropdown = ttk.Combobox(
            window, textvariable=self.method_var,
            values=["Hash basierte Erkennung", "Struktur basierte Erkennung"]
        )
        self.method_dropdown.pack(pady=1)

        # Schwellenwert für Ähnlichkeit
        self.threshold_var = tk.DoubleVar()
        self.threshold_var.set(0.5)
        self.threshold_label = ttk.Label(window, text="Schwellenwert für Ähnlichkeit:")
        self.threshold_label.pack(pady=10)
        self.threshold_entry = ttk.Entry(window, textvariable=self.threshold_var)
        self.threshold_entry.pack(pady=10)

        # Bestätigung Ordner (Knopf)
        self.safePath = ttk.Button(
            window, text="Ordner prüfen", command=self.adopt_folder
        )
        self.safePath.pack(pady=10)

        # Variable zum speichern des ausgewählten Pfades
        self.selectFilePath = None


        # Fortschrittsanzeige-Widget hinzufügen
        self.progress_bar = ttk.Progressbar(
            self.window, orient="horizontal", length=300, mode="determinate"
        )
        self.progress_bar.pack_forget()  # Zuerst verstecken


    def select_folder(self):
        file_path = filedialog.askdirectory()
        if file_path:
            self.selectPathDescription.config(text=file_path)
            self.selectFilePath = file_path

    def adopt_folder(self):
        if self.selectFilePath:

            file_count = len([name for name in os.listdir(self.selectFilePath)
                              if os.path.isfile(os.path.join(self.selectFilePath, name))])
            self.progress_bar['maximum'] = file_count
            self.progress_bar.pack(pady=20)
            self.progress_bar['value'] = 0
            self.window.update_idletasks()
            OutputWindow(self.selectFilePath, self.method_var.get(), self.threshold_var.get(), self.progress_bar).run()

            '''self.window.destroy() -> auskommentiert
            # Übergeben Sie method_var und threshold_var an die OutputWindow-Klasse
            OutputWindow(self.selectFilePath, self.method_var, self.threshold_var).run() -> auskommentiert'''


 

class DuplicateFinder:
    def __init__(self, path):
        self.path = path

    def find_duplicates_hash(self, update_progress_callback=None):
        hashes = {}
        duplicates = []
        file_names = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        total_files = len(file_names)

        for i, filename in enumerate(file_names):
            filepath = os.path.join(self.path, filename)
            try:
                with Image.open(filepath) as img:
                    h = imagehash.average_hash(img)
                    if h in hashes:
                        duplicates.append((filename, os.path.basename(hashes[h])))
                    else:
                        hashes[h] = filepath
            except Exception as e:
                print(f"Fehler beim Lesen von {filename}: {e}")

            if update_progress_callback:
                update_progress_callback(i + 1, total_files)

        return duplicates

    '''def find_duplicates_hash(self):
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
        return duplicates'''

    def find_duplicates_structure(self, similarity_threshold, update_progress_callback=None):
        images = {}
        duplicates = []
        file_names = [f for f in os.listdir(self.path) if os.path.isfile(os.path.join(self.path, f))]
        total_files = len(file_names)

        for i, filename in enumerate(file_names):
            filepath = os.path.join(self.path, filename)
            try:
                img = io.imread(filepath)
                img = resize(img, (128, 128), anti_aliasing=True)
                img_gray = color.rgb2gray(img)

                for existing_img, existing_img_path in images.values():
                    data_range = existing_img.max() - existing_img.min()
                    similarity = structural_similarity(existing_img, img_gray, data_range=data_range)
                    if similarity > similarity_threshold:
                        duplicates.append((filename, os.path.basename(existing_img_path)))
                        break
                else:
                    images[filename] = (img_gray, filepath)
            except Exception as e:
                print(f"Fehler beim Lesen von {filename}: {e}")

            if update_progress_callback:
                update_progress_callback(i + 1, total_files)
            

        return duplicates
    
    '''def find_duplicates_structure(self, similarity_threshold):
        images = {}
        duplicates = []

        for folder_name, subfolders, file_names in os.walk(self.path):
            for filename in file_names:
                supported_formats = (".png", ".jpg", ".jpeg", ".gif", ".bmp")
                if filename.lower().endswith(supported_formats):
                    filepath = os.path.join(folder_name, filename)
                    try:
                        img = io.imread(filepath)

                        # Zuschneiden oder Skalieren der Bilder auf die gleiche Größe (z.B. 128x128)
                        img = resize(img, (128, 128), anti_aliasing=True) 

                        # Konvertiere das Bild in Graustufen (L-Modus)
                        img_gray = color.rgb2gray(img)
                        # Berechnung der strukturellen Ähnlichkeit
                        for existing_img, existing_img_path in images.values():
                            data_range = existing_img.max() - existing_img.min()
                            similarity = structural_similarity(existing_img, img_gray, data_range=data_range)
                            if similarity > similarity_threshold:
                                duplicates.append((filename, os.path.basename(existing_img_path)))
                                break
                        else:
                            # Falls keine Duplikate gefunden wurden, fügen Sie das Bild zur images-Datenstruktur hinzu
                            images[filename] = (img_gray, filepath)

                    except Exception as e:
                        print(f"Fehler beim Lesen von {filename}: {e}")
        return duplicates'''


class OutputWindow:
    def __init__(self, path, method, threshold, progress_bar):
        self.window = tk.Tk()
        self.window.title("Ergebnisse")

        self.method = method  # Übergeben Sie method_var 
        self.threshold = threshold  # Übergeben Sie threshold_var
        self.progress_bar = progress_bar
        
        self.show_duplicates_images(path)


    def show_duplicates_images(self, path):
        finder = DuplicateFinder(path)
        if self.method == "Hash basierte Erkennung":
            duplicates = finder.find_duplicates_hash(self.update_progress_bar)
        elif self.method == "Struktur basierte Erkennung":
            duplicates = finder.find_duplicates_structure(self.threshold, self.update_progress_bar)
        else:
            duplicates = []

        if duplicates:
            self.show_duplicates(duplicates)
        else:
            self.display_message("Keine Duplikate gefunden!")


    '''def show_duplicates_images(self, path):
        finder = DuplicateFinder(path)
        method = self.method_var.get()  # Zugriff auf method_var-Wert
        threshold = self.threshold_var.get()  # Zugriff auf threshold_var-Wert
        if method == "Hash basierte Erkennung":
            duplicates = finder.find_duplicates_hash()
        elif method == "Struktur basierte Erkennung":
            duplicates = finder.find_duplicates_structure(threshold)  # Verwenden Sie threshold als Parameter
        else:
            duplicates = []

        if duplicates:
            self.show_duplicates(duplicates)
        else:
            self.display_message("Keine Duplikate gefunden!")'''

    def display_message(self, message):
        label = ttk.Label(self.window, text=message)
        label.pack(padx=10, pady=10)

    def show_duplicates(self, duplicates):
        duplicate_list = tk.Listbox(self.window, width=150, height=20)
        duplicate_list.pack(padx=10, pady=10)

        for path1, path2 in duplicates:
            duplicate_list.insert(tk.END, f"Das Bild {os.path.basename(path1)} ist ein Duplikat von {os.path.basename(path2)}")

    def run(self):
        self.window.mainloop()

    
    def update_progress_bar(self, current, total):
        print(f"Updating progress: {current}/{total}")  # Zum Debuggen
        self.progress_bar['value'] = current
        self.window.update_idletasks() # Stellen Sie sicher, dass die GUI aktualisiert wird
        '''if current == total:
            self.progress_bar['value'] = 100  # Erzwingen Sie, dass der Fortschrittsbalken auf 100% gesetzt wird'''

    

###############################################################################################################################

if __name__ == "__main__":
    # Hauptteil der Software um das GUI zu initialisieren
    window = tk.Tk()
    gui = InputWindow(window)
    window.mainloop()