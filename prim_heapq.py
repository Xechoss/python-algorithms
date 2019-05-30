"""
prim算法
原理解释：
把一堆节点分成两组，一组已标记（已经在最小生成树里面了），另一组不在最小生成树里面。每次都找链接两组节点的最小的那一条边
该边一边连接着一组的点，把那条边的连接着的没有标记的点标记。然后再找连接两组节点的最小的边。。。
直到所有的点都被标记后，最小生成树建立完成！

过程分析：
首先任选一个节点（在这个程序中，我们选的是 1 节点），
然后遍历所有和当前节点相邻的节点。{每个节点都有一个权值其表示的是min(当前节点到相邻节点的距离, 该节点本身带有的权值)。每个节点的初始值都是无穷大！}
当 当前节点 到 相邻的节点 的权值小于该相邻结点的权值的时候，就更新该节点的权值，并且把该节点放到最小堆里面，同时更新路径。
知道最小堆里面的元素没有的时候，跳出循环。
"""
import numpy as np
import heapq as pq


class Node(object):
    def __init__(self, id=0, value=0.0):
        self.id = id
        self.value = value

    def __lt__(self, other):
        return self.value < other.value


def print_f(path, i):
    P = []  # 储存路径
    while i != 0:
        P.append(int(i))
        i = path[i]
    print(': 1', end='')
    for i in range(len(P) - 1, -1, -1):
        print('<-%d' % (P[i] + 1), end='')
    print()


def main():
    n = int(input())  # 节点的个数
    G = np.zeros((n, n), dtype=np.double)  # 图的信息，各节点相连情况和他们之间的距离，
    for i in range(n):
        G[i, :] = np.array(input().split(), dtype=int)
    vis = np.zeros(n, dtype=int)  # 用于标记每个点，标记为 0 的节点在V- A集里面，还没有找到最小对应值，标记为非 0 的节点表示在A集里面
    val = np.zeros(n, dtype=np.double)  # 每个节点的储存值
    val[val == 0] = np.inf  # 初始化每个节点的储存值
    val[0] = 0.0
    path = np.zeros(n, dtype=int)  # 每个节点的前驱， 该节点是从哪一个节点走到这的
    h = []
    pq.heappush(h, Node(0, val[0]))
    while len(h) >= 1:  # 当堆里面没有元素的时候跳出循环
        P = pq.heappop(h)  # 把堆顶元素取出（节点权值最小）
        u = P.id
        vis[u] = 1  # 把该节点标记，表示该节点已经在最小生成树里面了
        for i in range(n):  # 遍历和该节点相邻的每一个没标记的节点
            if G[u][i] != 0 and vis[i] == 0:  # 若两点之间不连通，或者要遍历的点已经在最小生成树里面了就直接跳出 跳过该节点
                if val[i] > G[u][i]:  # 如果该结点的权值大于连接两点的边值，就进行更新
                    val[i] = G[u][i]  # 更新点权
                    path[i] = u  # 更新路径
                    pq.heappush(h, Node(i, val[i]))  # 把该节点放在最小堆里面

    for i in range(1, n):  # 输出结果
        print(int(val[i]), end='')
        print_f(path, i)
    return


if __name__ == '__main__':
    main()

"""
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
