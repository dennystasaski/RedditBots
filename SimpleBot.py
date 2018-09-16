import praw
import config

def bot_login():
	print('Attempting to log in')
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "A very cool bot v0.1")
	print('Successfully logged in')
	return r

def reply_to_comment(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "sir" in comment.body:
			comment.reply('I am testing my bot.  Congrats!')

def submit_text_post(r):
	r.subreddit('test').submit('Test text post', selftext='I am a bot noob', url=None, flair_id=None, flair_text=None, resubmit=True, send_replies=True)

r = bot_login()
reply_to_comment(r)
submit_text_post(r)