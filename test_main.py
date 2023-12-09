from main import *


def test_find_duplicates_hash():
    test_path = "/Users/simonhani/Documents/git_Repository/Duplikatserkennung/Testbilder"
    finder = DuplicateFinder(test_path)
    duplicates = finder.find_duplicates_hash()

    expected_results = [("baum5.jpg", "baum6.JPG"),
                        ("Baum1.png", "Baum1_Aufloesung_groesser.jpg"),
                        ("baum3.jpg", "baum3_Aufloesung_kleiner.jpg"),
                        ("baum2.jpg", "Baum1_Aufloesung_groesser.jpg"),
                        ("baum4_gedreht.jpg", "baum4.jpg"),
                        ("baum1_ohne_Hintergrund.png", "Baum1_Aufloesung_groesser.jpg"),
                        ("Baum1_duplex.jpg", "Baum1_Aufloesung_groesser.jpg"),
                        ("Baum1_Zeichnungslinie.jpg", "Baum1_Aufloesung_groesser.jpg"),
                        ("Baum1_Aufloesung.jpg", "Baum1_Aufloesung_groesser.jpg"),]
    for expected in expected_results:
        assert expected in duplicates


def test_find_duplicates_structure():
    test_path = "/Users/simonhani/Documents/git_Repository/Duplikatserkennung/Testbilder"
    similarity_threshold = 0.5  # Angabe des Schwellwertes
    finder = DuplicateFinder(test_path)

    duplicates = finder.find_duplicates_structure(similarity_threshold)

    expected_results = [("baum5.jpg", "baum6.JPG"),
                        ("Baum1.png", "Baum1_Aufloesung_groesser.jpg"),
                        ("baum3.jpg", "baum3_Aufloesung_kleiner.jpg"),
                        ("baum2.jpg", "Baum1_Aufloesung_groesser.jpg"),
                        ("baum4_gedreht.jpg", "baum4.jpg"),
                        ("baum5_sw.jpg", "baum6.JPG"),
                        ("Baum1_duplex.jpg", "Baum1_Aufloesung_groesser.jpg"),
                        ("Baum1_Zeichnungslinie.jpg",
                         "Baum1_Aufloesung_groesser.jpg"),
                        ("Baum1_Aufloesung.jpg",
                         "Baum1_Aufloesung_groesser.jpg")]

    for expected in expected_results:
        assert expected in duplicates
