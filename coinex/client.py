import hashlib
import time
from urllib.parse import urlencode

import requests

from coinex.enums import RequestMethod
from coinex.exceptions import CoinExBaseException, RequestFailedToSendException


class Client:
    def __init__(self, api_key=None, api_secret=None):
        self.session = requests.Session()
        self.base_url = "https://api.coinex.com/v1"
        self.access_id = api_key
        self.secret_key = api_secret

    def _sign(self, data: dict = None, headers: dict = None):
        payload = {key: value for key, value in sorted(data.items())}
        payload.update({"secret_key": self.secret_key})
        payload_query = urlencode(payload)

        signature = hashlib.md5(payload_query.encode()).hexdigest().upper()

        headers.update({"Authorization": signature.upper()})

    def _get(self, url, params, headers):
        return self.session.get(url=url, params=params, headers=headers)

    def _dispatch(self, url, method: RequestMethod, data, headers):
        headers.update({"Content-Type": "application/json"})

        if method == RequestMethod.GET:
            return self._get(url=self.base_url + url, params=data, headers=headers)

    def _get_response(self, response):
        response = response.json()

        if response["code"] == 0:
            return response["data"]
        else:
            raise CoinExBaseException(
                code=response["code"], message=response["message"]
            )

    def _request(
        self,
        url,
        method: RequestMethod,
        data: dict = None,
        headers: dict = None,
        has_signature: bool = False,
    ):
        headers = dict() if not headers else headers
        data = dict() if not data else data

        if has_signature:
            data.update({"access_id": self.access_id})
            data.update({"tonce": int(time.time() * 1000)})
            self._sign(data=data, headers=headers)

        try:
            response = self._dispatch(
                url=url, method=method, data=data, headers=headers
            )
        except requests.exceptions.RequestException as e:
            raise RequestFailedToSendException(str(e))

        return self._get_response(response)
