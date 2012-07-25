#-*- coding:utf-8 -*-
from chartnet import db
from chartnet.setting import EACH_PAGE_POST_NUM
from datetime import datetime
from time import time

class User(db.Model):
	__tablename__ = 'sp_user'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(45), nullable=False)
	password = db.Column(db.String(45), nullable=False)

	def __init__(self,name=None,password=None):
		self.name = name
		self.password = password

	def __repr__(self):
		return '<User %r>' % self.name

class AboutReply(db.Model):
	__tablename__ = 'about_reply'
	id = db.Column(db.Integer, primary_key=True)
	author = db.Column(db.String(45), nullable=False)
	email = db.Column(db.String(100), nullable=False)
	url = db.Column(db.String(200), nullable=False)
	comment = db.Column(db.String(400), nullable=False)
	reply_date = db.Column(db.DateTime, nullable=False)
	so_good = db.Column(db.Integer, nullable=False)
	so_bad = db.Column(db.Integer, nullable=False)
	parent_id = db.Column(db.Integer)

	def __init__(self, author, email, url, comment, so_good=0, so_bad=0, parent_id=None):
		self.author = author
		self.email = email
		self.url = url
		self.comment = comment
		self.parent_id = parent_id
		self.so_good = so_good
		self.so_bad = so_bad
		self.reply_date = datetime.now()

	def __repr__(self):
		return '<AboutReply %r>' % self.author

class Article(db.Model):
	__tablename__ = 'sp_posts'
	_id = db.Column('id',db.Integer, primary_key=True)
	_category = db.Column('category',db.String(17), nullable=False)
	_title = db.Column('title',db.String(100), nullable=False)
	_content = db.Column('content',db.Text, nullable=False)
	_comment_num = db.Column('comment_num',db.Integer, nullable=False)
	_closecomment = db.Column('closecomment',db.Integer, nullable=False)
	_tags = db.Column('tags',db.String(100), nullable=True)
	_password = db.Column('password',db.String(8), nullable=True)
	_add_time = db.Column('add_time',db.Integer, nullable=False)
	_edit_time = db.Column('edit_time',db.Integer, nullable=False)
	_shorten_content = db.Column('shorten_content',db.String(200), nullable=True)

	def __init__(self,_category='', _title='', _content='', _comment_num=0, _closecomment=0, _tags=None, _password=None, _shorten_content='', _add_time=0, _edit_time=0):
		self._category = _category
		self._title = _title
		self._content = _content
		self._comment_num = _comment_num
		self._closecomment = _closecomment
		self._tags = _tags
		self._password = _password
		self._add_time = _add_time
		self._edit_time = _edit_time
		self._shorten_content = _shorten_content
	
	def __repr__(self):
		return '<Article %r>' % self._title

class Link(db.Model):
	__tablename__ = 'sp_links'
	id = db.Column('id',db.Integer, primary_key=True)
	displayorder = db.Column('displayorder',db.Integer, nullable=False)
	name = db.Column('name',db.String(100), nullable=False)
	url = db.Column('url',db.String(100), nullable=False)

	def __init__(self,name=None,displayorder=None,url=None):
		self.name = name
		self.displayorder = displayorder
		self.url = url

	def __repr__(self):
		return '<Link %r>' % self.name

class Category(db.Model):
	__tablename__ = 'sp_category'
	id = db.Column('id',db.Integer, primary_key=True)
	name = db.Column('name',db.String(17), nullable=False)
	id_num = db.Column('id_num',db.Integer, nullable=False)
	content = db.Column('content',db.Text, nullable=False)

	def __init__(self,name=None,id_num=None,content=None):
		self.name = name
		self.id_num = id_num
		self.content = content

	def __repr__(self):
		return '<Category %r>' % self.name

