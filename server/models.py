from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash


class User(object):
    """User Model.

    Parameters
    ----------
    username : String
        User name.

    Attributes
    ----------
    tablename : String
        Name of user table.

    """
    tablename = 'user'

    def __init__(self, username):
        self.user = current_app.db[self.tablename].find_one({'username': username})

    def user(self):
        return self.user

    @staticmethod
    def hash_password(password):
        """Hash a password.

        Parameters
        ----------
        password : String
            Password of a user.

        Returns
        -------
        String
            Password hash.

        """
        return generate_password_hash(password)

    def check_password(self, password):
        """Check a password.

        Parameters
        ----------
        password : String
            A password user typed.

        Returns
        -------
        Boolen
            True of False.

        """
        return check_password_hash(self.user['password_hash'], password)


class Blog(object):
    """Blog Model.

    Parameters
    ----------
    slug : String
        The slug of a blog.

    Attributes
    ----------
    tablename : String
        Name of blog table.

    """
    tablename = 'blog'

    def __init__(self, slug):
        self.blog = current_app.db[self.tablename].find_one({'slug': slug})

    def blog(self):
        return self.blog

    @staticmethod
    def blogs(page, limit):
        """Get a blogs page .

        Parameters
        ----------
        page : Int
            Page number.
        limit : Int
            Number of blogs in a page.

        Returns
        -------
        List
            A list of blogs.

        """
        return current_app.db[Blog.tablename].find().skip((page-1)*limit).limit(limit)

    @staticmethod
    def new_blog(title, slug, tags, content):
        """New a blog.

        Parameters
        ----------
        title : String
            Blog title.
        slug : String
            Blog slug.
        tags : List
            Blog tags.
        content : String
            Blog content.

        Returns
        -------
        Object
            Mongodb ObjectId.

        """
        blog = {
            'title': title,
            'slug': slug,
            'tags': tags,
            'content': content,
            'pub_date': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return current_app.db[Blog.tablename].insert_one(blog)

    def update_blog(self, title, slug, tags, content):
        """Update a blog.

        Parameters
        ----------
        title : String
            New title of the blog.
        slug : String
            New slug of the blog.
        tags : List
            New tags of the blog.
        content : String
            New content of the blog.

        Returns
        -------
        Object
            Mongodb ObjectId.

        """
        update = {}
        if self.blog['title'] != title:
            update['title'] = title
        if self.blog['slug'] != slug:
            update['slug'] = slug
        if self.blog['tags'] != tags:
            update['tags'] = tags
        if self.blog['content'] != content:
            update['content'] = content

        _id = self.blog['_id']
        return current_app.db[self.tablename].update_one({'_id': _id}, {'$set': update})

    def delete_blog(self):
        """Delete a blog.

        Parameters
        ----------


        Returns
        -------
        Object
            Mongodb ObjectId.

        """
        _id = self.blog['_id']
        return current_app.db[self.tablename].delete_one({'_id': _id})
