import os

import pycrowd

class TestBounties(object):
    def test_list_bounties_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Bugcrowd(uname, pw)
        r = test.list_bounties()
        assert r.status_code == 200

    def test_list_bounties_fails(self):
        uname = "nonExistent"
        pw = "wrongPassword"

        test = pycrowd.Bugcrowd(uname, pw)
        r = test.list_bounties()
        assert r.status_code == 401
