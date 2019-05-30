"""
【问题描述】采用优先队列搜索算法求解TSP问题，用一最小堆来存储活结点表，
其优先级是结点的当前费用。并在搜索过程中，使用界限条件（当前结点已经走过的路径长度要小于已求得的最短路径）
进行“剪枝”操作（不再对后续结点进行遍历），从而提高搜索效率。采用heapq模块来实现最小堆。
【输入形式】在屏幕上输入顶点个数和连接顶点间的边的邻接矩阵。
【输出形式】搜索过程，最优值和其中一条最优路径。
"""
import numpy as np
import heapq as hq


class Node:
    def __init__(self, path=None, cost=None):
        self._path = path
        self._cost = cost

    def __lt__(self, other):
        return self._cost < other._cost


def priority_tsp(g, s):
    best_cost = np.inf
    best_path = None
    n, _ = g.shape
    start_node = Node(path=[s], cost=0)
    list_open = []
    hq.heappush(list_open, start_node)
    while list_open:
        cur = hq.heappop(list_open)
        print(cur._path)
        if cur._cost >= best_cost:
            continue
        if len(cur._path) == n:
            new_cost = cur._cost + g[cur._path[-1] - 1, s-1]
            if new_cost < best_cost:
                best_cost = new_cost
                best_path = list(cur._path)
                continue
        for i in range(1, n+1):
            if i not in cur._path:
                new_cost = cur._cost + g[cur._path[-1] - 1, i - 1]
                if new_cost < best_cost:
                    new_path = list(cur._path)
                    new_path.append(i)
                    new_node = Node(path=new_path, cost=new_cost)
                    hq.heappush(list_open, new_node)
    return best_cost, best_path


def main():
    n = int(input())
    g = np.zeros((n, n), dtype=np.double)
    for i in range(n):
        g[i, :] = np.array(input().split(), dtype=np.double)
    g[g == 0] = np.inf
    s = 1
    best_cost, best_path = priority_tsp(g, s)
    print('{}: {}'.format(int(best_cost), best_path))


if __name__ == '__main__':
    main()
"""
【样例输入】
4
0 30 6 4
30 0 5 10
6 5 0 20
4 10 20 0
【样例输出】
[1]
[1, 4]
[1, 3]
[1, 3, 2]
[1, 4, 2]
[1, 4, 2, 3]
[1, 3, 2, 4]
[1, 4, 3]
[1, 3, 4]
[1, 2]
25: [1, 4, 2, 3]
【样例说明】
 输入：顶点个数为4。连接顶点间边的邻接矩阵大小为4行4列，位置[i,j]上元素值表示第i个顶点到第j个顶点的距离，0表示两个顶点间没有边连接。
 输出：在整个算法过程中的先后搜索路径，最优值为25，最优路径为[1, 3, 2, 4]。
"""
