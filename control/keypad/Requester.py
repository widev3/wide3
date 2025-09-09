from single_include import httpx, urljoin


class Requester(object):
    def __init__(self, endpoint, headers=None, verify=False, timeout=10):
        self.__endpoint = endpoint
        self.__headers = headers
        self.__verify = verify
        self.__timeout = timeout

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
            response = httpx.get(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                headers=self.__headers,
            )
            return response.status_code, response.json()
        except:
            return False

    def put(self, endpoint, params=None, json=None):
        try:
            response = httpx.put(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                json=json,
                headers=self.__headers,
            )
            return response.status_code, response.json()
        except:
            return False

    def post(self, endpoint, params=None, json=None):
        try:
            response = httpx.post(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                json=json,
                headers=self.__headers,
            )
            return response.status_code, response.json()
        except:
            return False

    def delete(self, endpoint, params=None):
        try:
            response = httpx.delete(
                url=urljoin(self.__endpoint, endpoint),
                timeout=self.__timeout,
                verify=self.__verify,
                params=params,
                headers=self.__headers,
            )
            return response.status_code, response.json()
        except:
            return False
