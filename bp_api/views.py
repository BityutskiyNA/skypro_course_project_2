import logging

from flask import Blueprint, jsonify
from bp_post.dao.post_dao import PostDAO
from bp_post.dao.comment_dao import CommentDAO
from config import POST_PATH_POSTS, POST_PATH_COMMENTS

bp_api = Blueprint('bp_api',__name__)
postDAO = PostDAO(POST_PATH_POSTS)
commentsDAO = CommentDAO(POST_PATH_COMMENTS)
api_logger = logging.getLogger("api_logger")

@bp_api.route('/posts/')
def api_post_all():
    posts = postDAO.get_all()
    api_logger.info("Запрос /api/posts")
    return jsonify([post.as_dict() for post in posts])

@bp_api.route('/posts/<int:pk>/')
def api_post_single(pk: int):
    posts = postDAO.get_by_pk(pk)
    api_logger.info(f"Запрос /api/posts/{pk}")
    return jsonify(posts.as_dict())

