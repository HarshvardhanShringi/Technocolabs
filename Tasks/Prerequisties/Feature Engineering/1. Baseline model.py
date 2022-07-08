# importing libraries
from learntools.core import binder
binder.bind(globals())
from learntools.feature_engineering.ex1 import *
import pandas as pd

# initializing data
click_data = pd.read_csv('../input/feature-engineering-data/train_sample.csv',parse_dates=['click_time'])
click_data.head()

#label encoding
clicks = click_data.copy()
click_times = click_data['click_time']
clicks['day'] = clicks['click_time'].dt.day.astype('uint8')
# Fill in the rest
clicks['hour'] = click_times.dt.hour.astype('uint8')
clicks['minute'] = click_times.dt.minute.astype('uint8')
clicks['second'] = click_times.dt.second.astype('uint8')

# train, test and split
from sklearn import preprocessing

cat_features = ['ip', 'app', 'device', 'os', 'channel']
# Create new columns in clicks using preprocessing.LabelEncoder()
label_encoder = preprocessing.LabelEncoder()
for feature in cat_features:
    encoded = label_encoder.fit_transform(clicks[feature])
    clicks[feature + '_labels'] = encoded
clicks.head()



feature_cols = ['day', 'hour', 'minute', 'second', 
                'ip_labels', 'app_labels', 'device_labels',
                'os_labels', 'channel_labels']
valid_fraction = 0.1
clicks_srt = clicks.sort_values('click_time')
valid_rows = int(len(clicks_srt) * valid_fraction)
train = clicks_srt[:-valid_rows * 2]
# valid size == test size, last two sections of the data
valid = clicks_srt[-valid_rows * 2:-valid_rows]
test = clicks_srt[-valid_rows:]

# Train with LightGBM

import lightgbm as lgb

dtrain = lgb.Dataset(train[feature_cols], label=train['is_attributed'])
dvalid = lgb.Dataset(valid[feature_cols], label=valid['is_attributed'])
dtest = lgb.Dataset(test[feature_cols], label=test['is_attributed'])

param = {'num_leaves': 64, 'objective': 'binary'}
param['metric'] = 'auc'
num_round = 1000
bst = lgb.train(param, dtrain, num_round, valid_sets=[dvalid], early_stopping_rounds=10)


# Evaluate the model
from sklearn import metrics
ypred = bst.predict(test[feature_cols])
score = metrics.roc_auc_score(test['is_attributed'], ypred)
print(f"Test score: {score}")
