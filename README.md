# Classification_Phone_sensor_Data
Classification of a dataset collected by accelerometer and gyroscope in the mobile phone while performing a certain activity.

#### Use scrits for python 3  OR  Use .ipybn files for Jupyter Notebook


###To download dataset click [**here**](https://prithviai-my.sharepoint.com/:f:/g/personal/aakash_pandey_prithvi_ai/EhnIDiH1ExlKoje3P-9SpRYB3X5w_d0eFgWL3qWJrcEGnQ?e=fmAepS)  



Copy each to the working folder and download the dataset from above link and copy folder **accel** data from **Data/raw/train/phone**
 to a new folder called **Accl_data**
similarly copy **gyro** folder to a new folder called **Gyro_data**
 

copy **accel** data from **Data/raw/test/phone** to a new folder called **Accl_Test_data**
copy **gyro** data from **Data/raw/test/phone** to a new folder called **Gyro_Test_data**
 

copy **accel** data from **Data/val/phone** to a new folder called **Accl_Val_data**
copy **gyro** data from **Data/valphone** to a new folder called **Gyro_Val_data**


### select either the .ipybn files or the scripts (.ipybn files are prefered)
 1. cleaning-train
 2. cleaning-Test
 3. cleaning-Val-Data
 4. classify_Phonedata
 
 Run 1., 2. and 3. to get a cleaned csv files named Cleaned_Train_data and Cleaned_Test_data and Cleaned_Val_data in the working folder which will be used in 4.Classify_Phonedata to train and test and validate the selected classifier and to find the accuracy.

### Libraries used are:
Sklearn
xgboost
pandas
numpy
