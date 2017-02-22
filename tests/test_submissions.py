import os

import pycrowd


class TestSubmissions(object):

    def test_get_submission_for_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Bugcrowd(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        assert r.status_code == 200