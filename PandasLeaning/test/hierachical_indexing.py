# --utf-8--
import  pandas as pd
from pandas import Series, DataFrame
import numpy as np


data = Series(np.random.randn(10), index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],
                                          [1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
