import math
def fun(m,n,c):
    count=0
    mid=m+(expression(m)*(n-m))/(expression(m)-expression(n))
    m=mid
    while math.fabs(expression(m))>c:
        count+=1
        mid=m+(expression(m)*(n-m))/(expression(m)-expression(n))
        m=mid
    print(count)
    print("%.11f" % m)
def expression(x):
    return 3600/x*((1+x/12)**240- 1)-500000
def main():
    a,b,c=map(float,input().split())
    fun(a,b,c)
if __name__ == '__main__':
    main()