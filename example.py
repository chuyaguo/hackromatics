import hackromatics

# a couple sample syncromatics hosted web sites for transit
losangeles = 'http://ladotbus.com' 	# Los Angeles transit
penn = 'http://pennrides.com'		# UPenn transit

# connect to a syncromatics transit web site
api = hackromatics.API(losangeles)

# do get info about the transit regions...
regions = api.regions()

# to iterate through all the information you can loop through everything
# in this ugly for loop...

for region in api.regions():
	print 'REGION:', region.ID, region.Name
	for route in api.routes(region.ID):
		print '\tROUTE:', route.ID, route.Name
		print '\t\t', 'VEHICLES:'
		for vehicle in api.vehicles(route.ID):
			print '\t\t', vehicle.ID, vehicle.Name, \
						vehicle.Longitude, vehicle.Latitude
		print '\t\t', 'BUS STOPS:'
		for waypoint in api.waypoints(route.ID):
			print '\t\t', waypoint.Longitude, waypoint.Latitude
