from bs4 import BeautifulSoup

html = '''
    <body>
     <div id="container">
        <!-- 顶栏 -->
        <div class="header">
        <h1>图书管理系统</h1>
        <a href="#">退出登录</a>
        </div>

        <!-- 搜索表单区域 -->
        <form class="search-form" action="#" method="post">
        <input type="text" name="name" placeholder="书籍名" />
        <select name="book_type">
            <option value="">书籍类型</option>
            <option value="1">男频</option>
            <option value="2">女频</option>
        </select>
        <select name="book_types">
            <option value="">种类</option>
            <option value="1">玄幻</option>
            <option value="2">科幻</option>
            <option value="3">武侠</option>
            <option value="4">仙侠</option>
            <option value="5">恋爱</option>
        </select>
        <button type="submit">查询</button>
        <button type="reset" class="clear">清空</button>
        </form>

        <table class="table table-striped table-bordered">
        <thead>
            <tr>
                <th>书名</th>
                <th>作者</th>
                <th>字数</th>
                <th>更新日期</th>
                <th>链接</th>
                <th>操作</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>龙族</td>
                <td>江南</td>
                <td>100万</td>
                <td>2026-4-27</td>
                <td><a href="" class="hrefs">点击</a></td>
                <td class="btn-group">
                    <button class="edit">编辑</button>
                    <button class="delete">删除</button>
                </td>
            </tr>
        </table>

        <!-- 页脚版权区域 -->
        <footer class="footer">
        <p class="company-name">书籍</p>
        <p class="copyright">版权所有114514</p>
        </footer>

        <script>
        //点击列表中每一条记录后面的删除按钮，弹出一个提示框，提示：您是否要删除这条记录？ 如果确定，则移出这条记录
        const deleteButtons = document.querySelectorAll('.delete');
        for (let i = 0; i < deleteButtons.length; i++) {
            deleteButtons[i].addEventListener('click', function () {
            if (confirm('您是否要删除这条记录？')) {
                //点击确定按钮，删除当前记录
                this.parentNode.parentNode.remove();
            }
            });
        }
        
        //通过js实现鼠标移入移出效果，鼠标移入，背景色为青色，鼠标移出，背景色为 白色。
        const trs = document.querySelectorAll('tr');
        for (let i = 1; i < trs.length; i++) {
            trs[i].addEventListener('mouseenter', function () {
            this.style.backgroundColor = '#f2e2e2';
            });
            trs[i].addEventListener('mouseleave', function () {
            this.style.backgroundColor = '#fff';
            });
        }
        </script>

    </div>
</body>
'''
#初始化bs对象
page = BeautifulSoup(html,"html.parser")
# find("属性名",attrs={"属性":"值"})
divOne = page.find("div",attrs={"id":"container"})#一个结果
divAll = page.find_all("div",attrs={"id":"container"})#一堆
# print(divAll.text)
find_a = page.find("a")
if find_a:
    print(find_a.get("href"))

find_td = page.find_all("td")
for i in find_td:
    print(i.text)