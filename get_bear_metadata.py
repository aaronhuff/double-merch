import logging
import json
import os
from dotenv import load_dotenv
from quicknode import QuickNodeEndpoint as qn

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting")

    load_dotenv()
    qn_name, qn_token = os.environ.get("QUICKNODE_NAME"), os.environ.get("QUICKNODE_TOKEN")

    node = qn(qn_name, qn_token)
    bears = []
    for i in range(1, 251):
        logging.info(f"Fetching page {i}")
        fetch = node.fetchNFTsByCreator(
            '3xVDoLaecZwXXtN59o6T3Gfxwjcgf8Hc9RfoqBn995P9',
            page=i,
            perPage=40
        )
        bears.append(fetch["assets"])
    logging.info(f"Total bears: {len(bears)}")
    logging.info("Done")

    logging.info("Writing to file")
    with open("bears.json", "w") as f:
        json.dump(bears, f)
    logging.info("Done")
