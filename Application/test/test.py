import unittest
import googlemapEx
import videoModule
import aiModule

skin_cancer_names = ["Actinic Keratoses", "Basal Cell Carcinoma",
                     "Benign Keratosis", "Dermatofibroma",
                     "Melanocytic Nevi","Melanoma","Vascular Skin Lesions"]

class ModuleTest(unittest.TestCase):
    def test_googlemapEx(self):
        position = googlemapEx.get_position("BU")
        result = googlemapEx.get_nearby_results(position,5000,"School")[0]
        self.assertEqual(position,(42.3504997, -71.1053991))
        self.assertEqual(type(result),dict)

    def test_videoModule(self):
        output = videoModule.processResult(("Actinic Keratoses",0.8))
        self.assertEqual(output, "please click learn -> Actinic Keratoses")
        output = videoModule.processResult(("Actinic Keratoses",0.95))
        self.assertEqual(output, "we highly recommand to go see a nearby dermatologist")

    def test_aiModule(self):
        self.assertEqual(aiModule.test("filepath")[0] in skin_cancer_names, True)
        self.assertEqual(type(aiModule.test("filepath")[1]),float)
        

if __name__ == "__main__":
    unittest.main()
