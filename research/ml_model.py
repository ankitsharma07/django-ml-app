# import libraries
import json

import joblib
import numpy as np
import pandas as pd

from sklearn.ensemble import ExtraTreesClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder


class Model:
    def load_data(data_path):
        df = pd.read_csv(data_path)
        x_cols = [i for i in df.columns if i != "income"]

        # input matrix and target variable
        X = df[x_cols]
        y = df["income"]

        return X, y

    def split_data(X, y):
        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.3, random_state=1234
        )

    def preprocessing(X_train):
        pass


if __name__ == "__main__":
    pass
