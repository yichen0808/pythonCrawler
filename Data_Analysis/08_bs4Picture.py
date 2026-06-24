import requests
from bs4 import BeautifulSoup
# 获取url是/开头,直接拼接
# 不是则去掉最后一个/后内容,拼接

url = "https://bizhi1.com/"
reqs = requests.get(url)
# print(reqs.text)
page = BeautifulSoup(reqs.text,"html.parser")
content_all = page.find_all("a",attrs={"class":"media-pic"})
for i in content_all:
    href = i.get("href")
    name = i.find("img").get("alt","")
    # 如果 img 标签没有 alt 属性，get('alt') 会返回 None，而 get('alt', '') 会返回空字符串 ''，程序不会报错
    src = i.find("img").get("src")
    pic = requests.get(src)
    # print(f"name:{name} href:{href} src:{src}\n")
    # 保存数据
    with open(f"{name}.jpg",mode="wb") as f:
        f.write(pic.content)
    break