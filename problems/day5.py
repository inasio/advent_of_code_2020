from helpers.data_access import get_data
import numpy as np
from time import time


def find_row(x):
    line = x[:7]
    row = 127
    mod = 64
    for lett in line:
        if lett == "F":
            row -= mod
        mod /= 2
    return row


def find_col(x):
    line = x[-3:]
    col = 7
    mod = 4
    for lett in line:
        if lett == "L":
            col -= mod
        mod /= 2
    return col


if __name__ == "__main__":

    data = get_data(day=5).split("\n")
    ### Part 1
    t0 = time()
    max_id = 0
    for x in data:
        row = find_row(x)
        col = find_col(x)
        seat_id = row * 8 + col
        if seat_id > max_id:
            max_id = seat_id
    print(f"max seat id = {max_id}")

    ### Part 2
    t0 = time()
    all_ids = []
    for x in data:
        row = find_row(x)
        col = find_col(x)
        seat_id = row * 8 + col
        all_ids.append(seat_id)
    sorted_ids = sorted(all_ids)
    for i, id in enumerate(sorted_ids[1:-1]):
        if id - sorted_ids[i] > 1:
            print(id - 1)

