#-*- coding:utf-8 -*-
import sae.const
#分类明细
HEAD_SUBCATEGORY = {u'wenzhang':[(u'首页','/'),(u'生活',''),(u'人物','')],u'xiangce':[(u'首页','/'),(u'家庭',''),(u'风景',''),(u'QQ空间','')],u'yule':[(u'首页','/'),(u'幽默',''),(u'游戏','')],u'链接':(),'about':[(u'首页','/'),(u'关于','#')]}
#分页大小
EACH_PAGE_POST_NUM = 10
#主页
BASE_URL = 'http://chartnet.sinaapp.com/'
#网站名称
SITE_TITLE = "Countryside's house"
#使用SAE Storage 服务（保存上传的附件），需在SAE管理面板创建
STORAGE_DOMAIN_NAME = 'attachment' 
debug = True
#MYSQL配置信息
MYSQL_USER = 'root'
MYSQL_PASS = 'java2002'
MYSQL_HOST_M = '127.0.0.1'
MYSQL_HOST_S = '127.0.0.1'
MYSQL_PORT = '3306'
MYSQL_DB = 'sae_chouse'

#MYSQL_USER = sae.const.MYSQL_USER
#MYSQL_PASS = sae.const.MYSQL_PASS
#MYSQL_HOST_M = sae.const.MYSQL_HOST
#MYSQL_HOST_S = sae.const.MYSQL_HOST_S
#MYSQL_PORT = sae.const.MYSQL_PORT
#MYSQL_DB = sae.const.MYSQL_DB