file_to_load = 'data_in_degrees'
file_to_write = 'test_data.txt'

import numpy as np
import math

deg = np.loadtxt(file_to_load, usecols=0, skiprows=1, unpack=True)

f = open(file_to_write, 'a')
f.write('x y dx dy')
i = 0
t = 0
for num in deg:
    y = math.radians(num)
    s = str(t) + " " + str(y) + " 0.0167 0.00873\n"
    f.write(s)
    t += 1.4167


f.close()