class Tag(db.Model):
	__tablename__ = 'sp_tags'
	id = db.Column('id',db.Integer, primary_key=True)
	name = db.Column('name',db.String(17), nullable=False)
	id_num = db.Column('id_num',db.Integer, nullable=False)
	content = db.Column('content',db.Text, nullable=False)

	def __init__(self,name=None,id_num=None,content=None):
		self.name = name
		self.id_num = id_num
		self.content = content

	def __repr__(self):
		return '<Tag %r>' % self.name

class Comment(db.Model):
	__tablename__ = 'sp_comments'
	id = db.Column('id',db.Integer, primary_key=True)
	postid = db.Column('postid',db.Integer, primary_key=True)
	author = db.Column('author',db.String(20), nullable=True)
	email = db.Column('email',db.String(30), nullable=True)
	url = db.Column('url',db.String(75), nullable=True)
	visible = db.Column('visible',db.Integer, nullable=True)
	add_time = db.Column('add_time',db.Integer, nullable=False)
	content = db.Column('content',db.Text, nullable=False)

	def __init__(self,postid=None,author=None,email=None,url=None,visible=None,content=None,):
		self.postid = postid
		self.author = author
		self.email = email
		self.url = url
		self.visible = visible
		self.add_time = int(time())
		self.content = content

	def __repr__(self):
		return '<Comment %r>' % self.content

class OperatorDB:

#operator AboutReply 2012/6/7
	def getAboutReplyAll(self):
		return AboutReply.query.order_by(AboutReply.reply_date.desc()).all()
	
	def insertAboutReply(self,author, email, url, comment, parent_id=None):
		aboutReply = AboutReply(author,email,url,comment)
		db.session.add(aboutReply)
		db.session.commit()

	def addSogood(self,_id):
		updateSql = 'update about_reply set so_good=so_good+1 where id=%s' % _id
		db.session.execute(updateSql)
		db.session.commit()
	
	def addSobad(self,_id):
		updateSql = 'update about_reply set so_bad=so_bad+1 where id=%s' % _id
		db.session.execute(updateSql)
		db.session.commit()

