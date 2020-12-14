from helpers.data_access import get_data
from time import time
import numpy as np
from collections import Counter


def get_cluster_sizes(diff):
    cluster_size = 0
    cluster_sizes = {}
    for i in diff:
        if i == 3:
            cluster_sizes[cluster_size] += 1


if __name__ == "__main__":

    data = list(map(int, get_data(day=10).split("\n")))
    ### Part 1
    t0 = time()
    sorted_data = [0] + sorted(data) + [max(data) + 3]
    diff = np.diff(sorted_data)
    counts = Counter(diff)
    print(
        f"1-jolt diffs: {counts[1]}, 3-jolt diffs: {counts[3]},"
        + f" prod = {counts[1]*counts[3]}"
    )
    print(f"runtime {time()-t0:.4f} seconds")

    ### Part 2
    t0 = time()
    # based on the size of a cluster of 1s (say 311113 is size 4), number of independent
    # solutions. Total possible solutions are the product of the number of independent
    # solutions per cluster
    sols_per_cluster_size = {2: 2, 3: 4, 4: 7}
    str_diff = "".join(str(x) for x in diff)
    cluster_sizes = [len(x) for x in str_diff.split("3")]
    cluster_counts = Counter(cluster_sizes)
    total_sols = 1
    for cluster_size in [2, 3, 4]:
        total_sols *= (
            sols_per_cluster_size[cluster_size] ** cluster_counts[cluster_size]
        )
    print(f"total number of solutions {total_sols}")
    print(f"runtime {time()-t0:.4f} seconds")