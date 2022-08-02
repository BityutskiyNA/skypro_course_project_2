import pytest

from bp_post.dao.post import Post
from bp_post.dao.post_dao import PostDAO

def check_fields(post):
    fields = ['poster_name', 'poster_avatar', 'pic', 'content', 'views_count', 'likes_count', 'pk']

    for field in fields:
        assert hasattr(post, field), f'нет поля {field}'

class TestPostDao:
    @pytest.fixture
    def post_dao(self):
        post_dao_inst = PostDAO("./bp_post/tests/posts_mock.json")
        return post_dao_inst

    # +++ by_all
    def test_get_all_types(self, post_dao):
        posts = post_dao.get_all()
        assert type(posts) == list, "incorrect type for result"

        post = posts[0]
        assert type(post) == Post, "incorrect type for result item"

    def test_get_all_fields(self, post_dao):
        posts = post_dao.get_all()
        post = posts[0]
        check_fields(post)

    def test_get_all_correct_id(self, post_dao):
        posts = post_dao.get_all()
        correct_pk = {1,2,3}
        pks = set([post.pk for post in posts])
        assert pks == correct_pk, 'не совпадают id'

    def test_get_by_pk_correct_type(self, post_dao):
        post = post_dao.get_by_pk(1)
        assert type(post) == Post, 'не совпадают type'

    def test_get_by_pk_correct_fields(self, post_dao):
        post = post_dao.get_by_pk(1)
        check_fields(post)
    #
    def test_get_by_pk_none(self, post_dao):
        post =  post_dao.get_by_pk(999)
        assert post is None, 'не совпадают id'
    #
    @pytest.mark.parametrize('pk',[1,2,3])
    def test_get_by_pk_correct_id(self, post_dao, pk):
        post = post_dao.get_by_pk(pk)
        assert post.pk == pk, 'не совпадают pk'

    # +++ by_pk

    # +++ by_user
    def test_get_by_user_correct_type(self, post_dao):
        posts = post_dao.get_posts_by_user('leo')
        assert type(posts) == list, "incorrect type for result"
        post = posts[0]
        assert type(post) == Post, 'не совпадают type'

    def test_get_by_user_correct_fields(self, post_dao):
        posts = post_dao.get_posts_by_user('leo')
        post = posts[0]
        check_fields(post)

    def test_get_by_user_correct_id(self, post_dao):
        posts = post_dao.get_posts_by_user('leo')
        correct_pk = {1}
        pks = set([post.pk for post in posts])
        assert pks == correct_pk, 'не совпадают id'
    #--- by_user
