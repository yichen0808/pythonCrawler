import requests

# 创建会话（使用 Session，不是 session）
session = requests.Session()
data = {
    "name":"my_name",
    "password":"my_password"
}
url = ""
i = 0
resq = session.post(url,data=data)
print(resq.text)
print(resq.cookies)

url1 = ""
resq1 = session.get(url1)
print(resq1.json())
# 直接cookie
# resq = requests.post(url,header={"cookie":""})

