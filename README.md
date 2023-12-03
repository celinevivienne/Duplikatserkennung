# Duplikatserkennung
## Konzipierung und Entwicklung einer Software, welche für die Identifizierung von Duplikaten von Bildern verwendet werden kann

Die vorliegende Arbeit verfolgt das zentrale Ziel, eine effiziente Python-Software zu entwickeln, die in der Lage ist, Duplikate in Bildern zu erkennen. Der Fokus liegt dabei auf der praktischen Anwendung von Python, insbesondere im Kontext des Bildverarbeitungsbereichs. Diese Software wurde gezielt konzipiert, um Studierenden eine praxisorientierte Lernumgebung zu bieten, in der sie ihre Python-Kenntnisse vertiefen und gleichzeitig Einblicke in die Herausforderungen der Bilderkennung gewinnen können.

Im Rahmen dieser Arbeit werden folgende spezifischen Ziele verfolgt: 

- Entwicklung von Clean Code: Das Hauptziel ist die Entwicklung einer Software mit sauberem, gut strukturiertem Code, der leicht verständlich und wartbar ist. 
- Effiziente Duplikaterkennung: Die Software sollte Duplikate in Bilddateien effizient und genau identifizieren, wobei sauberer Code und effektive Algorithmen eingesetzt werden. 
- Bildqualitätsbewertung und Verbesserung: Die Software sollte die Bildqualität bewerten und bei Duplikaten das qualitativ bessere Bild behalten, wobei Test Driven Development (TDD) und Unittesting verwendet werden, um die Qualität sicherzustellen. 
- Benutzerfreundliche Oberfläche: Die Benutzeroberfläche sollte intuitiv und benutzerfreundlich sein, unter Berücksichtigung der Benutzererfahrung. 
- Integration von Version Control (z. B. Git): Die Software sollte Mechanismen zur Versionierung und Verfolgung von Änderungen im Quellcode integrieren und die Vorteile des Version Control Systems nutzen. 
- Kollaborative Entwicklung mit Pair Programming: Die Studierenden arbeiten in Paaren, um die Entwicklung zu beschleunigen und sicherzustellen, dass bestmöglicher Code entsteht. 
- Unittesting: Die Softwareentwicklung sollte Testfälle erstellen und Unittesting durchführen, um sicherzustellen, dass die Software ordnungsgemäss funktioniert.

  
### Anforderungen an die Software

| Priorität | Anforderung | Kurzbeschreibung |
|----------|----------|----------|
| Muss | Datenzugriff | Die Software sollte sowohl den lokalen Datenzugriff (z. B. von der Festplatte) als auch den Datenzugriff in der Cloud (z. B. von Cloud-Speicherdiensten) unterstützen.  |
| Muss | Dublikatserkennung | Die Software sollte in der Lage sein, Duplikate nicht nur anhand des Dateinamens, sondern auch anhand des Bildinhalts (auf Pixelbasis) zu erkennen, um wirklich identische Bilder zu identifizieren. |
| Muss | Duplikatliste erstellen | Nach der Identifizierung von Duplikaten sollten diese in einer übersichtlichen Liste angezeigt werden, um den Benutzern die Überprüfung zu erleichtern. |
| Muss | Benutzeroberfläche | Die Benutzeroberfläche sollte eine benutzerfreundliche Möglichkeit bieten, Ordner auszuwählen und dem Benutzer ermöglichen, diese Ordner einfach hinzuzufügen oder zu entfernen.  |
| Kann | Möglichkeit zum Löschen von Duplikaten | Die Software sollte dem Benutzer die Möglichkeit bieten, Duplikate sicher zu löschen.|
| Kann | Ähnliche Bilder anzeigen| Die Software sollte in der Lage sein, ähnliche Bilder zu identifizieren und dem Benutzer eine Liste dieser ähnlichen Bilder zur Verfügung stellen, basierend auf visuellen Ähnlichkeiten.|

## Los geht's

