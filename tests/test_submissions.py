import os

import pycrowd


class TestSubmissions(object):

    def test_get_submission_for_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        client = pycrowd.Client(uname, pw)
        bounty = client.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")
        r = bounty.get_submissions_for_bounty()

        assert r.status_code == 200

    def test_get_submission_for_bounty_with_assignment(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        client = pycrowd.Client(uname, pw)
        bounty = client.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")
        r = bounty.get_submissions_for_bounty(assignment='mine')

        assert r.status_code == 200

    def test_get_submission_for_bounty_with_assignment_and_sort(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        client = pycrowd.Client(uname, pw)
        bounty = client.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")
        r = bounty.get_submissions_for_bounty(assignment='mine', sort='newest')

        assert r.status_code == 200