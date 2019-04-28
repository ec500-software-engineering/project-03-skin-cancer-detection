skin_cancer_names = ["Actinic Keratoses", "Basal Cell Carcinoma",
                     "Benign Keratosis", "Dermatofibroma",
                     "Melanocytic Nevi","Melanoma","Vascular Skin Lesions"]

def processResult(result):
    if result[1] >= 0.9:
        return "we highly recommand to go see a nearby dermatologist"
    else:
        return "please click learn -> " + result[0]
