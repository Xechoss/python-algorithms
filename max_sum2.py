def max_sum(n, a):
    best_sum = 0
    s = 0
    for i in range(n):
        if s > 0:
            s = s+a[i]
        else:
            s = a[i]
            left = i+1
        if s > best_sum:
            best_sum = s
            right = i+1
    return left, right, best_sum


def main():
    a = [int(i) for i in input().split()]
    l, r, s = max_sum(len(a), a)
    print(s)
    print(l)
    print(r)


if __name__ == '__main__':
    main()