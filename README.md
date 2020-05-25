# Classification_Phone_sensor_Data
Classification of a dataset collected by accelerometer and gyroscope in the mobile phone while performing a certain activity.

##### Use scrits for python 3  OR  Use .ipybn files for Jupyter Notebook


### To download dataset click [**here**](https://prithviai-my.sharepoint.com/:f:/g/personal/aakash_pandey_prithvi_ai/EhnIDiH1ExlKoje3P-9SpRYB3X5w_d0eFgWL3qWJrcEGnQ?e=fmAepS)  



## Introduction

I have done classification for just data recorded by sensors on phone but same logic can be applied and watch data
 can also be appended with respective phone data and can be further classified using same model. This model will then 
 work to classify the activity being done by taking all the 2 senator's data from each phone and the watch.


Download the dataset from above link and copy folder **"accel"** from **Data/raw/train/phone**
 to a new folder called **"Accl_data"**
similarly copy **gyro** folder to a new folder called **"Gyro_data"**
 

copy **accel** from **Data/raw/test/phone** to a new folder called **"Accl_Test_data"**
copy **gyro** from **Data/raw/test/phone** to a new folder called **"Gyro_Test_data"**
 

copy **"accel"** from **Data/val/phone** to a new folder called **"Accl_Val_data"**
copy **"gyro"** from **Data/valphone** to a new folder called **"Gyro_Val_data"**


### select either the .ipybn files or the scripts (.ipybn files are prefered)
 1. cleaning-train
 2. cleaning-Test
 3. cleaning-Val-Data
 4. classify_Phonedata
 
 Run 1., 2. and 3. to get cleaned csv files named Cleaned_Train_data and Cleaned_Test_data and Cleaned_Val_data in the working folder which will be used in 4.Classify_Phonedata to train and test and validate the selected classifier and to find the accuracy.

### Libraries used are:
Sklearn, 
xgboost, 
pandas, 
numpy

### Classifier
Used **XGBClassifier** from XGBoost to reduce the time for classification since the sample size is very large.
