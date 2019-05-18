"""
【问题描述】组合梯形公式求积分近似值
【输入形式】在屏幕上依次输入积分上限、下限和等距子区间个数
【输出形式】输出使用组合梯形公式求得的积分近似值
"""
import math


def fun(x):  # 数值积分函数
    return 2+math.sin(2*math.sqrt(x))


def traprl(a, b, m):
    h = (b-a)/m
    s = 0
    for i in range(1, m):
        x = a+h*i
        s += fun(x)
    s = h*(fun(a)+fun(b))/2+h*s
    return s


def main():
    """
    【样例1输入】
    1 6 10
    """
    a, b, m = map(int, input().split())  # 输入a，b，m：积分下限、上限、等步长个数
    s = traprl(a, b, m)
    print("%.8f" % s)
    """
    【样例1输出】
    8.19385457
    """


if __name__ == '__main__':
    main()
"""
【样例1说明】输入：积分上限a为1、下限b为6和等距子区间个数m为10。输出：积分近似值（保留小数点后8位有效数字）
【评分标准】根据输入得到的输出准确
"""
