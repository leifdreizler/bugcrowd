import os

import pycrowd


class TestSubmissions(object):

    def test_get_submission_for_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        assert r.status_code == 200

    def test_get_submission_for_bounty_with_assignment(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f", assignment='mine')

        assert r.status_code == 200

    def test_get_submission_for_bounty_with_assignment_and_sort(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f", assignment='mine', sort='newest')

        assert r.status_code == 200

    def test_create_submission(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.create_submission("84b71b04-a363-441f-91e0-8519ad3a4f4f", "Test1", "29-04-2016 12:00:00")

        assert r.status_code == 201
