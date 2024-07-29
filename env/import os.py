import os
from steam_web_api import Steam

KEY = os.environ.get('steam_project')
steam = Steam(KEY)

steam.users.search_user("the12thchairman")