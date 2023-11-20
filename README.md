# Duplikatserkennung
## Konzipierung und Entwicklung einer Software, welche für die Identifizierung von Duplikaten von Bildern verwendet werden kann

Die Software wurde entwickelt, um Duplikate in einer Bilddatenbank zu erkennen.

Anforderungen:

Muss-Ziele
- Datenzugriff: Die Software sollte sowohl den lokalen Datenzugriff (z. B. von der Festplatte) als auch den Datenzugriff in der Cloud (z. B. von Cloud-Speicherdiensten) unterstützen. 
- Dublikatserkennung: Die Software sollte in der Lage sein, Duplikate nicht nur anhand des Dateinamens, sondern auch anhand des Bildinhalts (auf Pixelbasis) zu erkennen, um wirklich identische Bilder zu identifizieren. 
- Duplikatliste erstellen: Nach der Identifizierung von Duplikaten sollten diese in einer übersichtlichen Liste angezeigt werden, um den Benutzern die Überprüfung zu erleichtern.
- Benutzeroberfläche: Die Benutzeroberfläche sollte eine benutzerfreundliche Möglichkeit bieten, Ordner auszuwählen und dem Benutzer ermöglichen, diese Ordner einfach hinzuzufügen oder zu entfernen. 

Kann-Ziele:
- Möglichkeit zum Löschen von Duplikaten: Die Software sollte dem Benutzer die Möglichkeit bieten, Duplikate sicher zu löschen.
- Ähnliche Bilder anzeigen: Die Software sollte in der Lage sein, ähnliche Bilder zu identifizieren und dem Benutzer eine Liste dieser ähnlichen Bilder zur Verfügung stellen, basierend auf visuellen Ähnlichkeiten.



You can use [GitHub markdown
notation](https://docs.github.com/en/github/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax)
or [GitLab markdown notation](https://docs.gitlab.com/ee/user/markdown.html) in
case you are using one of these platforms. This will give a nicely formatted
documentation when looking at your project online.

## Get started

Explain what the user has to type to get started with your solution. Which one
is the main Python file? In the simplest case, this could look something like
this:

``
    python main.py
``

In other cases the user might first have to install some project dependencies
first has to run something like this (a sample requirements.txt file is also
included in the project template):

``
    pip install -r requirements.txt
``

## Understanding the sources --> Hier erläutern, wie Projekt grob aufgebaut ist

Explain any high level concepts that you are using in your software. What were
your ideas for creating the whole software? What might not be apparent from the
sources alone? You can also add diagrams, photos of whiteboards or flipcharts
or even crudly drawing napkin sketches of the core concepts of your software
when they are readable and helpful for understanding.
