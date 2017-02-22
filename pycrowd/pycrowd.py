import requests


class Client(object):
    def __init__(self, username, password):
        self.url = 'https://api.bugcrowd.com/'
        self.uname = username
        self.pw = password
        self.version_header = {"Accept": "application/vnd.bugcrowd.v2+json"}

    def list_bounties(self):
        r = requests.get('https://api.bugcrowd.com/bounties', auth=(self.uname, self.pw), headers=self.version_header)
        return r

    def get_bounty(self, bounty_uuid):
        r = self.request('bounties/' + bounty_uuid)
        # TODO remove bountry uuid when populated from JSON
        return Bounty(self, r.text, bounty_uuid)

    def request(self, path, payload=None):
        return requests.get(self.url + path, auth=(self.uname, self.pw), headers=self.version_header, params=payload)

class Bounty(object):
    def __init__(self, client, json, bounty_uuid):
        self.client = client
        self.json = json
        #todo remove and populate from JSON
        self.bounty_uuid = bounty_uuid
        self.createFromJson(json)

    def createFromJson(self, json):
        json = json
        #TODO

    def get_submissions_for_bounty(self, assignment='', filter='', search='', sort=''):
        payload = {}
        if assignment != '':
            payload['assignment'] = assignment
        if filter != '':
            payload['filter'] = filter
        if search != '':
            payload['search'] = search
        if sort != '':
            payload['sort'] = sort

        r = self.client.request('bounties/' + self.bounty_uuid + '/submissions', payload=payload)

        return r


class Submission(object):
    def __init__(self):
        pass
