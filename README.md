# Spider_learning
[Good explanation](http://www.junnanzhu.com/?p=560)
## 动态网页的爬取
```
对于静态网页而言，要爬取其中的内容其实比较简单，我们可以在python中使用urllib或者urllib2来获取网页的源代码。之后可以使用BeautifulSoup对所获取的源代码进行解析或者也可以自己写正则表达式来提取自己想要的内容。那么我们注意到静态网页随着html代码的生成，页面的内容和显示效果基本上不会发生变化（除非你修改代码）。但是现实中很多网页却不是这样，比如说打开一个百度页面，你首先会看到一个百度搜索框，之后页面下方会慢慢加载出推荐的新闻、图片等；或者是你在京东浏览某件你比较感兴趣的商品的评论信息，随着评论的不断加载，更多的评论也呈现在你眼前。这些都是一些比较常见的动态网页的例子。

在介绍动态网页之前我们稍微来谈一谈Ajax，什么是Ajax呢？Ajax全称为“Asynchronous Javascript And Xml”（异步Js和XML），是指一种创建交互式网页应用的网页开发技术。通过在后台与服务器进行少量数据交换，Ajax可以使网页实现异步更新。这也意味着可以在不重新加载整个网页的情况下，对网页的某部分进行更新。像网页微信、网页qq这些，我们并不需要去刷新网页，但是有新消息来时，我们还是可以接收到消息提示。这样的好处就是先将不变的部分加载出来，要变的部分单独在后台同步，这样可以很大程度上降低数据的流量交换以及提高网页加载的速度。这也就造就了Ajax网页的三个特点：页面加载快速、不刷新网页就能更新内容、源代码内容与网页内容不同。所以说判断一个网页是不是动态网页很简单，如果在页面查看的源代码和审查元素所看到的html不同，那么就说明这个网页是动态生成的。

那么如果要爬取动态网页，我们势必要做出些调整。首先我们必须要明确我们需要爬取的目标是什么，如果这个目标本身就是网页的一个“不变”的部分，那么我们还是可以像静态网页那么去处理。如果我们锁定的目标会引起网页源代码变化，那么我们就要想方设法去获取这些目标的具体位置。一般来说它们会处在网页加载的Js文件之中，而且往往以Json的格式出现。那么我们怎么知道他会加载哪些文件呢？很简单，我们使用Chrome打开一个网页，你在审查元素中的network中可以看见随着时间或者你在网页上的操作（鼠标点击、拖动等），会有一些Js文件被加载。如果你要抓取某段评论，那么我们将鼠标拖动到评论区中，然后在加载的文件列表中找出所需的内容，Chrome的network状态栏中会显示时间信息，你一般可以根据时间信息缩小查找文件的范围。这些内容知乎上也有关于抓取Ajax渲染的页面的讨论。

那么另一种方式，我们可以借助Selenium来实现。Selenium是Thoughtworks公司的一个集成测试的强大工具。Selenium 是 ThoughtWorks 专门为 Web 应用程序编写的一个验收测试工具。与其他测试工具相比，使用 Selenium 的最大好处是： Selenium 测试直接在浏览器中运行，就像真实用户所做的一样。可以使用pip install来安装Selenium：

Selenium的核心是webdriver，使用webdriver可以去调用系统的浏览器（Firefox）从而模拟用户的行为，这一步如果出错的话，可能是浏览器版本问题或者是需要下载第三方的驱动（比如geckodriver）。另外用户可以从Selenium的API文档上查询出诸如鼠标点击、拖动等操作的函数，并且其中也包含一些find_element_by_id( )之类的函数，这个就很类似于在对经过BeautifulSoup解析后的网页调用findAll("", {"id":"XX"})查找元素。

值得一提的是，某些网页只是因为时间的原因才呈现出动态网页的模样，什么意思呢，比如一些网页会先把比较引人注目的标题亮出来，然后几秒延迟之后，会不断加载出之后的所有内容，其后的网页内容就不会随时间或者你鼠标的拖动而改变，从而呈现出静态网页的特性。这个时候最简单的方法就是在Selenium中调用浏览器打开这个网页并且设置时间延迟，当然这段时间延迟要使得这个网页的内容全部被加载，然后再将其保存成静态网页，然后就可以用BeautifulSoup这些比较熟悉的方式去处理。
```

收集各种爬虫 （默认爬虫语言为 python）, 欢迎大家 提 pr 或 issue, 收集脚本见此项目 [github-search](https://github.com/facert/github_search)

### A
* [暗网爬虫(Go)](https://github.com/s-rah/onionscan)
* [爱丝APP图片爬虫](https://github.com/x-spiders/aiss-spider)

### B
* [Bilibili 用户](https://github.com/airingursb/bilibili-user)
* [Bilibili 视频](https://github.com/airingursb/bilibili-video)
* [B站760万视频信息爬虫](https://github.com/chenjiandongx/bili-spider)
* [博客园(node.js)](https://github.com/chokcoco/cnblogSpider)
* [百度百科(node.js)](https://github.com/nswbmw/micro-scraper)
* [北邮人水木清华招聘](https://github.com/Marcus-T/Crawler_Job)
* [百度云网盘](https://github.com/gudegg/yunSpider)
* [琉璃神社爬虫](https://github.com/Chion82/hello-old-driver)

### C
* [cnblog](https://github.com/jackgitgz/CnblogsSpider)
* [caoliu 1024](https://github.com/LintBin/1024crawer)

### D
* [豆瓣读书](https://github.com/lanbing510/DouBanSpider)
* [豆瓣爬虫集](https://github.com/dontcontactme/doubanspiders)
* [豆瓣害羞组](https://github.com/rockdai/haixiu)
* [DNS记录和子域名](https://github.com/TheRook/subbrute)

### E
* [E绅士](https://github.com/shuiqukeyou/E-HentaiCrawler)

### G
* [Girl-atlas](https://github.com/pein0119/girl-atlas-crawler)
* [girl13](https://github.com/xuelangcxy/girlCrawler)
* [github trending](https://github.com/bonfy/github-trending)
* [Github 仓库及用户分析爬虫](https://github.com/chenjiandongx/Github)

### I
* [Instagram](https://github.com/xTEddie/Scrapstagram)
* [INC500 世界5000强爬虫](https://github.com/XetRAHF/Scrapping-INC500)

### J
* [京东](https://github.com/taizilongxu/scrapy_jingdong)
* [京东搜索+评论](https://github.com/Chyroc/JDong)
* [京东商品+评论](https://github.com/samrayleung/jd_spider)
* [机票](https://github.com/fankcoder/findtrip)
* [煎蛋妹纸](https://github.com/kulovecc/jandan_spider)
* [今日头条，网易，腾讯等新闻](https://github.com/lzjqsdd/NewsSpider)

### K
* [看知乎](https://github.com/atonasting/zhihuspider)
* [课程格子校花榜](https://github.com/xinqiu/kechenggezi-Spider)
* [konachan](https://github.com/wudaown/konachanDL)

### L
* [链家](https://github.com/lanbing510/LianJiaSpider)
* [链家成交在售在租房源](https://github.com/XuefengHuang/lianjia-scrawler)
* [拉勾](https://github.com/GuozhuHe/webspider)
* [炉石传说](https://github.com/youfou/hsdata)
* [leetcode](https://github.com/bonfy/leetcode)
* [领英销售导航器爬虫 LinkedInSalesNavigator](https://github.com/XetRAHF/Spider_LinkedInSalesNavigatorURL)

### M
* [马蜂窝(node.js)](https://github.com/golmic/mafengwo-spider)
* [MyCar](https://github.com/Thoxvi/MyCar_python)
* [漫画喵 一键下载漫画~](https://github.com/miaoerduo/cartoon-cat)
* 美女写真套图爬虫 [（一）](https://github.com/chenjiandongx/mmjpg)[（二）](https://github.com/chenjiandongx/mzitu)

### N
* [新闻监控](https://github.com/NolanZhao/news_feed)

### O
* [ofo共享单车爬虫](https://github.com/SilverBooker/ofoSpider)

### P
* [Pixiv](https://github.com/littleVege/pixiv_crawl)
* [PornHub](https://github.com/xiyouMc/WebHubBot)
* [packtpub](https://github.com/niqdev/packtpub-crawler)
* [91porn](https://github.com/eqblog/91_porn_spider)

### Q
* [QQ空间](https://github.com/LiuXingMing/QQSpider)
* [QQ 群](https://github.com/caspartse/QQ-Groups-Spider)
* [清华大学网络学堂爬虫](https://github.com/kehao95/thu_learn)
* [去哪儿](https://github.com/lining0806/QunarSpider)
* [前程无忧Python招聘岗位信息爬取分析](https://github.com/chenjiandongx/51job)

### R
* [人人影视](https://github.com/gnehsoah/yyets-spider)
* [RSS 爬虫](https://github.com/shanelau/rssSpider)
* [rosi 妹子图](https://github.com/evilcos/crawlers)
* [reddit 壁纸](https://github.com/tsarjak/WallpapersFromReddit)
* [reddit](https://github.com/dannyvai/reddit_crawlers)

### S
* [soundcloud](https://github.com/Cortexelus/dadabots)
* [Stackoverflow 100万问答爬虫](https://github.com/chenjiandongx/stackoverflow)
* [Shadowsocks 账号爬虫](https://github.com/chenjiandongx/soksaccounts)


### T
* [tumblr](https://github.com/facert/tumblr_spider)
* [TuShare](https://github.com/waditu/tushare)
* [天猫双12爬虫](https://github.com/LiuXingMing/Tmall1212)
* [Taobao mm](https://github.com/carlonelong/TaobaoMMCrawler)
* [Tmall 女性文胸尺码爬虫](https://github.com/chenjiandongx/cup-size)
* [淘宝直播弹幕爬虫(node)](https://github.com/xiaozhongliu/taobao-live-crawler)

### V
* [视频信息爬虫](https://github.com/billvsme/videoSpider)
* [电影网站](https://github.com/chenqing/spider)

### W
* [乌云公开漏洞](https://github.com/hanc00l/wooyun_public)
* [微信公众号](https://github.com/bowenpay/wechat-spider)
* [“代理”方式抓取微信公众号文章](https://github.com/lijinma/wechat_spider)
* [网易新闻](https://github.com/armysheng/tech163newsSpider)
* [网易精彩评论](https://github.com/dongweiming/commentbox)
* [微博主题搜索分析](https://github.com/luzhijun/weiboSA)
* [网易云音乐](https://github.com/RitterHou/music-163)

### X
* [雪球股票信息(java)](https://github.com/decaywood/XueQiuSuperSpider)
* [新浪微博](https://github.com/LiuXingMing/SinaSpider)
* [新浪微博分布式爬虫](https://github.com/ResolveWang/weibospider)

### Y
* [英美剧 TV (node.js)](https://github.com/pockry/tv-crawler)

### Z
* [ZOL 手机壁纸爬虫](https://github.com/chenjiandongx/wallpaper)
* [知乎(python)](https://github.com/LiuRoy/zhihu_spider)
* [知乎(php)](https://github.com/owner888/phpspider)
* [知网](https://github.com/yanzhou/CnkiSpider)
* [知乎妹子](https://github.com/yjm12321/zhihu-girl)
* [自如实时房源提醒](https://github.com/facert/ziroom_realtime_spider)

### 其他
* [各种爬虫](https://github.com/Nyloner/Nyspider)
* [DHT 爬虫](https://github.com/blueskyz/DHTCrawler)
* [SimDHT](https://github.com/dontcontactme/simDHT)
* [p2pspider](https://github.com/dontcontactme/p2pspider)
