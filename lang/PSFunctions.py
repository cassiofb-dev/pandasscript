import pandas as pd
import matplotlib.pyplot as plt

def load(file_path):
  data = pd.read_csv(file_path)
  # data.info()
  return data

def save(data, file_path):
  if isinstance(data, pd.DataFrame):
    if file_path != None:
      return data.to_csv(file_path)
  else:
    print("ERROR: Only data can be saved!")

def select_from(column, row, data):
  if not isinstance(data, (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can be selected from!")
  if column == None and row == None:
    return data
  elif column == None and row != None:
    return data.loc[row, :]
  elif column != None and row == None:
    return data.loc[:, column]
  else:
    return data.loc[row, column]

def mean(data):
  if not isinstance(data, (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can have mean!")
  return data.mean()

def median(data):
  if not isinstance(data, (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can have median!")
  return data.median()

def std(data):
  if not isinstance(data, (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can have standart deviation!")
  return data.std()

def columns(data):
  if not isinstance(data, (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can have columns!")
  return data.columns.to_series()

def cut(start, end, data, vertical=0):
  if not isinstance(data, (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can have something to cut!")
  if vertical == 1:
    return data.iloc[:, start:end]
  return data.iloc[start:end]

def plot(series, title):
  if not isinstance(series,  (pd.DataFrame, pd.Series)):
    return print("ERROR: Only data can be plotted!")

  x = series.columns.to_numpy()
  y = series.iloc[0].to_numpy()
  plt.figure(figsize=(8, 5))
  plt.plot(x, y)
  plt.title(title)
  plt.savefig(f"{title}.png")
  return 0