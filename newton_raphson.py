import numpy as np


def fun(t):
    y = 9600*(1-np.e**(-t/15.0))-480*t
    return y


def dfun(t):
    y = 640*(np.e**(-t/15.0))-480
    return y


def newton(p0, delta, epsilon, max1):
    for i in range(1, max1):
        p1 = p0-fun(p0)/dfun(p0)
        err = abs(p1-p0)
        #relerr = 2*err/(abs(p1)+delta)
        p0 = p1
        y = fun(p0)
        if err < delta or abs(y) < epsilon:
            break
    return p0


def main():
    a, b, c = map(float, input().split())
    b = int(b)
    c = int(c)
    delta = 10**(-b)
    epsilon = 10**(-c)
    max1 = 50
    t = newton(a, delta, epsilon, max1)
    print("%.5f" % t)
    x = 2400*(1-np.e**(-t/15.0))
    print("%.5f" % x)


if __name__ == '__main__':
    main()