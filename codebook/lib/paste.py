import requests
import sys
from urllib.parse import urlencode

URI = "http://sprunge.us"

def upload(text):
    return requests.post(URI, { 'sprunge': text }).content

