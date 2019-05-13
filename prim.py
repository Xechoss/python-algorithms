"""
【问题描述】Prim算法解决的是带权重的无向图上连接所有顶点的耗费最小的生成树。
【输入形式】在屏幕上输入顶点个数和连接顶点间的边的权矩阵。
【输出形式】从源到各个顶点的最短距离及路径。
"""
import numpy as np


def prim(c, n):
    """
    先找出结点中是low最小的顶点j，根据closest选取边（j,closest[j]），最后将j添加到s中，对应修改closest，low
    """
    low = np.zeros(n, dtype=np.int)
    closest = np.zeros(n, dtype=np.int)
    s = np.zeros(n, dtype=np.bool)
    s[0] = True
    for i in range(1, n):  # 对low，closest，s初始赋值
        low[i] = c[0][i]
        closest[i] = 0
        s[i] = False
    for i in range(n - 1):
        m = 999
        j = 0
        for k in range(1, n):
            if (low[k] < m) and (not s[k]):
                m = low[k]  # 找出结点中是low最小的顶点j
                j = k
        s[j] = True  # 第j个结点加入s中
        for k in range(1, n):
            if (c[j][k] < low[k]) and (not s[k]):
                low[k] = c[j][k]  # 修改对应low，closest的值
                closest[k] = j
    for i in range(1, n):
        print(str(low[i]) + ': ', end='')
        t = str(i + 1)
        j = i
        while True:
            if j == 0:
                break
            t = t + '-<' + str(closest[j] + 1)
            j = closest[j]
            m = list(t)
            m.reverse()
            result = "".join(m)
        print(result)
    """
    【样例输出】
15: 1<-2
7: 1<-3
9: 1<-3<-4
6: 1<-3<-6<-5
5: 1<-3<-6
3: 1<-3<-6<-8<-7
8: 1<-3<-6<-8
    """


def main():
    """
    【样例输入】
    8
    0 15 7 0 0 0 0 10
    15 0 0 0 0  0 0 0
    7 0 0 9 12 5 0 0
    0 0 9 0 0 0 0 0
    0 0 12 0 0 6 0 0
    0 0 5 0 6 0 14 8
    0 0 0 0 0 14 0 3
    10 0 0 0 0 8 3 0
    """
    n = int(input())
    c = np.zeros((n, n), dtype=np.int)
    for i in range(n):
        c[i, :] = np.array(input().split(), dtype=np.int)
    for i in range(n):
        for j in range(n):
            if c[i][j] == 0:
                c[i][j] = 999
    prim(c, n)


if __name__ == '__main__':
    main()
"""
【样例说明】
 输入：顶点个数为8。连接顶点间边的权矩阵大小为8行8列，位置[i,j]上元素值表示第i个顶点到第j个顶点的距离，0表示两个顶点间没有边连接。
 输出：每行表示其余各顶点的值及其到起始点1的路径。
"""
