# -- coding: utf-8 --

import matplotlib.pyplot as plt

from random_walk.b.a import Randomwalk

while True:
    rw = Randomwalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_point))
    plt.scatter(rw.x_value,rw.y_value,c=point_numbers,edgecolors = 'none',s=1)
    #plt.figure(figsize=(10,6))
    plt.show()
    #如果是2.7，则将input 替换为raw_input
    keep_runing = input("Make another walk?(y/n)")
    if keep_runing == 'n':
        break