#operator Article 2012/6/7
	def get_post_page(self,_start=0,_end=20):
		sumSize = len(Article.query.all())
		_newer = _start > 0
		_older = sumSize>_end
		return Article.query.order_by(Article._add_time.desc()).all()[_start:_end],_newer,_older

	def get_post_page_category(self,_start,_end,cat):
		return Article.query.order_by(Article._add_time.desc()).filter_by(_category=cat).all()[_start:_end]

	def get_post_page_tags(self,_start,_end,tags):
		return Article.query.order_by(Article._add_time.desc()).filter(Article._tags.contains(tags)).all()[_start:_end]
	
	def get_post_older_newer(self,postid):
		_older = Article.query.order_by(Article._id.desc()).filter(Article._id<postid).first()
		_newer = Article.query.order_by(Article._id.asc()).filter(Article._id>postid).first()
		return _older,_newer

	def get_max_id(self):
		result = db.session.execute("select max(id) as maxid from `sp_posts`")
		maxid = 0
		for row in result:
			if row['maxid']:
				maxid = row['maxid']
		result.close()
		return maxid

	def get_last_post_add_time(self):
		result = db.session.execute("SELECT `add_time` FROM `sp_posts` ORDER BY `id` DESC LIMIT 1")
		add_time = 0
		for row in result:
			if row['add_time']:
				add_time = row['add_time']
		result.close()
		return add_time

	def get_last_post_edit_time(self):
		result = db.session.execute("SELECT `edit_time` FROM `sp_posts` ORDER BY `id` DESC LIMIT 1")
		edit_time = 0
		for row in result:
			if row['edit_time']:
				edit_time = row['edit_time']
		result.close()
		return edit_time
	
	def add_new_article(self, category,title,content,tags,password,shorten_content):
		timestamp = int(time())		
		_article = Article(category,title,content,0,0,tags,password,shorten_content,timestamp,timestamp)
		db.session.add(_article)
		db.session.commit()
		return _article._id

	def update_article(self, id,category,title,content,tags,password,shorten_content):
		timestamp = int(time())		
		_article = Article.query.filter_by(_id=id).first()
		_article._category = category
		_article._title = title
		_article._content = content
		_article._tags = tags
		_article._password = password
		_article._shorten_content = shorten_content
		_article._edit_time = timestamp
		db.session.commit()

	def add_new_comment(self,postid,author,email,url,visible,content):
		comment = Comment(postid,author,email,url,visible,content)
		db.session.add(comment)
		_article = Article.query.filter_by(_id=postid).first()
		_article._comment_num = _article._comment_num+1
		db.session.commit()
		return comment.id

	#回复
	def get_post_comments(self,postid):
		return Comment.query.order_by(Comment.add_time.desc()).filter_by(postid=postid).all()

	def get_comments_new(self,count=5):
		return Comment.query.order_by(Comment.add_time.desc()).all()[:count]
	
	def get_comment_by_id(self,id):
		return Comment.query.fiter_by(id=id).first()

	def del_comment_by_id(self,id):
		db.session.execute('delete from `sp_comments` where id=%s' % id)
		db.session.commit()
	
	#查询文章详情
	def detail_post_by_id(self, _id=''):
		if _id:
			return Article.query.filter_by(_id=_id).first()
	
	#删除文章
	def del_post_by_id(self, _id = ''):
		_article = Article.query.filter_by(_id=_id).first()
		if _article:
			db.session.execute('DELETE FROM `sp_posts` WHERE `id` = %s LIMIT 1' % _id)
			db.session.execute('DELETE FROM `sp_comments` WHERE `postid` = %s LIMIT %s' % (_id,_article._comment_num))
			db.session.commit()
	
	def get_post_for_homepage(self):
		return Article.query.order_by(Article._id.desc()).all()[:EACH_PAGE_POST_NUM]
	
	#用户登录
	def login_user(self,name='',password=''):
		result = db.session.execute("SELECT `id` FROM `sp_user` WHERE `name`='%s' and `password`='%s'" % (name,password))
		for row in result:
			if row['id']:
				return True
		return False
	
	def has_user(self):
		result = db.session.execute("select`id` from `sp_user` LIMIT 1")
		for row in result:
			if row['id']:
				return True
		return False

	def add_user(self,name='',password=''):
		_user = User(name,password)
		db.session.add(_user)
		db.session.commit()
		
	#link
	def get_all_links(self):
		return Link.query.order_by(Link.displayorder.asc()).all()

	def add_new_link(self, name, displayorder, url):
		_link = Link(name, displayorder, url)
		db.session.add(_link)
		db.session.commit()
	
	def update_link_edit(self, id, name, displayorder, url):
		_link = Link.query.filter_by(id=id).first()
		_link.name = name
		_link.displayorder = displayorder
		_link.url = url
		#db.session.update(_link)
		db.session.commit()

	def get_link_by_id(self, id):
		return Link.query.filter_by(id=id).first()
	
	def del_link_by_id(self, id):
		db.session.execute("DELETE FROM `sp_links` WHERE `id` = %s LIMIT 1" % id)
		db.session.commit()
	
	#类别
	def get_all_cat_name(self):
		return Category.query.order_by(Category.name.asc()).all()
	
	def add_postid_to_cat(self, name = '', postid = ''):
		_category = Category.query.filter_by(name=name).first()
		if _category:
			_category.id_num = _category.id_num+1
			_category.content = postid+','+_category.content
		else:
			_category = Category(name,1,postid)
			db.session.add(_category)
		db.session.commit()
	
	#标签2012/6/26
	def get_all_tag_name(self):
		return Tag.query.order_by(Tag.id_num.asc()).all()[:10]
	
	def add_postid_to_tags(self, tags = [], postid = ''):
		for tag_name in tags:
			_tag = Tag.query.filter_by(name=tag_name).first()
			if _tag:
				_tag.id_num = _tag.id_num+1
				_tag.content = postid+','+_tag.content
			else:
				_tag = Tag(tag_name,1,postid)
				db.session.add(_tag)
		db.session.commit()

operatorDB = OperatorDB()
