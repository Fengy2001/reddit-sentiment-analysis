import os, time, json, requests, re
import streamlit as st
import pandas as pd
from datasets import Dataset
from reddit import reddit
from sentiment_analysis import sentiment_analysis

def get_posts_of_interest(subreddit):
    posts = subreddit.get_new_posts()
    posts_of_interest = {}
    for post, post_id in posts.items():
        if " Discussion Thread for " in post:
            posts_of_interest[post] = post_id
    
    for post, post_id in posts_of_interest.items():
        subreddit.save_new_comments(post_id)
    
def update(subreddit):
    get_posts_of_interest(subreddit)

def visualize():
    pass

def main():
    wsb = reddit("wallstreetbets","default_account","WSB-data-gathering")
    if (st.button("Update") or reddit_data.empty):
        update(wsb)

reddit_data = pd.DataFrame()
main()