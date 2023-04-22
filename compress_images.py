import glob
import logging
from PIL import Image

logging.basicConfig(level=logging.INFO)

logging.info("Finding all images in images/original/")
images = glob.glob("images/original/*.png")
logging.info("Found {} images".format(len(images)))

logging.info("Compressing images and saving to images/")
for image in images:
    logging.info("Compressing {}".format(image))
    new_path = "images/thumbnails/" + image.split("/")[-1]
    img = Image.open(image)
    img.thumbnail((300, 300))
    img.save(new_path, "PNG")

logging.info("Done!")
