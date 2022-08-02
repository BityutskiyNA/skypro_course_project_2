import json
from bp_post.dao.comment import Comment
from exceptions.exceptions import DataSourceError


class CommentDAO:
    def __init__(self, path):
        self.path = path

    @property
    def _load(self):
        """
            Загружаем данные из файла
        """
        try:
            file = open(self.path, encoding="utf-8")
            comments = json.load(file)
        except(FileNotFoundError, json.JSONDecodeError):
            raise DataSourceError()

        return comments

    def _load_comments(self):
        """
            Создаем объекты из загруженных данных
        """
        commets = self._load
        list_of_comment = [Comment(**comment_data) for comment_data in commets]
        return list_of_comment

    def get_all(self):
        """
            Возвращаем все комментарии
        """
        comments = self._load_comments()
        return comments

    def get_by_pk(self, post_id: int) -> list[Comment]:
        """
            - Получаем комментарии по pk
        """
        comments: list[Comment] = self._load_comments()
        found_posts: list[Comment] = [comment for comment in comments if post_id == comment.post_id]

        return found_posts
