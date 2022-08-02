from flask import Flask, render_template, request

from bp_api.views import bp_api
from bp_post.views import bp_post
import config_logger


from exceptions.exceptions import DataSourceError


def create_and_config_app(config_path):
    app = Flask(__name__)
    app.register_blueprint(bp_post)
    app.register_blueprint(bp_api, url_prefix='/api')
    app.config.from_pyfile(config_path)
    config_logger.confg(app)
    return app

app = create_and_config_app('config.py')

@app.errorhandler(404)
def page_error_404(error):
    return "Страница отсуствует", 404

@app.errorhandler(500)
def page_error_404(error):
    return "На сервере ошибка", 500

@app.errorhandler(DataSourceError)
def page_error_data_sourse_error(error):
    return "Не корректные данные", 500


if __name__ == '__main__':
    app.run()
