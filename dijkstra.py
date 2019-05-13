"""
【问题描述】Dijkstra算法解决的是带权重的有向图上单源最短路径问题。
            所有边的权重都为非负值。设置顶点集合S并不断地作贪心选择来扩充这个集合。
            使用最小堆数据结构构造优先队列。
【输入形式】在屏幕上输入顶点个数和连接顶点间的边的权矩阵。
【输出形式】从源到各个顶点的最短距离及路径。
"""
import numpy as np


def dijkstra(n, v, dist, prev, c, s):
    for i in range(n):
        dist[i] = c[v][i]
        s[i] = False
        if dist[i] == 999:
            prev[i] = 0
        else:
            prev[i] = v
    dist[v] = 0
    s[v] = True
    for i in range(n-1):
        temp = 999
        u = v
        for j in range(n):
            if (not s[j]) and (dist[j] < temp):
                u = j
                temp = dist[j]
            s[u] = True
            for k in range(n):
                if (not s[k]) and (c[u][k] < 999):
                    new_dist = dist[u]+c[u][k]
                    if new_dist < dist[k]:
                        dist[k] = new_dist
                        prev[k] = u

    for i in range(n):
        if i == v:
            prev[i] = -1
    for i in range(n):
        if i != v:
            print(str(dist[i])+': ', end='')
            t = str(i+1)
            j = i
            while True:
                if j == 0:
                    break
                t = t+'>-'+str(prev[j]+1)
                j = prev[j]
                m = list(t)
                m.reverse()
                result = "".join(m)
            print(result)


def main():
    n = int(input())
    c = np.zeros((n, n), dtype=np.int)
    for i in range(n):
        c[i, :] = np.array(input().split(), dtype=np.int)
    for i in range(n):
        for j in range(n):
            if c[i][j] == 0:
                c[i][j] = 999
    dist = np.zeros(n, dtype=np.int)
    s = np.zeros(n, np.bool)
    prev = np.zeros(n, np.int)
    dijkstra(n, 0, dist, prev, c, s)


if __name__ == '__main__':
    main()

"""
【样例输入】
5
0 10 0 30 100
0 0 50 0 0
0 0 0 0 10
0 0 20 0 60
0 0 0 0 0
【样例输出】
10: 1->2
50: 1->4->3
30: 1->4
60: 1->4->3->5
【样例说明】
 输入：顶点个数为5。连接顶点间边的权矩阵大小为5行5列，位置[i,j]上元素值表示第i个顶点到第j个顶点的距离，0表示两个顶点间没有边连接。
 输出：每行表示源1到其余各顶点的最短距离及路径
"""
