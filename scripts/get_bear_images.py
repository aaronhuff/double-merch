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
    with open(f"images/original/{name}", "wb") as f:
        f.write(image)


def get_bear_images(bears):
    logging.info("Getting bear images")
    os.makedirs("images", exist_ok=True)
    bear_num = 0
    for bear in bears:
        bear_num += 1
        image_url = bear["url"]
        image_name = bear["name"] + ".png"
        if not os.path.exists(f"images/original/{image_name}"):
            logging.info(f"Getting image for {bear['name']}")
            image = requests.get(image_url)
            write_image(image.content, image_name)
        else:
            logging.warning(f"Image {image_name} already exists")
    logging.info(f"{bear_num} bears downloaded")


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logging.info("Starting")
    bears = load_bears()
    get_bear_images(bears)
    logging.info("Done")