Um das Python-Programm zu starten, sollte der Benutzer die Datei mit dem Hauptcode ausführen. In diesem Fall ist die Hauptdatei diejenige, die die GUI initialisiert und das Hauptprogramm startet. Das ist die Datei, die die tkinter-Bibliothek verwendet.

Die Benutzer sollten in der Kommandozeile (Terminal) den folgenden Befehl ausführen, um das Programm zu starten:

``
    python main.py
``

Bevor das Programm ausgeführt wird, müssen auch die entsprechenden verwendeten Bibliotheken installiert werden. Alle Bibliotheken, die im Voraus installiert werden müssen, sind im requirements.txt abgelegt.


``
    pip install -r requirements.txt
``

Die im Code verwendeten Bibliotheken sind:
- PIL (Python Imaging Library): Für die Bildverarbeitung, insbesondere zum Öffnen von Bildern.
- imagehash: Eine Bibliothek zur Berechnung von Hash-Werten für Bilder.
- os: Eine integrierte Python-Bibliothek, die Operationen auf dem Betriebssystem ermöglicht, hier insbesondere für Datei- und Verzeichnisoperationen.
- tkinter: Die Standard-GUI-Bibliothek für Python, die für die Erstellung der grafischen Benutzeroberfläche (GUI) verwendet wird.

Diese Bibliotheken werden für die Erstellung einer GUI-Anwendung zur Duplikatserkennung von Bildern verwendet.
Nachdem diese Schritte abgeschlossen sind, kann der Benutzer das Programm durch Ausführen des oben genannten python-Befehls starten.


## Verstehen der Quelle

### Warum eine Duplikatssoftware? (Nutzen)

Wir haben diese Software zur Duplikaterkennung entwickelt, um in der heutigen schnelllebigen Welt, in der sich ständig grosse Mengen doppelter Bilder ansammeln, eine praktische Lösung zu bieten. Die Hauptmotivation unserer Arbeit ist es, den Speicherplatz zu optimieren, der durch diese redundanten Bilder unnötig belegt wird.

Mit dem Entfernen der Duplikate wird der Benutzer automatisch beim Organisieren/Aufräumen grosser Mengen an Bildern unterstützt. Heutzutage, wo Zeit von entscheidender Bedeutung ist, ist unsere automatisierte Lösung ein praktischer Helfer.


### Projektstruktur

Das Hauptprogramm besteht aus drei Klassen: InputWindow, DuplicateFinder und OutputWindow.

> **InputWindow** kümmert sich um die Benutzeroberfläche (GUI) für die Eingabe des Ordners mit den zu prüfenden Bildern.

> **DuplicateFinder** ist für die eigentliche Duplikatserkennung verantwortlich. Es gibt bereits eine Implementierung für die Hash-basierte Duplikatserkennung (find_duplicates_hash). Es gibt auch Platzhalter-Funktionen (ausgeklammert), die für zusätzliche Duplikatserkennungsmethoden verwendet werden könnten.

> **OutputWindow** zeigt die Ergebnisse der Duplikatserkennung in einem neuen Fenster an.

### Funktionsweise

Der Benutzer startet das Programm und wählt über die GUI (InputWindow) den Ordner mit den zu prüfenden Bildern aus.
Das Programm verwendet die DuplicateFinder-Klasse, um Duplikate in diesem Ordner zu finden. Aktuell wird nur die Hash-basierte Methode (find_duplicates_hash) verwendet.Die Ergebnisse werden dann in einem separaten Fenster (OutputWindow) angezeigt.

Das Programm verwendet die tkinter-Bibliothek für die Benutzeroberfläche und die Pillow-Bibliothek für die Bildverarbeitung. Die Hash-basierte Methode vergleicht Bilder anhand ihrer durchschnittlichen Hash-Werte.

#### Clean Code

#### Version Control 

#### Testing
Erster Testlauf: Duplikatserkennung in Python

Wir haben unsere Duplikatserkennungssoftware einem ersten Test unterzogen, um die Effektivität und Genauigkeit unter verschiedenen Bedingungen zu bewerten. Hier sind die Testfälle, die wir durchgeführt haben:

