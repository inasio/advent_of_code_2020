from helpers.data_access import get_data
from time import time
from itertools import combinations


def get_all_sums(data_subset):
    all_pairs = combinations(data_subset, 2)
    all_sums = set([sum(x) for x in all_pairs])
    return all_sums


if __name__ == "__main__":

    data = list(map(int, get_data(day=9).split("\n")))
    ### Part 1
    t0 = time()
    preamble_len = 25
    all_sums = get_all_sums(data[:preamble_len])
    dataset_len = len(data)
    for i in range(1, dataset_len - preamble_len):
        all_sums = get_all_sums(data[i : i + preamble_len])
        if data[i + preamble_len] not in all_sums:
            break

    n_sol = data[i + preamble_len]
    print(
        f"first num not part of sum of prev. {preamble_len}: {n_sol}"
        + f", index {i+preamble_len}"
    )
    print(f"runtime {time()-t0:.4f} seconds")

    ### Part 1
    t0 = time()
    low_ix, high_ix = 0, 1
    while True:
        sum_interval = sum(data[low_ix:high_ix])
        if sum_interval == n_sol:
            break
        elif sum_interval < n_sol:
            high_ix += 1
        elif sum_interval > n_sol:
            low_ix += 1
            high_ix = low_ix + 1

    min_from_interval = min(data[low_ix:high_ix])
    max_from_interval = max(data[low_ix:high_ix])
    print(
        f"min from cont. sum {min_from_interval}, max from cont. sum {max_from_interval}\n"
        + f"sum from both extremes: {min_from_interval+max_from_interval}"
    )
