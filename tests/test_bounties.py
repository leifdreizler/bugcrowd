import os

import pycrowd

class TestBounties(object):
    def test_list_bounties_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.list_bounties()

        assert r.status_code == 200

    def test_list_bounties_fails(self):
        uname = "nonExistent"
        pw = "wrongPassword"

        test = pycrowd.Client(uname, pw)
        r = test.list_bounties()

        assert r.status_code == 401

    def test_single_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        b = test.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        assert b.uuid == "84b71b04-a363-441f-91e0-8519ad3a4f4f"

    # def test_single_bounty_fails(self):
    #     uname = os.environ.get('BCUSER')
    #     pw = os.environ.get('BCPW')

    #     test = pycrowd.Client(uname, pw)
    #     r = test.get_bounty("123")

    #     assert r.status_code == 404

    def test_get_custom_fields_for_bounty(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.get_custom_fields_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        print(r.text)
        assert r.status_code == 200

    def test_delete_custom_field(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.delete_custom_field_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f", "021d9127-8088-4477-b124-0e961c2a785c")

        assert r.status_code == 200

    def test_create_custom_field_for_bounty(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.create_custom_field_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f", "newField")

        assert r.status_code == 201

    def test_update_custom_field_label_for_bounty(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = pycrowd.Client(uname, pw)
        r = test.update_custom_field_label_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f",
                                                      "957c6d99-3caa-4489-8b62-40829f7a94c0", "newNewField")

        assert r.status_code == 200