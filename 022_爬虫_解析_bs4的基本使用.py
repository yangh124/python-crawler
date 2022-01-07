from bs4 import BeautifulSoup

soup = BeautifulSoup(open('022_爬虫_解析_bs4的基本使用.html', 'r'), 'lxml')

# 根据标签名查找节点
# 找到的是第一个符合条件的数据
print(soup.a)

# 获取标签的属性和属性值
print(soup.a.attrs)

# bs4中的一些函数
# （1）find
# 返回的是第一个符合条件的数据
print(soup.find('a'))
# 根据title值获取标签对象
print(soup.find('a', title='a2'))
# class要加下划线
print(soup.find('a', class_='a1'))

# （2）findAll
print(soup.find_all('a'))
print(soup.find_all(['a', 'span']))
print(soup.find_all('li', limit=2))

# （3）select
# 返回一个列表
print(soup.select('a'))
# .代表class #代表id  css语法
print(soup.select('.a1'))
print(soup.select('#l1'))
# 查找有id的li
print(soup.select('li[id]'))
print(soup.select('li[id="l2"]'))

# 层级选择器
# 后代选择器 所有子代，子代的子代
print(soup.select('div li'))

# 子代选择器
print(soup.select('div > li'))

# 找到所有li a
print(soup.select('li,a'))

# 节点信息
obj = soup.select('#d1')[0]
print(obj.get_text())
print(obj.string)

# 节点的属性
obj = soup.select('#p1')[0]
# name标签名
print(obj.name)
# attrs 返回一个字典
print(obj.attrs)
# 获取节点的属性
print(obj.attrs.get('id'))
print(obj.attrs['id'])
