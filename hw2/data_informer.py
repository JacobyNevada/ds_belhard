import pandas as pd

class Data_Informer:
  @staticmethod
  def show_dataset(dataset):
    print(f"\nDataset head:\n{dataset}\n")

  @staticmethod
  def show_info(dataset):
    print(f"\nDataset info:\n{dataset.info()}\n")

  @staticmethod
  def show_describe(dataset):
    print(f"\nDataset describe:\n{dataset.describe()}\n")

  @staticmethod
  def show_types(dataset):
    print(f"\nDataset types:\n{dataset.dtypes}\n")

  @staticmethod
  def show_null_values(dataset):
    print(f"\nDataset null values:\n{dataset.isnull().sum()}\n")

  @staticmethod
  def show_nan_values(dataset):
    print(f"\nDataset NaN values:\n{dataset.isna().sum()}\n")

  @staticmethod
  def show_all_info(dataset):
    Data_Informer.show_dataset(dataset)
    Data_Informer.show_info(dataset)
    Data_Informer.show_describe(dataset)
    Data_Informer.show_types(dataset)
    Data_Informer.show_null_values(dataset)
    Data_Informer.show_nan_values(dataset)
