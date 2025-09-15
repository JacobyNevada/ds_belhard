import pandas as pd

from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

class Data_Trainer:
  def train_model(X, y):
    model = LogisticRegression(solver='lbfgs', max_iter=1000)
    model.fit(X, y)
    return model


  def predict(model, X):
    return model.predict(X)


  def evaluate_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    report = classification_report(y_true, y_pred)
    print(f"Accuracy: {accuracy:.2f}")
    print("\nClassification Report:")
    print(report)
