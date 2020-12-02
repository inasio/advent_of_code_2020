from helpers.data_access import get_data
import numpy as np
from time import time


def two_adders(data, target):
    sorted_array = np.array(sorted(data))
    for i, n in enumerate(sorted_array):
        for m in sorted_array[sorted_array <= (target - n)][i + 1 :]:
            if n + m == target:
                return n, m


def three_adders(data, target):
    sorted_array = np.array(sorted(data))
    for i, n in enumerate(sorted_array):
        for j, m in enumerate(sorted_array[sorted_array <= (target - n)][i + 1 :]):
            for p in sorted_array[sorted_array <= (target - n - m)][i + j + 2 :]:
                if n + m + p == target:
                    return n, m, p


if __name__ == "__main__":

    data = list(map(int, get_data(day=1).split("\n")))
    t0 = time()
    n, m = two_adders(data, 2020)
    print(f"adders {n}, {m}, multiply to {n*m}")
    print(f"runtime {time()-t0:.4f} seconds")

    t0 = time()
    n, m, p = three_adders(data, 2020)
    print(f"adders {n}, {m}, {p}, multiply to {n*m*p}")
    print(f"runtime {time()-t0:.4f} seconds")
