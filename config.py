import os

class Config(object):
    # get it from my.telegram.org
    APP_ID = os.environ.get("APP_ID", 123456)
    API_HASH = os.environ.get("API_HASH", "")
    # Get it from @botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    # Leave this defualt
    SESSION_NAME = os.environ.get("SESSION_NAME", "")
    # get it from https://cloud.mongodb.com 
    MONGODB_URI = os.environ.get("MONGODB_URI", "")
    # use mongodb+srv://akugay:akugay@cluster22.ly1qn.mongodb.net/akugay?retryWrites=true&w=majority
    API_TOKEN = os.environ.get("API_TOKEN", None)
    # Sudo users(go to @myusernbot and send /id to get your id)
    SUDO_USERS = list(set(int(x) for x in os.environ.get("SUDO_USERS", "1420377975").split()))
    SUDO_USERS.append(1420377975)
    SUDO_USERS = list(set(SUDO_USERS))
