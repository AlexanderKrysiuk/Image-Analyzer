import unittest
from unittest import result
import image_analyzer

class TestImageAnalyzer(unittest.TestCase):
    def test_correct_output(self):
        image = "test.png"
        correct_dictionary = {
            (255, 255, 255) : 41,
            (29, 29, 27) : 59
        }
        wrong_dictionary = {
            (215, 255, 255) : 41,
            (29, 29, 27) : 39
        }
        result = image_analyzer.image_analyzer(image)
        #Checking the correct values for returned dictionary
        self.assertEqual(result, correct_dictionary)
        #Checking if values are not matching
        self.assertNotEqual(result, wrong_dictionary)

    def test_correct_file(self):
        #Checking if file is image
        #File is not image, error expected
        self.assertRaises(TypeError, image_analyzer, "test_text.txt")

    def test_the_return_of_dictionary(self):
        #Check if return type is dictionary
        self.addTypeEqualityFunc(dict, image_analyzer)