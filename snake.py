from copy import deepcopy
from matplotlib import pyplot as plt
import numpy as np

from enum import Enum


class State(Enum):
    EMPTY = 0
    FULL = 1


def frozen(length, position_x, position_y, mymap):
    if length == 0:
        return 1

    path_count = 0

    new_position_x = position_x + 1
    new_position_y = position_y
    path_count += discover_direction(length, new_position_x, new_position_y, mymap)

    new_position_x = position_x - 1
    new_position_y = position_y
    path_count += discover_direction(length, new_position_x, new_position_y, mymap)

    new_position_x = position_x
    new_position_y = position_y + 1
    path_count += discover_direction(length, new_position_x, new_position_y, mymap)

    new_position_x = position_x
    new_position_y = position_y - 1
    path_count += discover_direction(length, new_position_x, new_position_y, mymap)

    return path_count


def discover_direction(length, position_x, position_y, mymap):
    if mymap[position_x, position_y] == 0 and position_y>=0 and position_x>=0:
        copy_map = deepcopy(mymap)
        copy_map[position_x, position_y] = 1
        plt.matshow(copy_map)
        plt.show(block=False)
        plt.pause(0.001)
        plt.close('all')
        path_count = frozen(length - 1, position_x, position_y, copy_map)
        return path_count
    return 0

n = 10
for i in range(8):
    mymap = np.zeros((n, n), dtype=int)
    mymap[0, 0] = 1
    answer = frozen(i, 0, 0, mymap)
    print(answer)
