import os
import bugcrowd

uname = os.environ.get('BCUSER')
pw = os.environ.get('BCPW')
test = bugcrowd.Client(uname, pw)

# Get a list of all bounties
b = test.list_bounties()
print(b)

# Get details of one bounty
b = test.get_bounty("84b71b04-a363-441f-91e0-8519ad3a4f4f")
print(b)
