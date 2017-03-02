import os
import bugcrowd

uname = os.environ.get('BCUSER')
pw = os.environ.get('BCPW')
test = bugcrowd.Client(uname, pw)

# Get a single submission
s = test.get_submission("b337bee1-1643-4ef8-af33-fde80cb4d987")
# Print single submission
print(s)
# Print uuid of submission
print(s.uuid)

# Get all submissions for a bounty
s = test.get_submissions_for_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")
print(s)
# Print uuid of first submission
print(s[0].uuid)
