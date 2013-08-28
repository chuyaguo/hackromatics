'''
Data structures for syncromatics transit system.
'''
from datetime import datetime


class Model:
    def __init__(self, api=None):
        self._api = api

    def __getstate__(self):
        # pickle
        pickle = dict(self.__dict__)
        try:
            del pickle['_api']  # do not pickle the API reference
        except KeyError:
            pass
        return pickle

    @classmethod
    def parse(cls, api, json):
        '''Parse a JSON object into a model instance.'''
        obj = cls(api)
        for k, v in json.items():
            setattr(obj, k, v)
        return obj

    @classmethod
    def parse_list(cls, api, json_list):
        '''Parse a list of JSON objects into a list of model instances.'''
        results = []
        for obj in json_list:
            if obj:
                results.append(cls.parse(api, obj))
        return results


class Region(Model):
    pass


class Route(Model):
    pass


class Vehicle(Model):
    pass


class Waypoint(Model):
    pass


