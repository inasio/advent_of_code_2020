from helpers.data_access import get_data
import numpy as np
from time import time


if __name__ == "__main__":

    data = get_data(day=2).split("\n")

    ### Part 1
    valid_ones = 0
    t0 = time()
    for line in data:
        nums, letter, password = line.split(" ")
        num_min, num_max = map(int, nums.split("-"))
        letter = letter[:-1]
        if num_min <= password.count(letter) <= num_max:
            valid_ones += 1
    print(f"num valid passwords: {valid_ones}")
    print(f"runtime {time()-t0:.4f} seconds")

    ### Part 2
    valid_ones = 0
    t0 = time()
    # data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]
    for line in data:
        nums, letter, password = line.split(" ")
        num_min, num_max = map(int, nums.split("-"))
        letter = letter[:-1]
        if (letter == password[num_min - 1]) + (letter == password[num_max - 1]) == 1:
            valid_ones += 1
    print(f"num valid passwords part 2: {valid_ones}")
    print(f"runtime {time()-t0:.4f} seconds")
