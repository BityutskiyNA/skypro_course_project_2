import pytest
import app as main
import json


class TestApi:
    post_keys = {'poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk'}

    @pytest.fixture
    def app_instance(self):
        app = main.app
        test_client = app.test_client()
        return test_client

    def test_all_post(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects = True)
        assert result.status_code == 200

    def test_one_post(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        assert result.status_code == 200

    def test_one_post_not_exist(self, app_instance):
        result = app_instance.get("/api/posts/0", follow_redirects=True)
        assert result.status_code == 500

    def test_single_post_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post =result.get_json()
        post_keys = set(post.keys())
        assert post_keys == self.post_keys

    def test_single_post_has_correct_type(self, app_instance):
        result = app_instance.get("/api/posts/1", follow_redirects=True)
        post =json.loads(result.data)

        assert type(post) == dict, "Не коррентный тип возвращаемых данных у /api/posts/х"

    def test_all_post_has_correct_keys(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        posts = result.get_json()
        for post in posts:
            assert set(post.keys()) == self.post_keys, "Не правильные ключи"

    def test_all_post_has_correct_type(self, app_instance):
        result = app_instance.get("/api/posts", follow_redirects=True)
        post =json.loads(result.data)
        assert type(post) == list, "Не коррентный тип возвращаемых данных у /api/posts"


