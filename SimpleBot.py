import praw
import config

def bot_login():
	print("Attempting to log in")
	r = praw.Reddit(username = config.username,
			password = config.password,
			client_id = config.client_id,
			client_secret = config.client_secret,
			user_agent = "A very cool bot v0.1")
	print("Successfully logged in")
	return r

def reply_to_comment(r):
	for comment in r.subreddit('test').comments(limit=25):
		if "sir" in comment.body:
			comment.reply("I am testing my bot.  Congrats!")

def submit_text_post(r):
	r.submit('test', 'My cool bot\'s first post!', text='Test body')
r = bot_login()
# loop here for constant running
# reply_to_comment(r)
submit_text_post(r)