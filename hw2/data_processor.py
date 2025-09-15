import pandas as pd

from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

class Data_Processor:

  def data_processing(dataset, category, numeric_features, categorical_features):
    X = dataset.drop(columns=[category])
    y = dataset[category]

    # Создание препроцессора
    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder(drop='first')

    preprocessor = ColumnTransformer(
      transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    # Применение препроцессора к данным
    X_processed = preprocessor.fit_transform(X)
    return X_processed, y, preprocessor
