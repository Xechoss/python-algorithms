import numpy as np
def mergeSort(a,d,start,end):
    if start<end:
        x=(start+end)//2
        print(np.array(a[start:end+1]))
        mergeSort(a,d,start,x)
        mergeSort(a,d,x+1,end)
        merge(a,d,start,x,end)
    if start==end:
        print(np.array(a[start:end+1]))

def merge(c,d,l,m,r):
    i=l
    j=m+1
    k=0

    while i<=m and j<=r:
        if c[i]<=c[j]:
            d[k]=c[i]
            k+=1
            i+=1
        else:
            d[k]=c[j]
            k+=1
            j+=1
    while i<=m:
        d[k]=c[i]
        k+=1
        i+=1
    while j<=r:
        d[k]=c[j]
        k+=1
        j+=1
    for x in range(k):
        c[l+x] =d[x]



def main():
    a=[int(i) for i in input().split()]
    d=[i for i in a]
    mergeSort(a,d,0,len(a)-1)
    print(np.array(d))


if __name__ == '__main__':
    main()