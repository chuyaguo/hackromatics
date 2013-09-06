hackromatics
============
Client wrapper api for Syncromatics (http://www.syncromatics.com/) transit system.

install
=======
Requires `requests` (https://github.com/kennethreitz/requests).

how to use
==========
```python
import hackromatics

# connect the the server
api = hackromatics.API('http://ladotbus.com')

# get the transit regions
regions = api.regions()

# print out some info about the regions
for region in regions:
    print region.Name
```

sample sites
============
Here is an incomplete list of Syncromatics hosted transit sites: 
- UPenn Transit System ('http://pennrides.com')
- Los Angeles Department of Transportation ('http://ladotbus.com')
- keywest ('http://kwtransit.com') 
- UC San Diego ('http://www.ucsdbus.com/') 
- University of South Florida ('http://www.usfbullrunner.com')
- SF Presidio ('http://www.presidiobus.com/')
- CSU Long Beach ('http://csulbshuttle.com')
- Mississippi State ('http://transit.msstate.edu/')
- CSU Pomona ('http://broncoshuttle.com/')
- University of Delaware ('http://udshuttle.com')
- University of San Diego ('http://usdtram.com')
- National Institute of Health ('http://wttsshuttle.com/')
- UC San Francisco ('http://ucsfshuttles.com')
