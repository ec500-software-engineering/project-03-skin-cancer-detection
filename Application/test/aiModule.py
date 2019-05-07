from keras.models import load_model
from keras.preprocessing import image
import numpy as np

import  tensorflow  as tf
    
def test(test):
    img_width, img_height = 75,100  #224,224 # 180, 135 #75,100
    results = ['nv','mel','bkl','bcc','akiec','vasc','df']
    lesion_type_dict = {
    'nv': 'Melanocytic Nevi',
    'mel': 'Melanoma',
    'bkl': 'Benign Keratosis ',
    'bcc': 'Basal Cell Carcinoma',
    'akiec': 'Actinic Keratoses',
    'vasc': 'Vascular Skin Lesions',
    'df': 'Dermatofibroma'
    }
    
    # load the model we saved
    #custom_objects={"categorical_accuracy": categorical_accuracy,'top_2_accuracy': top_2_accuracy,'top_3_accuracy':top_3_accuracy}
    model = tf.keras.models.load_model('cnn_model.h5')
    # model.compile(loss='binary_crossentropy',
    #               optimizer='rmsprop',
    #               metrics=['accuracy'])

    # predicting images
    img = image.load_img(test, target_size=(img_width, img_height))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)

    images = np.vstack([x])
    y_prob = model.predict(images)
    y_classes = y_prob.argmax(axis=-1)
    cl = results[y_classes[0]]
    return (lesion_type_dict[cl], y_prob[0][y_classes[0]])
