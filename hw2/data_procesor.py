import pandas as pd
from google.colab import drive
import os

class Data_Loader:

  def data_loading(file_link, category, numeric_features, categorical_features):
    try:
      drive.mount('/content/drive')
      file_path = f"/content/drive/{file_link}"

      # Загрузка CSV файла
      dataset = pd.read_csv(file_path)
       
      if not os.path.exists(file_path):
        raise FileNotFoundError(f"Файл {file_path} не найден")
             
      # Проверяем, что файл не пустой
      if os.path.getsize(file_path) == 0:
        raise ValueError(f"Файл {file_path} пустой")

      imputer = SimpleImputer(strategy='mean')

      # Выбираем только числовые колонки для импутации
      numeric_columns = numeric_features + [category]

      # Применяем импутер
      dataset[numeric_columns] = imputer.fit_transform(dataset[numeric_columns])

      imputer = SimpleImputer(strategy='most_frequent')

      # Применяем к строковым колонкам
      string_columns = categorical_features
      dataset[string_columns] = imputer.fit_transform(dataset[string_columns])

      return dataset[numeric_features + categorical_features + [category]]

    except FileNotFoundError as e:
      print(f"Ошибка: {e}")
      print("Проверьте наличие файла в Google Drive")
      return None
            
    except ValueError as e:
      print(f"Ошибка данных: {e}")
      return None
            
    except Exception as e:
      print(f"Неожиданная ошибка: {e}")
      return None
