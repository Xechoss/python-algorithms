import requests
fp=open('F:\服务外包创新创业\数据.txt','a')
r=requests.get("http://q.stock.sohu.com/hisHq?code=cn_002250,cn_002197&start=20080101&end=20181231")
print(r.status_code)
print(r.encoding)
fp.writelines(r.text)
fp.close()