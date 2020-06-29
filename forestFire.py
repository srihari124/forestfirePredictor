import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import warnings
import pickle
warnings.filterwarnings("ignore")

data = pd.read_csv("/home/srihari/COURSERA-ML/forestFire.csv")
data = np.array(data)

X = data[1:, 1:-1]
y = data[1:, -1]

X = X.astype('int')
y=y.astype('int')
# print(X,y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)
log_reg = LogisticRegression()


log_reg.fit(X_train, y_train)

pickle.dump(log_reg,open('model.pkl','wb'))


