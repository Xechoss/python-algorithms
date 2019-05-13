def binary_search(a, x, n):
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if x == a[mid]:
            return mid
        if x > a[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    a = [int(i) for i in input().split()]
    x = int(input())
    m = binary_search(a, x, len(a))
    if m != -1:
        print(m + 1)
    else:
        print(0)


if __name__ == '__main__':
    main()
