1. scrapy项目结构
    * 项目名称
        * 项目名称
            * spider目录（储存爬虫文件）
                * init
                * 自定义爬虫文件
            * init
            * items 定义数据结构的地方，爬取的数据都包含哪些
            * middlewares 中间件 代理
            * pipelines 管道 处理下载数据
            * settings 配置文件 
2. response的属性和方法
   * response.text 获取的是响应字符串
   * response.body 获取的二进制数据
   * response.xpath 使用XPATH
   * xxx.extract()  提取selector对象的data属性
   * xxx.extract_first()  提取的selector列表的第一个数据