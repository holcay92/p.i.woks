import numpy as np
import pandas as pd

dataset = pd.read_csv('piworks.csv')

dataset = pd.read_csv('piworks.csv')
X = dataset.iloc[:, :].values


from sklearn.impute import SimpleImputer
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
imputer.fit(X[:, 2:3])
X[:, 2:3] = imputer.transform(X[:, 2:3])
print(X)
