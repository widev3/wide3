from single_include import httpx, urljoin


class Requester(object):
    def __init__(self, endpoint):
        self.__endpoint = endpoint

    def check(self, endpoint="/", params=None):
        try:
            response = httpx.get(
                url=urljoin(self.__endpoint, endpoint),
                timeout=10,
                verify=False,
                params=params,
            )
            if response.status_code == 200:
                return True
            else:
                return False
        except:
            return False

    def get(self, endpoint, params=None):
        try:
            return httpx.get(
                url=urljoin(self.__endpoint, endpoint),
                timeout=10,
                verify=False,
                params=params,
            ).json()
        except:
            return False

    def put(self, endpoint, params=None, json=None):
        try:
            return httpx.put(
                url=urljoin(self.__endpoint, endpoint),
                timeout=10,
                verify=False,
                params=params,
                json=json,
            ).json()
        except:
            return False

    def post(self, endpoint, params=None, json=None):
        try:
            return httpx.post(
                url=urljoin(self.__endpoint, endpoint),
                timeout=10,
                verify=False,
                params=params,
                json=json,
            ).json()
        except:
            return False

    def delete(self, endpoint, params=None):
        try:
            return httpx.delete(
                url=urljoin(self.__endpoint, endpoint),
                timeout=10,
                verify=False,
                params=params,
            ).json()
        except:
            return False
