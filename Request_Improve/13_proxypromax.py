import requests
def proxy():
    url_proxy = "第三方代理地址"
    reqs = requests.get(url_proxy)
    data = reqs.json()
    use_count = 0
    total_count = data['data']['count']
    for ip in data['data']['iplist']:
        yield ip,use_count,total_count
        use_count+=1
def spider(ip):
    url = "http://baidu.com"

    while 1:
        try:
            # 代理
            proxy_ip, used_count, total_count = next(ip, (None, 0, 0))  # 使用None作为默认值

            # 判断IP是否用完
            if proxy_ip is None:
                print("所有代理IP已用完！")
                return None

            if used_count >= total_count:
                print(f"所有 {total_count} 个代理IP已用完！")
                return None

            # 检查IP是否为空字符串
            if not proxy_ip or proxy_ip.strip() == "":
                print("遇到空IP，跳过")
                continue
            proxy = {
                "http": "http://" + proxy_ip,
                "https": "https://" + proxy_ip
            }

            a = requests.get(url, proxies=proxy)
            a.encoding = 'utf-8'
            return a.text
        except StopIteration:
            # 生成器耗尽
            print("所有代理IP已用完！")
            return None
        except Exception as e:
            print(f"代理 {proxy_ip} 请求失败: {e}")
            continue
if __name__ == '__main__':
    ip = proxy()
    for i in range(10):
        result = spider(ip)
        if result:
            print(f"成功，长度: {len(result)}")
        else:
            print("失败")
            break