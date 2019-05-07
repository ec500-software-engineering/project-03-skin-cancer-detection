import random

skin_cancer_names = ["Actinic Keratoses", "Basal Cell Carcinoma",
                     "Benign Keratosis", "Dermatofibroma",
                     "Melanocytic Nevi","Melanoma","Vascular Skin Lesions"]


def test(filepath):
    return (random.choice(skin_cancer_names), round(random.random(),2))
