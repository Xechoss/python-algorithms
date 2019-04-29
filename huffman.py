"""
【问题描述】使用贪心算法求解Huffman编码问题，具体来说就是，根据每个字符的出现频率，
            使用最小堆构造最小优先队列，构造出字符的最优二进制表示，即前缀码。
            在程序开始说明部分，简要描述使用贪心算法求解Huffman编码问题的算法过程。
【输入形式】在屏幕上输入字符个数和每个字符的频率。
【输出形式】每个字符的Huffman编码。
【样例输入】
 6
 45 13 12 16 9 5
【样例输出】
a 0
b 101
c 100
d 111
e 1101
f 1100
【样例说明】
 输入：字符个数为6，a至f每个字符的频率分别为：45, 13, 12, 16, 9, 5。
 输出：每个字符对应的Huffman编码。
"""
import numpy as np


class node:
    def __init__(self, name=None, value=None):
        self._name = name
        self._value = value
        self._left = None
        self._right = None


# 哈夫曼树类
class huff_man_tree:

    # 根据Huffman树的思想：以叶子节点为基础，反向建立Huffman树
    def __init__(self, char_weights):
        self.a = [node(part[0], part[1]) for part in char_weights]  # 根据输入的字符及其频数生成叶子节点
        while len(self.a) != 1:
            self.a.sort(key=lambda node: node._value, reverse=True)
            c = node(value=(self.a[-1]._value + self.a[-2]._value))
            c._left = self.a.pop(-1)
            c._right = self.a.pop(-1)
            self.a.append(c)
        self.root = self.a[0]
        self.b = np.zeros(10, dtype=np.int)  # self.b用于保存每个叶子节点的Haffuman编码,range的值只需要不小于树的深度就行

    # 用递归的思想生成编码
    def pre(self, tree, length):
        node = tree
        if not node:
            return
        elif node._name:
            print(node._name + '的编码为:', end='')
            for i in range(length):
                print(self.b[i], end=' ')
            print()
            return
        self.b[length] = 0
        self.pre(node._left, length + 1)
        self.b[length] = 1
        self.pre(node._right, length + 1)

    # 生成哈夫曼编码
    def get_code(self):
        self.pre(self.root, 0)


def main():
    # 输入的是字符及其频数
    ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    char_weights = []
    n = int(input())
    weight = [int(i) for i in input().split()]
    for i in range(n):
        char_weights.append((ch[i], weight[i]))
    tree = huff_man_tree(char_weights)
    tree.get_code()


if __name__ == '__main__':
    main()
