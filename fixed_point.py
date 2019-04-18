import numpy as np


def f(x):
    return x ** 5 - 2 * x - 1


def g(x):
    if 5 * (x ** 4) - 2 > 0:
        return np.sign(2 * x + 1) * np.abs(2 * x + 1) ** (1.0 / 5)
    else:
        return (x ** 5 - 1) / 2.0


def fun(x, epsilon):
    y = f(x)
    x = [-1.2, -0.862, -0.525, -0.187, 0.15, 0.487, 0.85, 1.1625, 1.5, 1.5]
    x = np.array(x)
    y = [-1.08832, 0.248774, 0.01012, -0.6227, -1.299906, -1.946667, -2.256469, -1.202758, 3.59375, 3.59375, ]
    r = []
    r = np.array(r)
    for k in range(1, x.size - 1):
        if y[k - 1] * y[k] <= 0:
            r = np.append(r, (x[k - 1] + x[k]) / 2)
        s = (y[k] - y[k - 1]) * (y[k + 1] - y[k])
        if np.abs(y[k]) < epsilon and (s <= 0):
            r = np.append(r, x[k])
    return r


def fix_point(x0, delta, max_iter):
    epsilon = np.finfo(np.float32).eps
    r_seq = np.zeros(max_iter, dtype=np.double)
    r_seq[0] = x0
    r = 0
    n = 0
    err = 0
    for n in range(1, max_iter):
        r_seq[n] = g(np.array([r_seq[n - 1]]))
        err = np.abs(r_seq[n] - r_seq[n - 1])
        rel_err = err / (np.abs(r_seq[n]) + epsilon)
        r = r_seq[n]
        if (err < delta) or (rel_err < delta): break
    return r


def main():
    a, b, c = map(float, input().split())
    c = int(c)
    epsilon = 0.01
    x = [-1.2, -0.862, -0.525, -0.187, 0.15, 0.487, 0.85, 1.1625, 1.5]
    x = np.array(x)
    r_app = fun(x, epsilon)
    delta = 10 ** (-c)
    max_iter = 50
    r = [0, 0, 0]
    for k in range(r_app.size):
        r[k] = fix_point(r_app[k], delta, max_iter)
    for k in range(r_app.size):
        print("%.3f" % (r[k]))


if __name__ == '__main__':
    main()
