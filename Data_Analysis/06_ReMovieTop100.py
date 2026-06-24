import requests
import re
# 一.获取数据
# 二.解析
# 三.保存
f = open("Top100","w",encoding="utf-8")

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

pattern = re.compile(
    r'<div class="item">.*?'
    r'<span class="title">(?P<name>.*?)</span>.*?'
    r'导演:(?P<director>.*?)&nbsp;.*?'
    r'主演:(?P<actors>.*?)<br>.*?'
    r'<span class="rating_num".*?>(?P<score>.*?)</span>',
    re.S
)

for i in range(0,101,25):
    url = "https://movie.douban.com/top250?start={i}&filter="
    reqs = requests.get(url, headers=headers)
        # reqs.encoding = 'utf-8' 乱码解决
        # print(reqs.text)

    result = pattern.finditer(reqs.text)
    for item in result:
        name = item.group("name")
        director = item.group("director").strip()
        actors = item.group("actors").strip() #取消前后空格
        score = item.group("score")
        line = f"{name} 导演:{director} 主演:{actors}评分:{score}\n"
        print(line.strip())
        f.write(line)

f.close()
reqs.close()
print("爬取完成！")