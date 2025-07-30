import json


class JollyClass:
    def __init__(self, props=None, dict=None):
        if props:
            for prop in props:
                setattr(self, prop, None)
        elif dict:
            for k in dict:
                setattr(self, k, dict[k])

    def has(self, prop):
        return hasattr(self, prop)

    def has_not_none(self, prop):
        return self.has(prop) and getattr(self, prop)

    def set(self, prop, val):
        setattr(self, prop, val)

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True)

    def to_dict(self):
        return self.__dict__
