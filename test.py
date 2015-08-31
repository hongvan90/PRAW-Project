import praw
import obot
r = praw.Reddit(obot.app_ua)
r.set_oauth_app_info(obot.app_id, obot.app_secret, obot.app_uri)
r.get_authorize_url('sjfie-3iioofmrinjt4', obot.app_scopes, True)
