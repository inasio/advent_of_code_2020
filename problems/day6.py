from helpers.data_access import get_data
import numpy as np
from time import time

if __name__ == "__main__":

    data = get_data(day=6).split("\n\n")
    ### Part 1
    t0 = time()
    total_sum = 0
    for line in data:
        line = line.replace("\n", "")
        num_answers = len(set(line))
        total_sum += num_answers
    print(f"total sum = {total_sum}")
    ### Part 2
    t0 = time()
    total_sum = 0
    for line in data:
        group_data = line.split("\n")
        group_data_sets = list(map(set, group_data))
        num_common_answers = len(set.intersection(*group_data_sets))
        total_sum += num_common_answers
    print(f"total sum common answers = {total_sum}")
