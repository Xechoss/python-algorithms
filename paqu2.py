import numpy as np


def Merge(SR, TR, i, m, n):
    j = m + 1
    k = i
    while i <= m and j <= n:
        if (SR[i] < SR[j]):
            TR[k] = SR[i]
            i = i + 1
        else:
            TR[k] = SR[j]
            j = j + 1
        k = k + 1
    if i <= m:
        a = 0
        for l in range(0, m - i + 1):
            TR[k + a] = SR[i + a]
            a = a + 1
    if j <= n:
        a = 0
        for l in range(0, n - j + 1):
            TR[k + a] = SR[j + a]
            a = a + 1


def MSort(SR, TR1, s, t):
    TR2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    if s == t:
        TR1[s] = SR[s]
    else:
        m = int((s + t) / 2)
        print(SR[s:m + 1])
        MSort(SR, TR2, s, m)
        print(SR[m + 1:t + 1])
        MSort(SR, TR2, m + 1, t)
        Merge(TR2, TR1, s, m, t)


def main():
    num = [int(i) for i in input().split()]
    MSort(num, num, 0, len(num) - 1)
    print(np.array(num[0:len(num) + 1]))

if __name__ == '__main__':
    main()