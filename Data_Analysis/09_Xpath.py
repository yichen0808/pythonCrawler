from lxml import html
from lxml import etree

html_test = '''
<div>
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
        </tbody>
    </table>
</div>
'''
# 这个导入html
tree = html.fromstring(html_test)
# 这个导入etree
tree1 = etree.HTML(html_test)
# result = tree.xpath("//div/table/thead/tr")
# 结果: <Element tr at 0x20882f5b900>

# result = tree.xpath("//div/table/thead/tr/th/text()")
result = tree.xpath("//div/table/thead/tr//text()[normalize-space()]")
# 结果: ['书名', '作者', '字数', '更新日期', '链接', '操作']

# result = tree.xpath("//td/text()")[0]
# 结果: 龙族

# result = tree.xpath("//div/*/*/tr")
# 结果: [<Element tr at 0x1b9106aba40>, <Element tr at 0x1b9106aba90>]

# result = tree.xpath("//table/tbody/tr/td[5]/a[@class='hrefs']/text()")[0]
# 结果: 点击 其中td[5],从一开始

# result = tree.xpath("//div/*")[0]
# result2 = result.xpath("./thead/tr/th[2]/text()")[0]
print(result)
# 补充,拼接
a ="".join(['a','c','q','q'])
print(a)#acqq
