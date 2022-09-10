from coinex.client import Client
from coinex.enums import RequestMethod


class SpotClient(Client):
    def all_markets(self):
        return self._request(
            url="/market/list",
            method=RequestMethod.GET,
        )

    def all_markets_info(self):
        return self._request(url="/market/info", method=RequestMethod.GET)

    def my_balance(self):
        return self._request(
            url="/balance/info",
            method=RequestMethod.GET,
            has_signature=True,
        )
