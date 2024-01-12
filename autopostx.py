import os
import json
import tweepy
from flask import Flask, request, abort

# X API credentials
X_API_KEY = 'your_X_api_key'
X_API_SECRET = 'your_X_api_secret'
X_ACCESS_TOKEN = 'your_X_access_token'
X_ACCESS_SECRET = 'your_X_access_secret'

# GitHub webhook secret (set this when configuring the webhook)
GITHUB_WEBHOOK_SECRET = 'your_github_webhook_secret'

app = Flask(_name_)

def setup_X_api():
    auth = tweepy.OAuthHandler(X_API_KEY, X_API_SECRET)
    auth.set_access_token(X_ACCESS_TOKEN, X_ACCESS_SECRET)
    api = tweepy.API(auth)
    return api

def tweet_repo_creation(repo_name, repo_url):
    api = setup_X_api()
    tweet_text = f"ð New GitHub repository published! ð\n\nRepository: {repo_name}\nURL: {repo_url}"
    api.update_status(status=tweet_text)
    print("Tweeted successfully!")

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    signature = request.headers.get('X-Hub-Signature')
    if not signature or not is_valid_github_signature(signature, request.data):
        abort(401)

    event = request.headers.get('X-GitHub-Event')
    if event == 'create':
        payload = json.loads(request.data)
        repo_name = payload['repository']['name']
        repo_url = payload['repository']['html_url']
        tweet_repo_creation(repo_name, repo_url)

    return 'Webhook received!', 200

def is_valid_github_signature(signature, payload):
    import hmac
    import hashlib
    secret = bytes(GITHUB_WEBHOOK_SECRET, 'utf-8')
    hash_algorithm, github_signature = signature.split('=')
    expected_signature = hmac.new(secret, payload, hashlib.sha1).hexdigest()
    return hmac.compare_digest(github_signature, expected_signature)

if _name_ == '_main_':
    app.run(port=5000)