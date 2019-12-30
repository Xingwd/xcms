# -*- coding: UTF-8 -*-
import pytest
import json
from main import db
from main.models import BlogPost as Post, BlogCategory as Category


@pytest.fixture()
def init(app):
    with app.app_context():
        category1 = Category(name='c1')
        category2 = Category(name='c2')
        post1 = Post(title='Testing Title1', body='I am testing data.')
        post2 = Post(title='Testing Title2', body='')
        category1.posts.append(post1)
        category2.posts.append(post2)
        db.session.add(category1)
        db.session.add(category2)
        db.session.commit()


class TestPost:
    BASE_URI = '/xcms/blog/api/v1.0/posts'

    def test_get_posts(self, init, client):
        # category不存在
        assert client.get(self.BASE_URI + '?category_name=c10').status_code == 404
        # 全部数据
        resp1 = client.get(self.BASE_URI)
        assert resp1.status_code == 200
        assert len(json.loads(resp1.data).get('posts', [])) == 2
        # 属于c1的数据
        resp2 = client.get(self.BASE_URI + '?category_name=c1')
        assert resp2.status_code == 200
        assert len(json.loads(resp2.data).get('posts', [])) == 1

    def test_get_post(self, init, client):
        # post不存在
        assert client.get(self.BASE_URI + '/10').status_code == 404
        # post.id = 1
        resp = client.get(self.BASE_URI + '/1')
        assert resp.status_code == 200
        assert json.loads(resp.data).get('title') == 'Testing Title1'

    def test_create_post(self, init, auth, client):
        # 认证失败
        assert client.post(self.BASE_URI).status_code == 401
        # 没有request.json
        assert client.post(self.BASE_URI, headers=auth).status_code == 400
        # request.json中有category_name，没有title
        assert client.post(self.BASE_URI, headers=auth, json={'category_name': 'c1'}).status_code == 400
        # request.json中有title，没有category_name
        assert client.post(self.BASE_URI, headers=auth, json={'title': 'Title'}).status_code == 400
        # category不存在
        assert client.post(self.BASE_URI, headers=auth, json={'title': 'Title', 'category_name': 'c10'}).status_code == 404
        # 成功创建
        data = {
            'title': 'Create Testing Title',
            'body': 'I am testing data.',
            'category_name': 'c1'
        }
        assert client.post(self.BASE_URI, headers=auth, json=data).status_code == 201
        # 验证创建
        assert json.loads(client.get(self.BASE_URI + '/3').data).get('title') == 'Create Testing Title'

    def test_update_post(self, init, auth, client):
        # 认证失败
        assert client.put(self.BASE_URI + '/1').status_code == 401
        # 没有request.json
        assert client.put(self.BASE_URI + '/1', headers=auth).status_code == 400
        # 没有request.json['title']
        assert client.put(self.BASE_URI + '/1', headers=auth, json={}).status_code == 400
        # 没有找到post
        assert client.put(self.BASE_URI + '/10', headers=auth, json={'title': 'Update Title'}).status_code == 404
        # 成功更新
        data = {
            'title': 'Upate Testing Tilte',
            'body': 'I am testing data.',
            'category_name': 'c1'
        }
        assert client.put(self.BASE_URI + '/1', headers=auth, json=data).status_code == 201
        # 验证更新
        assert json.loads(client.get(self.BASE_URI + '/1').data).get('title') == 'Upate Testing Tilte'

    def test_delete_post(self, init, auth, client):
        # 认证失败
        assert client.delete(self.BASE_URI + '/1').status_code == 401
        # 没有找到post
        assert client.delete(self.BASE_URI + '/10', headers=auth).status_code == 404
        # 删除成功
        assert client.delete(self.BASE_URI + '/1', headers=auth).status_code == 201
        # 验证删除
        assert client.get(self.BASE_URI + '/1').status_code == 404


class TestCategory:
    BASE_URI = '/xcms/blog/api/v1.0/categories'

    def test_get_categories(self, init, client):
        # 全部数据
        resp = client.get(self.BASE_URI)
        assert resp.status_code == 200
        assert len(json.loads(resp.data)) == 2

    def test_get_category(self, init, client):
        # category不存在
        assert client.get(self.BASE_URI + '/10').status_code == 404
        # category.id = 1
        resp = client.get(self.BASE_URI + '/1')
        assert resp.status_code == 200
        assert json.loads(resp.data).get('id') == 1

    def test_create_category(self, init, auth, client):
        # 认证失败
        assert client.post(self.BASE_URI).status_code == 401
        # 没有request.json
        assert client.post(self.BASE_URI, headers=auth).status_code == 400
        # 没有request.json['name']
        assert client.post(self.BASE_URI, headers=auth, json={}).status_code == 400
        # 成功创建
        data = {
            'name': 'Testing'
        }
        assert client.post(self.BASE_URI, headers=auth, json=data).status_code == 201
        # 验证创建
        assert json.loads(client.get(self.BASE_URI + '/3').data).get('name') == 'Testing'

    def test_update_category(self, init, auth, client):
        # 认证失败
        assert client.put(self.BASE_URI + '/1').status_code == 401
        # 没有request.json
        assert client.put(self.BASE_URI + '/1', headers=auth).status_code == 400
        # 没有request.json['name']
        assert client.put(self.BASE_URI + '/1', headers=auth, json={}).status_code == 400
        # 成功更新
        data = {
            'name': 'New c1'
        }
        assert client.put(self.BASE_URI + '/1', headers=auth, json=data).status_code == 201
        # 验证更新
        assert json.loads(client.get(self.BASE_URI + '/1').data).get('name') == 'New c1'

    def test_delete_category(self, init, auth, client):
        # 认证失败
        assert client.delete(self.BASE_URI + '/10').status_code == 401
        # 没有找到category
        assert client.delete(self.BASE_URI + '/10', headers=auth).status_code == 404
        # 删除成功
        assert client.delete(self.BASE_URI + '/1', headers=auth).status_code == 201
        # 验证删除
        assert client.get(self.BASE_URI + '/1').status_code == 404
        # 验证post.category_id
        resp = client.get(TestPost.BASE_URI + '/1')
        assert json.loads(resp.data).get('category_id') is None
        assert json.loads(resp.data).get('category_name') is None
