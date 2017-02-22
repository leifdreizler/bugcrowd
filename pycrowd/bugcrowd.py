import requests

class Client(object):
    def __init__(self, username, password):
        self.uname = username
        self.pw = password
        self.version_header = {"Accept": "application/vnd.bugcrowd.v2+json"}

    def list_bounties(self):
        r = requests.get('https://api.bugcrowd.com/bounties', auth=(self.uname, self.pw), headers=self.version_header)
        return r

    def get_bounty(self, bounty_id):
        r = requests.get('https://api.bugcrowd.com/bounties/' + bounty_id, auth=(self.uname, self.pw),
                         headers=self.version_header)
        return r

    def get_submissions_for_bounty(self, bounty_uuid, assignment='', filter='', search='', sort=''):
        payload = {}
        if assignment != '':
            payload['assignment'] = assignment
        if filter != '':
            payload['filter'] = filter
        if search != '':
            payload['search'] = search
        if sort != '':
            payload['sort'] = sort

        r = requests.get('https://api.bugcrowd.com/bounties/' + bounty_uuid + '/submissions', auth=(self.uname, self.pw),
                         headers=self.version_header, params=payload)
        return r

class Bounty(object):
    def __init__(self):
        pass

class Submission(object):
    def __init__(self):
        pass