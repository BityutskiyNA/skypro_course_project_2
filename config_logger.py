import logging

def confg(app):
    api_logger = logging.getLogger('api_logger')
    api_logger.setLevel(logging.INFO)

    api_logger_handler = logging.FileHandler(filename=app.config["LOGGER_API_PATH"], encoding="utf-8")
    api_logger_handler.setLevel(logging.INFO)
    api_logger.addHandler(api_logger_handler)

    api_logger_format = logging.Formatter(app.config["LOGGER_API_FORMAT"])
    api_logger_handler.setFormatter(api_logger_format)