from main import *

def test_find_duplicates_hash():
    test_path = "/Users/simonhani/Documents/git_Repository/Duplikatserkennung/Testbilder"
    finder = DuplicateFinder(test_path)
    duplicates = finder.find_duplicates_hash()

    expected_results = [("baum4.jpg", "baum5.jpg"), ("baum2.jpg", "baum1.jpg")]

    for expected in expected_results:
        assert expected in duplicates