import pandas as pd
import numpy as np

pd.set_option("display.max_columns",500)

csv_data = pd.read_csv("../_data/StudentsPerformance.csv")

print(csv_data.columns)