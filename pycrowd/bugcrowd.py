import requests
import os

class Bugcrowd(object):
    def __init__(self, username, password):
        self.uname = username
        self.pw = password
        self.version_header = {"Accept": "application/vnd.bugcrowd.v2+json"}

    def list_bounties(self):
        r = requests.get('https://api.bugcrowd.com/bounties', auth=(uname, pw), headers=self.version_header)
        print(r.text)
        
uname = os.environ.get('BCUSER')
pw = os.environ.get('BCPW')

test = Bugcrowd(uname, pw)
test.list_bounties()
