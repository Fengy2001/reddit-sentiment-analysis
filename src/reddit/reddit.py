from reddit_driver import reddit_driver
import requests
import json

class reddit:
    def __init__(self, subreddit, account, secrets):
        self.subreddit = subreddit
        self.driver = reddit_driver(account, secrets)
        self.reddit_url = "https://oauth.reddit.com"
        self.posts = {}

    def get_new_posts(self):
        subreddit_new_url = self.reddit_url+"/r/"+self.subreddit+"/new?limit=10"
        response = requests.get(subreddit_new_url, headers=self.driver.get_header()).json()
        for post in response["data"]["children"]:
            if (post["data"]["title"] not in self.posts):
                self.posts[post["data"]["title"]] = post["data"]["id"]

        print(self.posts)

    def get_new_comments(self):
        subreddit_new_url = self.reddit_url+"/comments/1k0tt5k.json?sort=new"   
        response = requests.get(subreddit_new_url, headers=self.driver.get_header()).json()
        for comment in response[1]["data"]["children"]:
            if "body" in comment["data"]:
                print(comment["data"]["body"])

test = reddit("wallstreetbets", "default_account", "WSB-data-gathering")
test.get_new_comments()