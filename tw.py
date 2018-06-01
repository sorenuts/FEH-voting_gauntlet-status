#coding: utf-8
from get_info import getinfo
import twitter
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

consumer_key = os.environ.get("CONKEY")
consumer_secret = os.environ.get("CONSEC")
token = os.environ.get("TOKEN")
token_secret = os.environ.get("TOKENSEC")

auth = twitter.OAuth(consumer_key=consumer_key,
			consumer_secret=consumer_secret,
			token=token,
			token_secret=token_secret)

tw = twitter.Twitter(auth=auth)
string=getinfo()
tw.statuses.update(status=string)
