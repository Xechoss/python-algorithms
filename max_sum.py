def max_sum(n, a):
    best_sum = 0
    for i in range(n):
        this_sum = 0
        for j in range(i, n):
            this_sum += a[j]
            if this_sum > best_sum:
                best_sum = this_sum
    return best_sum


def main():
    a = [int(i) for i in input().split()]
    s = max_sum(len(a), a)
    print(s)


if __name__ == '__main__':
    main()