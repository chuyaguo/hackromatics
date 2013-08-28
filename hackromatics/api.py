'''
Client api wrapper for requesting transit information 
from a syncromatics web server.
'''
import time
from datetime import datetime

import requests

from models import Region, Route, Vehicle, Waypoint


class API:
    '''Syncromatics API'''
    def __init__(self, host): 
        self.host = host # example: http://www.pennrides.com
        self.session = requests.Session()

    def regions(self):
        path = '/regions'
        return _request(self, path=path,
                        payload_type=Region, payload_list=True)

    def route(self, route_id):
        path = '/route/{route_id}'
        return _request(self, path=path.format(route_id=route_id), 
                        payload_type=Route)

    def routes(self, region_id):
        path = '/region/{region_id}/routes'
        return _request(self, path=path.format(region_id=region_id), 
                           payload_type=Route, payload_list=True)

    def vehicles(self, route_id):
        path = '/route/{route_id}/vehicles'
        return _request(self, path=path.format(route_id=route_id), 
                        payload_type=Vehicle, payload_list=True)

    def waypoints(self, route_id):
        path = '/route/{route_id}/waypoints'
        return _request(self, path=path.format(route_id=route_id), 
                        payload_type=Waypoint, payload_list=True)


def _request(api, **kargs):
    payload_type = kargs['payload_type']
    response = api.session.get(''.join([api.host, kargs['path']]))
    if kargs.get('payload_list', False):
        return payload_type.parse_list(api, response.json())
    return payload_type.parse(api, response.json())

    