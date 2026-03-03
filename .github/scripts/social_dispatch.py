import os
import sys
import tweepy
import requests
from requests_oauthlib import OAuth1Session

# --- SOCIAL MEDIA DISPATCH ---

TWITTER_CONSUMER_KEY = os.environ.get("TWITTER_CONSUMER_KEY")
TWITTER_CONSUMER_SECRET = os.environ.get("TWITTER_CONSUMER_SECRET")
TWITTER_ACCESS_TOKEN = os.environ.get("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_TOKEN_SECRET = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")
LINKEDIN_ACCESS_TOKEN = os.environ.get("LINKEDIN_ACCESS_TOKEN")

def post_to_twitter(text):
    if not TWITTER_CONSUMER_KEY or not TWITTER_ACCESS_TOKEN:
        print("Skipping Twitter: Keys not found in environment.")
        return
    
    try:
        client = tweepy.Client(
            consumer_key=TWITTER_CONSUMER_KEY, consumer_secret=TWITTER_CONSUMER_SECRET,
            access_token=TWITTER_ACCESS_TOKEN, access_token_secret=TWITTER_ACCESS_TOKEN_SECRET
        )
        response = client.create_tweet(text=text)
        print(f"✅ Posted to Twitter: https://twitter.com/i/web/status/{response.data['id']}")
    except Exception as e:
        print(f"Error posting to Twitter: {e}")

def post_to_linkedin(text):
    if not LINKEDIN_ACCESS_TOKEN:
        print("Skipping LinkedIn: Token not found in environment.")
        return

    url = "https://api.linkedin.com/v2/userinfo"
    headers = {"Authorization": f"Bearer {LINKEDIN_ACCESS_TOKEN}"}
    try:
        user_info = requests.get(url, headers=headers).json()
        if 'sub' not in user_info:
            print(f"Error fetching LinkedIn profile: {user_info}")
            return
        person_urn = f"urn:li:person:{user_info['sub']}"

        post_url = "https://api.linkedin.com/v2/ugcPosts"
        post_data = {
            "author": person_urn,
            "lifecycleState": "PUBLISHED",
            "specificContent": {
                "com.linkedin.ugc.ShareContent": {
                    "shareCommentary": {"text": text},
                    "shareMediaCategory": "NONE"
                }
            },
            "visibility": {"com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"}
        }
        response = requests.post(post_url, headers=headers, json=post_data)
        if response.status_code == 201:
            print("✅ Posted to LinkedIn.")
        else:
            print(f"Error posting to LinkedIn: {response.text}")
    except Exception as e:
        print(f"Error during LinkedIn post: {e}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python social_dispatch.py 'your message'")
    else:
        message = " ".join(sys.argv[1:])
        post_to_twitter(message)
        post_to_linkedin(message)
