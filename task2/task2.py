import sys

file1, file2 = sys.argv[1:]


def file_reader(file):
    with open(file, "r") as f:
        data = [list(map(float, line.strip().split())) for line in f]
    return data


def pifagor(x, y, circle_x, circle_y, radius):
    hypotenuse = ((x - circle_x)**2 + (y - circle_y)**2)**0.5
    return (1, 2, 0)[(hypotenuse > radius) + (hypotenuse == radius)*2]


if __name__ == "__main__":
    file1_data = file_reader(file1)
    file2_data = file_reader(file2)

    circle_x, circle_y, radius = file1_data[0][0], file1_data[0][1], file1_data[1][0]

    for x, y in file2_data:
        print(pifagor(x, y, circle_x, circle_y, radius), sep="\n")
