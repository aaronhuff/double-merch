import requests
import os
import json
import logging


def load_bears():
    logging.info("Loading bears")
    with open("data/double_merch.json", "r") as f:
        bears = json.load(f)
    return bears


def write_image(image, name):
    logging.info(f"Writing image {name}")
    with open(f"images/{name}", "wb") as f:
        f.write(image)


def get_bear_images(bears):
    logging.info("Getting bear images")
    os.makedirs("images", exist_ok=True)
    for bear in bears:
        logging.info(f"Getting image for {bear['name']}")
        image_url = bear["url"]
        image = requests.get(image_url)
        image_name = bear["name"] + ".png"
        write_image(image.content, image_name)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting")
    bears = load_bears()
    get_bear_images(bears)
    logging.info("Done")
