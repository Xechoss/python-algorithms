"""
【问题描述】采用深度优先搜索算法求解TSP问题，并在搜索过程中，使用界限条件
（当前结点已经走过的路径长度要小于已求得的最短路径）进行“剪枝”操作（不再对后续结点进行遍历），
从而提高搜索效率。采用queue模块中的栈（LifoQueue）来实现深度优先搜索。
【输入形式】在屏幕上输入顶点个数和连接顶点间的边的邻接矩阵。
【输出形式】最优值和其中一条最优路径。
"""
import numpy as np
min_path = 999  # 全局变量
best = None
temp = 0


def dfs(g, s, path, vis):
    """
从根节点往下深度优先搜索
首先将结点vis为False，加入路径为True，移除重新设为false
不断搜索，每次修改当前路径长度，判断是否为叶子结点，是，则与最低比较
最短路径的时候，更新最短路径长，路径表。
    """
    global min_path
    global best
    global temp
    temp = 0
    n = len(vis)
    vis[s] = True
    # print(path)  # 输出当前路径
    m = True
    for i in range(n):  # 判断是否为叶结点
        if not vis[i]:
            m = False
    if m:  # 计算总的路径长度
        path_sum = 0
        for i in range(n - 1):
            path_sum = path_sum + g[path[i] - 1][path[i + 1] - 1]
        path_sum = path_sum + g[path[n - 1] - 1][0]
        if path_sum < min_path:  # 判断是否比最短路径短
            min_path = path_sum  # 复值
            best = path.copy()  # 复制路径
    for i in range(len(path)-1):
        temp = temp + g[path[i] - 1][path[i + 1] - 1]  # 当前路径的长度
    if temp < min_path:  # 截止
        print(path)
    for i in range(n):
        if not vis[i]:  # 判断所有不在路径上的点
            path.append(i + 1)  # 加入该结点
            dfs(g, i, path, vis)
            path.remove(i + 1)  # 去掉改结点

    vis[s] = False


def main():
    """
【输入形式】
4
0 30 6 4
30 0 5 10
6 5 0 20
4 10 20 0
    """
    n = int(input())
    g = np.zeros((n, n), dtype=np.double)
    for i in range(n):  # 邻接矩阵
        g[i, :] = np.array(input().split(), dtype=np.double)
    vis = np.zeros(n, dtype=np.bool)  # 是否添加标记数组
    path = [1]
    dfs(g, 0, path, vis)
    print(str(int(min_path))+': ', end='')  # 输出
    print(best)


if __name__ == '__main__':
    main()
"""
【样例输出】
[1]
[1, 2]
[1, 2, 3]
[1, 2, 3, 4]
[1, 2, 4]
[1, 3]
[1, 3, 2]
[1, 3, 2, 4]
[1, 3, 4]
[1, 4]
[1, 4, 2]
[1, 4, 2, 3]
[1, 4, 3]
25: [1, 3, 2, 4]
【样例说明】
 输入：顶点个数为4。连接顶点间边的邻接矩阵大小为4行4列，位置[i,j]上元素值表示第i个顶点到第j个顶点的距离，0表示两个顶点间没有边连接。
 输出：最优值为25，最优路径为[1, 3, 2, 4]。
"""
