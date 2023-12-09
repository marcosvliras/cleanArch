# pylint: disable=too-many-arguments

from typing import Dict


class HttpRequest:
    def __init__(
        self,
        url: str = None,
        headers: Dict = None,
        body: Dict = None,
        path_params: Dict = None,
        query_params: Dict = None,
        ipv4: str = None,
    ):
        self.url = url
        self.headers = headers
        self.body = body
        self.path_params = path_params
        self.query_params = query_params
        self.ipv4 = ipv4
