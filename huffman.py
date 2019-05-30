"""
【问题描述】使用贪心算法求解Huffman编码问题，具体来说就是，根据每个字符的出现频率，
            使用最小堆构造最小优先队列，构造出字符的最优二进制表示，即前缀码。
            在程序开始说明部分，简要描述使用贪心算法求解Huffman编码问题的算法过程。
【输入形式】在屏幕上输入字符个数和每个字符的频率。
【输出形式】每个字符的Huffman编码。
"""
import numpy as np


class node:  # 结点类：结点，权值，左右子树
    def __init__(self, name=None, value=None):
        self._name = name
        self._value = value
        self._left = None
        self._right = None


class huff_man_tree:
    """
    根据哈夫曼算法，以叶子结点为基础，反向建立哈夫曼树：
    1、生成叶子结点；包括字符，权值
    2、对所有结点以权值进行从大到小排序
    3、取出最小的两个结点，即最后两个结点（并且删除两个结点）
    4、权值相加，生成一个结点
    5、在将这个生成的结点加入到结点中
    """
    def __init__(self, char_weights):
        self.a = [node(part[0], part[1]) for part in char_weights]  # 生成叶子结点
        while len(self.a) != 1:
            self.a.sort(key=lambda node: node._value, reverse=True)  # 以权值进行从大到小排序
            c = node(value=(self.a[-1]._value + self.a[-2]._value))
            c._left = self.a.pop(-1)
            c._right = self.a.pop(-1)
            self.a.append(c)
        self.root = self.a[0]
        self.b = np.zeros(self.root.__sizeof__(), dtype=np.int)  # self.b用于保存每个叶子节点的哈夫曼编码

    """
    递归的思想生成编码，从根结点开始，左子树为0，右子树为1，依次存储在以结点为键、编码为值的字典中。
    """

    def set_code(self, tree, length, code):
        node = tree
        s = ""
        if not node:
            return
        elif node._name:
            for i in range(length):
                s = s + str(self.b[i])
            code[node._name] = s  # 哈夫曼编码字典
        self.b[length] = 0
        self.set_code(node._left, length + 1, code)  # 递归左子树
        self.b[length] = 1
        self.set_code(node._right, length + 1, code)  # 递归右子树

    """
    输出哈夫曼编码，对哈夫曼编码字典以键进行排序，依次输出哈夫曼编码
    """
    def get_code(self):
        code = {}
        self.set_code(self.root, 0, code)
        code_name = sorted(code, key=lambda code: code[0])  # 哈夫曼编码字典以键进行排序
        for temp in code_name:
            print(temp, end=' ')
            print(code.get(temp))


def main():
    """
    【样例输入】
     6
     45 13 12 16 9 5
    """
    ch = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
    char_weights = []
    n = int(input())
    weight = [int(i) for i in input().split()]
    for i in range(n):
        char_weights.append((ch[i], weight[i]))  # 结点与权值
    """
    【样例输出】
    a 0
    b 101
    c 100
    d 111
    e 1101
    f 1100
    """
    tree = huff_man_tree(char_weights)
    tree.get_code()
    """
    【样例说明】
     输入：字符个数为6，a至f每个字符的频率分别为：45, 13, 12, 16, 9, 5。
     输出：每个字符对应的Huffman编码。
    """


if __name__ == '__main__':
    main()
