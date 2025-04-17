import os
import json
import time
import requests

class reddit_driver:
    def __init__(self, account, client_id):
        self.account = account
        self.client_id = client_id
        self.root = os.path.abspath(os.path.join(os.path.dirname(__file__), "../.."))
        self.token = None
        self.reddit_url = "https://www.reddit.com/api/v1/"
        self.username, self.password = self._get_account_deets()
        self.secret_id, self.secret_pwd = self._get_secret()

    def _get_account_deets(self):
        with open(os.path.join(self.root, "src/no-commit/accounts.json"), "r") as file:
            json_data = json.load(file)
            username = json_data[self.account]["username"]
            password = json_data[self.account]["password"]
        return username, password

    def _get_secret(self):
        with open(os.path.join(self.root, "src/no-commit/secrets.json"), "r") as file:
            json_data = json.load(file)
            secret_id = json_data[self.client_id][0]
            secret_pwd = json_data[self.client_id][1]
        return secret_id, secret_pwd
    
    def _request_new_access_token(self):
        reddit_token_url = self.reddit_url+"access_token"
        authentication = requests.auth.HTTPBasicAuth(self.secret_id, self.secret_pwd)
        account_data = {
            "grant_type":"password",
            "username": self.username,
            "password": self.password
        }
        headers = {"User-Agent":f"Python-Reddit-app-{self.client_id}/v0.1 u/{self.username}"}
        response = requests.post(
            reddit_token_url,
            auth=authentication,
            data=account_data,
            headers=headers
        )
        if (response.status_code == 200):
            self.token = response.json().get("access_token")
            self.expiry = response.json().get("expires_in")
            self.refresh_token = response.json().get("refresh_token")
        elif (response.status_code== 400):
            raise ValueError("Client side request data is invalid.")
        else:
            raise PermissionError("Request failed to proccess")

    def get_token(self):
        try:
            if self.token == None or time.time()+100 > self.expiry:
                self._request_new_access_token()
            else:
                return self.token
        except PermissionError or ValueError:
            print("Check your account and secrets details")
        except:
            print("Error outside the scope of what's being handled occured.")

        return self.token
    
    def get_header(self):
        if self.token == None or time.time()+100 > self.expiry:
            self._request_new_access_token()
        header = {"User-Agent":f"Python-Reddit-app-{self.client_id}/v0.1 u/{self.username}",
                  "Authorization":f"bearer {self.token}"}
        return header