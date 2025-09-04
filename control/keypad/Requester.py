from single_include import httpx, urljoin


class Requester(object):
    def __init__(self, endpoint, headers=None, verify=False, timeout=10):
        self.__endpoint = endpoint
        self.__headers = headers
        self.__verify = verify
        self.__timeout = timeout

    def get_endpoint(self):
        return self.__endpoint

    def check(self, endpoint="/", params=None) -> bool:
        try:
            response = httpx.get(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                headers=self.__headers,
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
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                headers=self.__headers,
            ).json()
        except:
            return False

    def put(self, endpoint, params=None, json=None):
        try:
            return httpx.put(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                json=json,
                headers=self.__headers,
            ).json()
        except:
            return False

    def post(self, endpoint, params=None, json=None):
        try:
            return httpx.post(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                json=json,
                headers=self.__headers,
            ).json()
        except:
            return False

    def delete(self, endpoint, params=None):
        try:
            return httpx.delete(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                headers=self.__headers,
            ).json()
        except:
            return False
