import pandas as pd

class Data_Informer:
  def show_dataset(dataset):
    print(f"\nDataset head:\n{dataset}\n")


  def show_info(dataset):
    print(f"\nDataset info:\n{dataset.info()}\n")


  def show_describe(dataset):
    print(f"\nDataset describe:\n{dataset.describe()}\n")


  def show_types(dataset):
    print(f"\nDataset types:\n{dataset.dtypes}\n")


  def show_null_values(dataset):
    print(f"\nDataset null values:\n{dataset.isnull().sum()}\n")


  def show_nan_values(dataset):
    print(f"\nDataset NaN values:\n{dataset.isna().sum()}\n")


  def show_all_info(dataset):
    show_dataset(dataset)
    show_info(dataset)
    show_describe(dataset)
    show_types(dataset)
    show_null_values(dataset)
    show_nan_values(dataset)