Graustufen- und Duplex-Bilder: Die Software wurde darauf getestet, Duplikate zu erkennen, die in Graustufen konvertiert wurden sowie in Duplex-Modus, der nur zwei Farbtöne verwendet.

Gedrehte Bilder: Die Erkennung wurde mit Bildern durchgeführt, die um verschiedene Winkel gedreht wurden, um die Robustheit gegenüber Orientierungsänderungen zu überprüfen.

Bilder mit Zusätzen: Getestet wurde auch, ob die Software kleine Änderungen wie gekritzelte Linien auf den Bildern erkennen kann.

Verschiedene Auflösungen: Die Duplikatserkennung wurde auf Bilder mit unterschiedlichen Auflösungen angewendet, um die Skalierbarkeit der Software zu testen.

Transparenz: Es wurde überprüft, ob die Software Duplikate ohne Hintergrund, also mit transparenten Bereichen, erkennen kann.

Leicht abweichende Bilder: Schliesslich wurde die Fähigkeit der Software getestet, ähnliche, aber nicht identische Bilder zu identifizieren.

Die Ergebnisse dieser Tests geben Aufschluss über die Anpassungsfähigkeit und Genauigkeit unserer Software und liefern wichtige Erkenntnisse für die weitere Optimierung.

Die Duplikatserkennungssoftware hat in unserem ersten Testlauf gute Ergebnisse gezeigt und nahezu alle gestellten Aufgaben mit einer Erfolgsrate von 100% gemeistert. Einzig bei der Unterscheidung zwischen identischen und ähnlichen Bildern gab es Herausforderungen, die nicht vollständig erfolgreich waren. 
Dieses Ergebnis half uns dabei, unseren Code noch so anzupassen, dass in einem zweiten Testlauf auch die ähnlichen Bilder erkannt wurden. Dafür wurde der Schwellwert auf 70% reduziert. Anschliessend wurden sogar die ähnlichen Fotos von der Software erkannt


### Erweiterungen

1. Die Bilderkennungssoftware soll um **Cloud-Anbindung** erweitert werden, um Benutzern Zugriff auf ihre in der Cloud gespeicherten Bilder zu ermöglichen.
2. Es wird angestrebt, eine **mobile Anwendung** zu implementieren, die eine ansprechende Benutzeroberfläche bietet und es Nutzern erlaubt, Duplikate auf ihren Mobilgeräten einfach zu erkennen und zu organisieren.


