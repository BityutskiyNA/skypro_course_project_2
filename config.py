import os.path

POST_PATH_POSTS = os.path.join("data","data.json")
POST_PATH_COMMENTS = os.path.join("data","comments.json")

LOGGER_API_PATH = os.path.join("logs","api.log")
# LOGGER_API_FORMAT= f"%(asctime)s - [%(levelname)s] - %(name)s - (%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
LOGGER_API_FORMAT= f"%(asctime)s [%(levelname)s] %(message)s"

