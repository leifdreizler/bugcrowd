import requests
import json
import pprint

class Client(object):
    def __init__(self, username, password):
        self.uname = username
        self.pw = password
        self.version_header = {"Accept": "application/vnd.bugcrowd.v2+json"}

    def list_bounties(self):
        r = self.get('bounties')
        j = json.loads(r.text)

        bounties = []
        for each in j['bounties']:
            bounties.append(Bounty(each))

        return bounties

    def get_bounty(self, bounty_id):
        r = self.get('bounties/' + bounty_id)
        j = json.loads(r.text)

        return Bounty(j['bounty'])

    def get_submission(self, submission_id):
        r = self.get('submissions/' + submission_id)
        j = json.loads(r.text)

        return Submission(j['submission'])

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
        j = json.loads(r.text)
        
        submissions = []
        for each in j['submissions']:
            submissions.append(Submission(each))

        return submissions

    # TODO Add code for create submission once API is correct

    def update_submission(self, submission_uuid, title=None, internal_bug_type=None, custom_fields=None):
        payload = {}
        if title is not None:
            payload['title'] = title
        if internal_bug_type is not None:
            payload['internal_bug_type'] = internal_bug_type
        if custom_fields is not None:
            payload['custom_fields'] = custom_fields

        self.put('submissions/' + submission_uuid, json=payload)

        return self.get_submission(submission_uuid)

    def update_priority_on_submission(self, submission_uuid, level):
        current_priority = self.get_submission(submission_uuid).priority
        
        if current_priority == None: # Set
            self.post('submissions/' + submission_uuid + '/priority', json={'priority': {'level': level}})
        elif current_priority: # Update
            self.put('submissions/' + submission_uuid + '/priority', json={'priority': {'level': level}})
        elif level == None: # Delete
            self.delete('submissions/' + submission_uuid + '/priority')

        return level

    def get_comments_for_submission(self, submission_uuid):
        r = self.get('submissions/' + submission_uuid + '/comments')
        return r

    def add_comment_to_submission(self, submission_uuid, type, body):
        r = self.post('submissions/' + submission_uuid + '/comments', json={'comment': {'type': type, 'body': body}})
        return r

    def get_custom_fields_for_bounty(self, bounty_uuid):
        r = self.get('bounties/' + bounty_uuid + '/custom_field_labels')
        return r

    def create_custom_field_for_bounty(self, bounty_uuid, field_name):
        r = self.post('bounties/' + bounty_uuid + '/custom_field_labels', json={'field_name': field_name})

        return r

    def update_custom_field_label_for_bounty(self, bounty_uuid, field_id, new_label):
        r = self.put('bounties/' + bounty_uuid + '/custom_field_labels/' + field_id, json={'field_name': new_label})

        return r

    def delete_custom_field_for_bounty(self, bounty_uuid, field_id):
        r = self.delete('bounties/' + bounty_uuid + '/custom_field_labels/' + field_id)

        return r

    # Utility Methods

    def delete(self, path):
        r = requests.delete('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                               headers=self.version_header)

        if r.status_code is not 200:
            raise ApiException(r.text)

        return r

    def put(self, path, json=None):
        r = requests.put('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                            headers=self.version_header, json=json)

        if r.status_code is not 200:
            raise ApiException(r.text)

        return r

    def post(self, path, json=None):
        r = requests.post('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                             headers=self.version_header, json=json)
        if r.status_code is not 201:
            raise ApiException(r.text)

        return r

    def get(self, path, params=None):
        r = requests.get('https://api.bugcrowd.com/' + path, auth=(self.uname, self.pw),
                            headers=self.version_header, params=params)

        if r.status_code is not 200:
            raise ApiException(r.text)

        return r


class Bounty(object):
    def __init__(self, j):
        self.__dict__ = j

    def __repr__(self):
    	return pprint.pformat(vars(self))


class Submission(object):
    def __init__(self, j):
        self.__dict__ = j

    def __repr__(self):
    	return pprint.pformat(vars(self))

class ApiException(Exception):
    def __init__(self, message):
        self.message = message
