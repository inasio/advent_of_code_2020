from helpers.data_access import get_data
import numpy as np
from time import time
import re


def check_byr(p_dict):
    return 1920 <= int(p_dict["byr"]) <= 2002


def check_iyr(p_dict):
    return 2010 <= int(p_dict["iyr"]) <= 2020


def check_eyr(p_dict):
    return 2020 <= int(p_dict["eyr"]) <= 2030


def check_hgt(p_dict):
    if p_dict["hgt"][-2:] == "cm":
        return 150 <= int(p_dict["hgt"][:-2]) <= 193
    elif p_dict["hgt"][-2:] == "in":
        return 59 <= int(p_dict["hgt"][:-2]) <= 76
    else:
        return False


def check_hcl(p_dict):
    if (len(p_dict["hcl"]) == 7) and (p_dict["hcl"][0] == "#"):
        try:
            int(p_dict["hcl"][1:], 16)
            return True
        except ValueError:
            return False
    else:
        return False


def check_ecl(p_dict):
    return p_dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]


def check_pid(p_dict):
    if len(p_dict["pid"]) == 9:
        try:
            int(p_dict["pid"])
            return True
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":

    data = get_data(day=4).split("\n\n")
    ### Part 1
    valid_passports = 0
    t0 = time()
    for line in data:
        a = re.split(" |\n", line)
        p_dict = {x.split(":")[0]: x.split(":")[1] for x in a}
        keys = p_dict.keys()
        if (len(keys) == 8) or (len(keys) == 7 and "cid" not in keys):
            valid_passports += 1
    print(f"valid passports: {valid_passports}")
    print(f"runtime {time()-t0:.4f} seconds")

    ### Part 2
    t0 = time()
    valid_passports = 0
    t0 = time()
    for line in data:
        a = re.split(" |\n", line)
        p_dict = {x.split(":")[0]: x.split(":")[1] for x in a}
        keys = p_dict.keys()
        if (len(keys) == 8) or (len(keys) == 7 and "cid" not in keys):
            if (
                check_byr(p_dict)
                + check_iyr(p_dict)
                + check_eyr(p_dict)
                + check_hgt(p_dict)
                + check_hcl(p_dict)
                + check_ecl(p_dict)
                + check_pid(p_dict)
            ) == 7:
                valid_passports += 1
    print(f"valid passports part 2: {valid_passports}")
    print(f"runtime {time()-t0:.4f} seconds")
