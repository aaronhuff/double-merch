import requests
import os
import json
import logging


def load_bears():
    logging.info("Loading bears")
    with open("bears.json", "r") as f:
        bears = json.load(f)
    return bears[0]


def get_bear_images(bears):
    logging.info("Getting bear images")
    os.makedirs("images", exist_ok=True)
    for bear in bears:
        logging.info(f"Getting image for {bear['name']}")
        image_url = bear["imageUrl"]
        image = requests.get(image_url)
        image_name = bear["name"] + ".png"
        with open(f"images/{image_name}", "wb") as f:
            f.write(image.content)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting")
    bears = load_bears()
    get_bear_images(bears)
    logging.info("Done")
