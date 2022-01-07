import json
import jsonpath

obj = json.load(open('020_爬虫_解析_jsonpath.json', 'r', encoding='utf-8'))

# 所有书的作者
book_author_list = jsonpath.jsonpath(obj, '$.store.book[*].author')
print(book_author_list)

# 所有的价格
price_list = jsonpath.jsonpath(obj, '$..price')
print(price_list)

# store下的所有元素
tag_list = jsonpath.jsonpath(obj, '$.store.*')
print(tag_list)

# 第二本书
second_book = jsonpath.jsonpath(obj, '$..book[2]')
print(second_book)

# 第二本书
last_book = jsonpath.jsonpath(obj, '$..book[(@.length-1)]')
print(last_book)

'''
书店所有书的作者                                      $.store.book[*].author	
所有的作者                                           $..author	
store的所有元素。所有的bookst和bicycle	               $.store.*	
store里面所有东西的price	                           $.store..price	
第三个书                                             $..book[2]	
最后一本书                                           $..book[(@.length-1)]	
前面的两本书                                         $..book[0,1]    $..book[:2]
过滤出所有的包含isbn的书                               $..book[?(@.isbn)]	 
过滤出价格低于10的书                                   $..book[?(@.price<10)]	
所有元素。                                           $..*	
'''
