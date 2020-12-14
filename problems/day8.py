from helpers.data_access import get_data
from time import time
from copy import deepcopy


def run_instruction(data, current, acc):
    line = data[current]
    if line[1] == "nop":
        return line[0] + 1, acc
    elif line[1] == "acc":
        return line[0] + 1, acc + line[2]
    elif line[1] == "jmp":
        return line[0] + line[2], acc


def run_data_loop(data):
    seen_lines = [0]
    current, acc = 0, 0
    while True:
        current, acc = run_instruction(data, current, acc)
        if current in seen_lines:
            return current, acc
        if current == len(data) - 1:
            if data[current][1] == "acc":
                acc += data[current][2]
            return current, acc
        seen_lines.append(current)


if __name__ == "__main__":

    data = get_data(day=8).split("\n")
    ### Part 1
    t0 = time()
    data = [x.split() for x in data]
    data = [[i, x[0], int(x[1])] for i, x in enumerate(data)]
    current, acc = run_data_loop(data)
    print(f"first line to repeat itself {current}, value of accumulator {acc}")
    print(f"runtime {time()-t0:.4f} seconds")

    ### Part 2
    t0 = time()
    current, acc = 0, 0
    for i, line in enumerate(data):
        if line[1] == "nop":
            data_mod = deepcopy(data)
            data_mod[line[0]][1] = "jmp"
            current, acc = run_data_loop(data_mod)
        elif line[1] == "jmp":
            data_mod = deepcopy(data)
            data_mod[line[0]][1] = "nop"
            current, acc = run_data_loop(data_mod)
        if current == len(data) - 1:
            break
    print(f"program bug was in line {i}, value of accumulator {acc}")
    print(f"runtime {time()-t0:.4f} seconds")