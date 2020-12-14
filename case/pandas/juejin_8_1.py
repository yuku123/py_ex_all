import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_stockload = pd.read_csv("../../_data/juejin_8_1.csv")
df_stockload.set_index(["Date"], inplace=True)

'''
得到所有列
'''
print(df_stockload.columns)
print(df_stockload.loc['2018-01-02',['High','Volume']])

print(df_stockload.head(10))

df_stockload.High.plot(c='b')

plt.legend(['Close','30ave','60ave'],loc='best')
plt.show()
