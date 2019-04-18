import numpy as np


def quickSort(a, start, end):
    if start < end:
        x = partition(a, start, end)
        quickSort(a, start, x - 1)
        quickSort(a, x + 1, end)


def partition(a, p, q):
    x = a[q]
    i = p - 1
    for j in range(p, q):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i + 1], a[q] = a[q], a[i + 1]
    print(x, i + 1)
    return i + 1


def main():
    a = [int(i) for i in input().split()]
    quickSort(a, 0, len(a) - 1)
    print(np.array(a))


if __name__ == '__main__':
    main()
