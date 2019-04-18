import random


def partition(a, p, q):
    x = a[q]
    i = p-1
    for j in range(p, q):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[q] = a[q], a[i+1]
    return i+1


def randomized_partition(a, p, r):
    i = random.randint(p, r)
    a[i], a[p] = a[p], a[i]
    return partition(a, p, r)


def randomized_select(a, p, r, k):
    if p == r:
        return a[p]
    i = randomized_partition(a, p, r)
    j = i-p+1
    if k <= j:
        return randomized_select(a, p, i, k)
    else:
        return randomized_select(a, i+1, r, k-j)


def main():
    a = [int(i) for i in input().split()]
    k = int(input())
    x = randomized_select(a, 0, len(a)-1, k)
    print(x)


if __name__ == '__main__':
    main()