### Sequenzdiagramm
![Sequenzdiagramm](https://github.com/celinevivienne/Duplikatserkennung/assets/113386635/bcf469a7-52fe-448b-8ade-5f81cf8e30d9)<?xml version="1.0" encoding="us-ascii" standalone="no"?><svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" contentStyleType="text/css" height="454px" preserveAspectRatio="none" style="width:528px;height:454px;background:#FFFFFF;" version="1.1" viewBox="0 0 528 454" width="528px" zoomAndPan="magnify"><defs/><g><rect fill="#FFFFFF" height="251.9297" style="stroke:#181818;stroke-width:1.0;" width="10" x="131.5" y="112.4297"/><rect fill="#FFFFFF" height="40.1328" style="stroke:#181818;stroke-width:1.0;" width="10" x="136.5" y="149.5625"/><rect fill="#FFFFFF" height="138.5313" style="stroke:#181818;stroke-width:1.0;" width="10" x="284.5" y="225.8281"/><rect fill="#FFFFFF" height="64.2656" style="stroke:#181818;stroke-width:1.0;" width="10" x="456.5" y="254.9609"/><line style="stroke:#181818;stroke-width:0.5;stroke-dasharray:5.0,5.0;" x1="40" x2="40" y1="81.2969" y2="373.3594"/><line style="stroke:#181818;stroke-width:0.5;stroke-dasharray:5.0,5.0;" x1="136" x2="136" y1="81.2969" y2="373.3594"/><line style="stroke:#181818;stroke-width:0.5;stroke-dasharray:5.0,5.0;" x1="289.5" x2="289.5" y1="81.2969" y2="373.3594"/><line style="stroke:#181818;stroke-width:0.5;stroke-dasharray:5.0,5.0;" x1="461.5" x2="461.5" y1="81.2969" y2="373.3594"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="64" x="5" y="77.9951">Benutzer</text><ellipse cx="40" cy="13.5" fill="#E2E2F0" rx="8" ry="8" style="stroke:#181818;stroke-width:0.5;"/><path d="M40,21.5 L40,48.5 M27,29.5 L53,29.5 M40,48.5 L27,63.5 M40,48.5 L53,63.5 " fill="none" style="stroke:#181818;stroke-width:0.5;"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="64" x="5" y="385.3545">Benutzer</text><ellipse cx="40" cy="397.1563" fill="#E2E2F0" rx="8" ry="8" style="stroke:#181818;stroke-width:0.5;"/><path d="M40,405.1563 L40,432.1563 M27,413.1563 L53,413.1563 M40,432.1563 L27,447.1563 M40,432.1563 L53,447.1563 " fill="none" style="stroke:#181818;stroke-width:0.5;"/><rect fill="#E2E2F0" height="30.2969" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="103" x="85" y="50"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="89" x="92" y="69.9951">InputWindow</text><rect fill="#E2E2F0" height="30.2969" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="103" x="85" y="372.3594"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="89" x="92" y="392.3545">InputWindow</text><rect fill="#E2E2F0" height="30.2969" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="116" x="231.5" y="50"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="102" x="238.5" y="69.9951">OutputWindow</text><rect fill="#E2E2F0" height="30.2969" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="116" x="231.5" y="372.3594"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="102" x="238.5" y="392.3545">OutputWindow</text><rect fill="#E2E2F0" height="30.2969" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="122" x="400.5" y="50"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="108" x="407.5" y="69.9951">DuplicateFinder</text><rect fill="#E2E2F0" height="30.2969" rx="2.5" ry="2.5" style="stroke:#181818;stroke-width:0.5;" width="122" x="400.5" y="372.3594"/><text fill="#000000" font-family="sans-serif" font-size="14" lengthAdjust="spacing" textLength="108" x="407.5" y="392.3545">DuplicateFinder</text><rect fill="#FFFFFF" height="251.9297" style="stroke:#181818;stroke-width:1.0;" width="10" x="131.5" y="112.4297"/><rect fill="#FFFFFF" height="40.1328" style="stroke:#181818;stroke-width:1.0;" width="10" x="136.5" y="149.5625"/><rect fill="#FFFFFF" height="138.5313" style="stroke:#181818;stroke-width:1.0;" width="10" x="284.5" y="225.8281"/><rect fill="#FFFFFF" height="64.2656" style="stroke:#181818;stroke-width:1.0;" width="10" x="456.5" y="254.9609"/><polygon fill="#181818" points="119.5,108.4297,129.5,112.4297,119.5,116.4297,123.5,112.4297" style="stroke:#181818;stroke-width:1.0;"/><line style="stroke:#181818;stroke-width:1.0;" x1="40" x2="125.5" y1="112.4297" y2="112.4297"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="32" x="47" y="107.3638">Start</text><line style="stroke:#181818;stroke-width:1.0;" x1="141.5" x2="188.5" y1="136.5625" y2="136.5625"/><line style="stroke:#181818;stroke-width:1.0;" x1="188.5" x2="188.5" y1="136.5625" y2="149.5625"/><line style="stroke:#181818;stroke-width:1.0;" x1="147.5" x2="188.5" y1="149.5625" y2="149.5625"/><polygon fill="#181818" points="157.5,145.5625,147.5,149.5625,157.5,153.5625,153.5,149.5625" style="stroke:#181818;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="91" x="153.5" y="131.4966">select_folder()</text><line style="stroke:#181818;stroke-width:1.0;" x1="146.5" x2="188.5" y1="188.6953" y2="188.6953"/><line style="stroke:#181818;stroke-width:1.0;" x1="188.5" x2="188.5" y1="188.6953" y2="201.6953"/><line style="stroke:#181818;stroke-width:1.0;" x1="141.5" x2="188.5" y1="201.6953" y2="201.6953"/><polygon fill="#181818" points="151.5,197.6953,141.5,201.6953,151.5,205.6953,147.5,201.6953" style="stroke:#181818;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="90" x="153.5" y="183.6294">adopt_folder()</text><polygon fill="#181818" points="272.5,221.8281,282.5,225.8281,272.5,229.8281,276.5,225.8281" style="stroke:#181818;stroke-width:1.0;"/><line style="stroke:#181818;stroke-width:1.0;" x1="141.5" x2="278.5" y1="225.8281" y2="225.8281"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="124" x="148.5" y="220.7622">Initialisiere mit Pfad</text><polygon fill="#181818" points="444.5,250.9609,454.5,254.9609,444.5,258.9609,448.5,254.9609" style="stroke:#181818;stroke-width:1.0;"/><line style="stroke:#181818;stroke-width:1.0;" x1="294.5" x2="450.5" y1="254.9609" y2="254.9609"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="143" x="301.5" y="249.895">find_duplicates_hash()</text><polygon fill="#181818" points="305.5,280.0938,295.5,284.0938,305.5,288.0938,301.5,284.0938" style="stroke:#181818;stroke-width:1.0;"/><line style="stroke:#181818;stroke-width:1.0;stroke-dasharray:2.0,2.0;" x1="299.5" x2="455.5" y1="284.0938" y2="284.0938"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="126" x="311.5" y="279.0278">R&#252;ckgabe Duplikate</text><line style="stroke:#181818;stroke-width:1.0;" x1="294.5" x2="336.5" y1="318.2266" y2="318.2266"/><line style="stroke:#181818;stroke-width:1.0;" x1="336.5" x2="336.5" y1="318.2266" y2="331.2266"/><line style="stroke:#181818;stroke-width:1.0;" x1="289.5" x2="336.5" y1="331.2266" y2="331.2266"/><polygon fill="#181818" points="299.5,327.2266,289.5,331.2266,299.5,335.2266,295.5,331.2266" style="stroke:#181818;stroke-width:1.0;"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="114" x="301.5" y="313.1606">show_duplicates()</text><polygon fill="#181818" points="51,351.3594,41,355.3594,51,359.3594,47,355.3594" style="stroke:#181818;stroke-width:1.0;"/><line style="stroke:#181818;stroke-width:1.0;stroke-dasharray:2.0,2.0;" x1="45" x2="283.5" y1="355.3594" y2="355.3594"/><text fill="#000000" font-family="sans-serif" font-size="13" lengthAdjust="spacing" textLength="111" x="57" y="350.2935">Zeige Ergebnisse</text><!--SRC=[TT2nJiGm30RWFKzXtGJ3lS0D3ATIgLCH32VTKlbIjxMkf57YSXBFniQBuLGAj0ZM-FCVssXb2d0aDyix1UCn25lsw0HsbVEpdDYrqsq76A4wRUlrB5jG_mB5x4UsA5IgeR2OeZGcVmVx1ms50xo8jXcqmc-gqqT6ttCrqaXMccuQDUJk_b-7xUHNhAK_O9rWvLWOHuvCWU2L1PuwR7zoTGzJBxmebNSwVTFcNM8pO1pMO-XAwlOv_Vdpmrvxl6WXzLoLvBYb7eVfjehRJfhEawpYxoiTu4pS4po6dYwEOoJp1G00]--></g></svg>


**löschen**
Explain any high level concepts that you are using in your software. What were
your ideas for creating the whole software? What might not be apparent from the
sources alone? You can also add diagrams, photos of whiteboards or flipcharts
or even crudly drawing napkin sketches of the core concepts of your software
when they are readable and helpful for understanding.
