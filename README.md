# Skin Cancer Detection

# Run:
Install libraries in the requirements.txt then open Application directory and simply run Application.py
# Test:
Open Application directory and run test.py to test if all module work well

# Objective:
Build an application that detects skin cancer using AI. Bases on results, recommend nearby dermatoligists (if postive) or general practicioner (if negative). The application also provides video results based on the results to educate the user.

# Motivation:
1. Skin cancer is the most common type of cancer. About 1 in 5 Americans will be diagnosed with skin cancer in their lifetime.
2. Out of the skin cancers, melanoma constitutes about 75% of the deaths. About 1 person dies of melanoma every hour. It is the second most common form of cancer for young people aged 15 - 29
3. In 2019, new melanoma cases will increase by 7.7% and an estimated 7,230 people will die of melanoma!
4. However, skin cancer is curable if detected early.
5. Survival rate is 98% when detected early and drops to 23% when it metastasizes.
6. Some of the bottlenecks in traditional detection includes getting a doctor's appointment, waiting period, getting and waiting for the test results etc. Every moment of delay could be fatal.
7. Treated 30 to 59 days after biopsy - 5% higher risk of dying. Treated 119 days after biopsy - 41% higher risk.
8. Technology promises to accelerate skin cancer detection.

# User Story:
1. As a user, I would want to be able to take pictures of skin lesion.
2. As a user, I would want to know if the lesion is cancerous.
3. As a user, I would want the results to be fast. 
4. As a user, I want to ensure the privacy of the images.
5. As a user, I would want to be recommended to nearby dermatoligists or general practioner.
6. As a user, I would want to be educated on the results of the detected skin lesion.
7. As a user, I would want to keep a track of the images uploaded.

# Proposed Prototype:

<img width="615" alt="Screen Shot 2019-03-22 at 9 17 19 PM" src="https://user-images.githubusercontent.com/43215312/54859796-eedb0c00-4ce7-11e9-8778-d83419689505.png">

## Sprint 1:
* Build Project Architecture.
![Aechitecture](https://user-images.githubusercontent.com/43215312/54940724-b31b8e80-4f01-11e9-8072-d7053f437443.png)

* Decide Project tools and coding language.
* Set up project enviroment.
* Research and Plan.

## Sprint2:
* Started working On AI Module
Technology Used - Mobilenet
 ### Tested a machine learning model:

  Data Set used for Testing - https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000

  Model used for Testing - https://www.kaggle.com/kmader/skin-cancer-mnist-ham10000

  #### Block Diagram:
<img width="655" alt="Screen Shot 2019-03-25 at 1 03 01 PM" src="https://user-images.githubusercontent.com/43215312/54939450-03452180-4eff-11e9-837d-6610d17e14c4.png">

  #### Results:
  <img width="1154" alt="Screen Shot 2019-03-25 at 1 12 22 PM" src="https://user-images.githubusercontent.com/43215312/54939726-ac8c1780-4eff-11e9-9a09-83a5fff982b8.png">

<img width="349" alt="Screen Shot 2019-03-17 at 9 16 16 PM" src="https://user-images.githubusercontent.com/43215312/54940936-1c030680-4f02-11e9-8c60-51b65cc25116.png">

* Started working on UI Module:
Technology Used - Kivy

![EBKP{{78FXHJWZOQ %OPH03](https://user-images.githubusercontent.com/43215312/54941507-62a53080-4f03-11e9-9ae1-3b0fa38db3c8.png)

![Y471%WK_I(()XS 1N2WIZFX](https://user-images.githubusercontent.com/43215312/54941508-633dc700-4f03-11e9-83fe-fe8d837703c8.png)


## Sprint3:
* Challenges with loading the mobilenet model:
The trained model has good accuracy, however, throws errors when loading the model to predict a single image. The errors as shows in files Restore using .pb.ipynb and Restore using tf keras load (.h5 model).ipynb	seem to have errors that point to open github issues: https://github.com/keras-team/keras/issues/12588 

Hence we decided to build another model using Convolution Neural Network with keras tensorflow in backend. The new model however, seems to overfit the data. We are working on tuning it to fit the data in general.

We trained model using resnet50 which has an accuracy of 86% and fits the test data well. However, the model seems to be too slow in predicting the results.


* Converted the keras .h5 model to tensorflow lite:
We used tflite_converter to convert the keras model to tflite to be used in an andorid phone.


* Challenges with kivy:
kivy seemed to be an ideal choice for creating python based modules to use across various platforms. However, we faced challenges in converting the modules into android apk. We now built an application using andorid studio. The application uses the tflite model generated in the previous step to detect skin cancer lesions.




