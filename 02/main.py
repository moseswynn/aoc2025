from functools import reduce
from itertools import batched
def parse_input():
    with open("input.txt") as f:
        data = f.read()
    data = [r.split("-") for r in data.split(",")]
    return data

def find_factors(n):
    out =  list(set(reduce(
        list.__add__,
        ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
    out.sort()
    return out

def check_range(start, stop):
    for i in range(int(start), int(stop)+1):
        length = len(str(i))
        factors = find_factors(length)
        for factor in factors:
            if factor == length:
                continue
            batches = list(batched(str(i), factor))
            if batches.count(batches[0]) == len(batches):
                yield i
                print(i)
                break

def main():
    bad_values = []
    ranges = parse_input()
    for rng in ranges:
        bad_values.extend(list(check_range(*rng)))
    output = sum(bad_values)
    with open("output.txt", "w+") as f:
        f.write(str(output))

if __name__ == "__main__":
    main()