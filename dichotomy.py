import math
def fun(m,n,c):
    accuracy=10**(-c)
    mid=(m+n)/2
    count=0
    sum=3600/mid*((1+mid/12)**240- 1)-500000
    while (n-m)>accuracy:
        count=count+1
        if sum==0:
            break
        elif sum>0:
            n=mid
        else:
            m=mid
        mid=(m+n)/2
        sum=3600/mid*((1+mid/12)**240-1)-500000
    print(count)
    print("%.11f" % mid)
def main():
    print("输出区间，精确位数：")
    a,b,c=map(float,input().split())
    c=int(c)
    fun(a,b,c)
if __name__ == '__main__':
    main()