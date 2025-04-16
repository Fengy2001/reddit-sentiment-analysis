import os
import json
import requests
import requests.auth

root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))

def get_account_deets(account):
    with open(os.path.join(root, "src/no-commit/accounts.json"), "r") as file:
        json_data = json.load(file)
        username = json_data[account]["username"]
        password = json_data[account]["password"]
    return username, password

def get_secret(client_id):
    with open(os.path.join(root, "src/no-commit/secrets.json"), "r") as file:
        json_data = json.load(file)
        secret_id = json_data[client_id][0]
        secret_pwd = json_data[client_id][1]
    return secret_id, secret_pwd

def get_access_token(account = "default_account", client_id = "WSB-data-gathering"):
    username, password = get_account_deets(account)
    secret_id, secret_pwd= get_secret(client_id)

    reddit_token_url = "https://www.reddit.com/api/v1/access_token"
    authentication = requests.auth.HTTPBasicAuth(secret_id, secret_pwd)
    account_data = {
        "grant_type":"password",
        "username": username,
        "password": password
    }
    headers = {"User-Agent":"Python-Reddit-app"}
    
    response = requests.post(
        reddit_token_url,
        auth=authentication,
        data=account_data,
        headers=headers
    )
    
    if (response.status_code == 200):
        return response.json().get("access_token")
    else:
        return PermissionError("Request was not proccessed.")
    