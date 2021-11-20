import sys

n, m = map(int, sys.argv[1:])


def path_through_array(n, m):
    if n:
        arr = [el for el in range(1, n + 1)]
        start, end = 0, m - 1
        answer = arr[:1]

        while arr[0] != arr[end % n]:
            start, end = end, (end + (m - 1)) % n
            answer.append(arr[start % n])
        return answer
    return []


if __name__ == "__main__":
    print("".join(map(str, path_through_array(n, m))), sep="\n")
