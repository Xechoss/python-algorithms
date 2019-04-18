import numpy


def perm(a, k, m):
    if k == m:
        print(numpy.array(a))
    else:
        for i in range(k, m):
            a[k], a[i] = a[i], a[k]
            perm(a, k+1, m)
            a[k], a[i] = a[i], a[k]


def main():
    s = input().split()
    a = [int(i) for i in s]
    perm(a, 0, len(a))


if __name__ == '__main__':
    main()