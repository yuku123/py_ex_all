# -- utf-8--
import numpy as np
import matplotlib.pyplot as plt

arr=np.loadtxt("../test.csv",delimiter='\t',dtype='string_')
print(str(arr))

arr_distinct=np.unique(arr)
print(arr_distinct.size)
print(str(arr_distinct))
#np.savetxt("../test_distinct.csv",arr_distinct,delimiter=',')