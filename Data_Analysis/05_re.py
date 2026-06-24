import re
# 注.先学正则表达式
# data = re.findall("20","我今年20了,大学2年")
# print(data)
#
# data = re.findall(r"\d+","我今年20了,大学2年")  #r为取消转义
# print(data)
#
# data = re.finditer(r"\d+","我今年20了,大学2年")#迭代器
# for item in data:
#     print(item.group()) #从组中拿数据
#
# data = re.match(r"\d+","我今年20了,大学2年").group()  #从第一个开始^\d
# print(data)
#
# data = re.search(r"\d+","我今年20了,大学2年").group()  #只查到第一个
# print(data)
# 预加载
# my = re.compile(r"\d+")
# data = my.findall("我今年20了,大学2年")
# print(data)

s = '''
    <option value="1">玄幻</option>
    <option value="2">科幻</option>
'''
# 格式(?P<自己命名>正则),
# 对象用迭代器
# 使用用group()
my = re.compile(r'<option value="(?P<values>\d+)">(?P<type>.*?)</option>')
result = my.finditer(s)
for item in result:
    print(item.group("values"))
    print(item.group("type"))
