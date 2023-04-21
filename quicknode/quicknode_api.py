from jsonrpcclient import request, parse, Ok
import requests


class QuickNodeEndpoint:
    def __init__(self, name: str, token: str):
        self.url = f"https://{name}.solana-mainnet.discover.quiknode.pro/{token}/"

    def fetchNFTsByCreator(
                self, creator: str, page: int = 1, perPage: int = 20
            ):
        request_data = [{"creator": creator, "page": page, "perPage": perPage}]
        response = requests.post(
            self.url, json=request("qn_fetchNFTsByCreator", request_data)
        )
        parsed = parse(response.json())

        if isinstance(parsed, Ok):
            return parsed.result
        else:
            raise Exception(parsed.message)
