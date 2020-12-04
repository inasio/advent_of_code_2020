from helpers.data_access import get_data
import numpy as np
from time import time


if __name__ == "__main__":

    data = get_data(day=3).split("\n")
    width = len(data[0])
    ### Part 1
    t0 = time()
    num_trees = 0
    index = 0
    h_skip, v_skip = 3, 1
    for i, line in enumerate(data):
        if i % v_skip == 0:
            if line[index % width] == "#":
                num_trees += 1
            index += h_skip
    print(f"num trees ran into: {num_trees}")
    print(f"runtime {time()-t0:.4f} seconds")

    ### Part 2
    num_total = 1
    index = 0
    h_v_tuples = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    for h_skip, v_skip in h_v_tuples:
        index = 0
        num_trees = 0
        for i, line in enumerate(data):
            if i % v_skip == 0:
                if line[index % width] == "#":
                    num_trees += 1
                index += h_skip
        num_total *= num_trees
    print(f"num trees ran into part 2: {num_total}")
    print(f"runtime {time()-t0:.4f} seconds")

