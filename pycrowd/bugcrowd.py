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

    def update_submission(self, submission_uuid, title=None, internal_bug_type=None, customFields=None):
        payload = {}
        if title is not None:
            payload['title'] = title
        if internal_bug_type is not None:
            payload['internal_bug_type'] = internal_bug_type
        if customFields is not None:
            payload['custom_fields'] = customFields

        r = self.put('submissions/' + submission_uuid, json=payload)

        return r

    def set_priority_on_submission(self, submission_uuid, level):
        r = self.post('submissions/' + submission_uuid + '/priority', json={'priority': {'level': level}})

        return r

    def update_priority_on_submission(self, submission_uuid, level):
        r = self.put('submissions/' + submission_uuid + '/priority', json={'priority': {'level': level}})

        return r

    def delete_priority_on_submission(self, submission_uuid):
        r = self.delete('submissions/' + submission_uuid + '/priority')

        return r

    def get_comments_for_submission(self, submission_uuid):
        r = self.get('submissions/' + submission_uuid + '/comments')
        return r

    def get_custom_fields_for_bounty(self, bounty_uuid):
        r = self.get('bounties/' + bounty_uuid + '/custom_field_labels')
        return r

    def delete(self, path):
        return requests.delete('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                               headers=self.version_header)

    def put(self, path, json=None):
        return requests.put('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                            headers=self.version_header, json=json)

    def post(self, path, json=None):
        return requests.post('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                             headers=self.version_header, json=json)

    def get(self, path, params=None):
        return requests.get('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                            headers=self.version_header, params=params)


class Bounty(object):
    def __init__(self):
        pass


class Submission(object):
    def __init__(self):
        pass
