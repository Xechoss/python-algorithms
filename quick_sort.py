import numpy as np


def quick_sort(a, start, end):
    if start < end:
        x = partition(a, start, end)
        quick_sort(a, start, x - 1)
        quick_sort(a, x + 1, end)


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
    quick_sort(a, 0, len(a) - 1)
    print(np.array(a))


if __name__ == '__main__':
    main()
