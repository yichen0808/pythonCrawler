import requests

# 需要爬取内容
content = input("请输入内容:")
url = f'https://www.sogou.com/web?query={content}'
# url.encode("utf-8")
# 模拟浏览器?
headers ={
"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}
# 爬取
reqs = requests.get(url,headers=headers)
# 输出爬取内容
print(reqs.text)
# 查看请求头信息
print(reqs.headers)
reqs.close()