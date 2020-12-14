# --utf-8--
import pandas as pd
from pandas import Series, DataFrame
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('/Users/zifang/workplace/pycharm_workplace/py_ex_all/_data/StudentsPerformance.csv')

graph1=data.groupby(['test preparation course']).size()

