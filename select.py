def partition(a, p, q, x):
    i = p-1
    for j in range(p, q):
        if a[j] <= x:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1], a[q] = a[q], a[i+1]
    return i+1


def select(a, p, r, k):
    if r-p < 50:
        a.sort()
        return a[p+k-1]
    for i in range((r-p-4)//5+1):
        x = select(a, p, p+(r-p-4)//5, (r-p-4)//10)
        i = partition(a, p, r, x)
        j = i-p+1
        if k <= j:
            return select(a, p, i, k)
        else:
            return select(a, i+1, r, k-j)


def main():
    a = [int(i) for i in input().split()]
    k = int(input())
    x = select(a, 0, len(a)-1, k)
    print(x)


if __name__ == '__main__':
    main()