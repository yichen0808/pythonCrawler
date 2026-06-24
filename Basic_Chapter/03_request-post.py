import requests

url = "http://baidu.com/sug"#举例
data = {
    "kw" : input("输入内容:")
}
reqs = requests.post(url,data=data)
print(reqs.text)
print(reqs.json())
# 老样子:明确爬取网站,伪装自己,请求,输出请求
reqs.close()