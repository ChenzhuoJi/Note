import numpy as np
from sklearn import preprocessing
data = np.array([[3, -1.5, 2, -5.4], [0, 4, -0.3, 2.1], [1, 3.3,
-1.9, -4.3]])
#均值移除
data_standardized=preprocessing.scale(data)
print("\nMean=",data_standardized.mean(axis=0))
print("Stddeviation=",data_standardized.std(axis=0))
data_scaler=preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled=data_scaler.fit_transform(data)
print("\nMin max scaled data=",data_scaled)