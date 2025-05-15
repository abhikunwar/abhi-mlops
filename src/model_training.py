import pandas as pd
from sklearn.preprocessing import LabelEncoder
import config
from config import *
import os
from utils.common_functions import read_yml
from sklearn.model_selection import train_test_split
import lightgbm as lgb
from sklearn.metrics import accuracy_score, f1_score
import joblib
def training():
    mapping = {}
    config_yaml_file = read_yml('path_config.yaml')
    model_path = os.path.join(config_yaml_file['model_saving_path']['model_dir_path'],config_yaml_file['model_saving_path']['model_file_name'])

    data_file_path = os.path.join(config_yaml_file['data_path']['RAW_DIR_PATH'],config_yaml_file['data_path']['RAW_FILE_NAME'])
    df = pd.read_csv(data_file_path)
    cat_cols = config_yaml_file['cat_numerical_feature']['cat_cols']
    numerical_column = config_yaml_file['cat_numerical_feature']['num_cols']

    labelencoder = LabelEncoder()
    for col in cat_cols:
        df[col] = labelencoder.fit_transform(df[col])
        mapping[col] = {a: b for a,b in zip(labelencoder.classes_,labelencoder.transform(labelencoder.classes_))}

    X = df.drop(columns=['booking_status','Booking_ID'])
    print(X.columns)
    y = df["booking_status"]   
    X_train,X_test,y_train,y_test = train_test_split(X,y) 
    model = lgb.LGBMClassifier(random_state=42)
    model.fit(X_train,y_train)
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    model_file_name = config_yaml_file['model_saving_path']['model_file_name']
    model_file_name = os.path.join(model_path)
    joblib.dump(model,model_file_name )

if __name__=="__main__":
   training()    



   
    
    






   


