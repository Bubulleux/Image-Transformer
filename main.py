import blackWhite
import asciiConverter
from PIL import Image
import mozaic
import clean_dataset

IMG_NAME = "cat2.png "
PATH = "imgSource/" + IMG_NAME
DATASET = "cats"
ASCII_SIZE = (80, 80)

image: Image = Image.open(PATH)
image = image.convert("RGB")
#
# asciiConverter.ascii_convert_color(ASCII_SIZE, image)

# mozaic.dataset_sort("cats")

mozaic.to_mozaic(ASCII_SIZE, image, DATASET, f"{IMG_NAME}_{DATASET}_{ASCII_SIZE[0]}x{ASCII_SIZE[1]}", img_size=(70, 70))

# clean_dataset.clean_dataset("cats")