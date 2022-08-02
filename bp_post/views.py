from flask import Flask, render_template, current_app, request
from werkzeug.exceptions import abort
from flask import Blueprint
from bp_post.dao.post_dao import PostDAO
from bp_post.dao.comment_dao import CommentDAO
from config import POST_PATH_POSTS, POST_PATH_COMMENTS

bp_post = Blueprint('bp_posts',__name__, template_folder='templates')
# DATA_PATH_POST = current_app.config['POST_PATH_POST']
postDAO = PostDAO(POST_PATH_POSTS)
commentsDAO = CommentDAO(POST_PATH_COMMENTS)

@bp_post.route('/')
def page_post_index():
    all_post = postDAO.get_all()
    return render_template('index.html', items = all_post)

@bp_post.route('/posts/<int:postid>')
def get_post(postid):
    post = postDAO.get_by_pk(postid)
    if post is None:
        abort('404')
    comments = commentsDAO.get_by_pk(postid)
    # comments = []
    return render_template('post.html', item=post, comments=comments)

@bp_post.route('/users/<users>')
def get_search_users(users):
    posts = postDAO.get_posts_by_user(users)
    return render_template('user-feed.html', items=posts)

@bp_post.route('/search/')
def get_search():
    s = request.args['s']
    posts = postDAO.search_in_content(s)
    return render_template('search.html', items=posts)
