import requests
url = "http://baidu.com"
url.encode("utf-8")
# 代理
proxy = {
    "http":"http://IP:端口",
    "https":"https://IP:端口"
}
a = requests.get(url,proxies=proxy)