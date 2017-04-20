import os

import pytest
import bugcrowd


class TestSubmissions(object):
    def test_get_submission_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)
        s = test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987")

        assert s.uuid == "b337bee1-1643-4ef8-af33-fde80cb4d987"

    def test_get_submission_fails(self):
        with pytest.raises(bugcrowd.ApiException):
            uname = "noOne"
            pw = "badPass"

            test = bugcrowd.Client(uname, pw)
            test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987")

    def test_get_submission_for_bounty_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")

        assert r[0].bounty['uuid'] == "84b71b04-a363-441f-91e0-8519ad3a4f4f"


    def test_update_submission_priority(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')
        test = bugcrowd.Client(uname, pw)
        
        assert test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987").priority == None
        test.update_priority_on_submission("b337bee1-1643-4ef8-af33-fde80cb4d987", 4)
        test.update_priority_on_submission("b337bee1-1643-4ef8-af33-fde80cb4d987", 4)
        assert test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987").priority == 4
        test.update_priority_on_submission("b337bee1-1643-4ef8-af33-fde80cb4d987", 2)
        assert test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987").priority == 2
        test.update_priority_on_submission("b337bee1-1643-4ef8-af33-fde80cb4d987", None)
        assert test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987").priority == None

    def test_update_submission_priority_fails(self):
        with pytest.raises(bugcrowd.ApiException):
            uname = "noOne"
            pw = "badPass"
            test = bugcrowd.Client(uname, pw)

            test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987")

    # TODO: Write stateful test for update submission priority server errors

    def test_get_submission_for_bounty_with_assignment(self):

        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f", assignment='mine')

        assert r[1].uuid == "9fdca5e5-633f-471d-b0df-c69abb0d35bb"
        assert r[1].caption == "Assigned_Zach, State_Triage"

    def test_get_submission_for_bounty_with_assignment_and_sort(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)
        r = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f", assignment='mine', sort='newest')

        assert r[0].uuid == "9fdca5e5-633f-471d-b0df-c69abb0d35bb"
        assert r[0].caption == "one"

    def test_get_comments_for_submission_passes(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)
        r = test.get_comments_for_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab")

        assert r.status_code == 200

    def test_add_comment_to_submission(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)
        r = test.add_comment_to_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab", "note", "testNote")

        assert r.status_code == 201

        r = test.add_comment_to_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab", "tester_message", "testerMessage")

        assert r.status_code == 201

    def test_update_submission(self):
        uname = os.environ.get('BCUSER')
        pw = os.environ.get('BCPW')

        test = bugcrowd.Client(uname, pw)

        r = test.get_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab")

        assert r.title == "New Title 1"

        r = test.update_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab", "New Title 2", "xss",
                                   {'customKey': 'updatedKey'})

        assert r.title == "New Title 2"

        r = test.update_submission("eea7936e-caf5-40ef-a77e-3daf22a0e0ab", "New Title 1", "xss",
                                   {'customKey': 'updatedKey'})

        assert r.title == "New Title 1"
