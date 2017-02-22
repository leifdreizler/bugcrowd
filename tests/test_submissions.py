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

    def test_get_comments_for_submission_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.get_comments_for_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab")

        assert r.status_code == 200


    def test_delete_priority_on_submission(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.delete_priority_on_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab")

        assert r.status_code == 200

    def test_set_priority_on_submission(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.set_priority_on_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab", 4)

        assert r.status_code == 201

    def test_update_priority_on_submission(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.update_priority_on_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab", 4)

        assert r.status_code == 200