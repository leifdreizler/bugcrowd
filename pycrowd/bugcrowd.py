import requests

class Client(object):
    def __init__(self, username, password):
        self.uname = username
        self.pw = password
        self.version_header = {"Accept": "application/vnd.bugcrowd.v2+json"}

    def list_bounties(self):
        r = self.get('bounties')

        return r

    def get_bounty(self, bounty_id):
        r = self.get('bounties/' + bounty_id)

        return r

    def get_submissions_for_bounty(self, bounty_uuid, assignment=None, filter=None, search=None, sort=None):
        payload = {}
        if assignment is not None:
            payload['assignment'] = assignment
        if filter is not None:
            payload['filter'] = filter
        if search is not None:
            payload['search'] = search
        if sort is not None:
            payload['sort'] = sort

        r = self.get('bounties/' + bounty_uuid + '/submissions', params=payload)
        return r

    def post(self, path, json=None):
        return requests.post('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                            headers=self.version_header, json=json)

    def get(self, path, params=None):
        return requests.get('https://api.bugcrowd.com/' + path , auth=(self.uname, self.pw),
                         headers=self.version_header, params=params)

class Bounty(object):
    def __init__(self):
        pass

class Submission(object):
    def __init__(self):
        pass