import requests

url = "https://movie.douban.com/j/chart/top_list"
# 从负载里面找
params = {
    "type" : "13",
    "interval_id" : "100:90",
    "action" : "",
    "start" : "0",
    "limit" : "20"
}
headers = {
"user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

reqs = requests.get(url,params=params,headers=headers)
print(reqs.text)
reqs.close()