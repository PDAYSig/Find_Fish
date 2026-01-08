from PIL import Image, ImageFile, ImageDraw
from Models.fish import Fish
from Models.photo import Photo
from Yolo_work.find_fish import find_fish
from Yolo_work.image_work import ImageWork
PHOTO = "fish_photograph.jpeg"

# new : Image = ImageWork.resize_image("fiskimynd.jpeg")
image = Image.open(PHOTO)
fish = find_fish()
bbox_and_conf = fish.locate_fish_bbox(PHOTO)
draw = ImageDraw.Draw(image)
draw.rectangle(bbox_and_conf[0], outline="red", width=3)
print(bbox_and_conf[1])
image.show()
