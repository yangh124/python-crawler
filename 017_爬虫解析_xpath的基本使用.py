from lxml import etree

'''
xpath解析
1. 解析本地文件   ->   etree.parse('xxx.html')
2. 解析response  ->  etree.HTML(response)
'''
tree = etree.parse('017.html')

# 1.路径查询
# //表示所有子节点，不考虑层级关系 /表示下面一级
li_list = tree.xpath('//body//ul/li')
print(li_list)

# 2.谓词查询
# 查找所有有id属性的li标签
text = tree.xpath('//ul/li[@id]/text()')
print(text)

# 3.属性查询，内容查询
# 查找所有有id属性为a的li标签
id_text = tree.xpath('//ul/li[@id="a"]/text()')
print(id_text)
# 查找所有有id属性为a的li标签
id_class = tree.xpath('//ul/li[@id="a"]/@class')
print(id_class)

# 4.模糊查询
# 查询id包含l的li标签
contains = tree.xpath('//ul/li[contains(@id,"l")]/text()')
print(contains)
# 查询id starts_with l的li标签
starts_with = tree.xpath('//ul/li[starts-with(@id,"c")]/text()')
print(starts_with)

# 5.逻辑运算  and or & |
and_res = tree.xpath('//ul/li[starts-with(@id,"l") and @class="c1"]/text()')
or_res = tree.xpath('//ul/li[starts-with(@id,"l")]/text() | //ul/li[@class="c1"]/text()')
print(and_res)
print(or_res)
