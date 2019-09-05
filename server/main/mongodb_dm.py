from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash


class User:
    tablename = 'user'

    def __init__(self, app=current_app):
        self.app = app
        self.session = app.db[self.tablename]

    def user(self, username):
        return self.session.find_one({'username': username})

    def check_password(self, username, password):
        doc = self.user(username)
        if doc:
            return check_password_hash(doc['password_hash'], password)

    def insert_one(self, username, password):
        if self.session.find_one({'username': username}):
            self.app.logger.error("User %r is existed", username)
            return None

        else:
            user_info = {
                'username': username,
                'password_hash': generate_password_hash(password)
            }
            return self.session.insert_one(user_info)


class Blog:
    tablename = 'blog'

    def __init__(self, app=current_app):
        self.app = app
        self.session = app.db[self.tablename]

    def blog(self, id):
        return self.session.find_one({'_id': id})

    def blogs(self, page, limit):
        return self.session.find().skip((page-1)*limit).limit(limit)

    def insert_one(self, title, author, tags, content, publish_time=None):
        if self.session.find_one({'title': title}):
            self.app.logger.error("Title %r is existed", title)
            return None

        else:
            def blog_id():  # 记录最新id值，用来控制id自动增长
                id_coll = self.app.db['blog_id'].find_one()
                if id_coll:
                    id = id_coll['current_id']
                    self.app.db['blog_id'].update_one({'current_id': id}, {'$set': {'current_id': id + 1}})
                    return id + 1
                else:
                    self.app.db['blog_id'].insert_one({'current_id': 1})
                    return 1

            blog_info = {
                '_id': blog_id(),
                'title': title,
                'author': author,
                'tags': tags,
                'content': content,
                'publish_time': publish_time or datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return self.session.insert_one(blog_info)

    def update_one(self, id, title, author, tags, content):
        if self.blog(id):
            update = {
                'title': title,
                'author': author,
                'tags': tags,
                'content': content
            }
            return self.session.update_one({'_id': id}, {'$set': update})
        else:
            return None

    def delete_one(self, id):
        self.session.delete_one({'_id': id})
