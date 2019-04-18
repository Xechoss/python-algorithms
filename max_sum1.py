def max_sum(a, left, right):
    x = 0
    y = 0
    if left == right:
        best_sum = a[left] if a[left] > 0 else 0
    else:
        mid = (left + right) // 2
        x, y, left_sum = max_sum(a, left, mid)
        x, y, right_sum = max_sum(a, mid+1, right)
        s1 = 0
        best_left = 0
        for i in range(mid, left-1, -1):
            best_left += a[i]
            if best_left > s1:
                s1 = best_left
                x = i+1
        s2 = 0
        best_right = 0
        for i in range(mid+1, right+1):
            best_right += a[i]
            if best_right > s2:
                s2 = best_right
                y = i+1
        best_sum = s1 + s2
        if best_sum < left_sum:
            best_sum = left_sum
        if best_sum < right_sum:
            best_sum = right_sum
    return x, y, best_sum


def main():
    a = [int(i) for i in input().split()]
    left, right, s = max_sum(a, 0, len(a)-1)
    print(s)
    print(left)
    print(right)


if __name__ == '__main__':
    main()
