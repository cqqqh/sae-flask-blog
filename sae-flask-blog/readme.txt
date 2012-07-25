是一款运行在SAE/python上轻型的、基于FLASK框架的blog程序。
版本号为v0.0.1，示例 http://chartnet.sinaapp.com/
此项目是基于新浪的sae平台开发，采用FLASK框架，参照SAEpy-log进行了重写。
由于本人初步使用和学习PYTHON及FLASK，代码中会存在很多不合理的地方。

使用到的部分技术：
python+flask+sae：系统构建的基石
数据库访问：sqlalchemy，使用了flask-sqlalchemy扩展
jquery+markitup+highlight：界面展现的相关组件，markitup为在线编辑器，highlight为高亮显示（Sunburst风格）。
markitup：http://markitup.jaysalvat.com/home/
highlight：http://softwaremaniacs.org/soft/highlight/en/
摘要截取：采用正则表达式
附件上传：uploadify v2.1.4
附件存储：sae storage
图片压缩：PIL模块

已实现的功能：
日志的添加、修改、删除、浏览
日志信息的评论添加
评论管理
后台管理的登陆
未来想实现及优化的功能：

包含图片的日志，上下滚动页面，响应速度缓慢的问题。
类别及标签的翻页
相册功能