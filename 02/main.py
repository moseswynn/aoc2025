def parse_input():
    with open("input.txt") as f:
        data = f.read()
    data = [r.split("-") for r in data.split(",")]
    return data

def check_range(start, stop):
    for i in range(int(start), int(stop)+1):
        if (l := len(str(i))) % 2 == 0:
            split_index = int(l/2)
            if str(i)[:split_index] == str(i)[split_index:]:
                yield i

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