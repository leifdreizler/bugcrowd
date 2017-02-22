import requests
import os

class Bugcrowd(object):
    def __init__(self, username, password):
        self.uname = username
        self.pw = password
        self.version_header = {"Accept": "application/vnd.bugcrowd.v2+json"}

    def list_bounties(self):
        r = requests.get('https://api.bugcrowd.com/bounties', auth=(self.uname, self.pw), headers=self.version_header)
        return r
        
