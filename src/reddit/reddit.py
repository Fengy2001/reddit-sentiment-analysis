import os, time, json, requests, re
import pandas as pd
import numpy as np

from reddit_driver import reddit_driver

class reddit:
    def __init__(self, subreddit, account, secrets):
        self.subreddit = subreddit
        self.driver = reddit_driver(account, secrets)
        self.reddit_url = "https://oauth.reddit.com"
        self.posts = {}

    def get_new_posts(self):
        subreddit_new_url = self.reddit_url+"/r/"+self.subreddit+"/new"
        response = requests.get(subreddit_new_url, headers=self.driver.get_header()).json()
        for post in response["data"]["children"]:
            if (post["data"]["title"] not in self.posts):
                self.posts[post["data"]["title"]] = post["data"]["id"]
        return self.posts

    def save_new_comments(self, thread_id):
        try:
            subreddit_new_url = self.reddit_url+f"/comments/{thread_id}.json?sort=new"   
            response = requests.get(subreddit_new_url, headers=self.driver.get_header()).json()
            comments = []
            for comment in response[1]["data"]["children"]:
                if "body" in comment["data"]:
                    if "[removed]" in comment["data"]["body"]:
                        continue
                    sentence = repr(comment["data"]["body"])
                    sentence = re.sub(r"^['\"]+|['\"]+$", "", sentence)
                    sentence = re.sub(r"\\'", "'", sentence)
                    sentence = re.sub(r'\\"', '"', sentence)
                    comments.append(f'"{sentence}"')
            temp_df = pd.DataFrame(comments, columns=["Comments"])
            temp_df = temp_df.dropna()
            temp_df["sentiment"] = np.nan
            if not os.path.exists(self.driver.root+f"\\data\\{time.strftime("%Y-%m-%d")}.csv"):
                temp_df.to_csv(self.driver.root+f"\\data\\{time.strftime("%Y-%m-%d")}.csv", index=False)
            else:
                temp_df.to_csv(self.driver.root+f"\\data\\{time.strftime("%Y-%m-%d")}.csv", index=False, header=False, mode="a")
        except:
            raise("Something went terribly wrong.")
