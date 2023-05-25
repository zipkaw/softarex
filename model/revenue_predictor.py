
import numpy as np
import pandas as pd

from sklearn.neighbors import KNeighborsClassifier

from sklearn.model_selection import KFold

from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import mean_absolute_error

from .kn_model import Model1KNN
from .lgb_model import Model1lgb
from .rr_model import Model1RF
from .lin_model import Model2Linear

def prepare_test_data(test):
    df_test = pd.read_csv(test)

    df_all = pd.concat([df_test],axis=0)
    df_all['Open Date'] = pd.to_datetime(df_all["Open Date"])
    df_all['Year'] = df_all['Open Date'].apply(lambda x:x.year)
    df_all['Month'] = df_all['Open Date'].apply(lambda x:x.month)
    df_all['Day'] = df_all['Open Date'].apply(lambda x:x.day)
    df_all['week_name'] = df_all['Open Date'].apply(lambda x:x.day_name())

    le = LabelEncoder()
    df_all['City'] = le.fit_transform(df_all['City'])
    df_all['City Group'] = df_all['City Group'].map({'Other':0,'Big Cities':1}) #There are only 'Other' or 'Big city'
    df_all["Type"] = df_all["Type"].map({"FC":0, "IL":1, "DT":2, "MB":3}) #There are only 'FC' or 'IL' or 'DT' or 'MB'
    df_all["week_name"] = df_all["week_name"].map({"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}) #There are only 'FC' or 'IL' or 'DT' or 'MB'
    df_test = df_all
    df_train_col = [col for col in df_test.columns if col not in ['Id','Open Date']]
    df_test = df_test[df_train_col]
    return df_test

def prepare_train_data(train):
    df_trainval = pd.read_csv(train)

    y_trainval = df_trainval['revenue']
    del df_trainval['revenue']

    df_all = pd.concat([df_trainval],axis=0)
    df_all['Open Date'] = pd.to_datetime(df_all["Open Date"])
    df_all['Year'] = df_all['Open Date'].apply(lambda x:x.year)
    df_all['Month'] = df_all['Open Date'].apply(lambda x:x.month)
    df_all['Day'] = df_all['Open Date'].apply(lambda x:x.day)
    df_all['week_name'] = df_all['Open Date'].apply(lambda x:x.day_name())

    le = LabelEncoder()
    df_all['City'] = le.fit_transform(df_all['City'])
    df_all['City Group'] = df_all['City Group'].map({'Other':0,'Big Cities':1}) #There are only 'Other' or 'Big city'
    df_all["Type"] = df_all["Type"].map({"FC":0, "IL":1, "DT":2, "MB":3}) #There are only 'FC' or 'IL' or 'DT' or 'MB'
    df_all["week_name"] = df_all["week_name"].map({"Sunday":0, "Monday":1, "Tuesday":2, "Wednesday":3,"Thursday":4,"Friday":5,"Saturday":6}) #There are only 'FC' or 'IL' or 'DT' or 'MB'

    df_trainval = df_all.iloc[:df_trainval.shape[0]]
    df_train_col = [col for col in df_trainval.columns if col not in ['Id','Open Date']]
    df_trainval = df_trainval[df_train_col]

    return df_trainval, y_trainval

def train_model_and_predict(model, train_x, train_y):
    preds = []
    va_idxes = []

    kf = KFold(n_splits=4, shuffle=True, random_state=10)

    for i, (tr_idx, va_idx) in enumerate(kf.split(train_x)):
        tr_x, va_x = train_x.iloc[tr_idx], train_x.iloc[va_idx]
        tr_y, va_y = train_y.iloc[tr_idx], train_y.iloc[va_idx]
        model.fit(tr_x, tr_y, va_x, va_y)
        pred = model.predict(va_x)
        preds.append(pred)
        va_idxes.append(va_idx)

    va_idxes = np.concatenate(va_idxes)
    preds = np.concatenate(preds, axis=0)
    order = np.argsort(va_idxes)
    pred_train = preds[order]

    return pred_train

def predict(model, test_x):
    return model.predict(test_x)

def fitting_models(models:dict, df_trainval, y_trainval):
    predict_train = []
    lin = models.pop('Linear')
    for model in models.values():
        predict_train.append(train_model_and_predict(model, df_trainval, y_trainval))
    pred_dict = {}
    for i, sublists in enumerate(predict_train, start=1):
        pred_dict[i] = sublists

    train_x_2 = pd.DataFrame(pred_dict)
    train_model_and_predict(lin, train_x_2, y_trainval)
    return lin 

def predict_revenue(final_regressor, models:dict, df_test):
    predict_test = []
    
    for model in models.values():
        predict_test.append(predict(model, df_test))
    pred_dict = {}
    for i, sublists in enumerate(predict_test, start=1):
        pred_dict[i] = sublists

    test_x_2 = pd.DataFrame(pred_dict)
    return predict(final_regressor, test_x_2)

def save_to_csv(prediction, filename):
    submission = pd.DataFrame({'Prediction':prediction})
    return submission.to_csv(filename,index=True) 