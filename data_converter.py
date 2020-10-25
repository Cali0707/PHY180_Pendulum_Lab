import numpy as np
import math


def convert_degrees_to_radians(file_to_load, file_to_write, x_err, y_err):
    deg = np.loadtxt(file_to_load, usecols=(0, 1), unpack=True)
    f = open(file_to_write, 'a')
    f.write('x y dx dy')
    for i in range(len(deg[0])):
        x = deg[0][i]
        y = math.radians(deg[1][i])
        s = str(x) + " " + str(y) + " " + str(x_err) + " " + str(y_err) + "\n"
        f.write(s)

    f.close()


if __name__ == '__main__':
    file_to_load = 'lab3_measurements.txt'
    file_to_write = 'lab3_in_radians.txt'
    x_err = 0.0167
    y_err = 0.00873
    convert_degrees_to_radians(file_to_load, file_to_write, x_err, y_err)


