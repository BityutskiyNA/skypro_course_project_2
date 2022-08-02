import json
from pprint import pprint as pp
from bp_post.dao.post import Post
from exceptions.exceptions import DataSourceError


class PostDAO:
    def __init__(self, path):
        self.path = path

    @property
    def _load(self):
        """
        Загружаем данные из файла
        """
        try:
            file = open(self.path, encoding="utf-8")
            posts = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataSourceError()

        return posts


    def _load_posts(self):
        """
        Создаем объекты посты из данных
        """
        posts = self._load
        list_of_post = [Post(**posts_data) for posts_data in posts]
        return list_of_post

    def get_all(self):
        """
        Возвращаем все посты
        """
        posts = self._load_posts()
        return posts

    def get_by_pk(self, pk):
        """
        Получаем пост по pk
        """
        if type(pk) != int:
            raise TypeError('pk должен быть int')

        posts = self._load_posts()
        for post in posts:
            if post.pk == pk:
                return post

    def search_in_content(self, substring):
        """
            – возвращает список постов по ключевому слову
        """
        substring = str(substring).upper()
        posts = self._load_posts()
        found_posts = [post for post in posts if substring in post.content.upper()]

        return found_posts

    def get_posts_by_user(self, poster_name):
        """
            – возвращает посты определенного пользователя
        """
        poster_name = str(poster_name)
        posts = self._load_posts()
        found_posts = [post for post in posts if poster_name == post.poster_name]
        return found_posts

