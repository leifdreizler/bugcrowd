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

    def test_single_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Bugcrowd(uname, pw)
        r = test.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        print(r.text)
        assert r.status_code == 200

    def test_single_bounty_fails(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Bugcrowd(uname, pw)
        r = test.get_bounty("123")

        assert r.status_code == 404