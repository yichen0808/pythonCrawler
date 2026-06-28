# 模拟你使用浏览器
from selenium import webdriver

# 初始化 ChromeDriver
driver = webdriver.Chrome()

# 打开 Google 首页
driver.get("https://www.bing.com")

# 打印网页标题
print("Page title: ", driver.title)

# 关闭浏览器
driver.quit()
# 剩下的略