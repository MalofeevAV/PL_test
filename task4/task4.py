import sys

file = sys.argv[1:][0]

with open(file, "r") as f:
    numbers = list(map(int, f.read().splitlines()))


def amount_of_moves(numbers):
    min_value = float("inf")
    for i in range(len(numbers)):
        tmp, min = numbers[i], 0
        for num in numbers:
            min += abs(tmp - num)
        if min < min_value:
            min_value = min
    return min_value


if __name__ == "__main__":
    print(amount_of_moves(numbers), sep="\n")