from authentication import reddit_auth

class reddit:
    def __init__(self, subreddit, account, secrets):
        self.subreddit = subreddit
        self.authenticator = reddit_auth(account, secrets)

    def get_new_posts(self):
        new_url = self.authenticator.reddit_url+"/r"+self.subreddit+"/new"
        