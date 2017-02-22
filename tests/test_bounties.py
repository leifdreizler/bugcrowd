import os

import pycrowd

class TestBounties(object):
    def test_list_bounties_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        client = pycrowd.Client(uname, pw)
        r = client.list_bounties()

        # TODO update when JSON is parsed
        assert 1 == 1

    def test_list_bounties_fails(self):
        uname = "nonExistent"
        pw = "wrongPassword"

        client = pycrowd.Client(uname, pw)
        r = client.list_bounties()

        # TODO update when JSON is parsed
        assert 1 == 1

    def test_single_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        client = pycrowd.Client(uname, pw)
        r = client.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        # TODO update when JSON is parsed
        assert 1 == 1

    def test_single_bounty_fails(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        client = pycrowd.Client(uname, pw)
        r = client.get_bounty("123")

        # TODO update when JSON is parsed
        assert 1 == 1